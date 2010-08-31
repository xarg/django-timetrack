import json
import re
from datetime import datetime, timedelta

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

from settings import SITE_ID
from models import Project, Entry, EntryLog, EntryTime, Tag

@login_required
def index(REQUEST):
    projects = Project.objects.filter(archived=False).filter(site=SITE_ID).\
                filter(user=REQUEST.user)
    entries = Entry.objects.filter(project__in=[x.id for x in projects]).\
                filter(user=REQUEST.user)
    return render_to_response(
        'index.html',
        {
            'projects': projects,
            'entries': entries,
            'SITE_URL': 'http://' + REQUEST.META.get('HTTP_HOST') + '/',
        },
        context_instance=RequestContext(REQUEST)
    )

def suggest(REQUEST, model = None):
    """ Return results for Project names or Tags """
    query = REQUEST.GET.get('q')
    objects = []
    data = []
    if model == 'Project':
        objects = Project.objects.filter(title__startswith=query).all()
    elif model == 'Tag':
        objects = Tag.objects.filter(name__startswith=query).all()

    for object in objects:
        if model == 'Project':
            data.append(object.title)
        elif model == 'Tag':
            data.append(object.name)
    return HttpResponse(json.dumps(data), content_type='application/json')

def submit(REQUEST, command = None):
    """ This is command processing """
    command_patterns = {
        'add_project':
            re.compile('^add (?P<project>.+)(?: with )?(?P<tags>.+)?$')
    }

    for action, pattern in command_patterns.items():
        match = pattern.match(command)
        if match:
            if action == 'add_project':
                project = match.group('project')
                tags = str(match.group('tags')).split(' ')
                import pdb; pdb.set_trace()
    return HttpResponse('OK')

def start_stop(REQUEST, pk = None):
    """
    - Start/Stop an Entry adding an EntryTime and recalculating
    Entry.elapsed_time for the new action
    """
    entry = get_object_or_404(Entry, pk=pk)
    entry.start_stop()
