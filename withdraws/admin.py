from django.contrib import admin

# Register your models here.

from django.contrib import admin
from withdraws.models import Withdraw

admin.site.register(Withdraw)
