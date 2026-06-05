from rest_framework import serializers
from .models import Table, MenuItem, Order, OrderItem, Reservation


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'table', 'status', 'total_amount', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        total = 0

        for item_data in items_data:
            menu_item = item_data['item']
            quantity = item_data['quantity']

            if menu_item.stock < quantity:
                raise serializers.ValidationError(f"{menu_item.name} out of stock")

            menu_item.stock -= quantity
            menu_item.save()

            OrderItem.objects.create(
                order=order,
                item=menu_item,
                quantity=quantity
            )

            total += menu_item.price * quantity

        order.total_amount = total
        order.save()

        order.table.status = "occupied"
        order.table.save()

        return order
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        table = data['table']
        date = data['date']
        time = data['time']

        # check existing booking
        if Reservation.objects.filter(table=table, date=date, time=time).exists():
            raise serializers.ValidationError("This table is already booked at this time.")

        return data