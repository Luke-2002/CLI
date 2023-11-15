#!/usr/bin/env python3

import argparse
import requests
import json

API_BASE_URL = "http://34.125.4.182/"  # API URL FROM GCP

def get_response(url, method='get', data=None):
    try:
        if method == 'get':
            response = requests.get(url)
        elif method == 'post':
            response = requests.post(url, json=data)
        elif method == 'put':
            response = requests.put(url, json=data)
        elif method == 'delete':
            response = requests.delete(url)

        if response.status_code == 200:
            try:
                return json.dumps(response.json(), indent=4)
            except ValueError:
                return response.text
        else:
            return f"Error: HTTP {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request Exception: {e}"

# Define all command functions here

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

def is_prime_command(number):
    url = f"{API_BASE_URL}/is-prime/{number}"
    print(get_response(url))

def fibonacci_command(number):
    url = f"{API_BASE_URL}/fibonacci/{number}"
    print(get_response(url))

def slack_alert_command(message):
    url = f"{API_BASE_URL}/slack-alert/{message}"
    print(get_response(url))

def keyval_command(method, key=None, value=None):
    url = f"{API_BASE_URL}/keyval"
    if key:
        url += f"/{key}"
    data = {'storage-key': key, 'storage-val': value} if key and value else None
    print(get_response(url, method=method, data=data))

def main():
    parser = argparse.ArgumentParser(description="CLI for your REST API")
    subparsers = parser.add_subparsers(dest="command")

    # Define subparsers for each command

    subparsers.add_parser("hello", help="Access the root endpoint")

    special_parser = subparsers.add_parser("special", help="Greet a user")
    special_parser.add_argument("name", help="Name to greet")

    md5_parser = subparsers.add_parser("md5", help="Compute MD5 hash of text")
    md5_parser.add_argument("text", help="Text to compute MD5 for")

    factorial_parser = subparsers.add_parser("factorial", help="Compute factorial of a number")
    factorial_parser.add_argument("number", type=int, help="Number to compute factorial for")

    subparsers.add_parser("api", help="Access the sample API endpoint")

    is_prime_parser = subparsers.add_parser("is_prime", help="Check if a number is prime")
    is_prime_parser.add_argument("number", type=int, help="Number to check")

    fibonacci_parser = subparsers.add_parser("fibonacci", help="Get Fibonacci sequence up to a number")
    fibonacci_parser.add_argument("number", type=int, help="Number to get sequence for")

    slack_alert_parser = subparsers.add_parser("slack_alert", help="Send a message to a Slack channel")
    slack_alert_parser.add_argument("message", help="Message to send")

    keyval_parser = subparsers.add_parser("keyval", help="Interact with key-value store")
    keyval_parser.add_argument("method", choices=['post', 'get', 'put', 'delete'], help="HTTP method to use")
    keyval_parser.add_argument("--key", help="Key for the key-value store")
    keyval_parser.add_argument("--value", help="Value for the key-value store")

    args = parser.parse_args()

    # Call the appropriate function based on the command

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
    elif args.command == "is_prime":
        is_prime_command(args.number)
    elif args.command == "fibonacci":
        fibonacci_command(args.number)
    elif args.command == "slack_alert":
        slack_alert_command(args.message)
    elif args.command == "keyval":
        keyval_command(args.method, key=args.key, value=args.value)

if __name__ == "__main__":
    main()
