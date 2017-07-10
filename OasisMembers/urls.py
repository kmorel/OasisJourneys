import django.conf.urls
import views

urlpatterns = [
    django.conf.urls.url(r'^$', views.index, name='index'),
    django.conf.urls.url(r'^members/$', views.members, name='members'),
    django.conf.urls.url(r'^member/(?P<member_id>[0-9]+)/$',
                         views.member,
                         name='member')
]
