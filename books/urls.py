from django.urls import path
from .views import ArtBookListView, TextBookListView, BookDetailView, SearchResultsListView

urlpatterns=[
    path('', ArtBookListView.as_view(), name='art_book_list'),
    path('textbook/', TextBookListView.as_view(), name='text_book_list'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path("search/", SearchResultsListView.as_view(), name='search_results'),
]