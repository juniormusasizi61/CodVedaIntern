from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import redirect
from .models import Task
from .forms import SignUpForm, TaskForm

# ----- Roles & Permissions -----
# We'll use two roles: "admin" (Django admin/superuser) and "regular" (default)
# Managers/advanced roles could be added by assigning Django Group permissions.
def ensure_default_groups():
    # Create a "regular" group if missing (can be extended later)
    Group.objects.get_or_create(name="regular")

class OwnerOrAdminMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return self.request.user.is_superuser or obj.owner == self.request.user

# ----- Auth -----
class SignUpView(FormView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("tasks:list")

    def form_valid(self, form):
        user = form.save()
        ensure_default_groups()
        regular_group = Group.objects.get(name="regular")
        user.groups.add(regular_group)
        login(self.request, user)
        return super().form_valid(form)

# ----- Tasks -----
class TaskListView(LoginRequiredMixin, ListView):
    template_name = "tasks/task_list.html"
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.all()
        return Task.objects.filter(owner=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, OwnerOrAdminMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:list")

class TaskDeleteView(LoginRequiredMixin, OwnerOrAdminMixin, DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:list")
