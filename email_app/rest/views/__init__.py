from rest_framework.response import Response
from django.core.mail import send_mail
from core.rest.permission import IsOrganizationMember
from email_app.rest.serializers import EmailSerializer
from rest_framework import generics


class EmailView(generics.CreateAPIView):
    serializer_class = EmailSerializer
    permission_classes = [IsOrganizationMember]

    def perform_create(self, serializer):
        subject = serializer.validated_data["subject"]
        message = serializer.validated_data["message"]
        sender = self.request.user.email
        recipient_list = serializer.validated_data["recipient_list"]

        send_mail(
            subject,
            message,
            sender,
            recipient_list,
            fail_silently=False,
        )

        return Response({"message": "Email sent successfully"})


# def post(self, request, *args, **kwargs):
#     serializer = EmailSerializer(data=request.data)

#     if serializer.is_valid():
#         subject = serializer.validated_data["subject"]
#         message = serializer.validated_data["message"]
#         recipient_list = serializer.validated_data["recipient_list"]

#         # Send the email without a template
#         send_mail(
#             subject,
#             message,
#             "your_email@gmail.com",
#             recipient_list,
#             fail_silently=False,
#         )

#         return Response({"message": "Email sent successfully"})
#     else:
#         return Response(serializer.errors, status=400)
