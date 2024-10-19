from django.contrib import admin
from .models import Product, Contact
# superuser[
#     username: admin1
#     email: admin1@gmail.com
#     password:admin1
# ]
# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
