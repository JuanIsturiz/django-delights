from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import MenuItemForm, IngredientForm, RecipeRequirementForm, PurchaseForm


# Create your views here.


# Home View
class HomeView(TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["menu_items"] = MenuItem.objects.all()
        data["ingredients"] = Ingredient.objects.all()
        data["purchases"] = Purchase.objects.all()
        return data


# Ingredients List View
class IngredientsView(ListView):
    template_name = "inventory/ingredients_list.html"
    model = Ingredient


# Create New Ingredient View
class NewIngredientView(CreateView):
    template_name = "inventory/add_ingredient.html"
    model = Ingredient
    form_class = IngredientForm


# Update Ingredient View
class UpdateIngredientView(UpdateView):
    template_name = "inventory/update_ingredient.html"
    model = Ingredient
    form_class = IngredientForm


# MenuItems List View
class MenuItemView(ListView):
    template_name = "inventory/menu_list.html"
    model = MenuItem


# Create New Menu View
class NewMenuItemView(CreateView):
    template_name = "inventory/add_menu.html"
    model = MenuItem
    form_class = MenuItemForm


# Create Recipe Requirement View
class NewRecipeRequirement(CreateView):
    template_name = "inventory/add_recipe_requirement.html"
    model = RecipeRequirement
    form_class = RecipeRequirementForm
