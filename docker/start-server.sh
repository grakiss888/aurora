#!/bin/bash

gunicorn -w 4 -b 127.0.0.0:8000 wsgi:application
