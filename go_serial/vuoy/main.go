package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"time"

	"go.bug.st/serial"
)

var Port serial.Port

func ReadProgram(filename string) string {
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var programLines []string
	for scanner.Scan() {
		programLines = append(programLines, scanner.Text()+"\r\n") // ここを変更
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}

	program := []byte{}
	for _, line := range programLines {
		program = append(program, []byte(line)...)
	}

	return string(program)
}
func PortWrite(program string) {
	Port.Write([]byte(program + "\r"))
	time.Sleep(100 * time.Millisecond)
}
func programExecute(program string) {

	PortWrite("edit 1")
	n, err := Port.Write([]byte(program))
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Sent %v bytes \n", n)
	PortWrite("own = 1")
	PortWrite("dst = 0")
	PortWrite("edit 1")
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
	program := ReadProgram(filename)
	programExecute(program)
}
