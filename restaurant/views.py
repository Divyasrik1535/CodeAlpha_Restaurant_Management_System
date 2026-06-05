from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Table, MenuItem, Order, OrderItem, Reservation
from .serializers import TableSerializer, MenuItemSerializer, OrderSerializer, ReservationSerializer
from django.db.models import Sum
from rest_framework.decorators import action

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # 🔥 CANCEL ORDER API
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()

        # restore stock
        order_items = OrderItem.objects.filter(order=order)
        for item in order_items:
            menu_item = item.item
            menu_item.stock += item.quantity
            menu_item.save()

        # free table
        order.table.status = "available"
        order.table.save()

        # delete order
        order.delete()

        return Response({"message": "Order cancelled successfully"})
    @action(detail=False, methods=['get'])
    def daily_sales(self, request):
        from django.utils.timezone import now

        today = now().date()

        orders = Order.objects.filter(created_at__date=today)

        total_revenue = orders.aggregate(total=Sum('total_amount'))['total'] or 0
        total_orders = orders.count()

        return Response({
            "date": today,
            "total_orders": total_orders,
            "total_revenue": total_revenue
        })
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer