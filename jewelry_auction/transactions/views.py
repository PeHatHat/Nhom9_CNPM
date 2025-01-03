from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Transaction
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def is_admin(user):
    return user.role == 'ADMIN'

@login_required
def transaction_list(request):
    if request.user.role == 'ADMIN':
        transactions = Transaction.objects.all().order_by('-timestamp')
    else:
        transactions = Transaction.objects.filter(
            Q(winning_bidder=request.user) | Q(jewelry_owner=request.user)
        ).order_by('-timestamp')
    
    # Pagination
    paginator = Paginator(transactions, 10)  # Show 10 transactions per page
    page = request.GET.get('page')
    try:
        transactions_page = paginator.page(page)
    except PageNotAnInteger:
        transactions_page = paginator.page(1)
    except EmptyPage:
        transactions_page = paginator.page(paginator.num_pages)

    return render(request, 'transactions/transaction_list.html', {'transactions': transactions_page})

@login_required
def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.user.role != 'ADMIN' and request.user != transaction.winning_bidder and request.user != transaction.jewelry_owner:
        return HttpResponseForbidden("You don't have permission to view this transaction.")
    return render(request, 'transactions/transaction_detail.html', {'transaction': transaction})