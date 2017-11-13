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

    url(r'^(?P<pk>[0-9]+)/choice/$', ChoiceListView.as_view(), name='choice'),

    #api/polls/1/choice/vote/2
    url(r'^(?P<question_no>[0-9]+)/choice/vote/(?P<pk>[0-9]+)$', ChoiceVoteView.as_view(), name='vote'),

    url(r'^(?P<pk>[0-9]+)/update/$', PollsUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', PollsDeleteView.as_view(), name='delete'),
]
