from django.urls import path

from app import views
urlpatterns = [
    path('addStudent/',views.addStudent,name='addStudent'),
    path('paid_student/<int:pk>/',views.paid_student,name='paid_student'),
    path('unpaid_student/<int:pk>/',views.unpaid_student,name='unpaid_student'),
    path('edit_student/<int:pk>/',views.edit_student,name='edit_student'),
    path('delete_student/<int:pk>/',views.delete_student,name='delete_student')
]
