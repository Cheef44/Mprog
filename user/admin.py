from django.contrib import admin
from .models import UserComments
from .models import UserStatus

admin.site.register(UserComments)
admin.site.register(UserStatus)