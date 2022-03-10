from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from core.libraries.sys_params import SysParams as SystemParams
from django.core.mail import send_mail

sys_params = SystemParams()


@api_view(['POST'])
def sendEmail(request):
    s3_enabled = (sys_params.as_dict().get("S3_ENABLED", 0))

    email_to = request.data['email']
    mess_title = "This is message title"
    mess_body = "This is message body"
    from_to = "MyTaxi <noreply@mytaxi.uz>"

    if request.method == "POST" and s3_enabled:

        send_mail(
            mess_title,
            mess_body,
            from_to,
            [email_to],
            fail_silently=False,
        )

        return Response("Email has been sent successfully", status=status.HTTP_200_OK)

    return Response({"error": {
                        "message": "method not allowed or s3_params is not enabled"
                    }}, 
                    status=status.HTTP_405_METHOD_NOT_ALLOWED)
