from django.contrib import admin
from . import models


#Register the user model with admin so we can use it /admin page
admin.site.register(models.UserProfile)
