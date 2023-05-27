from django.urls import path
from . import views
from django.views.generic import TemplateView
#from .views import some_view

urlpatterns = [

    path('spwh/sparepart/<pk>/printqr/', views.PrintQR.as_view(), name='QR-print'),
    path('spwh/sparepart/scan/',views.scancard, name='scan qr code'),
    path('spwh/sparepart/scan/search/',TemplateView.as_view(template_name="spwh/suben.html"), name='submit search code'),
    path('spwh/sparepart/prescan/',views.prescancard, name='prescan qr code'),
    path('spwh/sparepart/sbexnote/success/',TemplateView.as_view(template_name="spwh/subenok.html"), name='success exported'),
    path('spwh/sparepart/sbexnote/<pk>',views.submitExNote, name='submit export note'),
    
    path('spwh/sparepart/qrtest/',TemplateView.as_view(template_name="spwh/qrtest.html"), name='qr scan test'),
    
]

