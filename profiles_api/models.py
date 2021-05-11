from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# This is our user model maanger
class userProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, name, email, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must specify an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name) # new model of the user

        user.set_password(password) # providing encryption
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save new super user with given details"""
        user = self.create_user(name, email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



# This is our user model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in this system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #model manager which is going to be custom
    objects = userProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Returns the full name of the user"""
        return self.name

    def get_short_name(self):
        """Returns short name of the user"""
        return self.name

    def __str__(self):
        """Return string representation of the user(model)"""
        return self.email
