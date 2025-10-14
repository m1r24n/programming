package main

import "fmt"

func main() {
	var x = 10
	var y int
	var a float64
	z := 0.0
	y = x * 2
	z = float64(x * y)
	a = float64(x) * z
	fmt.Println("Hello, world!")
	fmt.Println("value of x", x)
	fmt.Println("value of y", y)
	fmt.Println("value of z", z)
	fmt.Println("value of a", a)
}
