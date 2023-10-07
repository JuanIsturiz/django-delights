from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import MenuItemForm, IngredientForm, RecipeRequirementForm, PurchaseForm
from django.db.models import Sum
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# Home View
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["menu_items"] = MenuItem.objects.all()
        data["ingredients"] = Ingredient.objects.all()
        data["purchases"] = Purchase.objects.all()
        return data


# Ingredients List View
class IngredientsView(LoginRequiredMixin, ListView):
    template_name = "inventory/ingredients_list.html"
    model = Ingredient


# Create New Ingredient View
class NewIngredientView(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_ingredient.html"
    model = Ingredient
    form_class = IngredientForm


# Update Ingredient View
class UpdateIngredientView(UpdateView):
    template_name = "inventory/update_ingredient.html"
    model = Ingredient
    form_class = IngredientForm


# MenuItems List View
class MenuItemView(LoginRequiredMixin, ListView):
    template_name = "inventory/menu_list.html"
    model = MenuItem


# Create New Menu View
class NewMenuItemView(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_menu.html"
    model = MenuItem
    form_class = MenuItemForm


# Create Recipe Requirement View
class NewRecipeRequirement(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_recipe_requirement.html"
    model = RecipeRequirement
    form_class = RecipeRequirementForm


# Purchases List View
class PurchasesView(LoginRequiredMixin, ListView):
    template_name = "inventory/purchases_list.html"
    model = Purchase


# Create Recipe Requirement View
class NewPurchase(LoginRequiredMixin, TemplateView):
    template_name = "inventory/add_purchase.html"
    model = Purchase
    form_class = PurchaseForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = [X for X in MenuItem.objects.all() if X.is_available()]
        return context

    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            required_ingredient.save()

        purchase.save()
        return redirect("/purchases")


# Reports View
class ReportsView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += (
                    recipe_requirement.ingredient.price_per_unit
                    * recipe_requirement.quantity
                )

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context


# Logout View
def log_out(request):
    logout(request)
    return redirect("/")
