from .models import *
from rest_framework import serializers


# Serializer for displaying products, includes all fields from the Product model
class ShowProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Serializer for handling the contact form data, excludes no fields (all fields included)
class ContactFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        exclude = ()

    # Custom method to handle the creation of a Contact instance
    def create(self, validated_data):
        # Create a new Contact object using the validated data from the form
        contact_form = Contact.objects.create(
            email=validated_data['email'],
            message=validated_data['message'],
            subject=validated_data['subject'],
        )
        # Save the newly created Contact object to the database
        contact_form.save()
        return contact_form


# Serializer for handling verification codes
class CodeSerializer(serializers.Serializer):
    # Code to be sent, only for output, not required as input (read_only)
    code = serializers.IntegerField(required=False, read_only=True)
    # Code entered by the user for verification, optional
    entered_code = serializers.IntegerField(required=False)

