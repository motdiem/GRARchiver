GRARchiver
==========

Quick Google Reader Archiver

### What is this ?

This is a small python script to archive your read items from google reader, before google reader closes on july 1st.
No warranty whatsoever - look at the source, I obviously don't know what I'm doing.

### Prerequisites

This uses [Request](http://docs.python-requests.org/en/latest/) to process the http requests.

### Usage
Launch with 
    python GRARchiver.py

### More Info
- Everything is done locally on your machine - at no point I receive any information from GRARchiver
- If you are using 2-factor authentication, you'll need to generate an application specific passwd
- What you do with the JSON file is up to you

### Acknowledgments
- Google Reader unofficial documentation from [undoc](http://undoc.in/) and [nick bradbury](http://ranchero.com/downloads/GoogleReaderAPI-2009.pdf)
