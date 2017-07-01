import django.conf.urls
import views

urlpatterns = [
    django.conf.urls.url(r'^$', views.index, name='index'),
]
