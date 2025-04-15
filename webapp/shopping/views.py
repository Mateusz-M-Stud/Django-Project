from django.shortcuts import render, redirect, get_object_or_404
from .models import ShoppingList
from .forms import ProductForm

def shopping_list_detail(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, pk=list_id)
    return render(request, 'shopping/shopping_list_detail.html', {'shopping_list': shopping_list})

def shopping_list_detail(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, pk=list_id)
    items = shopping_list.products.all()  # Use related_name from your model
    return render(request, 'shopping/shopping_list.html', {'shopping_list': shopping_list, 'items': items})

def add_product(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, pk=list_id)  # Fetch the shopping list by ID

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)  # Don't commit yet
            product.shopping_list = shopping_list  # Associate the product with the shopping list
            product.save()  # Save the product to the database
            return redirect('shopping_list_detail', list_id=shopping_list.id)  # Redirect to the shopping list detail page
    else:
        form = ProductForm()

    return render(request, 'shopping/add_product.html', {'form': form})
