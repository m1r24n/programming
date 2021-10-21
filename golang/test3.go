package main

import "fmt"

func main() {
    var ( 
        data1, data2 float64 = 15.1111,25.333
        data3, data4 float64
    )
    fmt.Println("hello world")
    fmt.Println("data1 ",data1)
    fmt.Println("data2 ",data2)
    data3 = data1 / data2
    fmt.Println("data3 ",data3)
    data1,data4 =  55.5,11.333
    fmt.Println("data1 ",data1)
    fmt.Println("data4 ",data4)
    fmt.Println("This is the last line, thank you")
}
