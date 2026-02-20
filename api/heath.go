package handler

import (
	"encoding/json"
	"net/http"
	"time"
)

// Response estrutura o retorno JSON para facilitar o monitoramento
type HealthResponse struct {
	Status    string    `json:"status"`
	Timestamp time.Time `json:"timestamp"`
	Service   string    `json:"service"`
}

func Handler(w http.ResponseWriter, r *http.Request) {
	// Definindo o cabeçalho como JSON
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)

	res := HealthResponse{
		Status:    "up",
		Timestamp: time.Now(),
		Service:   "api-gateway",
	}

	json.NewEncoder(w).Encode(res)
}