# from django import forms
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import Group


# from django.conf import settings

# from merchants.models import Merchant


# class MerchantAdmin(BaseUserAdmin):



# # Now register the new UserAdmin...
# admin.site.register(Merchant, MerchantAdmin)
# # ... and, since we're not using Django's built-in permissions,
# # unregister the Group model from admin.
# admin.site.unregister(Group)
from django.contrib import admin
from merchants.models import Merchant

admin.site.register(Merchant)
