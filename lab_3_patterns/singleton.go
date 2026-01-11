package main

import (
	"fmt"
	"sync"
)

type Logger struct {
	messages []string
}

var instance *Logger
var once sync.Once

func GetLogger() *Logger {
	once.Do(func() {
		instance = &Logger{messages: []string{}}
	})
	return instance
}

func (l *Logger) AddLog(msg string) {
	l.messages = append(l.messages, msg)
	fmt.Printf("Add log: %s\n", msg)
}
