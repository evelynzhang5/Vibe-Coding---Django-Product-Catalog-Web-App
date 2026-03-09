from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# /items  -> list page
def item_list(request):
    items = Item.objects.all().order_by('-created_at')   # newest first
    return render(request, 'catalog/item_list.html', {'items': items})


# /add  -> add item page
def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('item_list')   # redirect after successful submit
    else:
        form = ItemForm()

    return render(request, 'catalog/add_item.html', {'form': form})