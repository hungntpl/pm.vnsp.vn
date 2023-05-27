from django.db import models
from django.utils.timezone import now
# Create your models here.
class sparepart(models.Model):

    WAREHOUSE_LOC = [
        ('L', 'PI'),
        ('S', 'PR'),
    ]
    Def = 'S'

    spid = models.CharField(primary_key=True, max_length=25,verbose_name = "Số ID")
    whloc = models.CharField(max_length=1, blank=True, null=True,verbose_name = "Tên kho",choices=WAREHOUSE_LOC, default=Def) 
    ename = models.CharField(max_length=255, blank=True, null=True,verbose_name = "Tên gọi tiếng Anh")
    vname = models.CharField(max_length=255, blank=True, null=True,verbose_name = "Tên gọi tiếng Việt")
    spec = models.CharField(max_length=255, blank=True, null=True,verbose_name = "SPEC")
    remarks = models.CharField(max_length=255, blank=True, null=True,verbose_name = "Ghi chú")
    
    def __str__(self):
        return str(self.spid)
    
    class Meta:
        verbose_name = 'Spare part list'
        verbose_name_plural = "Danh mục phụ tùng"


class section(models.Model):

    secid = models.CharField(primary_key=True, max_length=25,verbose_name = "Bộ phận sử dụng") 
    secname = models.CharField(max_length=255, blank=True, null=True,verbose_name = "Tên gọi")
    remarks = models.CharField(max_length=255, blank=True, null=True,verbose_name = "Ghi chú")
    
    def __str__(self):
        return str(self.secid)
    
    class Meta:
        verbose_name = 'Section list'
        verbose_name_plural = "Bộ phận sử dụng"

class exportnote(models.Model):

    doexp = models.DateField(default=now, verbose_name = "Ngày xuất kho")  
    spid = models.ForeignKey(sparepart,default=None, on_delete=models.CASCADE, max_length=25, verbose_name= 'Mã sản phẩm')
    qty = models.IntegerField(default='1', blank=False, null=False, verbose_name = "Số lượng xuất kho")
    secid = models.ForeignKey(section, blank=False, null=False, on_delete=models.CASCADE, max_length=25, verbose_name= 'Bộ phận sử dụng')
    purpose = models.CharField(max_length=255, blank=True, null=True,verbose_name = "Mục đích sử dụng")
    expmc = models.CharField(max_length=255, blank=True, null=True,verbose_name = "QR Scanner")
    remarks = models.CharField(max_length=255, blank=True, null=True,verbose_name = "Ghi chú")
    
    
    def fname(self):
        return str(sparepart.objects.filter(spid= self.spid).values_list('vname', flat=True).first()) + "-" + str(sparepart.objects.filter(spid= self.spid).values_list('ename', flat=True).first())
    
    def whloc(self):
        return str(sparepart.objects.filter(spid= self.spid).values_list('whloc', flat=True).first())
    # def fname(self):
    #     return "{} {} {}".format(self.spid,self.qty, self.expmc)
    
    def __str__(self):
        return str(self.spid)
    
    class Meta:
        verbose_name = 'Export notice'
        verbose_name_plural = "Phiếu xuất kho"


