from piston.handler import BaseHandler
from piston.utils import rc

from timetracking.models import Project, Entry, EntryLog, EntryTime, Tag

class ProjectHandler(BaseHandler):
    allowed_methods = ('GET','POST','DELETE', 'PUT')
    model = Project
    
    def create(self, REQUEST):
        pass
    def read(self, REQUEST, id = None):
        pass
    def update(self, REQUEST, id = None):
        pass
    def delete(self, REQUEST, id = None):
        pass
    
class EntryHandler(BaseHandler):
    allowed_methods = ('GET','POST','DELETE', 'PUT')
    model = Entry
    
    def create(self, REQUEST):
        pass
    def read(self, REQUEST, id = None):
        pass
    def update(self, REQUEST, id = None):
        pass
    def delete(self, REQUEST, id = None):
        pass

class EntryLogHandler(BaseHandler):
    allowed_methods = ('GET','POST','DELETE', 'PUT')
    model = EntryLog
    
    def create(self, REQUEST):
        pass
    def read(self, REQUEST, id = None):
        pass
    def update(self, REQUEST, id = None):
        pass
    def delete(self, REQUEST, id = None):
        pass
    
class EntryTimeHandler(BaseHandler):
    allowed_methods = ('GET','POST','DELETE', 'PUT')
    model = EntryTime
    
    def create(self, REQUEST):
        pass
    def read(self, REQUEST, id = None):
        pass
    def update(self, REQUEST, id = None):
        pass
    def delete(self, REQUEST, id = None):
        pass
class TagHandler(BaseHandler):
    allowed_methods = ('GET','POST','DELETE', 'PUT')
    model = Tag
    
    def create(self, REQUEST):
        pass
    def read(self, REQUEST, id = None):
        pass
    def update(self, REQUEST, id = None):
        pass
    def delete(self, REQUEST, id = None):
        pass
