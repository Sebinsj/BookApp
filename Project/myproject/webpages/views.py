from django.shortcuts import render
from .models import Book
from django.contrib import messages

# Create your views here.
def home(request):

    books=Book.objects.all()
    if request.method=='POST':
        if "add" in request.POST:
            id=request.POST.get('id')
            name=request.POST.get('name')
            author=request.POST.get('author')
            Book.objects.create(id=id,name=name,
                                author=author

            )
            messages.success(request,'book added')

            
    data={
        "books":books
    }
    return render(request,'webpages/home.html',data)
