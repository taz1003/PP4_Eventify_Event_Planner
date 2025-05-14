# PP4_Eventify_Event_Planner

ERROR 1: Created test events from admin panel and after trying to connect events/views.py to templates, the events were not showing - FIXED
Fixed it by adding context_object_name = 'events' in the EventList view.
