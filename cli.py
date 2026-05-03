import argparse
import json
import re
import urllib.parse
from pathlib import Path

# Define regex patterns
EMAIL_RE = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
PHONE_RE = re.compile(r'^(\+?\d{1,3}[- ]?)?\(?\d{1,4}?\)?[- ]?\d{1,4}[- ]?\d{1,9}$')
USERNAME_RE = re.compile(r'^[a-zA-Z0-9._-]{3,}$')
URL_RE = re.compile(r'^(https?://)?(www\.)?([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,6})(/.*)?$')

# Directory for data files
DATA_DIR = Path('data')

# Load platforms from json files

def load_platforms(kind):
    platforms = []
    for platform_file in DATA_DIR.glob(f'**/{kind}.json'):
        with open(platform_file, 'r') as file:
            platforms.extend(json.load(file))
    return platforms

# Classify the type of entity

def classify(entity):
    if EMAIL_RE.match(entity):
        return 'email'
    elif PHONE_RE.match(entity):
        return 'phone'
    elif USERNAME_RE.match(entity):
        return 'username'
    elif URL_RE.match(entity):
        return 'url'
    else:
        return 'unknown'

# Pivot functions for different entity types

def pivots_email(entity):
    return load_platforms('email')


def pivots_username(entity):
    return load_platforms('username')


def pivots_domain(entity):
    return load_platforms('domain')


def pivots_phone(entity):
    return load_platforms('phone')

# Format and print output

def format_output(results):
    return json.dumps(results, indent=4)

# Main function

def main():
    parser = argparse.ArgumentParser(description='OSINT Search Tool')
    parser.add_argument('query', type=str, help='The entity to search for')
    args = parser.parse_args()

    entity = args.query
    entity_type = classify(entity)

    if entity_type == 'email':
        results = pivots_email(entity)
    elif entity_type == 'username':
        results = pivots_username(entity)
    elif entity_type == 'url':
        results = pivots_domain(entity)
    elif entity_type == 'phone':
        results = pivots_phone(entity)
    else:
        results = {'error': 'Unknown entity type'}

    print(format_output(results))

if __name__ == '__main__':
    main()