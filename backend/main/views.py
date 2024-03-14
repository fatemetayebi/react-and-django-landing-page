import json
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from config import settings
from .serializers import *
import random
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action


class ShowLevelView(generics.ListAPIView):
    serializer_class = ShowProductsSerializer
    queryset = Product.objects.filter(is_active=True)


# def create(request):
#     if request.method == "POST":
#         data = json.dumps(request.POST)
#         data = json.loads(data)
#         print(data)
#         contact = Contact(message=data["message"], name=data["name"], phone=data["phone"], email=data["email"])
#
#         code = random.randrange(1111, 9999)
#         # send email of contact us details
#         subject = 'message from guitar site '
#         message = f'This is a message from electric guitar site.\n'\
#                   f'enter {code} to confirm your email and send your message\n'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [contact.email, ]
#         send_mail(subject, message, email_from, recipient_list)
#
#         return HttpResponse('message sent')


class SaveContactForm(viewsets.ViewSet):
    serializer_class = ContactFormSerializer
    code = random.randint(1111, 9999)

    @action(detail=False, methods=['post'])
    def send_email(self, request):
        data = request.data
        serializer = ContactFormSerializer(data=data)
        email = data['email']
        if serializer.is_valid():
            send_mail(
                'this is verify email from app',
                message=f'This is a message from electric guitar site.\n'
                        f'Enter {self.code} to confirm your email and send your message.\n',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def get_code(self, request):
        data = request.data
        serializer = ContactFormSerializer(data=data)
        entered_code = data['code']

        if entered_code == self.code:
            serializer.save()
            return Response({'success': True, 'message': 'your massage sent'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'success': False, 'message': 'entered code is wrong'}, status=status.HTTP_400_BAD_REQUEST)
