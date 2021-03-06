# (Work in Progress) TLS Interop Test Runner

The TLS Interop Test Runner aims to test interoperability between implementations of TLS by running various tests involving clients and servers drawn from differing implementations.

It is fashioned after the [QUIC Interop Runner](https://github.com/marten-seemann/quic-interop-runner).

## Quickstart

Clone this repository into $GOPATH/src/github.com/xvzcf/tls-interop-runner, then run the following commands:

1. `make certs`
2. `make dc` (TODO: Flesh out testing API to remove this step)
3. `env SERVER_SRC=./impl-endpoints SERVER={rustls|boringssl} CLIENT_SRC=./impl-endpoints CLIENT=cloudflare-go docker-compose build`
4. `env SERVER_SRC=./impl-endpoints SERVER={rustls|boringssl} CLIENT_SRC=./impl-endpoints CLIENT=cloudflare-go docker-compose up`

set `SERVER=boringssl` for delegated credential tests.