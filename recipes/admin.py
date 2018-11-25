from django.contrib import admin
from .models import recipes, post, testerStatus, uatStatus

# admin.site.register(recipes)
# admin.site.register(post)
admin.site.register(testerStatus)
admin.site.register(uatStatus)