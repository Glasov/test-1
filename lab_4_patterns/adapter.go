package main

type USPlug interface {
	Connect110v() string
}

type EuroSocket struct{}

func (s *EuroSocket) Get220v() string { return "220v" }

type PowerAdapter struct {
	socket *EuroSocket
}

func (a *PowerAdapter) Connect110v() string {
	return a.socket.Get220v() + " converted to 110v"
}
