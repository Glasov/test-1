package main

import "fmt"

type Device interface {
	IsEnabled() bool
	Enable()
}

type Radio struct{ on bool }

func (r *Radio) IsEnabled() bool { return r.on }
func (r *Radio) Enable()         { r.on = true }

type Remote struct {
	device Device
}

func (r *Remote) TogglePower() {
	if r.device.IsEnabled() {
		fmt.Println("Turning off")
	} else {
		r.device.Enable()
		fmt.Println("Turning on")
	}
}
