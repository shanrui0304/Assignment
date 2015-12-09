from django.shortcuts import render, get_object_or_404

from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic

from django.utils import timezone
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
    	Return the last five published questions (not including those set to be
    	published in the future).
    	"""
    	return Question.objects.filter(
            pub_date__lte=timezone.now()
    	).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    model = Question
    template_name = 'polls/results.html'
