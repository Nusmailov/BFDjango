from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from main2.models import Student
from main2.forms import StudentForm


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'students'


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "student/student_detail.html"


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['name',]
    success_url = reverse_lazy('main2:student_list')
    template_name = "student/student_form.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ['name',]
    success_url = reverse_lazy('main2:student_list')
    template_name = "student/student_form.html"

    def get_queryset(self):
        return Student.objects.for_user(user=self.request.user)


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('main2:student_list')
    template_name = "student/student_confirm_delete.html"

    def get_queryset(self):
        return Student.objects.for_user(user=self.request.user)