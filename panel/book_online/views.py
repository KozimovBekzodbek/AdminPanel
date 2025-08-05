from django.shortcuts import render, redirect, get_object_or_404
from restoran.models import Book_Online
from panel.book_online.forms import BookOnlineForm



def BookOnlineList(request):
    book_online = Book_Online.objects.all()
    return render(request, 'panel/book_online/list.html', {"book_online":book_online})



def BookOnlineCreate(request):
    form = BookOnlineForm()
    if request.POST:
        form = BookOnlineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-online')
    return render(request, 'panel/book_online/create.html',{"form":form})



def BookOnlineUpdate(request,pk):
    old = get_object_or_404(Book_Online, pk=pk)
    if request.POST:
        form = BookOnlineForm(request.POST, instance=old)
        if form.is_valid():
            form.save()
            return redirect('book-online')
    form = BookOnlineForm(instance=old)
    return render(request, 'panel/book_online/update.html',{"form":form})


def BookOnlineDelete(request,pk):
    old = get_object_or_404(Book_Online, pk=pk)
    old.delete()
    return redirect('book-online')



