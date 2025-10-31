from django.shortcuts import render, redirect, get_object_or_404
from app1.models import *
from app1.forms import *

def index(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'category': category,
        'product': product
    }
    return render(request, 'index.html',context)


def product(request,id):
    category = Category.objects.all()
    product = Product.objects.filter(pk=id)
    order = Order.objects.filter(pk=id)
    employee = Employee.objects.filter(pk=id)
    orderdetail = OrderDetail.objects.filter(pk=id)
    context = {
        'category': category,
        'product': product,
        'order': order,
        'orderdetail': orderdetail,
        'employee': employee
    }
    return render(request, 'product.html',context)


def category(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'category.html',context)


def employee(request):
    employee = Employee.objects.all()
    context = {
        'employee': employee
    }
    return render(request, 'employee.html',context)


def order(request):
    order = Order.objects.all()
    context = {
        'order': order
    }
    return render(request, 'order.html',context)


def orderdetail(request):
    orderdetail = OrderDetail.objects.all()
    context = {
        'orderdetail': orderdetail
    }
    return render(request, 'orderdetail.html',context)







def addcategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'addcategory.html', {'form': form})


def addproduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'addproduct.html', {'form': form})


def addorder(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrderForm()
    return render(request, 'addorder.html', {'form': form})


def addorderdetail(request):
    if request.method == "POST":
        form = OrderDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrderDetailForm()
    return render(request, 'addorderdetail.html', {'form': form})


def addemployee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm()
    return render(request, 'addemployee.html', {'form': form})




def deletecategory(request,id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    categories = Category.objects.all()
    context = {
        'category': category,
        'categories': categories
    }

    return render(request, 'deletecategory.html',context)

def deleteproduct(request,id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    products = Product.objects.all()
    category = Category.objects.all()
    context = {
        'product': product,
        'products': products,
        'category': category,
    }
    return render(request, 'deleteproduct.html',context)

def deleteorderdetail(request,id):
    orderdetail = get_object_or_404(OrderDetail, pk=id)
    orderdetail.delete()
    orderdetails = OrderDetail.objects.all()
    context = {
        'orderdetail': orderdetail,
        'orderdetails': orderdetails
    }
    return render(request, 'deleteorderdetail.html',context)

def deleteemployee(request,id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    employees = Employee.objects.all()
    context = {
        'employee': employee,
        'employees':employees
    }
    return render(request, 'deleteemployee.html',context)

def deleteorder(request,id):
    order = get_object_or_404(Order, pk=id)
    order.delete()
    orders = Order.objects.all()
    context = {
        'order': order,
        'orders': orders
    }
    return render(request, 'deleteorder.html',context)




def updatecategory(request,id):
    category = get_object_or_404(Category, pk=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form =CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category
    }
    return render(request, 'updatecategory.html',context)


def updatemployee(request,id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form =EmployeeForm(instance=employee)
    context = {
        'form': form,
        'employee': employee
    }
    return render(request, 'updatecategory.html',context)


def updateorderdetail(request,id):
    orderdetail = get_object_or_404(OrderDetail, pk=id)
    if request.method == "POST":
        form = OrderDetailForm(request.POST, instance = orderdetail)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form =OrderDetailForm(instance=orderdetail)
    context = {
        'form': form,
        'orderdetail': orderdetail
    }
    return render(request, 'updatecategory.html',context)


def updateproduct(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product
    }
    return render(request, 'updateproduct.html', context)


def updateorder(request, id):
    order = get_object_or_404(Order, pk=id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrderForm(instance=order)
    context = {
        'form': form,
        'order': order
    }
    return render(request, 'updateorder.html', context)
