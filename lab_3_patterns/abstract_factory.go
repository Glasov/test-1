package main

type Chair interface{ SitOn() string }
type Sofa interface{ LieOn() string }

type FurnitureFactory interface {
	CreateChair() Chair
	CreateSofa() Sofa
}

type ModernChair struct{}

func (c ModernChair) SitOn() string { return "Sitting on a modern chair" }

type ModernSofa struct{}

func (s ModernSofa) LieOn() string { return "Lying on a modern sofa" }

type ModernFactory struct{}

func (f ModernFactory) CreateChair() Chair { return ModernChair{} }
func (f ModernFactory) CreateSofa() Sofa   { return ModernSofa{} }

type VictorianChair struct{}

func (c VictorianChair) SitOn() string { return "Sitting on a victorian chair" }

type VictorianSofa struct{}

func (s VictorianSofa) LieOn() string { return "Lying on a victorian sofa" }

type VictorianFactory struct{}

func (f VictorianFactory) CreateChair() Chair { return VictorianChair{} }
func (f VictorianFactory) CreateSofa() Sofa   { return VictorianSofa{} }
