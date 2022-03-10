import logging

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from core.libraries.sys_params import SysParams as SystemParams
from django.core.mail import send_mail

sys_params = SystemParams()
logger = logging.getLogger(__name__)

@api_view(['POST'])
def sendEmail(request):
    is_email_enabled = (sys_params.as_dict().get("is_email_enabled", 0))
    
    email_to = request.data['email']
    mess_title = request.data['mess_title']
    mess_body = request.data['mess_body']
    from_to = request.data['from_to']

    if request.method == "POST" and is_email_enabled:

        send_mail(
            mess_title,
            mess_body,
            from_to,
            [email_to],
            fail_silently=False,
        )

        return Response({"message": "Email has been sent successfully"}, status=status.HTTP_200_OK)

    return Response({"message": "method not allowed or is_email_enabled is not enabled"})
