from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        app_label = 'octofit_tracker'


class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        app_label = 'octofit_tracker'


class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()

    class Meta:
        app_label = 'octofit_tracker'


class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)

    class Meta:
        app_label = 'octofit_tracker'


User = get_user_model()


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'team': marvel},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'team': marvel},
            {'username': 'batman', 'email': 'batman@dc.com', 'team': dc},
            {'username': 'superman', 'email': 'superman@dc.com', 'team': dc},
        ]
        for u in users:
            User.objects.create_user(
                username=u['username'], email=u['email'], password='password')

        # Activities
        Activity.objects.create(
            user='ironman', activity_type='run', duration=30)
        Activity.objects.create(
            user='batman', activity_type='cycle', duration=45)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=80)

        # Workouts
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Squats', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS(
            'octofit_db database populated with test data.'))
