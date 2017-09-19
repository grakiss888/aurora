#!/bin/bash

gunicorn -w 4 -b 127.0.0.0:8009 wsgi:application
