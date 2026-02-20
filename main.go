// main.go (APENAS PARA TESTE LOCAL)
package main

import (
	"log"
	"net/http"
	"github.com/gbonis/go-gateway/api"
)

func main() {
	// Mimetiza o roteamento que a Vercel faria
	http.HandleFunc("/health", handler.Handler)

	log.Println("Servidor local de teste rodando em http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}