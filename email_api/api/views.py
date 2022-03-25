import logging

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from core.libraries.sys_params import SysParams as SystemParams
from django.core.mail import send_mail
from django.conf import settings

from email_api.models import SendMessage

sys_params = SystemParams()
logger = logging.getLogger(__name__)


@api_view(['POST'])
def sendEmail(request):
    email_to = request.data['email_to']
    mess_title = request.data['mess_title']
    mess_body = request.data['mess_body']
    from_to = settings.DEFAULT_FROM_EMAIL
    
    if request.method == "POST":
    
        send_mail(
            mess_title,
            mess_body,
            from_to,
            [email_to],
        )
        
        message = SendMessage.objects.create(
            email = email_to,
            mess_title = mess_title,
            mess_body = mess_body,
            status = 1
        )
        if message != None:
            message.save()
            
        return Response({"status": "success"}, status=status.HTTP_200_OK)
    
    return Response({"message": "method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
