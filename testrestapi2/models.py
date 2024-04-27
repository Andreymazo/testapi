from django.db import models

class HistoryApi(models.Model):
    cad_num = models.CharField()
    shirota = models.CharField()
    dolgota = models.CharField()
    created = models.DateTimeField(auto_now_add=True)


