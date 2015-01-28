from django.contrib import admin

# Register your models here.
from .models import Chapter, Novel
for m in (Chapter, Novel):
    admin.site.register(m)
