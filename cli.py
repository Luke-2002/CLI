#!/usr/bin/env python3

import argparse
import requests
import json

API_BASE_URL = "http://34.125.4.182/"  # API URL FROM GCP

def get_response(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            try:
                return json.dumps(response.json(), indent=4)
            except ValueError:
                return response.text
        else:
            return f"Error: HTTP {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request Exception: {e}"

def hello_world_command():
    url = f"{API_BASE_URL}"
    print(get_response(url))

def special_hello_command(name):
    url = f"{API_BASE_URL}/special/{name}"
    print(get_response(url))

def md5_command(text):
    url = f"{API_BASE_URL}/md5/{text}"
    print(get_response(url))

def factorial_command(number):
    url = f"{API_BASE_URL}/factorial/{number}"
    print(get_response(url))

def api_command():
    url = f"{API_BASE_URL}/api"
    print(get_response(url))

# Add more command functions here for additional endpoints

def main():
    parser = argparse.ArgumentParser(description="CLI for your REST API")
    subparsers = parser.add_subparsers(dest="command")

    # Hello World command
    subparsers.add_parser("hello", help="Access the root endpoint")

    # Special Hello command
    special_parser = subparsers.add_parser("special", help="Greet a user")
    special_parser.add_argument("name", help="Name to greet")

    # MD5 command
    md5_parser = subparsers.add_parser("md5", help="Compute MD5 hash of text")
    md5_parser.add_argument("text", help="Text to compute MD5 for")

    # Factorial command
    factorial_parser = subparsers.add_parser("factorial", help="Compute factorial of a number")
    factorial_parser.add_argument("number", type=int, help="Number to compute factorial for")

    # API command
    subparsers.add_parser("api", help="Access the sample API endpoint")

    # Add more subparsers here for additional endpoints

    args = parser.parse_args()

    if args.command == "hello":
        hello_world_command()
    elif args.command == "special":
        special_hello_command(args.name)
    elif args.command == "md5":
        md5_command(args.text)
    elif args.command == "factorial":
        factorial_command(args.number)
    elif args.command == "api":
        api_command()
    # Add more elif branches here for additional endpoints

if __name__ == "__main__":
    main()

