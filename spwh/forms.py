from django.db import models
from django.forms import ModelForm
from .models import exportnote
from django import forms

# class Book(models.Model):
#     name = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)
class inputmanual(forms.Form):
    pk = forms.CharField(label='the key', max_length=100)
    
class ExpNoteForm(ModelForm):
    vname = forms.CharField(label="Tên gọi")
    class Meta:
        model = exportnote
        # fields = pass
        fields = '__all__'
        # fields = ['doexp', 'spid','qty','remarks']
        # exclude = ("doexp", )
    field_order = ['spid','vname', 'qty','secid','purpose','remarks']

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields['spid'].widget.can_change_related = False
    #     form.base_fields['spid'].widget.can_add_related = False
    #     return form