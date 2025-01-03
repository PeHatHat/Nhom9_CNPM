from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from users.models import User
from jewelry.models import Jewelry
from auctions.models import Auction
from bids.models import Bid
from transactions.models import Transaction
from django.db.models import Sum, Count ,Max

def is_admin_or_manager(user):
    return user.role in ['ADMIN', 'MANAGER']

@login_required
@user_passes_test(is_admin_or_manager)
def dashboard(request):
    # Thống kê chung
    total_users = User.objects.count()
    total_jewelry = Jewelry.objects.count()
    total_auctions = Auction.objects.count()
    total_bids = Bid.objects.count()

    # Thống kê về JCoin
    total_jcoin_in_system = User.objects.aggregate(Sum('jcoin_balance'))['jcoin_balance__sum'] or 0

    # Thống kê giao dịch
    total_successful_transactions = Transaction.objects.filter(status='COMPLETED').count()
    total_transaction_value = Transaction.objects.filter(status='COMPLETED').aggregate(Sum('amount'))['amount__sum'] or 0
    total_fee_collected = Transaction.objects.filter(status='COMPLETED').aggregate(Sum('fee'))['fee__sum'] or 0
    
    # Top 5 người dùng có nhiều Jcoin nhất
    top_5_users_by_jcoin = User.objects.order_by('-jcoin_balance')[:5]

    # Top 5 trang sức có giá trị đấu giá cao nhất
    top_5_highest_priced_jewelry = Jewelry.objects.annotate(
        highest_bid=Max('auction__bids__amount')
    ).order_by('-highest_bid')[:5]

    # Số lượng đấu giá theo trạng thái
    auction_status_counts = Auction.objects.values('status').annotate(count=Count('status'))

    context = {
        'total_users': total_users,
        'total_jewelry': total_jewelry,
        'total_auctions': total_auctions,
        'total_bids': total_bids,
        'total_jcoin_in_system': total_jcoin_in_system,
        'total_successful_transactions': total_successful_transactions,
        'total_transaction_value': total_transaction_value,
        'total_fee_collected': total_fee_collected,
        'top_5_users_by_jcoin': top_5_users_by_jcoin,
        'top_5_highest_priced_jewelry': top_5_highest_priced_jewelry,
        'auction_status_counts': auction_status_counts,
    }

    return render(request, 'core/dashboard.html', context)