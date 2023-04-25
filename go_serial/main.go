package main

import (
	"bufio"
	"fmt"
	"go.bug.st/serial"
	"log"
	"os"
	"strings"
	"time"
)

func main() {

	//read program
	file, err := os.Open("src/printtmp.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var programLines []string
	for scanner.Scan() {
		programLines = append(programLines, scanner.Text()+"\r")
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}

	program := []byte{}
	for _, line := range programLines {
		program = append(program, []byte(line)...)
	}

	//serial connection
	mode := &serial.Mode{
		BaudRate: 115200,
	}
	port, err := serial.Open("/dev/ttyUSB0", mode)
	defer port.Close()
	if err != nil {
		log.Fatal(err)
	}

	//execute program
	port.Write([]byte("edit 1 \r"))
	time.Sleep(100 * time.Millisecond)
	n, err := port.Write(program)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("Sent %v bytes\n", n)
	time.Sleep(100 * time.Millisecond)
	port.Write([]byte("edit 0 \r"))
	time.Sleep(500 * time.Millisecond)

	port.Write([]byte("run \r"))

	buff := make([]byte, 1000)
	for {
		// Reads up to 100 bytes
		n, err := port.Read(buff)
		if err != nil {
			log.Fatal(err)
		}

		receivedData := string(buff[:n])
		fmt.Printf("%s", receivedData)

		if strings.Contains(receivedData, "EOF") {
			fmt.Println("\nEOF")
			break
		}
	}

}
