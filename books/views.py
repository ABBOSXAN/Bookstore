from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import models
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Book, Review


# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

    def get_context_data(self, created_at=models.DateTimeField(auto_now=True), **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = created_at
        return context


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'
    queryset = Book.objects.all().prefetch_related('reviews__author', )


class SearchResultsListView(ListView):
    model = Book
    template_name = 'books/search_results.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query))
