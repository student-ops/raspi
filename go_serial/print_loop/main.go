package main

import (
	"fmt"
	"go_serial/lib"
	"log"
	"time"
)

func main() {
	err, port := lib.OpenPort()
	if err != nil {
		log.Fatal(err)
	}

	defer port.Close()
	filename := "../basic_src/print_loop.txt"
	program := lib.ReadProgram(filename)
	time.Sleep(time.Second)
	go lib.ProgramExecute(program, port)

	buff := make([]byte, 300)
	for {
		n, err := port.Read(buff)
		if err != nil {
			log.Fatal(err)
		}

		receivedData := string(buff[:n])
		fmt.Printf("%s", receivedData)
	}

}
