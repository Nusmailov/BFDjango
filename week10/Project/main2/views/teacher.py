from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin


from main2.models import Teacher


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    context_object_name = 'teachers'


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    fields = ['name', 'surname', ]
    success_url = reverse_lazy('main2:teacher_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    fields = ['name', 'surname', ]
    success_url = reverse_lazy('main2:teacher_list')

    def get_queryset(self):
        return Teacher.objects.for_user(user=self.request.user)


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    fields = ['name', 'surname', ]
    success_url = reverse_lazy('main2:teacher_list')

    def get_queryset(self):
        return Teacher.objects.for_user(user=self.request.user)

