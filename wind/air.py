#!/usr/bin/env python

import os
import re
import xively
import subprocess
import time
import datetime
import requests
import sys

temperature = 0
humidity = 0

# extract feed_id and api_key from environment variables
FEED_ID = "YOUR_FEED_ID" #CHANGE IT
API_KEY = "YOUR_KEY" #CHANGE IT
DEBUG = False

# initialize api client
api = xively.XivelyAPIClient(API_KEY)

# Run the DHT program to get the humidity and temperature readings!

def read_dht():
  while(True):

    output = subprocess.check_output(["./Adafruit_DHT", "2302", "4"]);
    if DEBUG:
      print output
    matches = re.search("Temp =\s+([0-9.]+)", output)
    if (not matches):
      time.sleep(3)
      continue
    temperature = float(matches.group(1))

    # search for humidity printout
    matches = re.search("Hum =\s+([0-9.]+)", output)
    if (not matches):
      time.sleep(3)
      continue
    humidity = float(matches.group(1))
    if DEBUG:
      print "Temperature: %.1f C" % temperature
      print "Humidity:    %.1f %%" % humidity

    return {'temperature':temperature,'humidity':humidity}
    #time.sleep(10)

def get_datastream(feed):
  try:
    temp_datastream = feed.datastreams.get("Temperature")
    if DEBUG:
      print "Found existing temperature datastream"
  except:
    if DEBUG:
      print "Creating new temperature datastream"
    temp_datastream = feed.datastreams.create("Temperature", tags="temperature")

  try:
    humidity_datastream = feed.datastreams.get("Humidity")
    if DEBUG:
      print "Found existing humidity datastream"
  except:
    if DEBUG:
      print "Creating new humidity datastream"
    humidity_datastream = feed.datastreams.create("Humidity", tags="humidity")

  return {'tempds':temp_datastream, 'humidityds':humidity_datastream}

def run():
  print "Starting Xively DHT script"

  feed = api.feeds.get(FEED_ID)

  datastreams = get_datastream(feed)
  datastreams['tempds'].max_value = None
  datastreams['tempds'].min_value = None
  datastreams['humidityds'].max_value = None
  datastreams['humidityds'].min_value = None

  while True:
    dhtdata = read_dht()

    if DEBUG:
      print "Updating Xively feed with temperature: %.1f C" % dhtdata['temperature']
      print "Updating Xively feed with humidity: %.1f percent" % dhtdata['humidity']

    datastreams['tempds'].current_value = dhtdata['temperature']
    datastreams['tempds'].at = datetime.datetime.utcnow()

    datastreams['humidityds'].current_value = dhtdata['humidity']
    datastreams['humidityds'].at = datetime.datetime.utcnow()
    #print datetime.datetime.now()
    #print datetime.datetime.utcnow()

    try:
      datastreams['tempds'].update()
      datastreams['humidityds'].update()
    except requests.HTTPError as e:
      print "HTTPError({0}): {1}".format(e.errno, e.strerror)

    time.sleep(120)

run()