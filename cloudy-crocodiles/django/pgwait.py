#!/usr/bin/python

import os
import psycopg2
import sys
import time

MAX_RETRIES = 24
RETRY_DELAY = 5


def main():
    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    attempts = 0
    success = False

    while attempts < MAX_RETRIES and success is False:
        try:
            _ = psycopg2.connect(
                dbname=POSTGRES_DB,
                host=POSTGRES_HOST,
                password=POSTGRES_PASSWORD,
                user=POSTGRES_USER,
            )
            success = True
        except:  # noqa: E722
            print(".", end="")
            time.sleep(RETRY_DELAY)
        finally:
            attempts += 1

    if success:
        print("Success!")
        sys.exit(0)
    print("Error contacting postgresql server!")
    sys.exit(1)


if __name__ == "__main__":
    main()
