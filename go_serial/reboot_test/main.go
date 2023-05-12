package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"time"

	"go.bug.st/serial"
)

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
func programExecute(program string, port serial.Port) {

	//execute program
	fmt.Println("serial connected")
	port.Write([]byte("edit 1 \r"))
	time.Sleep(100 * time.Millisecond)
	n, err := port.Write([]byte(program))
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("Sent %v bytes \n", n)
	time.Sleep(100 * time.Millisecond)
	port.Write([]byte("edit 0 \r"))

	// command mode 
	time.Sleep(100 * time.Millisecond)
	port.Write([]byte("own = 1 \r"))
	time.Sleep(100 * time.Millisecond)
	port.Write([]byte("dst =0 \r"))
	time.Sleep(100 * time.Millisecond)
	port.Write([]byte("ssave \r"))
	time.Sleep(100 * time.Millisecond)
	port.Write([]byte("psave \r"))
	time.Sleep(100 * time.Millisecond)
	port.Write([]byte("Auto="pload:run" \r"))
	time.Sleep(100 * time.Millisecond)

}

func main() {
	mode := &serial.Mode{
		BaudRate: 115200,
	}
	port, err := serial.Open("/dev/ttyUSB0", mode)
	if err != nil {
		log.Fatal(err)
	}
	defer port.Close()
	filename := "../basic_src/send_loop.txt"
	program := ReadProgram(filename)
	programExecute(program, port)
}
