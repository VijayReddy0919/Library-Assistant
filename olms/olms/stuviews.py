import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from olmsapp.models import CustomUser, Student, Book, Issuedbookdetails

logger = logging.getLogger(__name__)

@login_required(login_url='/')
def BOOKSDETAILS(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 12)  # Show 12 books per page

    page_number = request.GET.get('page')
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {'books': books}
    return render(request, 'student/books_details.html', context)

@login_required(login_url='/')
def RESERVE_BOOKS(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        book_id = request.POST.get('book_id')
        # Logic to reserve the book for the student
        # ...
        messages.success(request, 'Book reserved successfully!')
        return redirect('reserve_books')  # Redirect to the reserve books page
    else:
        students = Student.objects.all()
        books = Book.objects.filter(isIssued='0')  # Only show available books
        context = {
            'students': students,
            'books': books
        }
        return render(request, 'admin/issue_books.html', context)

@login_required(login_url='/')
def STUDENT_REG(request):
    if request.method == "POST":
        # Logic for handling student registration
        # ...
        messages.success(request, 'Student registered successfully!')
        return redirect('signup')  # Redirect to the signup page
    return render(request, 'student/registration.html')  # Render the registration form

# Other existing functions remain unchanged...
@login_required(login_url='/')
def ISSUE_BOOKS(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        book_id = request.POST.get('book_id')
        # Logic to issue the book to the student
        issued_book = Issuedbookdetails(student_id=student_id, book_id=book_id)
        issued_book.save()
        messages.success(request, 'Book has been issued successfully!!!')
        return redirect('manage_issued_books')
    
    # Render the form for issuing books
    return render(request, 'admin/issue_books.html')

@login_required(login_url='/')
def ISSUE_BOOKS(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        book_id = request.POST.get('book_id')
        # Logic to issue the book to the student
        issued_book = Issuedbookdetails(student_id=student_id, book_id=book_id)
        issued_book.save()
        messages.success(request, 'Book has been issued successfully!!!')
        return redirect('manage_issued_books')
    
    # Render the form for issuing books
    return render(request, 'admin/issue_books.html')