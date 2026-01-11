package main

type Database interface {
	Query() string
}

type RealDatabase struct{}

func (r *RealDatabase) Query() string { return "Data from Real DB" }

type DatabaseProxy struct {
	realDB *RealDatabase
	role   string
}

func (p *DatabaseProxy) Query() string {
	if p.role != "admin" {
		return "Access Denied"
	}
	if p.realDB == nil {
		p.realDB = &RealDatabase{}
	}
	return "Proxy: " + p.realDB.Query()
}
