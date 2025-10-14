package main

import "fmt"

func main() {
	var (
		count, N uint64
	)
	fmt.Println("hello world")
	fmt.Printf("What is the maximum value ")
	fmt.Scanf("%d", &N)
	for count = 0; count <= N; count++ {
		fmt.Printf("value %d is ", count)
		if count%2 == 0 {
			fmt.Println("even")
		} else {
			fmt.Println("odd")
		}
	}
}
