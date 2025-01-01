from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdmin
from django.db.models import Q

class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == 'ADMIN':
                return Transaction.objects.all()
            else:
                return Transaction.objects.filter(
                    Q(winning_bidder=user) | Q(jewelry_owner=user)
                )
        else:
            return Transaction.objects.none()