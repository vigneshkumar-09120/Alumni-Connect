from django.urls import path, re_path
from .views import StudentHomeView, StudentListView, StudentCreateView, StudentCommentView, StudentSearchView, StudentUploadView, StudentDeleteView,StudentUpdateView ,SkillView
from base.decorators import switch_view
from alumni.views import AlumniHomeView
from admin.views import AdminHomeView
from base.views import IPView
from .import views

urlpatterns = [
    path('', views.StudentListView, name='list_student'),
    path('new', switch_view(StudentCreateView.as_view(), IPView.as_view(), IPView.as_view()), name='new_student'),
    path('upload', switch_view(StudentUploadView.as_view(), IPView.as_view(), IPView.as_view()), name='upload_student'),
    path("delete/<int:pk>/", StudentDeleteView.as_view(), name="delete_student"),
    path('comments', StudentCommentView.as_view(), name='list_student_comment'),
    path('search', StudentSearchView.as_view(), name='search_student'),
     path("edit/<int:pk>/", StudentUpdateView.as_view(), name="update_student"),
     path("skillfm",views.SkillView,name='skillfm'),
     path("sprofile",views.sprofile,name='sprofile'),
     path("alsearch",views.AlumniList,name='alsearch'),
       path("chatbot",views.chatbot,name='chatbot'),

]