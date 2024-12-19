from django.core.management.base import BaseCommand
from core.models import User, Jewelry, Auction, Bid, Transaction, Request, Blog
from django.utils import timezone
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Creates sample data for the application'

    def handle(self, *args, **kwargs):
        # Tạo superuser 'nhom9' (nếu chưa có)
        try:
            manager = User.objects.get(username='nhom9')
            self.stdout.write(self.style.WARNING('User "nhom9" already exists'))
        except User.DoesNotExist:
            manager = User.objects.create_superuser(username='nhom9', email='nhom9@example.com', password='yourpassword') # Thay yourpassword bằng mật khẩu bạn muốn
            self.stdout.write(self.style.SUCCESS('Successfully created user "nhom9"'))

        # Tạo user 'testuser' (nếu chưa có)
        try:
            user = User.objects.get(username='testuser')
            self.stdout.write(self.style.WARNING('User "testuser" already exists'))
        except User.DoesNotExist:
            user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword', role='member')
            self.stdout.write(self.style.SUCCESS('Successfully created user "testuser"'))

        # Tạo user 'staffuser' (nếu chưa có)
        try:
            staff = User.objects.get(username='staffuser')
            self.stdout.write(self.style.WARNING('User "staffuser" already exists'))
        except User.DoesNotExist:
            staff = User.objects.create_user(username='staffuser', email='staff@example.com', password='staffpassword',role='staff')
            self.stdout.write(self.style.SUCCESS('Successfully created user "staffuser"'))

        # Tạo jewelry (nếu chưa có)
        try:
            jewelry = Jewelry.objects.get(name='Nhẫn kim cương')
            self.stdout.write(self.style.WARNING('Jewelry "Nhẫn kim cương" already exists'))
        except Jewelry.DoesNotExist:
            jewelry = Jewelry.objects.create(name='Nhẫn kim cương', description='Nhẫn kim cương tuyệt đẹp', seller=user, initial_price=1000, status='approved', image_1='jewelry_images/ring.jpg')
            self.stdout.write(self.style.SUCCESS('Successfully created jewelry "Nhẫn kim cương"'))

        # Tạo auction và gán manager là user có username='nhom9' (nếu chưa có)
        try:
            # Kiểm tra xem đã có auction cho jewelry này chưa
            auction = Auction.objects.get(jewelry=jewelry)
            self.stdout.write(self.style.WARNING(f'Auction for jewelry "{jewelry.name}" already exists'))
        except Auction.DoesNotExist:
            # Nếu chưa có auction, tạo mới và gán manager
            auction = Auction.objects.create(jewelry=jewelry, start_time=timezone.now(), end_time=timezone.now() + timezone.timedelta(days=7), status='open', manager=manager)
            self.stdout.write(self.style.SUCCESS(f'Successfully created auction for jewelry "{jewelry.name}"'))

        # Tạo một số blog posts
        try:
            blog_post1 = Blog.objects.get(title="Blog Post 1")
            self.stdout.write(self.style.WARNING('Blog post "Blog Post 1" already exists'))
        except Blog.DoesNotExist:
            blog_post1 = Blog.objects.create(title="Blog Post 1", content="Nội dung blog post 1", author=manager)
            self.stdout.write(self.style.SUCCESS('Successfully created blog post "Blog Post 1"'))

        try:
            blog_post2 = Blog.objects.get(title="Blog Post 2")
            self.stdout.write(self.style.WARNING('Blog post "Blog Post 2" already exists'))
        except Blog.DoesNotExist:
            blog_post2 = Blog.objects.create(title="Blog Post 2", content="Nội dung blog post 2", author=manager)
            self.stdout.write(self.style.SUCCESS('Successfully created blog post "Blog Post 2"'))

        self.stdout.write(self.style.SUCCESS('Tạo data mẫu thành công!'))