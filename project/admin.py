from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Project)
admin.site.register(Project_Team)
admin.site.register(Status)
admin.site.register(Project_Module)
admin.site.register(Project_Task)
admin.site.register(User_Task)
admin.site.register(Badge)
admin.site.register(Task_Badge)
