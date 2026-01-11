package main

type House struct {
	HasPool   bool
	HasGarage bool
	Floors    int
}

type HouseBuilder struct {
	house House
}

func NewHouseBuilder() *HouseBuilder                  { return &HouseBuilder{} }
func (b *HouseBuilder) SetPool() *HouseBuilder        { b.house.HasPool = true; return b }
func (b *HouseBuilder) SetGarage() *HouseBuilder      { b.house.HasGarage = true; return b }
func (b *HouseBuilder) SetFloors(n int) *HouseBuilder { b.house.Floors = n; return b }
func (b *HouseBuilder) Build() House                  { return b.house }
