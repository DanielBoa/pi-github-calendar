import requests
import xml.etree.ElementTree as ET

# Takes Github username, password/access token[, and HTTP headers dict]
# Returns a HEAD request for given users events.
def get_user_events_head(user, password, headers={}):
  url = 'https://api.github.com/users/' + user + '/events'
  auth = (user, password)
  return requests.head(url, auth=auth, headers=headers)

# Takes Github username and password/access token.
# Returns a polling function which will return true once a new user event exists.
def create_events_poller(user, password):
  e_tag = get_user_events_head(user, password).headers['ETag']
  headers = { 'If-None-Match': e_tag }

  def poller():
    return get_user_events_head(user, password, headers).status_code == 200

  return poller

# Takes svg contributions calendar as text.
# Returns multidimensional List representation of contributions.
def parse_contrib_svg(svg_text):
  root_el = ET.fromstring(svg_text)
  week_g_els = root_el.find('g').findall('g')
  weeks_of_rects_els = [week_g.findall('rect') for week_g in week_g_els]
  return [[int(day_el.attrib['data-count']) for day_el in week] for week in weeks_of_rects_els]

# Takes Github username.
# Returns user contributions data organised as a multidimensional list of weeks/days. 
def get_user_contrib_data(user):
  user_contrib_url = 'https://github.com/users/' + user + '/contributions'
  response = requests.get(user_contrib_url)
  return parse_contrib_svg(response.text)