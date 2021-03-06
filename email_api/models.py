from django.db import models


class SysParams(models.Model):
    param = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    comment = models.CharField(max_length=255)


class SendMessage(models.Model):
    email = models.EmailField(max_length=100)
    mess_title = models.CharField(max_length=255)
    mess_body = models.TextField()
    to = models.EmailField(max_length=100, db_column='from')
    create_time = models.DateTimeField(auto_now_add=True)
    sent_time = models.DateTimeField(auto_now_add=True)

    status = models.BooleanField(default=0)
