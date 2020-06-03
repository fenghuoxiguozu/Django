import xadmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,)
from xadmin.layout import Fieldset, Main, Side
from django.forms import ModelMultipleChoiceField
from django.utils.translation import ugettext as _


ACTION_NAME = {
    'add': _('Can add %s'),
    'change': _('Can change %s'),
    'edit': _('Can edit %s'),
    'delete': _('Can delete %s'),
    'view': _('Can view %s'),
}


def get_permission_name(p):
    action = p.codename.split('_')[0]
    if action in ACTION_NAME:
        return ACTION_NAME[action] % str(p.content_type)
    else:
        return p.name


class PermissionModelMultipleChoiceField(ModelMultipleChoiceField):

    def label_from_instance(self, p):
        return get_permission_name(p)

class UserAdmin(object):
    # change_user_password_template = None

    list_display = ('id', 'nickname','uid','sex') + BaseUserAdmin.list_display
    list_filter = ('is_superuser', 'is_active')
    readonly_fields = ['last_login']
    search_fields = ('username',)
    model_icon = 'fa fa-user'
    relfield_style = 'fk-ajax'
    style_fields = {'user_permissions': 'm2m_transfer'}

    def get_model_form(self, **kwargs):
        if self.org_obj is None:
            self.form = UserCreationForm
        else:
            self.form = UserChangeForm
        return super(UserAdmin, self).get_model_form(**kwargs)

    def get_field_attrs(self, db_field, **kwargs):
        attrs = super(UserAdmin, self).get_field_attrs(db_field, **kwargs)
        if db_field.name == 'user_permissions':
            attrs['form_class'] = PermissionModelMultipleChoiceField
        return attrs

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset('其他字段',
                             'nickname', 'last_login'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                ),
                Side(
                    Fieldset(('Status'),
                             'is_active', 'is_superuser','is_deleted'
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()

xadmin.site.register(User, UserAdmin)