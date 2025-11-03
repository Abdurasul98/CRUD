from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView,ListView
from django.urls import reverse_lazy
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







# def addcategory(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = CategoryForm()
#     return render(request, 'addcategory.html', {'form': form})
#
#
# def addproduct(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = ProductForm()
#     return render(request, 'addproduct.html', {'form': form})
#
#
# def addorder(request):
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = OrderForm()
#     return render(request, 'addorder.html', {'form': form})
#
#
# def addorderdetail(request):
#     if request.method == "POST":
#         form = OrderDetailForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = OrderDetailForm()
#     return render(request, 'addorderdetail.html', {'form': form})
#
#
# def addemployee(request):
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = EmployeeForm()
#     return render(request, 'addemployee.html', {'form': form})




# def deletecategory(request,id):
#     category = get_object_or_404(Category, pk=id)
#     category.delete()
#     categories = Category.objects.all()
#     context = {
#         'category': category,
#         'categories': categories
#     }
#
#     return render(request, 'index.html',context)
#
# def deleteproduct(request,id):
#     product = get_object_or_404(Product, pk=id)
#     product.delete()
#     products = Product.objects.all()
#     category = Category.objects.all()
#     context = {
#         'product': product,
#         'products': products,
#         'category': category,
#     }
#     return render(request, 'index.html',context)
#
# def deleteorderdetail(request,id):
#     orderdetail = get_object_or_404(OrderDetail, pk=id)
#     orderdetail.delete()
#     orderdetails = OrderDetail.objects.all()
#     context = {
#         'orderdetail': orderdetail,
#         'orderdetails': orderdetails
#     }
#     return render(request, 'index.html',context)
#
# def deleteemployee(request,id):
#     employee = get_object_or_404(Employee, pk=id)
#     employee.delete()
#     employees = Employee.objects.all()
#     context = {
#         'employee': employee,
#         'employees':employees
#     }
#     return render(request, 'index.html',context)
#
# def deleteorder(request,id):
#     order = get_object_or_404(Order, pk=id)
#     order.delete()
#     orders = Order.objects.all()
#     context = {
#         'order': order,
#         'orders': orders
#     }
#     return render(request, 'index.html',context)




# def updatecategory(request,id):
#     category = get_object_or_404(Category, pk=id)
#     if request.method == "POST":
#         form = CategoryForm(request.POST, instance = category)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form =CategoryForm(instance=category)
#     context = {
#         'form': form,
#         'category': category
#     }
#     return render(request, 'updatecategory.html',context)
#
#
# def updatemployee(request,id):
#     employee = get_object_or_404(Employee, pk=id)
#     if request.method == "POST":
#         form = EmployeeForm(request.POST, instance = employee)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form =EmployeeForm(instance=employee)
#     context = {
#         'form': form,
#         'employee': employee
#     }
#     return render(request, 'updateemployee.html',context)
#
#
# def updateorderdetail(request,id):
#     orderdetail = get_object_or_404(OrderDetail, pk=id)
#     if request.method == "POST":
#         form = OrderDetailForm(request.POST, instance = orderdetail)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form =OrderDetailForm(instance=orderdetail)
#     context = {
#         'form': form,
#         'orderdetail': orderdetail
#     }
#     return render(request, 'updateorderdetail.html',context)
#
#
# def updateproduct(request, id):
#     product = get_object_or_404(Product, pk=id)
#     if request.method == "POST":
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = ProductForm(instance=product)
#     context = {
#         'form': form,
#         'product': product
#     }
#     return render(request, 'updateproduct.html', context)
#
#
# def updateorder(request, id):
#     order = get_object_or_404(Order, pk=id)
#     if request.method == "POST":
#         form = OrderForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = OrderForm(instance=order)
#     context = {
#         'form': form,
#         'order': order
#     }
#     return render(request, 'updateorder.html', context)



# bu add
class AddCategory(CreateView):
    form_class = CategoryForm
    template_name = 'addcategory.html'
    success_url = reverse_lazy('index')

class AddProduct(CreateView):
    form_class = ProductForm
    template_name = 'addproduct.html'
    success_url = reverse_lazy('index')

class AddOrder(CreateView):
    form_class = OrderForm
    template_name = 'addorder.html'
    success_url = reverse_lazy('index')

class AddOrderDetail(CreateView):
    form_class = OrderDetailForm
    template_name = 'addorderdetail.html'
    success_url = reverse_lazy('index')

class AddEmployee(CreateView):
    form_class = EmployeeForm
    template_name = 'addemployee.html'
    success_url = reverse_lazy('index')


# bu update
class UpdateCategory(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'updatecategory.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'pk'

class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'updateproduct.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'pk'

class UpdateOrder(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'updateorder.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'pk'

class UpdateOrderDetail(UpdateView):
    model = OrderDetail
    form_class = OrderDetailForm
    template_name = 'updateorderdetail.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'pk'

class UpdateEmployee(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'updateemployee.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'pk'


# bu delete
class DeleteCategory(DeleteView):
    model = Category
    template_name = 'deletecategory.html'
    success_url = reverse_lazy('index')

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'deleteproduct.html'
    success_url = reverse_lazy('index')

class DeleteOrder(DeleteView):
    model = Order
    template_name = 'deleteorder.html'
    success_url = reverse_lazy('index')

class DeleteEmployee(DeleteView):
    model = Employee
    template_name = 'deleteemployee.html'
    success_url = reverse_lazy('index')

class DeleteOrderDetail(DeleteView):
    model = OrderDetail
    template_name = 'deleteorderdetail.html'
    success_url = reverse_lazy('index')


class ReadProduct(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['employee'] = Employee.objects.all()
        context['orderdetail'] = OrderDetail.objects.all()
        return context
