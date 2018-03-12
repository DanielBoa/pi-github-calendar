#!/usr/bin/env python

def mag(vec):
  return abs(vec[1] - vec[0])

def linear_scale(domain, range):
  domainMag = float(mag(domain))
  rangeMag = float(mag(range))

  def scale(input):
    return range[0] + (float(input) * rangeMag) / domainMag

  return scale