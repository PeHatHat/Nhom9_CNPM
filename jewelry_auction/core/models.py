from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('guest', 'Guest'),
        ('member', 'Member'),
        ('staff', 'Staff'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    registration_date = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    jcoin_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Thêm related_name vào đây
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_groups',  # Thay đổi related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_user_permissions',  # Thay đổi related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

class Jewelry(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('auctioned', 'Auctioned'),
        ('sold', 'Sold'),
        ('delivered', 'Delivered'),
        ('received', 'Received'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jewelry_items")
    initial_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    preliminary_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image_1 = models.ImageField(upload_to='jewelry_images/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='jewelry_images/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='jewelry_images/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name

class Auction(models.Model):
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('canceled', 'Canceled'),
    )
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="managed_auctions")
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="staffed_auctions")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    jewelry = models.ManyToManyField(Jewelry, related_name="auctions")

    def __str__(self):
        return f"Auction {self.pk}"

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE, related_name="bids")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids_made')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Bid {self.pk} by {self.bidder.username} on {self.auction}"

class Transaction(models.Model):
    STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('completed', 'Completed'),
        ('delivered', 'Delivered'),
    )
    auction = models.OneToOneField(Auction, on_delete=models.SET_NULL, null=True, blank=True)
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='transactions_as_buyer')
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='transactions_as_seller')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='paid')

    def __str__(self):
        return f"Transaction {self.pk} for {self.auction}"

class Request(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('preliminary_price_sent', 'Preliminary Price Sent'),
        ('jewelry_received','Jewelry Received'),
        ('final_price_sent', 'Final Price Sent'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE, related_name="requests")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    preliminary_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Request {self.pk} for {self.jewelry.name} by {self.seller.username}"

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    publication_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title