from xmlrpc.server import list_public_methods
from django.contrib import admin
from myapp.models import tasklist

admin.site.register(tasklist)
