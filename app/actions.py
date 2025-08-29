from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.ui import ModelEditWindow
from app.ui import UserAddWindow, UserEditWindow, PermissionAddWindow, PermissionEditWindow


class ContentTypePack(ObjectPack):
    model=ContentType

    add_to_menu=True
    add_to_desktop=True

    add_window = ModelEditWindow.fabricate(model=ContentType)
    edit_window = ModelEditWindow.fabricate(model=ContentType)
    can_delete = True

    title="Content types"

class UserPack(ObjectPack):
    model=User

    add_to_menu=True
    add_to_desktop=True

    add_window = UserAddWindow
    edit_window = UserEditWindow
    can_delete = True

    columns=[
        {'data_index': 'username', 'header': 'Логин'},
        {'data_index': 'first_name', 'header': 'Имя',},
        {'data_index': 'last_name', 'header': 'Фамилия'},
        {'data_index': 'email', 'header': 'Почта'},
        {'data_index': 'is_active', 'header': 'Активность'},
        {'data_index': 'date_joined', 'header': 'Дата регистрации'},
        {'data_index': 'last_login', 'header': 'Последний вход'}
             ]

    title="Users"

class GroupPack(ObjectPack):
    model=Group

    add_to_menu=True
    add_to_desktop=True

    add_window = ModelEditWindow.fabricate(model=Group)
    edit_window = ModelEditWindow.fabricate(model=Group)
    can_delete = True

    title="Groups"

class PermissionPack(ObjectPack):
    model=Permission

    add_to_menu = True
    add_to_desktop = True

    add_window=PermissionAddWindow
    edit_window=PermissionEditWindow
    can_delete = True

    columns = [
        {'data_index': 'name'},
        {'data_index': 'content_type'},
        {'data_index': 'codename'},
    ]

    title="Permissions"

    def save_row(self, obj, create_new, request, context):
        ct_pk = (request.POST.get('content_type__pk')  or request.POST.get('content_type_id') or request.POST.get('content_type'))
        obj.content_type_id = int(ct_pk)
        return super().save_row(obj, create_new, request, context)
