from django.contrib.auth.models import User, Permission,Group
from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver

@receiver(m2m_changed, sender=User.groups.through)
def save(sender,pk_set,action, **kwargs):
    for pk in pk_set:
        groups = Group.objects.filter(id=pk)
        for g in groups:
            if action == 'pre_remove':
                print('Remove Group: ' + str(g))
            if action == 'pre_add':
                print('Added Group: ' + str(g))

