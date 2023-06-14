package main

import (
	"fmt"
	"log"
	"time"
	"go.bug.st/serial"
)
var Port serial.Port

func PortWrite(program string) {
	Port.Write([]byte(program + "\r"))
	time.Sleep(100 * time.Millisecond)
}
func programExecute(program string) {
	Port.Write([]byte{0x03})
}
func main() {
	mode := &serial.Mode{
		BaudRate: 115200,
	}
	var err error
	Port, err = serial.Open("/dev/ttyUSB0", mode)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("serial connected")
	programExecute("")
	defer Port.Close()
}
