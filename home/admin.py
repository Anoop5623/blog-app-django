from django.contrib import admin
from . import models


admin.site.register((models.blogmodel,models.blogcomment))





