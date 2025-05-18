# PP4_Eventify_Event_Planner

ERROR 1: Created test events from admin panel and after trying to connect events/views.py to templates, the events were not showing - FIXED
Fixed it by adding context_object_name = 'events' in the EventList view.
ERROR 2: Issues while creating Attendance model ('relation "events_attendance" already exists', cannot be migrated). FIXED
Fixed it by deleting all the migrations (python manage.py migrate events zero) and re-applying migrations.

Code from events/views.py line 18-29 taken from reddit.