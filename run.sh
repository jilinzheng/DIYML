#!/bin/bash

exec python3 src/diyml.py &
exec python3 src/worker.py
