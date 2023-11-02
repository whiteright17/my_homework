import re

def find_abc(text):
    pattern = re.compile(r'abc')
    matchers = pattern.finditer(text)
    return [match.group() for match in matchers]

def find_phone_numbers(text):
    pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    return pattern.findall(text)

def find_custom_pattern(text, pattern):
    pattern = re.compile(pattern)
    return pattern.findall(text)

def find_email_addresses(file_path):
    pattern = re.compile(r'\w+@\w+\.\w+')
    with open(file_path, 'r') as file:
        content = file.read()
        return pattern.findall(content)

def find_urls(text):
    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    matchers = pattern.finditer(text)
    subbed_str = re.sub(r'https?://(www\.)?(\w+)(\.\w+)', r'\2\3', text)
    return [match.group() for match in matchers], subbed_str
