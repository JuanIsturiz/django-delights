from django.db import models


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/menu"

    def is_available(self):
        return all(X.is_enough() for X in self.reciperequirement_set.all())

    def __str__(self) -> str:
        return f"Name: {self.name} - Price: {self.price}"


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(default=0.00)
    unit = models.CharField(max_length=100)
    price_per_unit = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/ingredients"

    def __str__(self):
        return f"""
    Name: {self.name}
    Quantity: {self.quantity}
    Unit: {self.unit}
    Price Per Unit: {self.price_per_unit}
    """


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/menu"

    def __str__(self):
        return f"Menu Item: {self.menu_item.name} - Ingredient: {self.ingredient.name} - Quantity: {self.quantity}"

    def is_enough(self):
        return self.quantity < self.ingredient.quantity


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return "/purchases"

    def __str__(self):
        return f"Menu Item: {self.menu_item.name} - Timestamp: {self.timestamp}"
