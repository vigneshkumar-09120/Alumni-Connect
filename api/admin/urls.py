from django.urls import path, re_path
from base.views import IPView
from .views import UploadView, ReportView, HelpView,EventView,EventDeleteView,EventUpdateView
from base.decorators import switch_view
from .import views

urlpatterns = [
    path('upload', switch_view(UploadView.as_view(), IPView.as_view(), IPView.as_view()), name='upload_admin'),
    path('reports', switch_view(ReportView.as_view(), IPView.as_view(), IPView.as_view()), name='reports'),
    path('help', switch_view(HelpView.as_view(), IPView.as_view(), IPView.as_view()), name='help'),
    path('eventform',EventView.as_view(),name='new_event'),
    path('eventlist',views.Event_list,name='list_event'),
    path("delete/<int:pk>/", EventDeleteView.as_view(), name="delete_event"),
    path("edit/<int:pk>/", EventUpdateView.as_view(), name="update_event"),
    path('profile/<int:id>',views.profileview,name='view_alumni'),

    

]