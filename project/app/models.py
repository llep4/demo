from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone

STATUS=(
    ('Новая', 'Новая'),
    ('Одобрено', 'Одобрено'),
    ('Отклонено', 'Отклонено'),
)

class User(AbstractUser):
    full_name = models.CharField(max_length=254, verbose_name="ФИО", blank=False)
    username = models.CharField(max_length=254, verbose_name="Логин", blank=False, unique=True)
    password = models.CharField(max_length=254, verbose_name="Пароль", blank=False)
    phone = models.CharField(
        max_length=30,
        verbose_name="Номер телефона",
        blank=False,
        unique=True,
        validators=[
            RegexValidator(
            regex=r"\+7\(\d\d\d\)-\d\d\d-\d\d-\d\d",
            message="Введите телефон +7 (ххх)-ххх-хх-хх",
            code="invalid_phone_number",
            )
        ]
    )
    email = models.EmailField(max_length=254, verbose_name="Почта", blank=False, unique=True)

class Statment(models.Model):
    title = models.CharField(max_length=254, verbose_name="Название", blank=False, null=False)
    description = models.CharField(max_length=254, verbose_name="Описание", blank=False, null=False)
    status = models.CharField(max_length=254, verbose_name='Статус', choices=STATUS, default='Новая')
    created_at = models.DateTimeField(auto_now_add=True)
    set_time = models.DateTimeField(default=timezone.now(), verbose_name='Выбрать время', blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering=["-created_at"]