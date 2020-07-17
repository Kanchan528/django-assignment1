from django.contrib import admin
from .models import AuthorInfo, Blog

# Register your models here.
admin.site.register(AuthorInfo)
admin.site.register(Blog)
