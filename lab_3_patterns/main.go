package main

import "fmt"

func main() {
	fmt.Println("--- 1. Singleton ---")
	l1, l2 := GetLogger(), GetLogger()
	l1.AddLog("System start")
	l2.AddLog("User login")
	fmt.Printf("Is same instance? %v\n\n", l1 == l2)

	fmt.Println("--- 2. Factory Method ---")
	fmt.Println(CreateButton("windows").Render())
	fmt.Println(CreateButton("web").Render() + "\n")

	fmt.Println("--- 3. Abstract Factory ---")
	var factory FurnitureFactory = ModernFactory{}
	fmt.Println(factory.CreateChair().SitOn() + "\n")

	fmt.Println("--- 4. Builder ---")
	house := NewHouseBuilder().SetFloors(2).SetPool().Build()
	fmt.Printf("House: Floors: %d, Pool: %v\n", house.Floors, house.HasPool)
}
