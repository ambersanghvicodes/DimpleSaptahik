from django.urls import path

from .views import EPaperView


app_name = "epaper"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('epaper/', EPaperView.as_view()),
    # path('articles/<int:pk>', ArticleView.as_view())
]