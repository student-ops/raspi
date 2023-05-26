package main

import (
	"go_serial/lib"
	"strings"
	"testing"
)

func TestReadProgram(t *testing.T) {
	filename := "src/printtmp.txt"
	expected := "10 Lclr\r20 Bme A,B,C\r30 PRINT \"@\"A/10;\".\";A%10;\"@\"B/10;\".\";B%10;\"@\"C/10;\".\";C%10,\"\\r\";\r40 PRINT \"EOF\"\r"

	program := lib.ReadProgram(filename)

	if !strings.EqualFold(program, expected) {
		t.Errorf("ReadProgram() failed, expected:\n%s\nbut got:\n%s", expected, program)
	}
}
