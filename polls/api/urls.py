from django.conf.urls import url

from .views import (
    PollsListView,
    PollsDetailsView,
    PollsUpdateView,
    PollsDeleteView,
    PollsCreateView,
    ChoiceListView,
    ChoiceCreateView,
    ChoiceVoteView
)

app_name = 'polls'
urlpatterns = [
    url(r'^$', PollsListView.as_view(), name='list'),
    url(r'^create/$', PollsCreateView.as_view(), name='create'),
    url(r'^choice/create/$', ChoiceCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', PollsDetailsView.as_view(), name='detail'),

    url(r'^choice/(?P<pk>[0-9]+)$', ChoiceListView.as_view(), name='choice'),
    url(r'^vote/(?P<pk>[0-9]+)$', ChoiceVoteView.as_view(), name='vote'),

    url(r'^(?P<pk>[0-9]+)/update/$', PollsUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', PollsDeleteView.as_view(), name='delete'),
]
