from django.contrib import admin
from timetracking.models import Project, Entry, EntryTime, EntryLog, Tag

class ProjectTagInline(admin.StackedInline):
    model = Tag.projects.through
    extra = 1
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('user', )
    list_diplay = ('title', 'datetime', 'user', )
    inlines = (ProjectTagInline, )
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
admin.site.register(Project, ProjectAdmin)

class EntryTagInline(admin.StackedInline):
    model = Tag.entries.through
    extra = 1
class EntryAdmin(admin.ModelAdmin):
    exclude = ('user', )
    list_display = ('body', 'project', 'user', 'estimated_time', 'active')
    list_display_links = ('body', )
    list_editable = ('estimated_time', )
    list_filter = ('active', )
    inlines = (EntryTagInline, )
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
    
admin.site.register(Entry, EntryAdmin)

class TagAdmin(admin.ModelAdmin):
    """ Administration for tags """
admin.site.register(Tag, TagAdmin)