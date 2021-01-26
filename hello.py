#!/usr/bin/env python3

import os
import json

# How to cite SO:
# FROM: https://stackoverflow.com 2021-01-25 by Elon Musk 2012
# for i in range:
#     print(i)  
# END FROM

# HTTP header that tell the browser what type of file you're sending.
# This specifies JSON, otherwise it would be plain text
# print('Content-Type: application/json')

print('Content-Type: text/html')

# Add a line to separate headers
print() 
# print(json.dumps(dict(os.environ), indent=2))

print("""
    <html>
    <body>
    <h1>HELLO I AM HTML</h1>
""")

# print query parameters
print(f"<p> QUERY_STRING={os.environ['QUERY_STRING']} </p>")
print("<ul>")
for parameter in os.environ['QUERY_STRING'].split('&'):
    (name, value) = parameter.split('=')
    print(f"<li><em>{name}</em> = {value}</li>")
print(f"<li><em>{os.environ['HTTP_USER_AGENT']}</em></li>")
print("</ul>")

