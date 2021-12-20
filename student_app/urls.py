from django.urls import path
from student_app.views import *

urlpatterns = [
    path('student_details_post/', StudentDetailsPost, name='StudentDetails_Post'),
    path('student_details_get/', StudentDetailsGet, name='StudentDetails_Get'),
    path('student_details_edit/<int:pk>/', StudentDetailsEdit, name='StudentDetails_Edit'),
    path('student_details_delete/<int:id>/', Delete, name='StudentDetails_Delete'),
    path('', login, name='login'),
    path('logout/', Logout, name='logout'),
]