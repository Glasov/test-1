package main

import "fmt"

func main() {
	fmt.Println("--- Strategy ---")
	cart := &ShoppingCart{strategy: &PayPal{}}
	cart.Checkout(500)

	fmt.Println("\n--- Chain of Responsibility ---")
	h1 := &TechnicalHandler{}
	fmt.Println(h1.Handle("technical"))

	fmt.Println("\n--- Iterator ---")
	coll := &NameCollection{names: []string{"Andrew", "Nemanja", "Ivan"}}
	it := coll.GetIterator()
	for it.HasNext() {
		fmt.Println(it.Next())
	}

	fmt.Println("\n--- Proxy ---")
	dbProxy := &DatabaseProxy{role: "user"}
	fmt.Println(dbProxy.Query())

	fmt.Println("\n--- Bridge ---")
	remote := &Remote{device: &Radio{}}
	remote.TogglePower()

	fmt.Println("\n--- Adapter ---")
	adapter := &PowerAdapter{socket: &EuroSocket{}}
	fmt.Println(adapter.Connect110v())
}
