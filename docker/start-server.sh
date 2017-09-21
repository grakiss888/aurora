#!/bin/bash
cd ../aurora
gunicorn --reload -w 4 -b 0.0.0.0:8009 wsgi:application --error-logfile /var/log/gunicorn/gunicorn.log --log-level debug
