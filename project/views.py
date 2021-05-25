from django.shortcuts import render, redirect

from project.forms import CategoryForm, UserCreationForm
from project.models import Product, Review, Category


# Create your views here.
def get_all_products(request):
    word = request.GET.get('search', '')
    products = Product.objects.filter(title__contains=word)
    print(products)
    data = {
        'all_products': products
    }
    return render(request, 'products.html', context=data)


def get_one_product(request, id):
    product = Product.objects.get(id=id)
    review = Review.objects.filter(product_id=id)
    data = {
        'product': product,
        'review': review,
    }
    return render(request, 'detail.html', context=data)


def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('category_name', '')
        print(name)
        Category.objects.create(name=name)
        return redirect('/add/')
    return render(request, 'add.html')


def add(request):
    if request.method == 'POST':
        print(request.POST)
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            Category.objects.create(name=name)
            return redirect('/add/')
        else:
            return render(request, 'add1.html', context={
                'form': form
            })
    data = {
        'form': CategoryForm()
    }
    return render(request, 'add1.html', context=data)


def main_page(request):
    return render(request, 'main.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('POST запрос без ошибок')
            return redirect('/admin/')
        else:
            print('POST запрос с ошибками')
            return render(request, 'register.html', context={'form': form})
    data = {
        'form': UserCreationForm()
    }
    print('Get запрос')
    return render(request, 'register.html', context=data)