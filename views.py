from django.contrib import auth
from django.shortcuts import render, redirect

from project.forms import CategoryForm, UserCreationForm, LoginForm, ProductForm
from project.models import Product, Review, Category

# Create your views here.
PAGE_SIZE = 1


def get_all_products(request):
    word = request.GET.get('search', '')
    page = int(request.GET.get('page', 1))
    products = Product.objects.filter(title__contains=word)
    count = products.count()
    print(products)
    if count % PAGE_SIZE == 0:
        buttons = count
    else:
        buttons = count // PAGE_SIZE + 1
    print([i for i in range(1, buttons + 1)])
    start = (page - 1) * PAGE_SIZE
    end = page * PAGE_SIZE
    data = {
        'all_products': products[start:end],
        'username': auth.get_user(request).username,
        'buttons': [i for i in range(1, buttons+1)]
    }
    return render(request, 'products.html', context=data)


def get_one_product(request, id):
    product = Product.objects.get(id=id)
    review = Review.objects.filter(product_id=id)
    data = {
        'product': product,
        'review': review,
        'username': auth.get_user(request).username
    }
    return render(request, 'detail.html', context=data)


def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('category_name', '')
        print(name)
        Category.objects.create(name=name)
        return redirect('/add/')
    return render(request, 'add.html', context={
        'username': auth.get_user(request).username
    })


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
        'form': CategoryForm(),
        'username': auth.get_user(request).username
    }
    return render(request, 'add1.html', context=data)


def main_page(request):
    data = {
        'username': auth.get_user(request).username
    }
    return render(request, 'main.html', context=data)


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
        'form': UserCreationForm(),
        'username': auth.get_user(request).username
    }
    print('Get запрос')
    return render(request, 'register.html', context=data)


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', context={'form': form})
    data = {
        'form': LoginForm(),
        'username': auth.get_user(request).username
    }
    return render(request, 'login.html', context=data)


def logout(request):
    auth.logout(request)
    return redirect('/')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/')
        else:
            data = {
                'form': ProductForm(),
                'username': auth.get_user(request).username
            }
            return render(request, 'add_product.html', context=data)

    data = {
        'form': ProductForm(),
        'username': auth.get_user(request).username
    }
    return render(request, 'add_product.html', context=data)

