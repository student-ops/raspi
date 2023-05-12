cd ../go_serial
go mod init test
go mod tidy
sudo chmod 777 /dev/ttyUSB0
gtkterm -p /dev/ttyUSB0 -s 115200 -e  -L &
sleep 3
cd ../tests
python3 wisun_receive.py

