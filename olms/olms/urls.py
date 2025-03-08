from django.contrib import admin
from django.urls import path
from . import views, adminviews, stuviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('Dashboard', views.DASHBOARD, name='dashboard'),
    path('Login', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('', views.Index, name='index'),
    path('doLogout', views.doLogout, name='logout'),
    path('AdminProfile', views.ADMIN_PROFILE, name='admin_profile'),
    path('AdminProfile/update', views.ADMIN_PROFILE_UPDATE, name='admin_profile_update'),
    path('Password', views.CHANGE_PASSWORD, name='change_password'),
    path('Admin/AddCategory', adminviews.ADD_CATEGORY, name='add_category'),
    path('Admin/ManageCategory', adminviews.MANAGE_CATEGORY, name='manage_category'),
    path('Admin/DeleteCategory/<str:id>', adminviews.DELETE_CATEGORY, name='delete_category'),
    path('UpdateCategory/<str:id>', adminviews.UPDATE_CATEGORY, name='update_category'),
    path('UpdateCategoryDetails', adminviews.UPDATE_CATEGORY_DETAILS, name='update_category_details'),
    path('Admin/AddAuthor', adminviews.ADD_AUTHOR, name='add_author'),
    path('Admin/ManageAuthor', adminviews.MANAGE_AUTHOR, name='manage_author'),
    path('Admin/DeleteAuthor/<str:id>', adminviews.DELETE_AUTHOR, name='delete_author'),
    path('UpdateAuthor/<str:id>', adminviews.UPDATE_AUTHOR, name='update_author'),
    path('UpdateAuthorDetails', adminviews.UPDATE_AUTHOR_DETAILS, name='update_author_details'),
    path('Admin/AddBooks', adminviews.ADD_BOOKS, name='add_books'),
    path('Admin/ManageBooks', adminviews.MANAGE_BOOKS, name='manage_books'),
    path('Admin/DeleteBooks/<str:id>', adminviews.DELETE_BOOKS, name='delete_books'),
    path('UpdateBooks/<str:id>', adminviews.UPDATE_BOOKS, name='update_books'),
    path('UpdateBooksDetails', adminviews.UPDATE_BOOKS_DETAILS, name='update_books_details'),
    path('Admin/ManageRegUsers', adminviews.MANAGE_REGUSERS, name='manage_regusers'),
    path('Admin/DeleteRegUsers/<str:id>', adminviews.DELETE_REGUSERS, name='delete_regusers'),
    path('Admin/Studenlibhistory/<str:id>', adminviews.STUDENT_LIB_HISTORY, name='student_lib_history'),
    path('Admin/SearchBook', adminviews.SEARCHBOOK, name='search_books'),
    path('Admin/SearchRegusers', adminviews.SEARCHREGUSERS, name='search_regusers'),
    path('Student/BooksDetails', stuviews.BOOKSDETAILS, name='books_details'),
    path('Student/StuReg', stuviews.STUDENT_REG, name='signup'),
    path('Student/IssueBooks', stuviews.ISSUE_BOOKS, name='issue_books'),  # New route for issuing books
    path('Admin/ManageIssuedBooks', adminviews.MANAGE_ISSUED_BOOKS, name='manage_issued_books'),  # New route for issued books
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
