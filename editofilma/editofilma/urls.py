"""editofilma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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


from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from filma import HodViews
from editofilma import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HodViews.home,name="home"),
    path('delete_movie/<str:movie_id>',HodViews.delete_movie,name="delete_movie"),
    path('delete_network/<str:network_id>',HodViews.delete_network,name="delete_network"),
    path('delete_genre/<str:genre_id>',HodViews.delete_genre,name="delete_genre"),
    path('add_network', HodViews.add_network,name="add_network"),
    path('add_network_save', HodViews.add_network_save,name="add_network_save"),
    path('add_genre', HodViews.add_genre,name="add_genre"),
    path('add_genre_save', HodViews.add_genre_save,name="add_genre_save"),
    path('add_movie', HodViews.add_movie,name="add_movie"),
    path('add_movie_save', HodViews.add_movie_save,name="add_movie_save"),
    path('manage_genre', HodViews.manage_genre,name="manage_genre"),
    path('manage_movie', HodViews.manage_movie,name="manage_movie"),
    path('manage_network', HodViews.manage_network,name="manage_network"),
    path('edit_genre/<str:genre_id>', HodViews.edit_genre,name="edit_genre"),
    path('edit_genre_save', HodViews.edit_genre_save,name="edit_genre_save"),
    path('edit_network/<str:network_id>', HodViews.edit_network,name="edit_network"),
    path('edit_network_save', HodViews.edit_network_save,name="edit_network_save"),
    path('edit_movie/<str:movie_id>', HodViews.edit_movie,name="edit_movie"),
    path('edit_movie_save', HodViews.edit_movie_save,name="edit_movie_save"),
    path('view_movie/<str:movie_id>', HodViews.view_movie,name="view_movie"),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
