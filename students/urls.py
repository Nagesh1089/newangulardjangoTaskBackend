from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create', views.student_create, name='student_create'),
    path('update', views.student_update, name='student_update'),
    path('delete', views.delete_student, name='student_delete'),
]
# POST http://127.0.0.1:8000/students/create
# GET http://127.0.0.1:8000/students/create
# DELETE http://127.0.0.1:8000/students/delete