from django.contrib import admin
from createOpenProject.models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=["uploaded_at"]

admin.site.register(Project,ProjectAdmin)