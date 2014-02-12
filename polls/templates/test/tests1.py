#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.
from polls.models import Poll, Choice   # Import the model classes we just wrote.

# No polls are in the system yet.
Poll.objects.all()
# []

# Create a new Poll.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
from django.utils import timezone
p = Poll(question="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
p.save()

# Now it has an ID. Note that this might say "1L" instead of "1", depending
# on which database you're using. That's no biggie; it just means your
# database backend prefers to return integers as Python long integer
# objects.
print ( p.id )
#1

# Access database columns via Python attributes.
print ( p.question )
#"What's new?"

print ( p.pub_date )
#datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
p.question="What's up?"
p.save()

# objects.all() displays all the polls in the database.
print ( Poll.objects.all() )
#[<Poll: Poll object>]