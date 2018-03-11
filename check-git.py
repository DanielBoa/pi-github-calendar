#!/usr/bin/env python

import os
import requests
import polling

user =         os.environ['GITHUB_USER']
access_token = os.environ['GITHUB_ACCESS_TOKEN']
e_tag = None

def create_events_api_url(user):
  return 'https://api.github.com/users/' + user + '/events'

def get_user_events_head(user, password):
  url = create_events_api_url(user)
  auth = (user, password)
  return requests.head(url, auth=auth)

def check_for_new_user_events():
  global e_tag
  last_e_tag = e_tag
  e_tag = get_user_events_head(user, access_token).headers['ETag']

  if last_e_tag == None:
    print('Started polling: ', e_tag)
    return False
    
  if last_e_tag != e_tag:
    print('New event: ', e_tag)
    return True
  else:
    print('No new events: ', e_tag)
    return False

polling.poll(
  lambda: check_for_new_user_events(),
  step=60,
  poll_forever=True
)