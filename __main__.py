#!/bin/bash
#
# PURPOSE
#	A daemon to parse feeds for audio files and manage those files
#
# TODO(PM): http://stackoverflow.com/questions/8567052

import sys
from datetime import datetime
import json
import feedparser

last_checked = datetime(2000,1,1)
date_format = '%d %b %Y %H:%M:%S' # TODO(PM): Note this is only string[5:-4]

def parse_entries(entries):
	"""Parse feed entries for links to audio files"""

	for entry in entries:
		content = entry.content[0]['value']	# TODO(PM): Assumes first element
		match = re.match('http://.*?.mp3', content)	# TODO(PM): No HTTPS, assumes MP3
		if match:
			print(match.group(0))

def entries_updated(feed):
	"""Return a list of the updated entries"""

	new_entries = []

	for entry in feed.entires:
		entry_dt = datetime(entry.updated[5:-4, date_format)
		if entry_dt > las_checked:
			new_entries.append(entry)

	return new_entries

def feed_updated(feed):
	"""Return true if the feed been updated since it was last checked"""

	feed_updated = datetime.strptime(feed.updated[5:-4], date_format)
	if feed_updated > last_checked:
		return true
	else:
		return false

def update_feed(feed):
	"""Update the feed"""

	if feed_updated(feed):
		new_entries = entries_updated(feed)
		audio_files = parse_entries(new_entries)

def add_feed(url):
	"""Try to add the url as a feed"""

	site = feedparser.parse(url)
	title = site.feed.title
	lowercase = title.lower()
	filename = lowercase.replace(" ", "_")
	with open(filename + '.json', 'w') as store:
		del site['bozo_exception']
		del site['bozo']
		json.dump(dict(site), store, indent=4)

def main():
	"""The main control flow of the application"""

	nargs = len(sys.argv)
	if nargs == 1:
		update_feeds()
	elif nargs == 2:
		add_feed(sys.argv[1])
	elif nargs > 2:
		print("Too many command-line arguments!")

if __name__ == "__main__":
	main()
	
