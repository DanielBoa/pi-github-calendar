#!/usr/bin/env python

import os
import polling
from git import create_events_poller

user = os.environ['GITHUB_USER']
access_token = os.environ['GITHUB_ACCESS_TOKEN']

check_for_new_user_events = create_events_poller(user, access_token)

print('before polling')

polling.poll(
  lambda: check_for_new_user_events(),
  step=60,
  poll_forever=True
)

print('after polling finished')