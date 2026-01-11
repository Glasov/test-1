package main

import "fmt"

type PaymentStrategy interface {
	Pay(amount int) string
}

type CreditCard struct{}

func (c CreditCard) Pay(a int) string { return fmt.Sprintf("Paid %d using Credit Card", a) }

type PayPal struct{}

func (p PayPal) Pay(a int) string { return fmt.Sprintf("Paid %d using PayPal", a) }

type ShoppingCart struct {
	strategy PaymentStrategy
}

func (s *ShoppingCart) SetStrategy(st PaymentStrategy) { s.strategy = st }
func (s *ShoppingCart) Checkout(a int) string          { return s.strategy.Pay(a) }
