import argparse
import requests

API_BASE_URL = "http://34.125.4.182/"  # API URL FROM GCP

def md5_command(text):
    url = f"{API_BASE_URL}/md5/{text}"
    response = requests.get(url)
    if response.status_code == 200:
        print("MD5 Result:", response.text)
    else:
        print("Error:", response.status_code)

def main():
    parser = argparse.ArgumentParser(description="CLI for your REST API")
    subparsers = parser.add_subparsers(dest="command")

    md5_parser = subparsers.add_parser("md5")
    md5_parser.add_argument("text", help="Text to compute MD5 for")

    args = parser.parse_args()

    if args.command == "md5":
        md5_command(args.text)

if __name__ == "__main__":
    main()
