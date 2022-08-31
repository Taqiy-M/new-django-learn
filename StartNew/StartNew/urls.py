
from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asosiy/', salom),
    path('all-students/', all_students),
    path('student/<int:a>', single_student),
    path('all-books/', all_books),
    path('delete-book/<int:a>/', delete_book),
    path('update-book/<int:a>/', book_update)
]
