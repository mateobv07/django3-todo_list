from django.contrib import admin
from .models import Todo

# Adding read only field for when it was created in admin panel
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

admin.site.register(Todo, TodoAdmin)
