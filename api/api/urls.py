from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import re_path, path, include
from django.contrib.auth.decorators import login_required
from base import views as baseviews
from base.views import IPView
from base.forms import UserLoginForm
from admin.views import AdminHomeView
from alumni.views import AlumniHomeView
from student.views import StudentHomeView
from base.decorators import switch_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    re_path(r"^register/$", baseviews.register, name="register"),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html", authentication_form=UserLoginForm
        ),
        name="login",
    ),


    path("djangoadmin/", admin.site.urls),
    path("students/", include('student.urls')),
    path('alumni/', include('alumni.urls')),
    path('admin/', include('admin.urls')),
    path("", login_required(switch_view(AdminHomeView.as_view(), AlumniHomeView.as_view(), StudentHomeView.as_view())), name="home"),
    path('activate_account', baseviews.activate_account, name='activate_account'),
    path("accounts/logout/", baseviews.log_out, name="logout"),
    path("error/", IPView.as_view(), name="error"),
    path("not_logged_in_error/", baseviews.not_logged_in_error, name="not_logged_in_error"),
    path(
        "activate/<uidb64>/<token>",
        baseviews.activate,
        name="activate",
    ),
    path('posts/', include('posts.urls'))
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


