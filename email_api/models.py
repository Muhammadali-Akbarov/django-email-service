from django.db import models


class SysParams(models.Model):
    param = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    comment = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'max_taxi_system_params'


class SendMessage(models.Model):
    sent_time = models.DateTimeField(null=True)
    status = models.BooleanField(default=0)

    class Meta:
        managed = False
        db_table = 'max_mail_send_message'