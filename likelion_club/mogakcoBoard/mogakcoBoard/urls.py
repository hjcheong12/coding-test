"""mogakcoBoard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from board import views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),
    path('account/', include('account.urls')),
    path('post_delete/<int:post_id>', views.post_delete, name='post_delete'),
    path('post_update/<int:post_id>', views.post_update, name='post_update'),
    path('comment_delete/<int:comment_id>', views.comment_delete, name='comment_delete'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)