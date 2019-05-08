from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def getresources(request):
    resource_list=Resource.objects.all()
    context={'resource_list' : resource_list }
    return render(request, 'club/resources.html', context=context)

def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meetings_list': meetings_list})

def meetingsdetail(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={
        'meet' : meet,
    }
    return render (request, 'club/meetingsdetail.html', context=context)