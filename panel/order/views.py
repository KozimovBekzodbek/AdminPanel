from django.shortcuts import render, redirect, get_object_or_404
from panel.order.forms import OrderForms
from restoran.models import Order


def OrderList(request):
    orders = Order.objects.all()

    return render(request, "panel\order\list.html", {"orders": orders})


def OrderCreate(request):
    form = OrderForms()
    if request.POST:
        form = OrderForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order-list')
    return render(request, "panel\order\create.html", {"form":form})



def OrderUpdate(request, pk):
    old = get_object_or_404(Order, pk=pk)
    if request.POST:
        form = OrderForms(request.POST, instance=old)
        if form.is_valid():
            form.save()
            return redirect('order-list')
    form = OrderForms(instance=old)
    return render(request,'panel/order/update.html', {"form":form})



def OrderDelete(request, pk):
    old = get_object_or_404(Order, pk=pk)
    old.delete()
    return redirect('order-list')
