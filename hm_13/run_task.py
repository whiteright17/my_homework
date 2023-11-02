from task_refactor import (
    find_abc,
    find_phone_numbers,
    find_custom_pattern,
    find_email_addresses,
    find_urls,
)

from hm_13.examples import text_to_search

abc_matches = find_abc(text_to_search)
print("Find 'abc':", abc_matches)

phone_numbers = find_phone_numbers(text_to_search)
print("Find number:", phone_numbers)

custom_pattern = r'[89]00-\d\d\d-\d\d\d\d'
custom_pattern_matches = find_custom_pattern(text_to_search, custom_pattern)
print("Find number 800 or 900:", custom_pattern_matches)

email_addresses = find_email_addresses('data.txt')
print("Find email:", email_addresses)

urls = '''
https://www.google.com
http://zelenska.com
https://youtube.com
https://www.nasa.gov
'''

url_matches, subbed_urls = find_urls(urls)
print("Edit URL:", subbed_urls)

