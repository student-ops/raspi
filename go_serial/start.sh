#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Please enter number:"
    echo -e "1: gateway\n2: vuoy\n3: print_loop ## test"
    read response
else
    response=$1
fi

sudo chmod 777 /dev/ttyUSB0
gtkterm -p /dev/ttyUSB0 -s 115200 -e -L &
sleep 10

if [ "$response" == "1" ]; then
    cd gateway
    go run main.go
elif [ "$response" == "2" ]; then
    cd vuoy
    go run main.go
elif [ "$response" == "3" ]; then
    cd print_loop
    go run main.go
else
    echo "Invalid input. Please enter 1, 2, or 3."
fi
