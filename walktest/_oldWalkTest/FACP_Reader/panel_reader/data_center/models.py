from django.db import models


class Test(models.Model):
    panel_types = [
        ('320', '320'),
        ('640', '640'),
        ('2-3030', '2-3030') 
    ]
    site_name = models.CharField(max_length=100)
    panel_type = models.CharField(max_length=100, choices=panel_types, default=None)
    test_date = models.DateTimeField(auto_now=True)
    device_list = models.FileField(upload_to='', default=None, null=False)
    alarm_history = models.FileField(upload_to='', default=None, null=False)
    test_results = models.FileField(upload_to='', default=None, null=True)


    def __str__(self):
        return self.site_name
