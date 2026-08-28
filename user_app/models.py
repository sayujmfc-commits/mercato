from django.db import models


class user_details(models.Model):

    userphoto = models.ImageField()

    username = models.CharField(max_length=200)

    useremail = models.CharField(max_length=208)

    userphone = models.CharField(max_length=12)

    userpassword = models.CharField(max_length=200)


class Order(models.Model):

    product = models.ForeignKey(
        'admin_app.Product',
        on_delete=models.CASCADE
    )

    customer_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    city = models.CharField(max_length=100)

    pincode = models.CharField(max_length=10)

    payment_method = models.CharField(max_length=50)

    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name + " - " + self.product.name