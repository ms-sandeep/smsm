from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # Student CRUD
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('students/add/', views.StudentCreateView.as_view(), name='student-add'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student-edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),
    # Chart endpoints
    path('chart/enrollment/', views.enrollment_chart, name='enrollment-chart-data'),
    path('chart/view/', views.EnrollmentChartView.as_view(), name='enrollment-chart-view'),
]
