from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
)
from rest_framework.response import Response

from polls.models import Question, Choice
from .serializers import PollsListSerializer, ChoiceSerializer, ChoiceVoteSerializer

class PollsListView(ListAPIView):
    """
        View Polls List
        /api/polls/
    """
    queryset = Question.objects.all()
    serializer_class = PollsListSerializer

class PollsDetailsView(RetrieveAPIView):
    """
        View Single polls Details
        api/polls/2/
    """
    queryset = Question.objects.all()
    serializer_class = PollsListSerializer

class PollsCreateView(CreateAPIView):
    """
        Create New Polls
        api/polls/create/
    """
    queryset = Question.objects.all()
    serializer_class = PollsListSerializer

class PollsUpdateView(UpdateAPIView):
    """
        Update polls
        api/polls/2/update/
    """
    queryset = Question.objects.all()
    serializer_class = PollsListSerializer

class PollsDeleteView(DestroyAPIView):
    """
        Delete polls
        api/polls/2/delete/
    """
    queryset = Question.objects.all()
    serializer_class = PollsListSerializer


class ChoiceCreateView(CreateAPIView):
    """
        Create New choise
        api/polls/choice/create/
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ChoiceVoteView(UpdateAPIView):
    """
        Give vote
        api/polls/choice/vote/2
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceVoteSerializer

"""
    def perform_create(self, serializer):
        question = Question.objects.get(pk=self.kwargs['pk'])
        try:
            selected_choice = question.choice_set.get(pk=self.kwargs['pk'])
            #selected_choice = Choice.objects.get(pk=self.kwargs['pk'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            raise ValidationError('You have already signed up')
        else:
            selected_choice.votes += 1
            selected_choice.save()

        serializer.save()
"""
class ChoiceListView(ListAPIView):
    """
        Get Choice of a single poll
        api/polls/choice/2
    """
    #queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    lookup_field = 'question'

    def get_queryset(self):
        return Choice.objects.all().filter(question= self.kwargs['pk'])