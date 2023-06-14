package main

import (
	"fmt"
	"log"
	"time"

	"test/lib"

	"go.bug.st/serial"
)

var Port serial.Port

func PortWrite(program string) {
	Port.Write([]byte(program + "\r"))
	time.Sleep(100 * time.Millisecond)
}
func ProgramExecuteAuto(program string) {
	// delete program
	Port.Write([]byte{0x03})
	time.Sleep(100 * time.Millisecond)
	PortWrite("edit 1")
	PortWrite("New")
	PortWrite("psave")
	PortWrite("edit 0")

	PortWrite("edit 1")
	n, err := Port.Write([]byte(program))
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Sent %v bytes \n", n)
	PortWrite("own = 1")
	PortWrite("dst = 0")
	PortWrite("Auto=\"pload:run\"")
	PortWrite("ssave")
	PortWrite("psave")
	PortWrite("edit 0")
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
	defer Port.Close()
	filename := "../basic_src/send_loop.txt"
	program := lib.ReadProgram(filename)
	ProgramExecuteAuto(program)
}
