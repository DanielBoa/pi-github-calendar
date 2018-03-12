#!/usr/bin/env python

import os
import polling
import git
from draw import draw_contrib_data

user = os.environ['GITHUB_USER']
access_token = os.environ['GITHUB_ACCESS_TOKEN']

def loop():
  check_for_new_user_events = git.create_events_poller(user, access_token)
  contrib_data = git.get_user_contrib_data(user)

  draw_contrib_data(contrib_data)

  polling.poll(
    lambda: check_for_new_user_events(),
    step=60,
    poll_forever=True
  )

  loop()

loop();
