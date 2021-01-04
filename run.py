#!/usr/bin/env python3

import argparse

from testcases import TESTCASES
from implementations import CLIENTS, SERVERS

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--server",
        help="server implementation. Valid implementations are: "
              + ", ".join(x.name() for x in SERVERS),
    )
    parser.add_argument(
        "-c",
        "--client",
        help="client implementation. Valid implementations are: "
              + ", ".join(x.name() for x in CLIENTS),
    )
    parser.add_argument(
        "-t",
        "--test",
        help="test case. Valid test cases are: "
             + ", ".join([x.name() for x in TESTCASES]),
    )
    return parser.parse_args()

print(get_args())
