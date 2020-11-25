from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Ebook, Comment

#Register your models here.
#admin.site.register(Category)
#admin.site.register(Ebook)
#admin.site.register(Comment)

class EbookAdmin(UserAdmin):

    list_display=('title','authors','pages','price','image','ebook','user')
    search_fields = ('title','authors','pages','price','image','ebook','user__username')
    list_filter=()

    filter_horizontal=()
    fieldsets =()
    ordering=()

class CommentAdmin(UserAdmin):
    list_display=('body','ebook','user')
    search_fields = ('body','ebook__ebook','user__username')
    list_filter=()

    filter_horizontal=()
    fieldsets =()
    ordering=()


admin.site.register(Comment , CommentAdmin)
admin.site.register(Ebook , EbookAdmin)