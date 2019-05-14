from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import ResourceForm, MeetingForm

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

def newresource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'club/newresource.html', {'form' : form})

def newmeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form' : form})