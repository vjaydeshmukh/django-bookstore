from django.urls import path
from . import views
from .views import AdminBookView

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('admin/books', views.admin_books, name='admin_books'),
    path('admin/books/details/<int:bookID>/', views.admin_book_details, name='admin_books_details'),
    path('admin/customers', views.admin_customers, name='admin_customers')
=======
    path('admin/books', AdminBookView.as_view()),
    path('admin/books/details/<int:bookID>/', views.admin_book_details, name='admin_books_details')
>>>>>>> origin/tgoze
]