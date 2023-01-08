from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from .forms import *
from .models import *
from .utils import *


class CNCIndex(DataMixin, ListView):
    model = CncListMetall
    template_name = 'cnc_mashine/index.html'
    context_object_name = 'list_cnc'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_dict = self.get_user_context(title='Главная страница')
        return context | c_dict


class ShowCNC(DataMixin, DeleteView):
    model = CncListMetall
    template_name = 'cnc_mashine/cnc.html'
    slug_url_kwarg = 'cnc_slug'
    context_object_name = 'cnc_name'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_dict = self.get_user_context(title=context['cnc_name'], cat_selected=context['cnc_name'].category_id.slug)
        return context | c_dict


class ShowCategory(DataMixin, ListView):
    model = CncListMetall
    template_name = 'cnc_mashine/index.html'
    context_object_name = 'list_cnc'
    allow_empty = False

    def get_queryset(self):
        return CncListMetall.objects.filter(category_id__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_dict = self.get_user_context(title=context['list_cnc'][0].category_id,
                                       cat_selected=context['list_cnc'][0].category_id.slug)
        return context | c_dict


class AddCNC(DataMixin, CreateView):
    form_class = AddCNC
    template_name = 'cnc_mashine/add_cnc.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_dict = self.get_user_context(title='Разместить объявление', cat_selected=None)
        return context | c_dict


class Register(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'cnc_mashine/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_dict = self.get_user_context(title='Регистрация', cat_selected=None)
        return context | c_dict

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class Login(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'cnc_mashine/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_dict = self.get_user_context(title='Вход', cat_selected=None)
        return context | c_dict

    def get_success_url(self):
        return reverse_lazy('home')


def contact(request):
    context = {
        'menu': menu,
        'title': 'Контакты',
        'cats': Category.objects.all()
    }
    return render(request, 'cnc_mashine/contact.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте',
        'cats': Category.objects.all()
    }
    return render(request, 'cnc_mashine/about.html', context=context)

def logout_user(request):
    logout(request)
    return redirect('login')






