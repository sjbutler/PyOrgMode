#!/usr/bin/python2
import sys
import pynotify
sys.path.append('/home/dionisos/logiciels/myPyOrgMode')


def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.set_timeout(300000)
    notice.set_urgency(pynotify.URGENCY_CRITICAL)
    notice.show()
    return

from PyOrgMode import PyOrgMode
from datetime import date

base = PyOrgMode.OrgDataStructure()
base.load_from_file("/home/dionisos/organisation/agenda.org")

urgent_tasks = []
for task in base.extract_todo_list():
    if (task.priority == 'A'):
        if hasattr(task, "scheduled") and task.scheduled and task.scheduled.should_be_done():
            urgent_tasks.append(task)

if len(urgent_tasks) != 0:
    message = ""
    for task in urgent_tasks:
        message += str(task) + "\n"
    sendmessage('You have some urgent tasks !!!', message)
