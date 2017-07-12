import django.conf.urls
import views

app_name = 'OasisMembers'
urlpatterns = [
    django.conf.urls.url(r'^$', views.index, name='index'),
    django.conf.urls.url(r'^members/$', views.members, name='members'),
    django.conf.urls.url(r'^member/(?P<member_id>[0-9]+)/$',
                         views.member,
                         name='member'),
    django.conf.urls.url(r'^member-notes-edit/(?P<member_id>[0-9]+)/$',
                         views.member_notes_edit,
                         name='member-notes-edit'),
    django.conf.urls.url(r'^member-notes-submit/(?P<member_id>[0-9]+)/$',
                         views.member_notes_submit,
                         name='member-notes-submit'),
]
