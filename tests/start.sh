gtkterm -p /dev/ttyUSB0 -s 115200 &
sleep 3
python3 wisun_readloop.py