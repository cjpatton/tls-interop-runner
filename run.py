#!/usr/bin/env python3
import argparse

TESTCASES = [
    # The client indicates support for delegated credentials and the server
    # signs the handshake with a delegated credential.
    "dc",
]}

CLIENTS = [
    "cloudflare-go",
]

SERVERS = [
    "boringssl",
    "cloudflare-go",
    "rustls",
]

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--server",
        help="server implementation. Valid implementations are: "
              + ", ".join(SERVERS),
    )
    parser.add_argument(
        "-c",
        "--client",
        help="client implementation. Valid implementations are: "
              + ", ".join(CLIENTS),
    )
    parser.add_argument(
        "-t",
        "--test",
        help="test case. Valid test cases are: "
             + ", ".join(TESTCASES.keys()),
    )
    return parser.parse_args()


if __name__ == "__main__":
    print(get_args())
