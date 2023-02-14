from django.urls import path, re_path
from . import views
from .views import PostListView, PostCreateView

from base.views import IPView
from base.decorators import switch_view

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', switch_view(IPView.as_view(), PostCreateView.as_view(), IPView.as_view()), name='new_post'),
]
