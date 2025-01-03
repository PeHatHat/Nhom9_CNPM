from django.shortcuts import render, get_object_or_404, redirect
from .models import Bid
from auctions.models import Auction
from .forms import BidForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseForbidden
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from notifications.models import Notification

@login_required
def place_bid(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)

    # Kiểm tra nếu phiên đấu giá đã kết thúc
    if auction.status != 'OPEN':
        return HttpResponseForbidden("This auction is not open for bidding.")

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                bid = form.save(commit=False)
                bid.user = request.user
                bid.auction = auction
                try:
                    bid.clean()  # Kiểm tra tính hợp lệ của bid
                    bid.save()

                    # Lấy danh sách tất cả các bids cho phiên đấu giá này, trừ bid vừa được tạo
                    other_bids = Bid.objects.filter(auction=auction).exclude(bid_id=bid.bid_id)

                    # Tạo thông báo cho những người dùng đã đặt giá thầu trước đó
                    for other_bid in other_bids:
                        Notification.objects.create(
                            user=other_bid.user,
                            message=f"Giá thầu của bạn cho trang sức '{auction.jewelry.name}' đã bị vượt qua. Giá thầu mới nhất là {bid.amount} JCoins."
                        )

                    # Tạo thông báo cho người dùng đã đặt giá thầu thành công
                    Notification.objects.create(
                        user=request.user,
                        message=f"Bạn đã đặt giá thầu thành công cho trang sức '{auction.jewelry.name}' với giá {bid.amount} JCoins."
                    )

                    return redirect('auctions:auction-detail', pk=auction_id)
                except ValidationError as e:
                    form.add_error('amount', e)
    else:
        form = BidForm()

    return render(request, 'bids/place_bid.html', {'form': form, 'auction': auction})

@login_required
def user_bids(request):
    bids = Bid.objects.filter(user=request.user).order_by('-timestamp')
    
    # Pagination
    paginator = Paginator(bids, 10)  # Show 10 bids per page
    page = request.GET.get('page')
    try:
        bids_page = paginator.page(page)
    except PageNotAnInteger:
        bids_page = paginator.page(1)
    except EmptyPage:
        bids_page = paginator.page(paginator.num_pages)
    
    return render(request, 'bids/user_bids.html', {'bids': bids_page})