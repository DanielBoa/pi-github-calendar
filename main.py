#!/usr/bin/env python

import os
import polling
import git

user = os.environ['GITHUB_USER']
access_token = os.environ['GITHUB_ACCESS_TOKEN']
check_for_new_user_events = git.create_events_poller(user, access_token)

git.get_user_contrib_data(user)

# polling.poll(
#   lambda: check_for_new_user_events(),
#   step=60,
#   poll_forever=True
# )