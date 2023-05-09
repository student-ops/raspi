sudo chmod 777 /dev/ttyUSB0
gtkterm -p /dev/ttyUSB0 -s 115200 -e  -L &
sleep 1
go run send.go

#  goプロセスのが終了すると、gtktermも終了するように。