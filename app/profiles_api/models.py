from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Helps Django to work with custom user Model """
    def create_user(self, email, name, password=None):
        """ Creates new user profile object """
        if not email:
            raise ValueError('Users must provide email address')
        #normalize_email: function in BaseUserManager class
        #Helps to normalize the email, that is,
        #If user added : abc@XYZ.com --> abc@xyz.com
        email = self.normalize_email(email)
        #Now create the customized user MODEL by providing the details
        user = self.model(email=email, name=name)
        #set the password : will encrypt the password before storing
        user.set_password(password)
        #saves the user object to db:
        #      id (auto-incrementing) primary key gets increamented
        # using=DEFAULT_DB_ALIAS
        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, password):
        """ Creates and saves a new superuser with given details """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Customized User Profile """
    # Specify the fields that will comprise of the profile model
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    #Specify which field will be used to login
    USERNAME_FIELD = 'email'
    #Mandatory fields
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Used to get full name of the user """
        return self.name

    def get_short_name(self):
        """ Used to get short name of the user """
        return self.name

    def __str__(self):
        """ Convert Object to string : Readable format """
        return self.email
