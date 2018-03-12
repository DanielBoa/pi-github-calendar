import scrollphathd as sphd
from scale import linear_scale

def get_brightness_scale(contrib_data):
  max_contrib_count = max([max(week) for week in contrib_data])
  domain = [0, max_contrib_count]
  return linear_scale(domain, [0.2, 1.0])

def draw_contrib_data(contrib_data):
  (width, height) = sphd.get_shape()
  first_day_index = len(contrib_data) - width
  weeks_to_draw = contrib_data[first_day_index:]
  brightness_scale = get_brightness_scale(weeks_to_draw)

  for x in range(width):
    for y in range(7):
      week_to_draw = weeks_to_draw[x]
      week = week_to_draw + ([0] * (7 - len(week_to_draw)))
      contrib_count = week[y]
      brightness = round(brightness_scale(contrib_count), 2) if contrib_count != 0 else 0
      sphd.set_pixel(x, y, brightness)

  sphd.show()