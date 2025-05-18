from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Event, Attendance, Comment
from datetime import date


# Attendance test
def test_update_attendance_redirects_if_not_logged_in(self):
    event = Event.objects.create(title='Test Event', slug='test-event')
    response = self.client.get(reverse(
        'update_attendance', args=[event.slug, 'ATTENDING']))
    self.assertRedirects(
        response, f"/accounts/login/?next=/events/{event.slug}/ATTENDING/")


def test_logged_in_user_can_update_attendance(self):
    user = User.objects.create_user(username='testuser', password='testpass')
    event = Event.objects.create(title='Test Event', slug='test-event')

    self.client.login(username='testuser', password='testpass')
    response = self.client.get(reverse(
        'update_attendance', args=[event.slug, 'ATTENDING']))

    self.assertRedirects(response, reverse('event_detail', args=[event.slug]))

    attendance = Attendance.objects.get(user=user, event=event)
    self.assertEqual(attendance.status, 'ATTENDING')

# Create event test


class CreateEventViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')


def test_logged_in_user_can_create_event(self):
    self.client.login(username='testuser', password='testpass')

    form_data = {
        'title': 'Test Event',
        'description': 'A test description',
        'slug': 'test-event',
        'location': 'Test Location',
        'start_time': '2030-01-01T10:00',
        'end_time': '2030-01-01T12:00'
    }

    response = self.client.post(reverse('create_event'), form_data)

    if Event.objects.count() == 0:
        print(response.context['form'].errors)

    self.assertEqual(Event.objects.count(), 1)
    event = Event.objects.first()
    self.assertEqual(event.title, 'Test Event')
    self.assertEqual(event.creator, self.user)
    self.assertRedirects(response, reverse(
        'event_detail', args=[event.slug]))


# Event detail test, attends to comment testing as well


class EventDetailViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='pass1234')
        self.event = Event.objects.create(
            title='Sample Event',
            slug='sample-event',
            description='Sample Description',
            location='Sample Location',
            date=date.today(),
            creator=self.user
        )

    def test_post_comment_to_event_detail(self):
        self.client.login(username='testuser', password='pass1234')

        response = self.client.post(
            reverse('event_detail', args=[self.event.slug]),
            data={
                'body': 'This is a test comment.'
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.body, 'This is a test comment.')
        self.assertEqual(comment.event, self.event)
        self.assertEqual(comment.author, self.user)
