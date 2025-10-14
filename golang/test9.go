package main

import "fmt"

func average(y []float64) float64 {
	total := 0.0
	for _, v := range y {
		total += v
	}
	return total / float64(len(y))
}
func read_data() []float64 {
	var x float64
	var r []float64
	var ls = 0
	// fmt.Printf("read data %d\n", es)
	for ls != 1 {
		fmt.Printf("enter a number (float64): ")
		fmt.Scanf("%f", &x)
		if x < 0 {
			fmt.Printf("must be a positif number\n")
		} else if x == 0 {
			ls = 1
		} else {
			r = append(r, x)
		}
	}
	return r
	// return ([]float64{10, 20, 30, 40, 50, 60, 70, 80, 90, 100})

}
func main() {
	// xs := []float64{98, 93, 77, 82, 83, 150}
	var xs []float64
	xs = read_data()
	fmt.Println("data ", xs)
	fmt.Println("average ", average(xs))
}
