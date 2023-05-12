package lib

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

func ProgramExecute(program string, port serial.Port) {

	//execute program
	time.Sleep(3 * time.Second)
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
	time.Sleep(100 * time.Millisecond)

	port.Write([]byte("run \r"))

}

func OpenPort() (error, serial.Port) {
	mode := &serial.Mode{
		BaudRate: 115200,
	}
	port, err := serial.Open("/dev/ttyUSB0", mode)
	if err != nil {
		log.Fatal(err)
	}
	return err, port
}
