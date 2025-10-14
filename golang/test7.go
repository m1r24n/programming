package main

import "fmt"

func main() {
	x := [10]float64{10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
	y := x[0:5]
	var total float64 = 0

	for _, value := range x {
		total += value
	}
	fmt.Println(x, total, len(x))
	total = 0
	for _, value := range y {
		total += value
	}
	fmt.Println(y, total, len(y))

}
