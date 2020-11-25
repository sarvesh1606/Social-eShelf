from django.shortcuts import render, get_object_or_404, redirect
from .models import Ebook, Comment, Category
from django.contrib import auth
from django.utils import timezone
from ebook import models

def home(request):
    ebooks = Ebook.objects.order_by('-id')[:4]
    return render(request, 'ebook/home.html', {
        'ebooks' : ebooks 
    })


def ebooks(request):
    #ebooks = Ebook.objects.all()
    ebooks = Ebook.objects.order_by('-id')

    return render(request, 'ebook/ebooks.html', {
		'ebooks': ebooks,
		})

def ebook(request, ebook_id):
    ebook = get_object_or_404(Ebook, pk = ebook_id)
    comments = ebook.comment_set.all()
    return render(request, 'ebook/ebook.html', {
		'ebook' : ebook,
        'comments' : comments,
		})

def comment(request, ebook_id):
    if request.method == 'POST':
        user = auth.get_user(request)
        ebook = get_object_or_404(Ebook, pk = ebook_id)

        # create the comment
        comment = Comment()
        comment.body = request.POST['body']
        comment.pub_time = timezone.datetime.now()
        comment.ebook = ebook
        comment.user = user
        comment.save()

        return redirect('ebook', ebook_id)
    else:
        return redirect('home')


def add(request):
    if request.method== "POST":


        '''    book=models.Ebook()
        book.title = request.POST.get('title')
        book.authors = request.POST.get('authors')

        book.pages = request.POST.get('pages')
        book.price = request.POST.get('price')
        image1 = request.FILES('image')
        book.image = Ebook.objects.create(image=image1)
        doc = request.FILES('ebook')
        book.ebook = Ebook.objects.create(ebook=doc) 
        book.save()'''


        user = auth.get_user(request)
        title = request.POST.get('title')
        authors = request.POST.get('authors')
        
        pages = request.POST.get('pages')
        price = request.POST.get('price')
        image = request.FILES['image']
        ebook = request.FILES['ebook']
        add = Ebook.objects.create(title=title ,authors=authors ,  pages=pages , price=price , image=image , ebook=ebook )
        add.user = user
        add.save()
    
    return render(request,'ebook/add.html')










































































































def categories(request):
    categories = Category.objects.order_by('name')
    return render(request, 'ebook/categories.html', {
		'categories': categories,
		})

def category(request, category_id):

    category = get_object_or_404(Category, pk = category_id)
    ebooks = category.ebook_set.all()


    return render(request, 'ebook/category.html', {
		'category' : category,
		'ebooks' : ebooks
		})