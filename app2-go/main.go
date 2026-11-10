package main

import (
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

var version = "dev"

func setupRouter() *gin.Engine {
	r := gin.New()
	r.Use(gin.Logger(), gin.Recovery())

	r.GET("/", func(c *gin.Context) {
		c.String(http.StatusOK, "Hello World 2")
	})
	r.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"status": "ok", "app": "app2", "version": version})
	})
	return r
}

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	if err := setupRouter().Run(":" + port); err != nil {
		panic(err)
	}
}
