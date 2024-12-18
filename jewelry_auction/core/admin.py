from django.contrib import admin
from .models import User, Jewelry, Auction, Bid, Transaction, Request, Blog

# Register your models here.

admin.site.register(User)
admin.site.register(Jewelry)
admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Transaction)
admin.site.register(Request)
admin.site.register(Blog)