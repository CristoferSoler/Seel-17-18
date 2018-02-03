from django.contrib.auth.models import User, Permission,Group
from django.core.mail import EmailMessage
from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string


@receiver(m2m_changed, sender=User.groups.through)
def save(sender,instance,pk_set,action, **kwargs):
    user = instance
    for pk in pk_set:
        groups = Group.objects.filter(id=pk)
        for g in groups:
            if action == 'pre_remove':
                if(str(g) == 'moderators'):
                    subject = 'Your moderator status has changed'
                    text = '\nYour moderator permissions have been revoked. \n \nThe reasons for this decision could be:\n- You behaved inappropriately. \n- You misused the authority.'
                    sendMail(str(g),user,subject,text)
            if action == 'pre_add':
                if(str(g) == 'moderators'):
                    subject = 'Your user  status has changed'
                    text = '\nWe are gladly informing you that you are now enjoying the status “Moderator”. We would like ' \
                           'to thank you for your contribution to ISAM, keep up the good work.\n\n As a moderator it is ' \
                           'now your task to:\n- Review articles, links, content and approve UAs \n- Protect Website Rules in' \
                           ' UA and in Info Page'
                    sendMail(str(g), user,subject,text)


def sendMail(group,user,subject,text):
    userEmail = getEmailOfUser(user)
    if(userEmail != None):
        mail_subject = subject
        messageBody = text

        message = render_to_string('email/permissionChanged.html', {
            'messageBody': messageBody,
            'user': user,
        })

        email = EmailMessage(
            mail_subject, message, to=[userEmail]
        )
        email.send()
        print('Email send')

def getEmailOfUser(user):
    userObject = User.objects.get(username=user)
    userEmail = userObject.email
    return userEmail