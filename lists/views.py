from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def view_list(request, parameter):
    list_ = List.objects.get(id=parameter)
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, parameter):
    list_ = List.objects.get(id=parameter)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
