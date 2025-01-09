from django.db import models
from common.models import BaseModel
from django.contrib.auth.models import AbstractUser
from .usermanager import CustomUserManager


class Users(BaseModel, AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "AD", "Admin"
        CUSTOMER = "CU", "Customer"

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    profile_pic = models.ImageField(
        upload_to="users/profile_pic", null=True, blank=True
    )
    phone_number = models.PositiveSmallIntegerField(unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    role = models.CharField(
        max_length=200, choices=Role.choices, default=Role.CUSTOMER
    )

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
