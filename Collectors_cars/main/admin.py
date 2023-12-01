from django.contrib import admin

from .models import Post

admin.site.register(Post)

#@admin.register(Post)
#class BlogAdmin(admin.ModelAdmin):
#    autocomplete_fields = ['author']
#    list_display = ('title', 'scale', 'text', 'date_pub')

#    def get_form(self, request, obj=None, **kwargs):
#        form = super(BlogAdmin, self).get_form(request, obj, **kwargs)
#        form.base_fields['author'].initial = request.user

#        if str(request.user) !='admin':
#            form.base_fields['author'].disabled = request.user