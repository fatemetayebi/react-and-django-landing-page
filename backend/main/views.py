import json
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from config import settings
from rest_framework import generics
from .serializers import *


class ShowLevelView(generics.ListAPIView):
    serializer_class = ShowProductsSerializer
    queryset = Product.objects.filter(is_active=True)


def create(request):
    if request.method == "POST":
        data = json.dumps(request.POST)
        data = json.loads(data)
        print(data)
        contact = Contact(message=data["message"], name=data["name"], phone=data["phone"], email=data["email"])
        contact.save()

        # send email of contact us details
        subject = 'message from guitar site '
        message = f'{contact.name}`s message: {contact.message} \n\n'\
                  f' {contact.name}`s email:{contact.email}\n\n' \
                  f'{contact.name}`s phon number: {contact.phone}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['fatitayyebi@gmail.com', ]
        send_mail(subject, message, email_from, recipient_list)

        return HttpResponse('message sent')
