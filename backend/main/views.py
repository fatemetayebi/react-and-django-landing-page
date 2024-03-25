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
from rest_framework.views import APIView


class ShowProductView(generics.ListAPIView):
    serializer_class = ShowProductsSerializer
    queryset = Product.objects.filter(is_active=True)



code = random.randint(1111, 9999)


class SendCodeView(APIView):
    serializer_class = ContactFormSerializer

    # @action(detail=False, methods=['post'])
    def post(self, request):
        data = json.dumps(request.POST)
        data = json.loads(data)
        # data = request.data

        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        request.session['email'] = email
        request.session['message'] = message
        request.session['subject'] = subject
        data = {
            'email': email,
            'subject': subject,
            'message': message
        }

        serializer = ContactFormSerializer(data=data)
        if serializer.is_valid():
            send_mail(
                'this is verify email from app',
                message=f'This is a message from electric guitar site.\n'
                        f'Enter {code} to confirm your email and send your message.\n',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyCodeView(APIView):
    serializer_class = CodeSerializer

    # @action(detail=False, methods=['post'])
    def post(self, request):
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            input_code = serializer.validated_data['entered_code']

            if input_code == code:
                SendEmailView.create(request)
                return Response({'success': True, 'message': 'your massage sent'}, status=status.HTTP_201_CREATED)

            else:
                return Response({'success': False, 'message': 'entered code is wrong'},
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def create(request):
    #     subject = request.session.get('subject')
    #     message = request.session.get('message')
    #     email = request.session.get('email')
    #     contact = Contact(message=message, subject=subject, email=email)
    #     contact.save()
    #
    #     # send email of contact us details
    #     subject = 'message from guitar site '
    #     message = f'email : {email}.\n'\
    #               f'subject : {subject}\n' \
    #               f'message : {message}\n'
    #     email_from = settings.EMAIL_HOST_USER
    #     recipient_list = [contact.email, ]
    #     send_mail(subject, message, email_from, recipient_list)
    #
    #     return HttpResponse('message sent')


class SendEmailView(APIView):
    serializer_class = ContactFormSerializer

    def create(request):
        subject1 = request.session.get('subject')
        message = request.session.get('message')
        email = request.session.get('email')
        contact = Contact(message=message, subject=subject1, email=email)
        print(f'{contact.message}  ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg')
        serializer = ContactFormSerializer(data=contact)
        if serializer.is_valid():
            serializer.save()

            # send email of contact us details
            subject = 'message from guitar site '
            message = f'email : {email}.\n' \
                      f'subject : {subject1}\n' \
                      f'message : {message}\n'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['fatitayyebi@gmail.com', 'nuclearsystem2022@gmail.com', ]
            send_mail(subject, message, email_from, recipient_list)
            return HttpResponse('message sent')
