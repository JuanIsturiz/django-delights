from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("logout/", views.log_out, name="logout"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("", views.HomeView.as_view(), name="home"),
    path("ingredients/", views.IngredientsView.as_view(), name="ingredients"),
    path("ingredients/new", views.NewIngredientView.as_view(), name="add_ingredient"),
    path(
        "ingredients/<pk>/update",
        views.UpdateIngredientView.as_view(),
        name="update_ingredient",
    ),
    path("menu/", views.MenuItemView.as_view(), name="menu"),
    path("menu/new", views.NewMenuItemView.as_view(), name="add_menu"),
    path(
        "reciperequirement/new",
        views.NewRecipeRequirement.as_view(),
        name="add_recipe_requirement",
    ),
    path("purchases/", views.PurchasesView.as_view(), name="purchases"),
    path("purchases/new", views.NewPurchase.as_view(), name="add_purchase"),
    path("reports/", views.ReportsView.as_view(), name="reports"),
]
