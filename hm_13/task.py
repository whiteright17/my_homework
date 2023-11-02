import re

from hm_13.examples import text_to_search

#pattern = re.compile(r'abc')

#matchers = re.finditer(pattern, text_to_search)
#for match in matchers:
#    print(match)

#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

#matchers = pattern.findall(text_to_search)
#print(matchers)

#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

#with open('data.txt','r') as file:
#    content = file.read()
#    matchers = pattern.findall(content)
#    print(matchers)

#pattern = re.compile(r'[89]00-\d\d\d-\d\d\d\d')

#with open('data.txt','r') as file:
#    content = file.read()
#    matchers = pattern.findall(content)
#    print(matchers)

#pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
#matchers = pattern.findall(text_to_search)
#print(matchers)

#pattern = re.compile(r'\w+@\w+\.\w+')
#with open('data.txt', 'r') as file:
#    content = file.read()
#    matchers = pattern.findall(content)
#    print(matchers)

urls = '''
https://www.google.com
http://zelenska.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matchers = pattern.finditer(urls)
subbed_str = re.sub(r'https?://(www\.)?(\w+)(\.\w+)', r'\2\3', urls)
print(subbed_str)