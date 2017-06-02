========
Heimdall
========

An API to retrieve hardware metrics from a computer.

Heimdall is designed to monitor basic metrics from a given machine. It stores
those metrics in local log files organized down to the hour. A big decision was to
avoid large SQL-style databases in favor of the expectation that files would be
recorded with timestamp names appended, allowing easy aggregation by hour or by
day.

The API currently records data every minute and writes to a log file marked with
the current hourly timestamp. Each entry is marked as well with a much more accurate
timestamp. All times are in UTC. New log files are created every hour.

Local files ensure that should networking prove particularly taxed,
statistics can still be delivered since accessing a large SQL database
might timeout.

Installation
------------

To install dependencies, run: ::
    
    pip install -r requirements.txt

Basic Use
---------

To run the RESTful server, simply run: ::

    python client.py

This makes the data accessible on ::

    http://localhost:5000/CurrentMetrics
    http://localhost:5000/CurrentHourlyMetrics

Making a simple GET request to those URIs returns the current table of data stored in diags.json.
Data can easily be seen via the command line as well via ::

    curl -i http://localhost:5000/CurrentMetrics

Furthermore, all logs can be cleared, such as in the event of too little disk 
space remaining. Currently there are no protections against writing logs 
indefinitely, so the disk must be flushed manually.
