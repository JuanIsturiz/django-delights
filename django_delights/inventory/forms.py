from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase


# New Ingredient Form
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


# New MenuItem Form
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


# New RecipeRequirement Form
class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"


# New Purchase Form
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
