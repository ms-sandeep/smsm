from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Count
from .models import Student, Course

class HomeView(TemplateView):
    template_name = 'core/home.html'

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'core/student_list.html'
    context_object_name = 'students'

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['name','dob','email','address']
    template_name = 'core/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ['name','dob','email','address']
    template_name = 'core/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'core/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')

def enrollment_chart(request):
    data = Course.objects.annotate(student_count=Count('enrollments')).values('course_name','student_count')
    labels = [d['course_name'] for d in data]
    values = [d['student_count'] for d in data]
    return JsonResponse({'labels': labels, 'values': values})

class EnrollmentChartView(TemplateView):
    template_name = 'core/enrollment_chart.html'
