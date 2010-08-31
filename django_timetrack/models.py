from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from fields import TimeSumField

class Project(models.Model):
    site = models.ForeignKey(Site)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    archived = models.BooleanField(default=False)
    estimated_time = TimeSumField(blank=True, help_text="Format: hh:mm") # How much time is allocated for this project
    created_datetime = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.title

class Entry(models.Model):
    class Meta:
        verbose_name_plural = 'Entries'
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    body = models.TextField()
    active = models.BooleanField(default=False)
    estimated_time = TimeSumField(blank=True, help_text="Format: hh:mm") # Allows 50:10 - 50 hours and 10 minutes
    elapsed_time = TimeSumField(blank=True, help_text="Format: hh:mm")

    def start_stop(self):
        """ Start/Stop entry"""
        active_entry = Entry.objects.filter(site=self.site).filter(user=self.user).filter(active=True)
        import pdb; pdb.set_trace()

        if active_entry: # We have an active Entry, calc timedelta, update then stop
            entry_time = EntryTime.objects.filter(entry=active_entry).filter(end_datetime = None)
            entry_time.end_datetime = datetime.now()
            entry_time.save()

            active_entry.active = False
            active_entry.elapsed_time += timedelta(entry_time.end_datetime, entry_time.start_datetime)
            active_entry.save()

            if active_entry != self: # Start if not the same entry
                self.active = True
                self.save()
        entry_time = EntryTime(entry=self)
        entry_time.save()

    def __unicode__(self):
        return self.body

class EntryTime(models.Model):
    """
    When user clicks start clock it
    creates and EntryTime with a start datetime
    """
    entry = models.ForeignKey(Entry)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(blank=True)

class EntryLog(models.Model):
    """ Provide a note for a Entry """
    entry = models.ForeignKey(Entry)
    body = models.TextField()
    created_datetime = models.DateTimeField(default=datetime.now())

class Tag(models.Model):
    """ Used for projects and entries """
    name = models.CharField(max_length=50)
    projects = models.ManyToManyField(Project, blank=True, related_name="project_tags")
    entries = models.ManyToManyField(Entry, blank=True, related_name="entry_tags")
    def __unicode__(self):
        return self.name
