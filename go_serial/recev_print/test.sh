#!/bin/bash

# Process IDs of the background tasks will be stored here.
pids=()

# Cleanup function to kill the background tasks.
cleanup() {
    echo "Caught SIGINT, cleaning up..."

    for pid in "${pids[@]}"; do
        kill "$pid"
    done
}

# Trap SIGINT (Ctrl+C) and call the cleanup function.
trap cleanup SIGINT

sudo chmod 777 /dev/ttyUSB0

# Start gtkterm in the background and save its process ID.
gtkterm -p /dev/ttyUSB0 -s 115200 -e  -L &
pids+=($!)

sleep 1

# Start go run in the background and save its process ID.
go run recive.go &
pids+=($!)

# Wait for all background tasks to finish.
wait