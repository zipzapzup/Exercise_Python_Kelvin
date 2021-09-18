package main

import "fmt"

// Euclid algorithmn in golang
// An algorithmn to find the largest common denominator in 2 integers

func algo(a int, b int) int {
	for b != 0 {
		remainder := a % b
		a = b
		b = remainder
	}
	return a

}

func main() {

	fmt.Println("hello world")
	fmt.Println(algo(20, 8))
	fmt.Println(algo(270, 192))
}
