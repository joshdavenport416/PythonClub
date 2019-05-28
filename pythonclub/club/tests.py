from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from django.contrib.auth.models import User
from .forms import ResourceForm


# Create your tests here.
#tests for models
class MeetingTest(TestCase):
    def test_string(self):
        type=Meeting(meetingtitle='Python 101')
        self.assertEqual(str(type),type.meetingtitle)
        
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def test_string(self):
        type=MeetingMinutes(minutes='sample')
        self.assertEqual(str(type),type.minutes)
    
    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'club_meetingminutes')

class ResourceTest(TestCase):
    def test_string(self):
        type=Resource(resourcename='some text book')
        self.assertEqual(str(type),type.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_string(self):
        type=Event(eventtitle='Holiday Party')
        self.assertEqual(str(type),type.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'club_event')

# form tests
class ResourceFormTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='user1', password='P@ssw0rd1')

    def test_ResourceForm(self):
        data={
            'resourcename' : 'resource1',
            'resourcetype' : 'type1',
            'dateentered' : datetime.date(2019,5,28),
            'userid' : self.user,
        }
        form = ResourceForm(data=data)
        self.assertTrue(form.is_valid)

    def test_ResourceFormInvalid(self):
        data = {
            'resourcename': 'resource1',
            'resourcetype': '',
            'dateentered': datetime.date(2019, 5, 28),
            'userid': self.user,
        }
        form = ResourceForm(data=data)
        self.assertFalse(form.is_valid())


