from django.conf.urls.defaults import *
from piston.resource import Resource

import views
from handlers import ProjectHandler, EntryHandler, EntryLogHandler, \
                    EntryTimeHandler, TagHandler
urlpatterns = patterns('',
    url(r'^suggest/(?P<model>\w+)?', views.suggest, name="suggest"),
    url(r'^submit/(?P<command>.+)?', views.submit, name="submit"),
    url(r'^start_stop/', views.start_stop, name="start_stop"),
    url(r'^api/Project/(?P<id>\d+)?', Resource(ProjectHandler),
        name="api_project"),
    url(r'^api/Entry/(?P<id>\d+)?', Resource(EntryHandler),
        name="api_entry"),
    url(r'^api/EntryLog/(?P<id>\d+)?', Resource(EntryLogHandler),
        name="api_entry_log"),
    url(r'^api/EntryTime/(?P<id>\d+)?', Resource(EntryTimeHandler),
        name="api_entry_time"),
    url(r'^api/Tag/(?P<id>\d+)?', Resource(TagHandler), name="apiTag"),
    url(r'', views.index, name="index")
)
