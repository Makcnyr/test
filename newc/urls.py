from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from newc.models import Articles


urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by('-date')[:20],
                             template_name="newc/posts.html")),
    path('<int:pk>/', DetailView.as_view(model=Articles, template_name='newc/post.html')),


]