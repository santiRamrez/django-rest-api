from django.urls import path, re_path
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import books, authors, users

app_name = "quickstart"
urlpatterns = [
    re_path('login/', users.login, name="login"),
    re_path('signup/', users.signup, name="signup"),
    re_path('test_token/', users.test_token, name="test_token"),
    path("books/", books.book_list, name="book_list"),
    path("books/<int:pk>/", books.book_detail, name="book_detail"),
    path("authors/", authors.author_list, name="author_list"),
]

