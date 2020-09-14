package main

import (
	"fmt"
	"io/ioutil"
)


func main(){
	data,err := ioutil.Readfile("./inp.txt")
	fmt.Println(data)
}

