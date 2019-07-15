from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import Permission, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Користувачі повинні мати email адресу')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(password=password, email=email)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    class Meta:
        db_table = 'user'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['post', 'first_name', 'last_name', 'date_birth']

    email = models.EmailField('Електронна пошта', unique=True)
    first_name = models.CharField('Ім\'я', max_length=30)
    last_name = models.CharField('Прізвище', max_length=50)
    date_birth = models.DateField('Дата народження')
    post = models.CharField('Посада', max_length=100)
    image = models.ImageField('Зображення', blank=True, upload_to='users')
    is_staff = models.BooleanField('Менеджер', default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = UserManager()
