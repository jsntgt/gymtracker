"""gymtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_view
from macros.views import ProductFormView, ProductDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/add', ProductFormView.as_view(), name="add_product"),
    path('product/<int:id>', ProductDetailView.as_view(), name="product_detail"),
    path('login/', auth_view.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('profile/update/', user_views.update, name="update"),
    path('', include('users.urls')),
    path('workout/', include('workout.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
