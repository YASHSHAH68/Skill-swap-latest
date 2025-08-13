from django.urls import path
from . import views

app_name = 'category_skills'

urlpatterns = [
    path('courses/' , views.CourseView , name="courses"),
    path('courses/detail/' , views.CourseDetailView , name="courses/detail"),
    path('instructors/', views.InstructorView , name="instructor")
]