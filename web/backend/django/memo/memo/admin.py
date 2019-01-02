from django.contrib import admin
from .models import Memo


class MemoAdmin(admin.ModelAdmin):
    fields = ('content', )


admin.site.register(Memo, MemoAdmin)
