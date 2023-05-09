from django.contrib import admin
from apps.inventory.models import * 

# Register your models here.
admin.site.register(Article)
admin.site.register(Ordering)
admin.site.register(OrderingArticle)
