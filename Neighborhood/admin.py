from django.contrib import admin

from .models import *
admin.site.register(Neighborhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(ContactInfo)