import requests

def create_events_api_url(user):
  return 'https://api.github.com/users/' + user + '/events'

# Takes Github username, password/access token[, and HTTP headers dict]
# Returns a HEAD request for given users events.
def get_user_events_head(user, password, headers={}):
  url = create_events_api_url(user)
  auth = (user, password)
  return requests.head(url, auth=auth, headers=headers)

# Takes Github username and password/access token.
# Returns a polling function which will return true once a new user event exists.
def create_events_poller(user, password):
  e_tag = get_user_events_head(user, password).headers['ETag']
  headers = { 'If-None-Match': e_tag }

  def poller():
    resource_changed = get_user_events_head(user, password, headers).status_code == 200
    print(resource_changed)
    return resource_changed

  return poller