import scrollphathd as sphd
from scale import linear_scale

def get_brightness_scale(contrib_data):
  max_contrib_count = max([max(week) for week in contrib_data])
  domain = [0, max_contrib_count]
  return linear_scale(domain, [0, 1])

def draw_contrib_data(contrib_data):
  (width, height) = sphd.get_buffer_shape()
  first_day_index = len(contrib_data) - width
  weeks_to_draw = contrib_data[first_day_index:]
  brightness_scale = get_brightness_scale(weeks_to_draw)

  for x in range(width):
    for y in range(7):
      contrib_count = weeks_to_draw[x][y]
      brightness = brightness_scale(contrib_count)
      sphd.set_pixel(x, y, brightness)

  sphd.show()