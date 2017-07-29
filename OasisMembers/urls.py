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
    django.conf.urls.url(r'^meetings/$', views.meetings, name='meetings'),
    django.conf.urls.url(r'^meeting/(?P<meeting_id>[0-9]+)/$',
                         views.meeting,
                         name='meeting'),
    django.conf.urls.url(r'^technique/(?P<technique_id>[0-9]+)/$',
                         views.technique,
                         name='technique'),
]
