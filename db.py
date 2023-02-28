from django.db import models
from django.contrib.auth.models import User





class Customer (models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number_phone = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    house = models.CharField(max_length=30)
    apartment = models.IntegerField()
    

class Order (models.Model):
    order_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_time_order = models.DateTimeField()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.order_id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class Food (models.Model):
    food_id = models.BigAutoField(primary_key=True)
    food_name = models.CharField(max_length=50)
    price = models.FloatField()
    weight = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='img')
            
def __str__ (self):
    return self.food_name, self.price, self.weight

class OrderFood (models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class Ingredients (models.Model):
    name_ingredient = models.CharField(max_length=50)
    arrival_date = models.DateTimeField()
    best_before_date = models.DateTimeField()
    weight_ingr = models.IntegerField(default=100)
    
    
class FoodIngredients (models.Model):
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    food_ingredients = models.ForeignKey(Food, on_delete=models.CASCADE, default='')
    add_order_ingredients = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.IntegerField()

class AdditionalProduct (models.Model):
    additional_product_id = models.BigAutoField(primary_key=True)
    add_prod_in_order = models.ForeignKey(Order, on_delete=models.CASCADE, default=0)
    product = models.ForeignKey(Ingredients, on_delete=models.CASCADE, default=0)
    count_portion = models.IntegerField(default=0)
    
class AdditionalDrink (models.Model):
    drink = models.CharField(max_length=30)
    add_drink_in_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    portion_drink = models.IntegerField(default=500)
    count_drink = models.IntegerField(default=0)
    
class AdditionalSauce (models.Model):
    sauce = models.CharField(max_length=30)
    add_sauce_in_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    portion_sauce = models.IntegerField(default=30)
    count_sauce = models.IntegerField(default=0)

class Courier (models.Model):
    courier_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number_phone = models.IntegerField()
    method_delivery = models.CharField(max_length=10)

class Delivery (models.Model):
    devilery_id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    receiving_time = models.DateTimeField()
    pay = models.CharField(max_length=10)


    



