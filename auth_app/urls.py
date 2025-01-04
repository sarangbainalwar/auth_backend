from django.urls import path
from auth_app.views import SignupView, LoginView

urlpatterns = [
     path('admin/', admin.site.urls),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
]
