from django.contrib import admin

from .models import Task
from .models import Post

admin.site.register(Task)

admin.site.register(Post)