from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext

class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__username = ext.ExtStringField(name='username', label='Логин', allow_blank=False, anchor='100%')
        self.field__first_name = ext.ExtStringField(name='first_name', label='Имя', anchor='100%')
        self.field__last_name = ext.ExtStringField(name='last_name', label='Фамилия', anchor='100%')
        self.field__email = ext.ExtStringField(name='email', label='Email', anchor='100%')
        self.field__is_active = ext.ExtCheckBox(name='is_active', label='Активный',anchor='100%', checked=True)
        self.field__is_staff = ext.ExtCheckBox(name='is_staff', label='Персонал',anchor='100%', checked=False)
        self.field__last_login = ext.ExtDateField(name='last_login',label='Последний вход',anchor='100%', format='d.m.Y')
        self.field__date_joined = ext.ExtDateField(name='date_joined', label='Дата регистрации',anchor='100%', format='d.m.Y')
        self.field__is_superuser = ext.ExtCheckBox(name='is_superuser', label='Администратор',anchor='100%')
        self.field__password = ext.ExtStringField(name='password',label='Пароль',anchor='100%')


    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_active,
            self.field__is_staff,
            self.field__date_joined,
            self.field__last_login,
            self.field__is_superuser,
            self.field__password
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'
        self.title='User: Добавление'


class UserEditWindow(BaseEditWindow):

    def _init_components(self):
        super(UserEditWindow, self)._init_components()

        self.field__username = ext.ExtStringField(name='username', label='Логин', allow_blank=False, anchor='100%')
        self.field__first_name = ext.ExtStringField(name='first_name', label='Имя', anchor='100%')
        self.field__last_name = ext.ExtStringField(name='last_name', label='Фамилия', anchor='100%')
        self.field__email = ext.ExtStringField(name='email', label='Email', anchor='100%')
        self.field__is_active = ext.ExtCheckBox(name='is_active', label='Активный', anchor='100%')
        self.field__is_staff = ext.ExtCheckBox(name='is_staff', label='Персонал', anchor='100%')
        self.field__last_login = ext.ExtDateField(name='last_login', label='Последний вход', anchor='100%', format='d.m.Y')
        self.field__date_joined = ext.ExtDateField(name='date_joined', label='Дата регистрации', anchor='100%', format='d.m.Y')
        self.field__is_superuser = ext.ExtCheckBox(name='is_superuser', label='Администратор', anchor='100%')
        self.field__password = ext.ExtStringField(name='password', label='Пароль', anchor='100%')

    def _do_layout(self):
        super(UserEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_active,
            self.field__is_staff,
            self.field__date_joined,
            self.field__last_login,
            self.field__is_superuser,
            self.field__password
        ))

    def set_params(self, params):
        super(UserEditWindow, self).set_params(params)
        self.height = 'auto'
        self.title = 'User: Редактирование'
