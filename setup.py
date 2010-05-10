#!/usr/bin/env python
import os
import fnmatch
from setuptools import setup

media_files = []
for dirpath, dirnames, filenames in os.walk(os.path.join('django_timetrack', 'media')):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        failed = False
        for pattern in ('*.py', '*.pyc', '*~', '.*', '*.bak', '*.swp*'):
            if fnmatch.fnmatchcase(filename, pattern):
                failed = True
        if failed:
            continue
        media_files.append(os.path.join(*filepath.split(os.sep)[1:]))

setup(
    name='django-timetrack',
    version='0.1',
    description='Django app that makes it easy to track your time using a js command line',
    author='Alexandru Plugaru',
    author_email='alexandru.plugaru@gmail.com',
    url='http://github.com/humanfromearth/django-timetrack',
    license='GPLv3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    packages=['django_timetrack'],
    package_data={'django_timetrack':[
        'templates/*.html',
    ] + media_files },
    requires=[
        'django (>=1.1)',
        'piston',
    ],
)
