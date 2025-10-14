package main

import "fmt"

func main() {
	var x [5]uint64
	var count uint64
	var N uint64 = 5
	fmt.Println("hello world")
	// fmt.Printf("What is the maximum value ")
	// fmt.Scanf("%d", &N)
	for count = 0; count < N; count++ {
		x[count] = count * 10
	}
	fmt.Println(x)
}
