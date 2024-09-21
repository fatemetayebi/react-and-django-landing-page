from .models import *
from rest_framework import serializers
from config import settings
import random
from django.core.mail import send_mail


class ShowProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContactFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['email', 'subject', 'message']

    # def validate(self, attrs):
    #     entered_code = int(attrs.get['entered_code'])
    #
    #     if self.code != attrs.get['entered_code']:
    #         raise serializers.ValidationError({'code': 'entered code is wrong try again'})
    #     return attrs

    # def create(self, validated_data):
    #     contact_form = Contact.objects.create(
    #         email=validated_data['email'],
    #         message=validated_data['message'],
    #         subject=validated_data['subject'],
    #     )
    #     contact_form.save()
    #     return contact_form




class CodeSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=False, read_only=True)
    entered_code = serializers.IntegerField(required=False)
# class ContactFormSerializer(serializers.ModelSerializer):
#     entered_code = serializers.IntegerField()
#
#     class Meta:
#         model = Contact
#         fields = ['entered_code', 'email', 'subject', 'message']
#
#     def send_verify_code(self):
#         email = self.validated_data["email"]
#         code = random.randint(1111, 9999)
#
#         # Email Sender
#         sender = send_mail(
#             'Verify your email',
#             f'Enter {code} to confirm your email and send your message',
#             settings.EMAIL_HOST_USER,
#             [email],
#             fail_silently=False,
#         )
#
#         return code
#
#     def validate(self, attrs):
#         entered_code = attrs.get('entered_code')
#
#         if self.instance.code != entered_code:
#             raise serializers.ValidationError({'code': 'Entered code is incorrect. Please try again.'})
#         return attrs
#
#     def create(self, validated_data):
#         contact_form = Contact.objects.create(
#             email=validated_data['email'],
#             subject=validated_data.get('subject'),
#             message=validated_data['message']
#         )
#         contact_form.save()
#         return contact_form
