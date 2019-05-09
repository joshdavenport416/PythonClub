from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

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