package main

import "fmt"

func main() {
		  var testing1  bool
		  testing1=true
		  var value1,value2  int

		  fmt.Println("Hello, world!")
		  if testing1 {
					 fmt.Println("true value")
		  }
		  testing1 = false
		  if testing1 {
					 fmt.Println("true value")
		  } else {
					 fmt.Println("false value")
		  }
		  value1 = 10
		  fmt.Println("value1 is ",value1)
		  value2= value1 * 2
		  fmt.Println("value2 is ",value2)
}
