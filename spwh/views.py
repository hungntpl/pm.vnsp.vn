from django.shortcuts import render
from django.shortcuts import redirect
# from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
# from django.contrib import messages
from .models import *
from uuid import getnode as get_mac

from .forms import ExpNoteForm, inputmanual
import socket

# Create your views here.

class PrintQR(LoginRequiredMixin, generic.DetailView):
    model = sparepart
    template_name = 'spwh/printqr.html'  # Specify your own


def prescancard(request):
    return render(request, "spwh/prescanqr.html")

def scancard(request):
    if request.method == "POST":
        form = inputmanual(request.POST)
        if form.is_valid():
            # expnote = form.save(commit=False)
            pk = form.cleaned_data['pk']
            # expnote.remarks = request.remarks
            # expnote.save()
            # return HttpResponseRedirect(reverse('submit export note'))
            return redirect('submit export note', pk=pk)
            # return redirect("submit export note")
    # form = ExpNoteForm(initial={'spid': pk, 'expmc': socket.gethostname(), 'vname': sparepart.objects.filter(spid= pk).values_list('vname', flat=True).first()})

    # form = ExpNoteForm(initial={'spid': pk, 'expmc': get_mac(), 'vname': sparepart.objects.filter(spid= pk).values_list('vname', flat=True).first()})
    # else:
    #     form = ExpNoteForm(initial={'spid': pk, 'expmc': sparepart.objects.filter(spid= pk).values_list('whloc', flat=True).first(), 'vname': sparepart.objects.filter(spid= pk).values_list('vname', flat=True).first()})
    else:
        form = inputmanual()
    # form.fields["spid"].disabled = True
    # form.fields["doexp"].disabled = True
        # form.fields["spid"].widget.attrs["readonly"] = True
        # form.fields["doexp"].widget.attrs["readonly"] = True
        # form.fields["vname"].widget.attrs["readonly"] = True
        # form.fields["expmc"].widget.attrs["readonly"] = True
    # form.fields["doexp"].widget.attrs["hidden"] = True
    
    

    return render(request, "spwh/scanqr.html", {"form": form})

def submitExNote(request, pk):

    if request.method == "POST":
        form = ExpNoteForm(request.POST)
        if form.is_valid():
            expnote = form.save(commit=False)
            # messages.info(request, 'Xuất kho thành công!')
            # expnote.remarks = request.remarks
            expnote.save()
            # return HttpResponseRedirect(reverse('submit export note'))
            return redirect('success exported')
            # return redirect("submit export note")
    # form = ExpNoteForm(initial={'spid': pk, 'expmc': socket.gethostname(), 'vname': sparepart.objects.filter(spid= pk).values_list('vname', flat=True).first()})

    # form = ExpNoteForm(initial={'spid': pk, 'expmc': get_mac(), 'vname': sparepart.objects.filter(spid= pk).values_list('vname', flat=True).first()})
    else:
        form = ExpNoteForm(initial={'spid': pk, 'expmc': sparepart.objects.filter(spid= pk).values_list('whloc', flat=True).first(), 'vname': sparepart.objects.filter(spid= pk).values_list('vname', flat=True).first()})

    # form.fields["spid"].disabled = True
    # form.fields["doexp"].disabled = True
    # form.fields["spid"].widget.attrs["can_change_related"] = False
    form.fields["spid"].widget.can_change_related = False
    form.fields["doexp"].widget.attrs["readonly"] = True
    form.fields["vname"].widget.attrs["readonly"] = True
    form.fields["expmc"].widget.attrs["readonly"] = True
    # form.fields["doexp"].widget.attrs["hidden"] = True
    
    

    return render(request, "spwh/suben.html", {"form": form})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip