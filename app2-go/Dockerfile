FROM golang:1.23-alpine AS build
WORKDIR /src
COPY go.mod go.sum* ./
COPY *.go ./
RUN go mod tidy && go mod download
ARG APP_VERSION=dev
RUN CGO_ENABLED=0 GOOS=linux go build -trimpath \
    -ldflags="-s -w -X main.version=${APP_VERSION}" -o /out/app .

FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=build /out/app /app
ENV GIN_MODE=release PORT=8080
EXPOSE 8080
USER nonroot:nonroot
ENTRYPOINT ["/app"]
