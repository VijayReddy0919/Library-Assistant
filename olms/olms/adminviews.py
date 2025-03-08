from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from olmsapp.models import CustomUser, Category, Author, Book, Student, Issuedbookdetails
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
import decimal
from django.db.models import Q

User = get_user_model()

@login_required(login_url='/')
def DASHBOARD(request):
    return render(request, 'admin/dashboard.html', {
        'issued_books_count': Issuedbookdetails.objects.count(),
    })

@login_required(login_url='/')
def ADD_CATEGORY(request):
    if request.method == "POST":
        catname = request.POST.get('catname')
        status = request.POST.get('status')
        cat = Category(
            catname=catname,
            status=status,
        )
        cat.save()
        messages.success(request, 'Category has been added successfully!!!')
        return redirect("add_category")
    
    return render(request, 'admin/add-category.html')

@login_required(login_url='/')
def MANAGE_CATEGORY(request):
    cat_list = Category.objects.all()
    paginator = Paginator(cat_list, 10)  # Show 10 categories per page

    page_number = request.GET.get('page')
    try:
        categories = paginator.page(page_number)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)

    context = {'categories': categories}
    return render(request, 'admin/manage_category.html', context)

@login_required(login_url='/')
def MANAGE_AUTHOR(request):
    author_list = Author.objects.all()
    paginator = Paginator(author_list, 10)  # Show 10 authors per page

    page_number = request.GET.get('page')
    try:
        authors = paginator.page(page_number)
    except PageNotAnInteger:
        authors = paginator.page(1)
    except EmptyPage:
        authors = paginator.page(paginator.num_pages)

    context = {'authors': authors}
    return render(request, 'admin/manage_author.html', context)

@login_required(login_url='/')
def MANAGE_BOOKS(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 10)  # Show 10 books per page

    page_number = request.GET.get('page')
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {'books': books}
    return render(request, 'admin/manage_books.html', context)

@login_required(login_url='/')
def MANAGE_ISSUED_BOOKS(request):
    issued_books_list = Issuedbookdetails.objects.all()
    paginator = Paginator(issued_books_list, 10)  # Show 10 issued books per page

    page_number = request.GET.get('page')
    try:
        issued_books = paginator.page(page_number)
    except PageNotAnInteger:
        issued_books = paginator.page(1)
    except EmptyPage:
        issued_books = paginator.page(paginator.num_pages)

    context = {'issued_books': issued_books}
    return render(request, 'admin/manage_issued_books.html', context)

@login_required(login_url='/')
def DELETE_CATEGORY(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, 'Category has been deleted successfully!!!')
    return redirect('manage_category')

@login_required(login_url='/')
def UPDATE_CATEGORY(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.catname = request.POST.get('catname')
        category.status = request.POST.get('status')
        category.save()
        messages.success(request, 'Category has been updated successfully!!!')
        return redirect('manage_category')
    
    return render(request, 'admin/update_category.html', {'category': category})

@login_required(login_url='/')
def UPDATE_CATEGORY_DETAILS(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.catname = request.POST.get('catname')
        category.status = request.POST.get('status')
        category.save()
        messages.success(request, 'Category details have been updated successfully!!!')
        return redirect('manage_category')
    
    return render(request, 'admin/update_category_details.html', {'category': category})

@login_required(login_url='/')
def ADD_AUTHOR(request):
    if request.method == "POST":
        author_name = request.POST.get('author_name')
        author = Author(name=author_name)
        author.save()
        messages.success(request, 'Author has been added successfully!!!')
        return redirect('manage_author')
    
    return render(request, 'admin/add_author.html')

@login_required(login_url='/')
def DELETE_AUTHOR(request, id):
    author = get_object_or_404(Author, id=id)
    author.delete()
    messages.success(request, 'Author has been deleted successfully!!!')
    return redirect('manage_author')

@login_required(login_url='/')
def UPDATE_AUTHOR(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == "POST":
        author.name = request.POST.get('author_name')
        author.save()
        messages.success(request, 'Author has been updated successfully!!!')
        return redirect('manage_author')
    
    return render(request, 'admin/update_author.html', {'author': author})

@login_required(login_url='/')
def UPDATE_AUTHOR_DETAILS(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == "POST":
        author.name = request.POST.get('author_name')
        author.save()
        messages.success(request, 'Author details have been updated successfully!!!')
        return redirect('manage_author')
    
    return render(request, 'admin/update_author_details.html', {'author': author})

@login_required(login_url='/')
def ADD_BOOKS(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        book = Book(title=title, author=author, category=category)
        book.save()
        messages.success(request, 'Book has been added successfully!!!')
        return redirect('manage_books')
    
    return render(request, 'admin/add_books.html')

@login_required(login_url='/')
def DELETE_BOOKS(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    messages.success(request, 'Book has been deleted successfully!!!')
    return redirect('manage_books')

@login_required(login_url='/')
def UPDATE_BOOKS(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.category = request.POST.get('category')
        book.save()
        messages.success(request, 'Book has been updated successfully!!!')
        return redirect('manage_books')
    
    return render(request, 'admin/update_books.html', {'book': book})

@login_required(login_url='/')
def UPDATE_BOOKS_DETAILS(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.category = request.POST.get('category')
        book.save()
        messages.success(request, 'Book details have been updated successfully!!!')
        return redirect('manage_books')
    
    return render(request, 'admin/update_books_details.html', {'book': book})

@login_required(login_url='/')
def MANAGE_REGUSERS(request):
    user_list = CustomUser.objects.all()
    paginator = Paginator(user_list, 10)  # Show 10 users per page

    page_number = request.GET.get('page')
    try:
        users = paginator.page(page_number)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'users': users}
    return render(request, 'admin/manage_regusers.html', context)

@login_required(login_url='/')
def DELETE_REGUSERS(request, id):
    user = get_object_or_404(CustomUser, id=id)
    user.delete()
    messages.success(request, 'Registered user has been deleted successfully!!!')
    return redirect('manage_regusers')

@login_required(login_url='/')
def STUDENT_LIB_HISTORY(request, id):
    student = get_object_or_404(Student, id=id)
    history = Issuedbookdetails.objects.filter(student=student)
    context = {'student': student, 'history': history}
    return render(request, 'admin/student_lib_history.html', context)

@login_required(login_url='/')
def SEARCHBOOK(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    
    context = {'books': books}
    return render(request, 'admin/search_books.html', context)

@login_required(login_url='/')
def SEARCHREGUSERS(request):
    query = request.GET.get('q')
    if query:
        users = CustomUser.objects.filter(username__icontains=query)
    else:
        users = CustomUser.objects.all()
    
    context = {'users': users}
    return render(request, 'admin/search_regusers.html', context)

# Other existing functions remain unchanged...
