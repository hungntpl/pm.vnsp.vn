from django.contrib import admin
# Register your models here.
from import_export.admin import ExportActionModelAdmin
from django.template.response import TemplateResponse
from .models import *

# admin.site.register(sparepart)



from import_export import resources, forms
from import_export.admin import ImportExportModelAdmin

class spResource(resources.ModelResource):

    class Meta:
        model = sparepart
        import_id_fields = ['spid']
        # skip_unchanged = True
        # report_skipped = True
        # # exclude = ('id')
        # fields = ('id','spid','whloc','ename','vname','spec','remarks')

class SectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(section, SectionAdmin)

class spAdmin(ImportExportModelAdmin):

    resource_class = spResource
    list_display = ('spid','whloc','ename','vname','spec','remarks')
    list_display_links = ['spid']
    list_filter = ['whloc']
    search_fields = ('spid','whloc','ename','vname','spec','remarks')

admin.site.register(sparepart,spAdmin)


class enResource(resources.ModelResource):

    class Meta:
        model = exportnote

        # import_id_fields = ['spid']
        # skip_unchanged = True
        # report_skipped = True
        # # exclude = ('id')
        # fields = ('id','spid','whloc','ename','vname','spec','remarks')

    # def __init__(self, form_fields=None):
    #     super().__init__()
    #     self.form_fields = form_fields

    # def get_export_fields(self):
    #     return [self.fields[f] for f in self.form_fields]

# class BookExportForm(forms.ExportForm):
#     pass
    # Add your logic to read fields from the form

# class enAdmin(ImportExportModelAdmin):

#     resource_class = enResource
#     list_display = ('spid','doexp','qty','purpose','remarks')
#     list_display_links = ['spid']
#     list_filter = ['doexp','expmc']
#     search_fields = ('spid__spid','expmc','doexp','purpose','remarks')

#     def get_export_resource_kwargs(self, request, *args, **kwargs):
#         formats = self.get_export_formats()
#         form = BookExportForm(formats, request.POST or None)
#         # get list of fields from form (hard-coded to 'author' for example purposes)
#         form_fields = ('spid','doexp','qty','purpose',)
#         return {"form_fields": form_fields}



# admin.site.register(exportnote,enAdmin)

# @admin.action(description='Lập phiếu xuất kho cho những mục đã chọn')



class enAdmin(ExportActionModelAdmin):
    resource_class = enResource
    list_display = ('spid','fname','secid','expmc','doexp','qty','purpose','remarks')
    list_display_links = ['spid']
    list_filter = ['doexp','secid','expmc']
    search_fields = ('spid__spid','expmc','doexp','purpose','remarks')

    # actions = ("make_exp_sum", "make_NG") # Necessary 
    actions = ["make_exp_sum"] # Necessary 

    @admin.action(description='Tổng hợp phiếu xuất kho')
    def make_exp_sum(modeladmin, request, queryset):
        # queryset.update(purpose='OK')
        return TemplateResponse(request, 'spwh/multi_export_note.html', {'entries': queryset})

    # @admin.action(description='Mark selected purpose as NG')
    # def make_NG(modeladmin, request, queryset):
    #     queryset.update(purpose='NG')

admin.site.register(exportnote,enAdmin)

