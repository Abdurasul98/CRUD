from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=200,null=True, blank=True)
    quantity_per_unit = models.IntegerField(null=True, blank=True)
    unit_price = models.FloatField(null=True, blank=True)
    units_in_stock = models.IntegerField(null=True, blank=True)
    units_on_order = models.IntegerField(null=True, blank=True)
    reorder_level = models.IntegerField(null=True, blank=True)
    discontinued = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Employee(models.Model):
    last_name = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    title = models.CharField(max_length=200,null=True, blank=True)
    title_of_courtesy = models.CharField(max_length=200,null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    city = models.CharField(max_length=200,null=True, blank=True)
    region = models.CharField(max_length=200,null=True, blank=True)
    postal_code = models.CharField(max_length=200,null=True, blank=True)
    country = models.CharField(max_length=200,null=True, blank=True)
    home_phone = models.CharField(max_length=200,null=True, blank=True)
    extension = models.CharField(max_length=200,null=True, blank=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/d',null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    reports_to = models.IntegerField(null=True, blank=True)
    phone_path = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.last_name


class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order_date = models.DateField(null=True, blank=True)
    required_date = models.DateField(null=True, blank=True)
    shipped_date = models.DateField(null=True, blank=True)
    ship_via =models.IntegerField(null=True, blank=True)
    freight = models.IntegerField(null=True, blank=True)
    ship_name = models.CharField(max_length=200,null=True, blank=True)
    ship_address = models.CharField(max_length=200,null=True, blank=True)
    ship_city = models.CharField(max_length=200,null=True, blank=True)
    ship_region = models.CharField(max_length=200,null=True, blank=True)
    ship_postal_code = models.CharField(max_length=200,null=True, blank=True)
    ship_country = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return str(self.order_date)


class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return str(self.unit_price)