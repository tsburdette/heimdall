========
Heimdall
========

An API to retrieve hardware metrics from a computer.

Heimdall is designed to monitor basic metrics from a given machine. It stores
those metrics in local log files and the current json payload in a another
local file. In an attempt to get a working prototype built, the decision was to
avoid large SQL-style databases in favor of the expectation that files would be
recorded with timestamp names appended, allowing easy aggregation by hour or by
day.

Additionally, the log directory structure suggests extending functionality by
specific metric and category, allowing easier retrieval of CPU, memory, disk, and
networking statistics individually (or by core/directory/NIC/etc). Local files
also ensure that should networking prove particularly taxed, statistics can still
be delivered since accessing a large SQL database might timeout.

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

Making a simple GET request to that URI returns the current table of data stored in diags.json.
Data can easily be seen via the command line as well via ::

    curl -i http://localhost:5000/CurrentMetrics
