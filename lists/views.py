from django.shortcuts import redirect, render
from lists.forms import ItemForm
from lists.models import Item, List
from django.core.exceptions import ValidationError


# Create your views here.


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, parameter):
    list_ = List.objects.get(id=parameter)
    error = None
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            list_.delete()
            error = "You can't have an empty list item"
            return render(request, 'home.html', {"error": error})

    return render(request, 'list.html', {'list': list_, 'error': error})


def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)


def add_item(request, parameter):
    list_ = List.objects.get(id=parameter)
    Item.objects.create(text=request.POST['text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
