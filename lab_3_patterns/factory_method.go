package main

type Button interface {
	Render() string
}

type HTMLButton struct{}

func (b HTMLButton) Render() string { return "<button>HTML Button</button>" }

type WindowsButton struct{}

func (b WindowsButton) Render() string { return "[Windows Button]" }

func CreateButton(osType string) Button {
	if osType == "windows" {
		return WindowsButton{}
	}
	return HTMLButton{}
}
