package main

type Handler interface {
	Handle(request string) string
	SetNext(handler Handler) Handler
}

type BaseHandler struct {
	next Handler
}

func (b *BaseHandler) SetNext(h Handler) Handler {
	b.next = h
	return h
}

type TechnicalHandler struct{ BaseHandler }

func (h *TechnicalHandler) Handle(req string) string {
	if req == "technical" {
		return "Technical support handled it"
	}
	if h.next != nil {
		return h.next.Handle(req)
	}
	return ""
}
