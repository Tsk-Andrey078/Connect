from django.contrib import admin

from .models import account, chats, message
# Register your models here.
admin.site.register(chats)
admin.site.register(message)
admin.site.register(account)