from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.ui import ModelEditWindow

from app.ui import UserAddWindow, UserEditWindow


class ContentTypePack(ObjectPack):
    model=ContentType

    add_to_menu=True
    add_to_desktop=True

    add_window = ModelEditWindow.fabricate(model=ContentType)
    add_windows = edit_window = ModelEditWindow.fabricate(model=ContentType)
    can_delete = True

    title="Content types"

class UserPack(ObjectPack):
    model=User

    add_to_menu=True
    add_to_desktop=True

    add_window = UserAddWindow
    add_windows = edit_window = UserEditWindow
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
    add_windows = edit_window = ModelEditWindow.fabricate(model=Group)
    can_delete = True

    title="Groups"

class PermissionPack(ObjectPack):
    model=Permission

    add_to_menu = True
    add_to_desktop = True

    add_window = ModelEditWindow.fabricate(model=Permission)
    add_windows = edit_window = ModelEditWindow.fabricate(model=Permission)
    can_delete = True

    title="Permissions"
