from django.db import models

# 🪑 Table Model
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, default="available")  # available / occupied

    def __str__(self):
        return f"Table {self.table_number}"


# 🍽️ Menu Items
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name


# 🧾 Order Model
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("preparing", "Preparing"),
        ("served", "Served"),
    ]

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    total_amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"


# 📦 Order Items (multiple items per order)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.item.name} x {self.quantity}"
# 📅 Reservation Model
class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.name} - Table {self.table.table_number}"