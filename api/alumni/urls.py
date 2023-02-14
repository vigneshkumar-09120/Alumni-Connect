from django.urls import path, re_path

from .views import AlumniListView, AlumniCreateView, AlumniUploadView, AlumniDeleteView, AlumniPostView, AlumniSearchView,AlumniUpdateView
from base.views import IPView
from .import views
from base.decorators import switch_view

urlpatterns = [
    path('', views.AlumniListView, name = 'list_alumni'),
    path('new', switch_view(AlumniCreateView.as_view(), IPView.as_view(), IPView.as_view()), name = 'new_alumni'),
    path('upload', switch_view(AlumniUploadView.as_view(), IPView.as_view(), IPView.as_view()), name = 'upload_alumni'),
    path("delete/<int:pk>/", AlumniDeleteView.as_view(), name="delete_alumni"),
    path('posts', AlumniPostView.as_view(), name='list_alumni_post'),
    path('search', AlumniSearchView.as_view(), name='search_alumni'),
    path("edit/<int:pk>/", AlumniUpdateView.as_view(), name="update_alumni"),
    path('job',views.CategoryView,name='job'),
    path('high',views.HigherView,name='high'),
    path('profile',views.Profile,name='profile'),
    path('update',views.update,name='update'),
     path('update2',views.update2,name='update2'),
     path('update3',views.update3,name='update3'),


]