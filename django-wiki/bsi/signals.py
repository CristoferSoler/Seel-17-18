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
                print('Remove Group: ' + str(g))
                sendMail(True,str(g),user)
            if action == 'pre_add':
                print('Added Group: ' + str(g))
                sendMail(False, str(g), user)


def sendMail(remove,group,user):
    userEmail = getEmailOfUser(user)
    if(userEmail != None):
        mail_subject = 'ISAM: Your permission group is changed'

        if(remove):
            messageBody = 'You have lost the permissions of the ' + group + ' group.'
        else:
            messageBody = 'You have got the permissions of the ' + group + ' group.'

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