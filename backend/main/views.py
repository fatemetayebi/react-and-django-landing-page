from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from config import settings
from .serializers import *
import random
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.sessions.backends.db import SessionStore
import json

# Generate a random 4-digit code
code = random.randint(1111, 9999)


def reset_value():
    global code
    code = random.randint(1111, 9999)


# API view to list active products
class ShowProductView(generics.ListAPIView):
    serializer_class = ShowProductsSerializer
    queryset = Product.objects.filter(is_active=True)


# API view to send verification code via email
class SendCodeView(APIView):
    serializer_class = ContactFormSerializer

    def post(self, request):
        # different ways to get data
        # data = json.loads(request.body)
        # data = json.dumps(request.POST)
        # email = request.data.get('email')

        # Extracting email, subject, and message from the request data
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')

        # Creating a dictionary to hold the data
        data = {
            'email': email,
            'subject': subject,
            'message': message
        }

        # print(f'{data}')
        # Serializing the contact form data
        serializer = ContactFormSerializer(data=data)
        if serializer.is_valid():
            # Save the contact form data if valid
            serializer.save()

            # Create a new session and store email, subject, and message
            session = SessionStore()
            session['email'] = email
            session['subject'] = subject
            session['message'] = message
            session.save()

            # Get the session key for later reference
            session_key = session.session_key

            # Check if code is expired
            if code == 0:
                reset_value()
            else:
                # Email user the verification code
                send_mail(
                    'this is verify email from app',
                    message=f'This is a message from electric guitar site.\n'
                            f'Enter {code} to confirm your email and send your message.\n',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                )

                # Return the session key and serialized data in the response
                return Response({'session_key': session_key, 'data': serializer.data}, status=status.HTTP_201_CREATED)

        # If validation fails, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API view to verify the code entered by the user
class VerifyCodeView(APIView):
    serializer_class = CodeSerializer

    def post(self, request):
        # Serialize the entered code
        serializer = CodeSerializer(data=request.data)
        # print(f'{request.data}ffffffffffffffffffffffffffffffff')
        if serializer.is_valid():
            input_code = serializer.validated_data['entered_code']

            # Check if the entered code matches the generated code
            if int(input_code) == int(code):
                # print("input_code is equal to code")
                # If the code is correct, trigger the SendEmailView's create method
                SendEmailView.create(request)
                return Response({'success': True, 'message': 'your code is correct'}, status=status.HTTP_201_CREATED)

            else:
                # If the code is wrong, return an error response
                return Response({'message': 'entered code is wrong'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            # If serializer validation fails, return the errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API view to send the contact form data to the admin's email after code verification
class SendEmailView(APIView):
    serializer_class = ContactFormSerializer

    # Custom create method to handle sending the email
    def create(request):
        # Retrieve session_key from the request data
        session_key = request.data.get('session_key')
        # print(session_key)

        if session_key:
            # Load the session using the session key
            session = SessionStore(session_key=session_key)

            # Check if the session exists
            if session.exists(session_key):
                # Retrieve email, subject, and message from the session
                subject1 = session.get('subject')
                message = session.get('message')
                email = session.get('email')

                # Prepare the data for serialization
                data = {
                    'email': email,
                    'subject': subject1,
                    'message': message
                }
                # print(f'{data} ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg')

                # Serialize the data
                serializer = ContactFormSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()

                    # Prepare the email details
                    subject = 'Message From Guitar Site'
                    message = f'email : {email}.\n' \
                              f'subject : {subject1}\n' \
                              f'message : {message}\n'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = ['fatitayyebi@gmail.com', ]

                    # Send the email to the admin
                    send_mail(subject, message, email_from, recipient_list)
                    # Handle code expiration
                    global code
                    code = 0
                    return HttpResponse('message sent')
                else:
                    # print('message didnt sendddddddddddddddddddddddddd')
                    # If validation fails, return an error response
                    return Response({'success': False, 'message': 'sending your message is failed'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                # If the session does not exist, return an error response
                return Response({'success': False, 'message': 'session not found'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # If no session key is provided, return an error response
            return Response({'success': False, 'message': 'session_key is required'},
                            status=status.HTTP_400_BAD_REQUEST)
