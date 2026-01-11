package main

type Iterator interface {
	HasNext() bool
	Next() string
}

type NameCollection struct {
	names []string
}

func (c *NameCollection) GetIterator() Iterator {
	return &NameIterator{names: c.names, index: 0}
}

type NameIterator struct {
	names []string
	index int
}

func (i *NameIterator) HasNext() bool { return i.index < len(i.names) }
func (i *NameIterator) Next() string {
	name := i.names[i.index]
	i.index++
	return name
}
