import os
import django

from django.core.management.base import BaseCommand

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jewelry_auction.settings')
django.setup()

from core.models import User, Jewelry, Auction, Bid, Transaction, Request, Blog

class Command(BaseCommand):
    help = 'Xóa dữ liệu từ các model được chỉ định.'

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Chế độ 'all' hoặc 'choose'.")

    def handle(self, *args, **options):
        mode = options['mode']

        if mode == 'all':
            self.delete_all_data()
        elif mode == 'choose':
            self.choose_and_delete_data()
        else:
            self.stdout.write(self.style.ERROR("Chế độ không hợp lệ. Vui lòng chọn 'all' hoặc 'choose'."))

    def delete_all_data(self):
        model_mapping = {
            7: Blog,
            6: Request,
            5: Transaction,
            4: Bid,
            3: Auction,
            2: Jewelry,
            1: User,
        }

        for model_index in model_mapping:
            model = model_mapping[model_index]
            if model_index == 1:
                model.objects.filter(is_superuser=False).delete()
            else:
                model.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"Đã xóa dữ liệu của model: {model.__name__}"))

    def choose_and_delete_data(self):
        self.stdout.write("Chọn các model cần xóa dữ liệu (nhập số thứ tự, cách nhau bởi dấu cách):")
        self.stdout.write("1. User")
        self.stdout.write("2. Jewelry")
        self.stdout.write("3. Auction")
        self.stdout.write("4. Bid")
        self.stdout.write("5. Transaction")
        self.stdout.write("6. Request")
        self.stdout.write("7. Blog")
        self.stdout.write("Nhập 'all' để xóa tất cả.")

        input_str = input("Nhập lựa chọn của bạn: ")
        if input_str.lower() == "all":
            self.delete_all_data()
        else:
            try:
                model_indices = [int(x) for x in input_str.split()]
                for model_index in model_indices:
                    self.delete_selected_data(model_index)
            except ValueError:
                self.stdout.write(self.style.ERROR("Lựa chọn không hợp lệ."))

    def delete_selected_data(self, model_index):
        model_mapping = {
            1: User,
            2: Jewelry,
            3: Auction,
            4: Bid,
            5: Transaction,
            6: Request,
            7: Blog,
        }
        try:
            model = model_mapping[model_index]
            if model_index == 1:
                model.objects.filter(is_superuser=False).delete()
            else:
                model.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"Đã xóa dữ liệu của model: {model.__name__}"))
        except (KeyError, ValueError):
            self.stdout.write(self.style.ERROR(f"Số thứ tự model '{model_index}' không hợp lệ."))