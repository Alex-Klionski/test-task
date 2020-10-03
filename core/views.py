from django.utils import timezone
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile, Device
from .forms import ProfileForm, DeviceForm, GiveOutForm


def register_page(request):
    return render(request, 'account/REGISTER.html')


def login_page(request):
    return render(request, 'account/LOGIN.html')


class ItemList(ListView):
    template_name = "core/userprofile_list.html"
    queryset = Device.objects.all()


class ProfileEditView(LoginRequiredMixin, UpdateView):

    form_class = ProfileForm
    model = UserProfile
    context_object_name = 'profile'
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('edit-avatar')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class DeviceCreate(LoginRequiredMixin, CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'device/device-add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user

        form.save()
        return super(DeviceCreate, self).form_valid(form)


class GiveOutCreate(LoginRequiredMixin, CreateView):
    model = Device
    form_class = GiveOutForm
    template_name = 'device/give-out.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        device = Device.objects.get(title=form.cleaned_data.get("device"))
        device.used_by = form.instance.used_by
        device.date = timezone.now()
        device.save()
        return redirect('index')