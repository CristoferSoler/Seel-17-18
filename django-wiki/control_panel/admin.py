from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.utils.translation import ugettext_lazy

from bsi.forms import LoginForm
from bsi.models import permissions


class NoStaffAdmin(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Admin Control Panel')

    # Text to put in each page's <h1>.
    site_header = ugettext_lazy('Administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

    login_form = LoginForm

    def has_permission(self, request):
        """
        Removed check for is_staff.
        """
        return permissions.can_add_change_delete_users(request.user)


user_admin_site = NoStaffAdmin(name='control_panel')
user_admin_site.register(User, UserAdmin)
user_admin_site.register(Group, GroupAdmin)