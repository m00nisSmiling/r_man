import requests
import os
import json
from termcolor import colored
import sys

print(colored('''\n          +   REQUEST   +    ENGINE     +''','red'))
print(colored('''    +             +             +              +''','green'))
print(colored('''          +[Developed By+ m00nissmiling]+   \n''','red'))



# OPTIONS REQUEST ENGINE
def t_options():

# OPTIONS Request Start
 colb = f"{http_in}://{input_host}{path2}"

 try:
  abf = input_query1
  abe = value_query1
 except NameError: 
  q_data = ''
  var1 = requests.options(f"{colb}", headers=req_header, allow_redirects=False)
  pass
 else:
  value_query = input("parameter's value: ")
  if value_query == '':
   q_data = f"?{input_query1}={value_query1}"
  else:
   q_data = f"?{input_query1}={value_query}"
  var1 = requests.options(f"{colb}{q_data}", headers=req_header, allow_redirects=False)
  
 bo = var1.headers
 print(colored("===================[URL]=====================","red"))
 print(colored(f"{colb}{q_data}","blue"))
  
# Status Code Fetches
 bs = var1.status_code
 if bs == 200:
  bss = colored("200 OK","green")
 elif bs == 201:
  bss = colored("201 Created","green")
 elif bs == 302:
  bss = colored("302 Found","yellow")
 elif bs == 301:
  bss = colored("301 Moved Permanently","yellow")
 elif bs == 404:
  bss = colored("404 Not Found","magenta")
 elif bs == 403:
  bss = colored("403 Forbidden","magenta")
 elif bs == 401:
  bss = colored("401 Unauthorized","magenta")
 elif bs == 400:
  bss = colored("400 Bad Request","magenta")
 elif bs == 500:
  bss = colored("500 Internal Server Error","red")
 elif bs == 503:
  bss = colored("503 Service Unavailable","red")
 else:
  bss = colored(f"{bs}","cyan")
 
# Request Conditions 
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f"""OPTIONS {path2}{q_data} {http_s}
Host: {input_host}
{aba}
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
 
  ""","green"))
 except UnboundLocalError:
  print(colored(f"""OPTIONS {path2}{q_data} {http_s}
Host: {input_host}
User-Agent: Python/3
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
 
  ""","green"))
  pass
 else:
  pass
       
       
# Response Header Fetches   
 hlist = []
 try:
  b = bo['Server']
 except KeyError:
  pass
 else:
  hlist.append(f'Server: {b}\n')

 try:
  b = bo['Set-Cookie']
 except KeyError:
  pass
 else:
  hlist.append(f'Set-Cookie: {b}\n')

 try:
  b = bo['Location']
 except KeyError:
  pass
 else:
  hlist.append(f'Location: {b}\n')
  
 try:
  b = bo['Content-Type']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Type: {b}\n')
 
 try:
  b = bo['X-Xss-Protection']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Xss-Protection: {b}\n')

 try:
  b = bo['Report-To']
 except KeyError:
  pass
 else:
  hlist.append(f'Report-To: {b}\n')

 try:
  b = bo['X-Frame-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Frame-Options: {b}\n')
  
 try:
  b = bo['Cross-Origin-Opener-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Opener-Policy: {b}\n')
  
 try:
  b = bo['Cache-Control']
 except KeyError:
  pass
 else:
  hlist.append(f'Cache-Control: {b}\n')

 try:
  b = bo['Access-Control-Allow-Origin']
 except KeyError:
  pass
 else:
  hlist.append(f'Access-Control-Allow-Origin: {b}\n')

 try:
  b = bo['Strict-Transport-Security']
 except KeyError:
  pass
 else:
  hlist.append(f'Strict-Transport-Security: {b}\n')
  
 try:
  b = bo['Cross-Origin-Resource-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Resource-Policy: {b}\n')
  
 try:
  b = bo['X-Content-Type-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Content-Type-Options: {b}\n')    
 
 try:
  b = bo['Referrer-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Referrer-Policy: {b}\n')

 try:
  b = bo['Vary']
 except KeyError:
  pass
 else:
  hlist.append(f'Vary: {b}\n')

 try:
  b = bo['upgrade']
 except KeyError:
  pass
 else:
  hlist.append(f'upgrade: {b}\n')

 try:
  b = bo['Content-Security-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Security-Policy: {b}\n')

 try:
  b = bo['connection']
 except KeyError:
  pass
 else:
  hlist.append(f'connection: {b}\n')  

 try:
  b = bo['Date']
 except KeyError:
  pass
 else:
  hlist.append(f'Date: {b}\n')  

 try:
  b = bo['Content-Length']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Length: {b}\n')  
  
# RESPONSE Create
 j = ''.join(hlist)
 print(colored("=================[Response]===================","red"))
 print(colored(f"{http_s} {bss}","green"))
 print(colored(j,"green"))
 print(var1.text)



# HEAD REQUEST ENGINE
def t_head():

# HEAD Request Start
 colb = f"{http_in}://{input_host}{path2}"

 try:
  abf = input_query1
  abe = value_query1
 except NameError: 
  q_data = ''
  var1 = requests.head(f"{colb}", headers=req_header, allow_redirects=False)
  pass
 else:
  value_query = input("parameter's value: ")
  if value_query == '':
   q_data = f"?{input_query1}={value_query1}"
  else:
   q_data = f"?{input_query1}={value_query}"
  var1 = requests.head(f"{colb}{q_data}", headers=req_header, allow_redirects=False)
  
 bo = var1.headers
 print(colored("===================[URL]=====================","red"))
 print(colored(f"{colb}{q_data}","blue"))
# Status Code Fetches
 bs = var1.status_code
 if bs == 200:
  bss = colored("200 OK","green")
 elif bs == 201:
  bss = colored("201 Created","green")
 elif bs == 302:
  bss = colored("302 Found","yellow")
 elif bs == 301:
  bss = colored("301 Moved Permanently","yellow")
 elif bs == 404:
  bss = colored("404 Not Found","magenta")
 elif bs == 403:
  bss = colored("403 Forbidden","magenta")
 elif bs == 401:
  bss = colored("401 Unauthorized","magenta")
 elif bs == 400:
  bss = colored("400 Bad Request","magenta")
 elif bs == 500:
  bss = colored("500 Internal Server Error","red")
 elif bs == 503:
  bss = colored("503 Service Unavailable","red")
 else:
  bss = colored(f"{bs}","cyan")

# Request Conditions 
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f"""HEAD {path2}{q_data} {http_s}
Host: {input_host}
{aba}
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
 
 ""","green"))
 except UnboundLocalError:
  print(colored(f"""HEAD {path2}{q_data} {http_s}
Host: {input_host}
User-Agent: Python/3
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
 
  ""","green"))
  pass
 else:
  pass
       
       
# Response Header Fetches   
 hlist = []
 try:
  b = bo['Server']
 except KeyError:
  pass
 else:
  hlist.append(f'Server: {b}\n')

 try:
  b = bo['Set-Cookie']
 except KeyError:
  pass
 else:
  hlist.append(f'Set-Cookie: {b}\n')

 try:
  b = bo['Location']
 except KeyError:
  pass
 else:
  hlist.append(f'Location: {b}\n')
  
 try:
  b = bo['Content-Type']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Type: {b}\n')
 
 try:
  b = bo['X-Xss-Protection']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Xss-Protection: {b}\n')

 try:
  b = bo['Report-To']
 except KeyError:
  pass
 else:
  hlist.append(f'Report-To: {b}\n')

 try:
  b = bo['X-Frame-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Frame-Options: {b}\n')
  
 try:
  b = bo['Cross-Origin-Opener-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Opener-Policy: {b}\n')
  
 try:
  b = bo['Cache-Control']
 except KeyError:
  pass
 else:
  hlist.append(f'Cache-Control: {b}\n')

 try:
  b = bo['Access-Control-Allow-Origin']
 except KeyError:
  pass
 else:
  hlist.append(f'Access-Control-Allow-Origin: {b}\n')

 try:
  b = bo['Strict-Transport-Security']
 except KeyError:
  pass
 else:
  hlist.append(f'Strict-Transport-Security: {b}\n')
  
 try:
  b = bo['Cross-Origin-Resource-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Resource-Policy: {b}\n')
  
 try:
  b = bo['X-Content-Type-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Content-Type-Options: {b}\n')    
 
 try:
  b = bo['Referrer-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Referrer-Policy: {b}\n')

 try:
  b = bo['Vary']
 except KeyError:
  pass
 else:
  hlist.append(f'Vary: {b}\n')

 try:
  b = bo['upgrade']
 except KeyError:
  pass
 else:
  hlist.append(f'upgrade: {b}\n')

 try:
  b = bo['Content-Security-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Security-Policy: {b}\n')

 try:
  b = bo['connection']
 except KeyError:
  pass
 else:
  hlist.append(f'connection: {b}\n')  

 try:
  b = bo['Date']
 except KeyError:
  pass
 else:
  hlist.append(f'Date: {b}\n')  

 try:
  b = bo['Content-Length']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Length: {b}\n')  
  
# RESPONSE Create
 j = ''.join(hlist)
 print(colored("=================[Response]===================","red"))
 print(colored(f"{http_s} {bss}","green"))
 print(colored(j,"green"))
 print(var1.text)




# GET REQUEST ENGINE
def t_get():

# Get Request Start
 colb = f"{http_in}://{input_host}{path2}" 
 try:
  abf = input_query1
  abe = value_query1
 except NameError: 
  q_data = ''
  var1 = requests.get(f"{colb}", headers=req_header, allow_redirects=False)
  pass
 else:
  value_query = input("parameter's value: ")
  if value_query == '':
   q_data = f"?{input_query1}={value_query1}"
  else:
   q_data = f"?{input_query1}={value_query}"
  var1 = requests.get(f"{colb}{q_data}", headers=req_header, allow_redirects=False)

 bo = var1.headers
 print(colored("===================[URL]=====================","red"))
 print(colored(f"{colb}{q_data}","blue"))
# Status Code Fetches
 bs = var1.status_code
 
 if bs == 200:
  bss = colored("200 OK","green")
 elif bs == 201:
  bss = colored("201 Created","green")
 elif bs == 302:
  bss = colored("302 Found","yellow")
 elif bs == 301:
  bss = colored("301 Moved Permanently","yellow")
 elif bs == 404:
  bss = colored("404 Not Found","magenta")
 elif bs == 403:
  bss = colored("403 Forbidden","magenta")
 elif bs == 401:
  bss = colored("401 Unauthorized","magenta")
 elif bs == 400:
  bss = colored("400 Bad Request","magenta")
 elif bs == 500:
  bss = colored("500 Internal Server Error","red")
 elif bs == 503:
  bss = colored("503 Service Unavailable","red")
 else:
  bss = colored(f"{bs}","cyan")

# Request Conditions 
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f"""GET {path2}{q_data} {http_s}
Host: {input_host}
{aba}
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
 
 ""","green"))
 except UnboundLocalError:
  print(colored(f"""GET {path2}{q_data} {http_s}
Host: {input_host}
User-Agent: Python/3
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
 
 ""","green"))
  pass
 else:
  pass
   
# Response Header Fetches   
 hlist = []
 try:
  b = bo['Server']
 except KeyError:
  pass
 else:
  hlist.append(f'Server: {b}\n')

 try:
  b = bo['Set-Cookie']
 except KeyError:
  pass
 else:
  hlist.append(f'Set-Cookie: {b}\n')

 try:
  b = bo['Location']
 except KeyError:
  pass
 else:
  hlist.append(f'Location: {b}\n')
  
 try:
  b = bo['Content-Type']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Type: {b}\n')
 
 try:
  b = bo['X-Xss-Protection']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Xss-Protection: {b}\n')

 try:
  b = bo['Report-To']
 except KeyError:
  pass
 else:
  hlist.append(f'Report-To: {b}\n')

 try:
  b = bo['X-Frame-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Frame-Options: {b}\n')
  
 try:
  b = bo['Cross-Origin-Opener-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Opener-Policy: {b}\n')
  
 try:
  b = bo['Cache-Control']
 except KeyError:
  pass
 else:
  hlist.append(f'Cache-Control: {b}\n')

 try:
  b = bo['Access-Control-Allow-Origin']
 except KeyError:
  pass
 else:
  hlist.append(f'Access-Control-Allow-Origin: {b}\n')

 try:
  b = bo['Strict-Transport-Security']
 except KeyError:
  pass
 else:
  hlist.append(f'Strict-Transport-Security: {b}\n')
  
 try:
  b = bo['Cross-Origin-Resource-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Resource-Policy: {b}\n')
  
 try:
  b = bo['X-Content-Type-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Content-Type-Options: {b}\n')    
 
 try:
  b = bo['Referrer-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Referrer-Policy: {b}\n')

 try:
  b = bo['Vary']
 except KeyError:
  pass
 else:
  hlist.append(f'Vary: {b}\n')

 try:
  b = bo['upgrade']
 except KeyError:
  pass
 else:
  hlist.append(f'upgrade: {b}\n')

 try:
  b = bo['Content-Security-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Security-Policy: {b}\n')

 try:
  b = bo['connection']
 except KeyError:
  pass
 else:
  hlist.append(f'connection: {b}\n')  

 try:
  b = bo['Date']
 except KeyError:
  pass
 else:
  hlist.append(f'Date: {b}\n')  

 try:
  b = bo['Content-Length']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Length: {b}\n')  
  
# RESPONSE Create
 j = ''.join(hlist)
 print(colored("=================[Response]===================","red"))
 print(colored(f"{http_s} {bss}","green"))
 print(colored(j,"green"))
 print(var1.text)



# DELETE REQUEST ENGINE
def t_delete():
 
# DELETE Request Start
 colb = f"{http_in}://{input_host}{path2}"

 try:
  abf = input_query1
  abe = value_query1
 except NameError: 
  q_data = ''
  var1 = requests.delete(f"{colb}", headers=req_header, allow_redirects=False)
  pass
 else:
  value_query = input("parameter's value: ")
  if value_query == '':
   q_data = f"?{input_query1}={value_query1}"
  else:
   q_data = f"?{input_query1}={value_query}"
  var1 = requests.delete(f"{colb}{q_data}", headers=req_header, allow_redirects=False)
  
 bo = var1.headers
 print(colored("===================[URL]=====================","red"))
 print(colored(f"{colb}{q_data}","blue"))
 
  
# Status Code Fetches
 bs = var1.status_code
 if bs == 200:
  bss = colored("200 OK","green")
 elif bs == 201:
  bss = colored("201 Created","green")
 elif bs == 302:
  bss = colored("302 Found","yellow")
 elif bs == 301:
  bss = colored("301 Moved Permanently","yellow")
 elif bs == 404:
  bss = colored("404 Not Found","magenta")
 elif bs == 403:
  bss = colored("403 Forbidden","magenta")
 elif bs == 401:
  bss = colored("401 Unauthorized","magenta")
 elif bs == 400:
  bss = colored("400 Bad Request","magenta")
 elif bs == 500:
  bss = colored("500 Internal Server Error","red")
 elif bs == 503:
  bss = colored("503 Service Unavailable","red")
 else:
  bss = colored(f"{bs}","cyan")

# Request Conditions 
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f"""DELETE {path2}{q_data} {http_s}
Host: {input_host}
{aba}
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
 
""","green"))
 except UnboundLocalError:
  print(colored(f"""DELETE {path2}{q_data} {http_s}
Host: {input_host}
User-Agent: Python/3
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
 
  ""","green"))
  pass
 else:
  pass
       
       
# Response Header Fetches   
 hlist = []
 try:
  b = bo['Server']
 except KeyError:
  pass
 else:
  hlist.append(f'Server: {b}\n')

 try:
  b = bo['Set-Cookie']
 except KeyError:
  pass
 else:
  hlist.append(f'Set-Cookie: {b}\n')

 try:
  b = bo['Location']
 except KeyError:
  pass
 else:
  hlist.append(f'Location: {b}\n')
  
 try:
  b = bo['Content-Type']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Type: {b}\n')
 
 try:
  b = bo['X-Xss-Protection']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Xss-Protection: {b}\n')

 try:
  b = bo['Report-To']
 except KeyError:
  pass
 else:
  hlist.append(f'Report-To: {b}\n')

 try:
  b = bo['X-Frame-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Frame-Options: {b}\n')
  
 try:
  b = bo['Cross-Origin-Opener-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Opener-Policy: {b}\n')
  
 try:
  b = bo['Cache-Control']
 except KeyError:
  pass
 else:
  hlist.append(f'Cache-Control: {b}\n')

 try:
  b = bo['Access-Control-Allow-Origin']
 except KeyError:
  pass
 else:
  hlist.append(f'Access-Control-Allow-Origin: {b}\n')

 try:
  b = bo['Strict-Transport-Security']
 except KeyError:
  pass
 else:
  hlist.append(f'Strict-Transport-Security: {b}\n')
  
 try:
  b = bo['Cross-Origin-Resource-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Resource-Policy: {b}\n')
  
 try:
  b = bo['X-Content-Type-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Content-Type-Options: {b}\n')    
 
 try:
  b = bo['Referrer-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Referrer-Policy: {b}\n')

 try:
  b = bo['Vary']
 except KeyError:
  pass
 else:
  hlist.append(f'Vary: {b}\n')

 try:
  b = bo['upgrade']
 except KeyError:
  pass
 else:
  hlist.append(f'upgrade: {b}\n')

 try:
  b = bo['Content-Security-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Security-Policy: {b}\n')

 try:
  b = bo['connection']
 except KeyError:
  pass
 else:
  hlist.append(f'connection: {b}\n')  

 try:
  b = bo['Date']
 except KeyError:
  pass
 else:
  hlist.append(f'Date: {b}\n')  

 try:
  b = bo['Content-Length']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Length: {b}\n')  
  
# RESPONSE Create
 j = ''.join(hlist)
 print(colored("=================[Response]===================","red"))
 print(colored(f"{http_s} {bss}","green"))
 print(colored(j,"green"))
 print(var1.text)


# POST REQUEST ENGINE
def t_post():
 colb = f"{http_in}://{input_host}{path2}"
 if d_type == 'json':
  q_data = {}
  inputt_query1 = []
  valuee_query1 = []
  input_query_count = int(input("Json Keypair Count[1,2,3,4,5]: "))
  for i in range(0,input_query_count):
   input_jquery = input(f"Json Key {i+1}: ")
   inputt_query1.append(input_jquery)
   input_jvalue = input(f"Json Value {i+1}: ")
   valuee_query1.append(input_jvalue)
   q_data[input_jquery] = input_jvalue
  var1 = requests.post(f"{colb}", headers=req_header, json=q_data, allow_redirects=False)
 elif d_type == 'www':
  value_query = input("parameter's value: ")
  if value_query == '':
   q_data = f"{input_query1}={value_query1}"
  else:
   q_data = f"{input_query1}={value_query}"
   var1 = requests.post(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)
  var1 = requests.post(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)
 else:
   value_query = input("parameter's value: ")
   if value_query == '':
    q_data = f"{input_query1}={value_query1}"
   else:
    q_data = f"{input_query1}={value_query}"
   var1 = requests.post(f"{colb}", headers=req_header, data=q_data, allow_redirects=False) 
   
# POST Request Start
 bo = var1.headers
 br = var1.request.headers
 print(colored("===================[URL]=====================","red"))
 print(colored(f"{colb}","blue"))
# Request Content Fetch 
 try: 
  fc = br['Content-Length']
 except KeyError:
  pass
 else:
  cf = fc
 
# Status Code Fetches
 bs = var1.status_code
 if bs == 200:
  bss = colored("200 OK","green")
 elif bs == 201:
  bss = colored("201 Created","green")
 elif bs == 302:
  bss = colored("302 Found","yellow")
 elif bs == 301:
  bss = colored("301 Moved Permanently","yellow")
 elif bs == 404:
  bss = colored("404 Not Found","magenta")
 elif bs == 403:
  bss = colored("403 Forbidden","magenta")
 elif bs == 401:
  bss = colored("401 Unauthorized","magenta")
 elif bs == 400:
  bss = colored("400 Bad Request","magenta")
 elif bs == 500:
  bss = colored("500 Internal Server Error","red")
 elif bs == 503:
  bss = colored("503 Service Unavailable","red")
 else:
  bss = colored(f"{bs}","cyan")
  
# Request Conditions  
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f"""POST {path2} {http_s}
Host: {input_host}
{aba}
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
Content-Length: {cf}
 
{q_data}""","green"))
 except UnboundLocalError:
  print(colored(f"""POST {path2} {http_s}
Host: {input_host}
User-Agent: Python/3
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
Content-Length: {cf}
  
{q_data}""","green"))
  pass
 else:
  pass
       
       
# Response Header Fetches   
 hlist = []
 try:
  b = bo['Server']
 except KeyError:
  pass
 else:
  hlist.append(f'Server: {b}\n')

 try:
  b = bo['Set-Cookie']
 except KeyError:
  pass
 else:
  hlist.append(f'Set-Cookie: {b}\n')

 try:
  b = bo['Location']
 except KeyError:
  pass
 else:
  hlist.append(f'Location: {b}\n')
  
 try:
  b = bo['Content-Type']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Type: {b}\n')
 
 try:
  b = bo['X-Xss-Protection']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Xss-Protection: {b}\n')

 try:
  b = bo['Report-To']
 except KeyError:
  pass
 else:
  hlist.append(f'Report-To: {b}\n')

 try:
  b = bo['X-Frame-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Frame-Options: {b}\n')
  
 try:
  b = bo['Cross-Origin-Opener-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Opener-Policy: {b}\n')
  
 try:
  b = bo['Cache-Control']
 except KeyError:
  pass
 else:
  hlist.append(f'Cache-Control: {b}\n')

 try:
  b = bo['Access-Control-Allow-Origin']
 except KeyError:
  pass
 else:
  hlist.append(f'Access-Control-Allow-Origin: {b}\n')

 try:
  b = bo['Strict-Transport-Security']
 except KeyError:
  pass
 else:
  hlist.append(f'Strict-Transport-Security: {b}\n')
  
 try:
  b = bo['Cross-Origin-Resource-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Resource-Policy: {b}\n')
  
 try:
  b = bo['X-Content-Type-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Content-Type-Options: {b}\n')    
 
 try:
  b = bo['Referrer-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Referrer-Policy: {b}\n')

 try:
  b = bo['Vary']
 except KeyError:
  pass
 else:
  hlist.append(f'Vary: {b}\n')

 try:
  b = bo['upgrade']
 except KeyError:
  pass
 else:
  hlist.append(f'upgrade: {b}\n')

 try:
  b = bo['Content-Security-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Security-Policy: {b}\n')

 try:
  b = bo['connection']
 except KeyError:
  pass
 else:
  hlist.append(f'connection: {b}\n')  

 try:
  b = bo['Date']
 except KeyError:
  pass
 else:
  hlist.append(f'Date: {b}\n')  

 try:
  b = bo['Content-Length']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Length: {b}\n')  
  
# RESPONSE Create
 j = ''.join(hlist)
 print(colored("=================[Response]===================","red"))
 print(colored(f"{http_s} {bss}","green"))
 print(colored(j,"green"))
 print(var1.text)



def t_patch():
# PATCH Request Start
 colb = f"{http_in}://{input_host}{path2}"
 if d_type == 'json':
  q_data = {}
  inputt_query1 = []
  valuee_query1 = []
  input_query_count = int(input("Json Keypair Count[1,2,3,4,5]: "))
  for i in range(0,input_query_count):
   input_jquery = input(f"Json Key {i+1}: ")
   inputt_query1.append(input_jquery)
   input_jvalue = input(f"Json Value {i+1}: ")
   valuee_query1.append(input_jvalue)
   q_data[input_jquery] = input_jvalue
  var1 = requests.patch(f"{colb}", headers=req_header, json=q_data, allow_redirects=False)
 elif d_type == 'www':
  value_query = input("parameter's value: ")
  if value_query == '':
   q_data = f"{input_query1}={value_query1}"
  else:
   q_data = f"{input_query1}={value_query}"
   var1 = requests.patch(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)
  var1 = requests.patch(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)
 else:
   value_query = input("parameter's value: ")
   if value_query == '':
    q_data = f"{input_query1}={value_query1}"
   else:
    q_data = f"{input_query1}={value_query}"
   var1 = requests.patch(f"{colb}", headers=req_header, data=q_data, allow_redirects=False) 
  
 bo = var1.headers
 br = var1.request.headers
 print(colored("===================[URL]=====================","red"))
 print(colored(f"{colb}","blue"))
# Request Content Fetch 
 try: 
  fc = br['Content-Length']
 except KeyError:
  pass
 else:
  cf = fc  

# Status Code Fetches
 bs = var1.status_code
 if bs == 200:
  bss = colored("200 OK","green")
 elif bs == 201:
  bss = colored("201 Created","green")
 elif bs == 302:
  bss = colored("302 Found","yellow")
 elif bs == 301:
  bss = colored("301 Moved Permanently","yellow")
 elif bs == 404:
  bss = colored("404 Not Found","magenta")
 elif bs == 403:
  bss = colored("403 Forbidden","magenta")
 elif bs == 401:
  bss = colored("401 Unauthorized","magenta")
 elif bs == 400:
  bss = colored("400 Bad Request","magenta")
 elif bs == 500:
  bss = colored("500 Internal Server Error","red")
 elif bs == 503:
  bss = colored("503 Service Unavailable","red")
 else:
  bss = colored(f"{bs}","cyan")
  
# Request Conditions  

 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f"""PATCH {path2} {http_s}
Host: {input_host}
{aba}
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
Content-Length: {cf}
 
{q_data}""","green"))
 except UnboundLocalError:
  print(colored(f"""PATCH {path2} {http_s}
Host: {input_host}
User-Agent: Python/3
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
Content-Length: {cf}
  
{q_data}""","green"))
  pass
 else:
  pass
       
       
# Response Header Fetches   
 hlist = []
 try:
  b = bo['Server']
 except KeyError:
  pass
 else:
  hlist.append(f'Server: {b}\n')

 try:
  b = bo['Set-Cookie']
 except KeyError:
  pass
 else:
  hlist.append(f'Set-Cookie: {b}\n')

 try:
  b = bo['Location']
 except KeyError:
  pass
 else:
  hlist.append(f'Location: {b}\n')
  
 try:
  b = bo['Content-Type']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Type: {b}\n')
 
 try:
  b = bo['X-Xss-Protection']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Xss-Protection: {b}\n')

 try:
  b = bo['Report-To']
 except KeyError:
  pass
 else:
  hlist.append(f'Report-To: {b}\n')

 try:
  b = bo['X-Frame-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Frame-Options: {b}\n')
  
 try:
  b = bo['Cross-Origin-Opener-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Opener-Policy: {b}\n')
  
 try:
  b = bo['Cache-Control']
 except KeyError:
  pass
 else:
  hlist.append(f'Cache-Control: {b}\n')

 try:
  b = bo['Access-Control-Allow-Origin']
 except KeyError:
  pass
 else:
  hlist.append(f'Access-Control-Allow-Origin: {b}\n')

 try:
  b = bo['Strict-Transport-Security']
 except KeyError:
  pass
 else:
  hlist.append(f'Strict-Transport-Security: {b}\n')
  
 try:
  b = bo['Cross-Origin-Resource-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Resource-Policy: {b}\n')
  
 try:
  b = bo['X-Content-Type-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Content-Type-Options: {b}\n')    
 
 try:
  b = bo['Referrer-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Referrer-Policy: {b}\n')

 try:
  b = bo['Vary']
 except KeyError:
  pass
 else:
  hlist.append(f'Vary: {b}\n')

 try:
  b = bo['upgrade']
 except KeyError:
  pass
 else:
  hlist.append(f'upgrade: {b}\n')

 try:
  b = bo['Content-Security-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Security-Policy: {b}\n')

 try:
  b = bo['connection']
 except KeyError:
  pass
 else:
  hlist.append(f'connection: {b}\n')  

 try:
  b = bo['Date']
 except KeyError:
  pass
 else:
  hlist.append(f'Date: {b}\n')  

 try:
  b = bo['Content-Length']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Length: {b}\n')  
  
# RESPONSE Create
 j = ''.join(hlist)
 print(colored("=================[Response]===================","red"))
 print(colored(f"{http_s} {bss}","green"))
 print(colored(j,"green"))
 print(var1.text)



# PUT REQUEST ENGINE
def t_put():
# PUT Request Start
 colb = f"{http_in}://{input_host}{path2}"
 if d_type == 'json':
  q_data = {}
  inputt_query1 = []
  valuee_query1 = []
  input_query_count = int(input("Json Keypair Count[1,2,3,4,5]: "))
  for i in range(0,input_query_count):
   input_jquery = input(f"Json Key {i+1}: ")
   inputt_query1.append(input_jquery)
   input_jvalue = input(f"Json Value {i+1}: ")
   valuee_query1.append(input_jvalue)
   q_data[input_jquery] = input_jvalue
  var1 = requests.put(f"{colb}", headers=req_header, json=q_data, allow_redirects=False)
 elif d_type == 'www':
  value_query = input("parameter's value: ")
  if value_query == '':
   q_data = f"{input_query1}={value_query1}"
  else:
   q_data = f"{input_query1}={value_query}"
   var1 = requests.put(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)
  var1 = requests.put(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)
 else:
   value_query = input("parameter's value: ")
   if value_query == '':
    q_data = f"{input_query1}={value_query1}"
   else:
    q_data = f"{input_query1}={value_query}"
   var1 = requests.put(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)  
 

 bo = var1.headers
 br = var1.request.headers
 print(colored("===================[URL]=====================","red"))
 print(colored(f"{colb}","blue")) 
 
# Request Content Fetch 
 try: 
  fc = br['Content-Length']
 except KeyError:
  pass
 else:
  cf = fc  

# Status Code Fetches
 bs = var1.status_code
 if bs == 200:
  bss = colored("200 OK","green")
 elif bs == 201:
  bss = colored("201 Created","green")
 elif bs == 302:
  bss = colored("302 Found","yellow")
 elif bs == 301:
  bss = colored("301 Moved Permanently","yellow")
 elif bs == 404:
  bss = colored("404 Not Found","magenta")
 elif bs == 403:
  bss = colored("403 Forbidden","magenta")
 elif bs == 401:
  bss = colored("401 Unauthorized","magenta")
 elif bs == 400:
  bss = colored("400 Bad Request","magenta")
 elif bs == 500:
  bss = colored("500 Internal Server Error","red")
 elif bs == 503:
  bss = colored("503 Service Unavailable","red")
 else:
  bss = colored(f"{bs}","cyan")
 
# Request Conditions  
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f"""PUT {path2} {http_s}
Host: {input_host}
{aba}
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
Content-Length: {cf}
 
 {q_data}""","green"))
 except UnboundLocalError:
  print(colored(f"""PUT {path2} {http_s}
Host: {input_host}
User-Agent: Python/3
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
Content-Length: {cf}
 
{q_data}""","green"))
  pass
 else:
  pass
       
       
# Response Header Fetches   
 hlist = []
 try:
  b = bo['Server']
 except KeyError:
  pass
 else:
  hlist.append(f'Server: {b}\n')

 try:
  b = bo['Set-Cookie']
 except KeyError:
  pass
 else:
  hlist.append(f'Set-Cookie: {b}\n')

 try:
  b = bo['Location']
 except KeyError:
  pass
 else:
  hlist.append(f'Location: {b}\n')
  
 try:
  b = bo['Content-Type']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Type: {b}\n')
 
 try:
  b = bo['X-Xss-Protection']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Xss-Protection: {b}\n')

 try:
  b = bo['Report-To']
 except KeyError:
  pass
 else:
  hlist.append(f'Report-To: {b}\n')

 try:
  b = bo['X-Frame-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Frame-Options: {b}\n')
  
 try:
  b = bo['Cross-Origin-Opener-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Opener-Policy: {b}\n')
  
 try:
  b = bo['Cache-Control']
 except KeyError:
  pass
 else:
  hlist.append(f'Cache-Control: {b}\n')

 try:
  b = bo['Access-Control-Allow-Origin']
 except KeyError:
  pass
 else:
  hlist.append(f'Access-Control-Allow-Origin: {b}\n')

 try:
  b = bo['Strict-Transport-Security']
 except KeyError:
  pass
 else:
  hlist.append(f'Strict-Transport-Security: {b}\n')
  
 try:
  b = bo['Cross-Origin-Resource-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Cross-Origin-Resource-Policy: {b}\n')
  
 try:
  b = bo['X-Content-Type-Options']
 except KeyError:
  pass
 else:
  hlist.append(f'X-Content-Type-Options: {b}\n')    
 
 try:
  b = bo['Referrer-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Referrer-Policy: {b}\n')

 try:
  b = bo['Vary']
 except KeyError:
  pass
 else:
  hlist.append(f'Vary: {b}\n')

 try:
  b = bo['upgrade']
 except KeyError:
  pass
 else:
  hlist.append(f'upgrade: {b}\n')

 try:
  b = bo['Content-Security-Policy']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Security-Policy: {b}\n')

 try:
  b = bo['connection']
 except KeyError:
  pass
 else:
  hlist.append(f'connection: {b}\n')  

 try:
  b = bo['Date']
 except KeyError:
  pass
 else:
  hlist.append(f'Date: {b}\n')  

 try:
  b = bo['Content-Length']
 except KeyError:
  pass
 else:
  hlist.append(f'Content-Length: {b}\n')  
  
# RESPONSE Create
 j = ''.join(hlist)
 print(colored("=================[Response]===================","red"))
 print(colored(f"{http_s} {bss}","green"))
 print(colored(j,"green"))
 print(var1.text)
 
 
# SET HOST AND PATH
input_http1 = input(colored("http or https : ","cyan"))
if input_http1 =='' or input_http1=='http':
 http_in = 'http'
 http_s = 'HTTP/1.1'
   
elif input_http1 =='HTTPS' or input_http1=='https':
 http_in = 'https'
 http_s = 'HTTP/2'

else:
 http_in = 'http'
 http_s = 'HTTP/1.1'


# Main Program Start

print(colored(f"Current Protocol Set To : {http_s}","magenta")) 
input_host1 = input(colored("Hostname: ","cyan"))
if input_host1 == '':
 print(colored("ERROR !! please specify the host name ","red"))
 input_host1 = input(colored("Hostname: ","cyan"))
 input_host = input_host1
 print(colored(f"Current Hostname Set To : {input_host}","magenta"))
else:
 input_host = input_host1
 print(colored(f"Current Hostname Set To : {input_host}","magenta"))
 
# main path
input_path = input(colored("Path: ","cyan"))
try:
 if input_path[0] == '/':
  path2 = input_path
 else:
  path_te = input_path[0:]
  path2 = f"/{path_te}"
except IndexError:
 path2 = f"/{input_path}"
 pass
print(colored(f"Current Path Set To : {path2}","magenta"))
   
input_query = ''
value_query = ''
q_data = ''

req_header = {"User-Agent": "Python/3"}
aba = "User-Agent: Python/3"
d_type = "www"


while True:
 input_main = input(colored("""[engine] > """,'red'))
 if input_main == 'help' :
  print(colored("""
 help            - help mode 
 exit            - exit from request engine
 show            - show current request  
 set-host / sh   - setting of http & host 
 set-header / sh - setting of headers
 set-path / sp   - setting of path
 set-para / spa  - setting of get parameter
 set-json / sj   - setting of json body [POST/PUT/PATCH]
 get / rg        - get request engine
 post / rp       - post request engine
 delete / rd     - delete request engine
 put / rP        - put request engine
 patch / rpat    - patch request engine
 options / ro    - options request engine
 head / rh       - head request engine  
  """,'yellow'))
 elif input_main == 'exit' or input_main == 'e':
  sys.exit()
  
 elif input_main == 'show':  
  print(colored(f"""
-------[Current--Request]---------- 
[METHOD] {path2}{q_data} {http_s}
Host: {input_host}
{aba}
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
 
{q_data}
-----------------------------------""","magenta"))
 
 elif input_main == 'set-host' or input_main == 'sh':
  print(colored("[+] Request Host Settings [activated]\n","green"))
  print(colored(f"\n- Current HTTP version : {http_s}","magenta"))
  print(colored(f"- Current Host : {input_host}\n","magenta"))
  
# SET HOST AND PATH
  input_http = input("http or https : ")
  if input_http == '':
   input_http == input_http1
  else:
   if input_http=='http':
    http_in = 'http'
    http_s = 'HTTP/1.1'
   
   elif input_http =='HTTPS' or input_http=='https':
    http_in = 'https'
    http_s = 'HTTP/2'

   else:
    http_in = 'http'
    http_s = 'HTTP/1.1'
   print(colored(f"Current HTTP version set to : {http_s}\n","red"))  
  input_host = input("Hostname: ")
  if input_host == '':
   input_host = input_host1
   print(colored(f"Current Host set to : {input_host}\n","red"))
  else:
   print(colored(f"Current Host set to : {input_host}\n","red"))

# Path Setting  
 elif input_main == 'set-path' or input_main == 'sp':
  print(colored("[+] Request Path Settings [activated]","green"))
  print(colored(f"\n- Current Path : {path2}\n","magenta"))
  input_path = input("Path: ")
  try:
   if input_path[0] == '/':
    path2 = input_path
   else:
    path_te = input_path[0:]
    path2 = f"/{path_te}"
  except IndexError:
   path2 = f"/{input_path}"
   pass 
  print(colored(f"Current Path set to : {path2}\n","red"))

  
# Parameter Setting
 elif input_main == 'set-para' or input_main == 'spa':
  print(colored("[+] Request Parameter Settings [activated]","green"))
  print(colored(f"\n- Current Parameter : {q_data}\n","magenta"))
  d_type = 'www'
  input_query1 = input("parameter: ")
  value_query1 = input("parameter's value: ")
  try:
   if input_query1[0]=="?":
    q_data = f"{input_query1}={value_query1}"
   else:
    q_data = f"?{input_query1}={value_query1}"
  except IndexError:
   q_data = ""
   pass
  print(colored(f"Current Parameter & value set to : {q_data}\n","red"))


# Header setting
 elif input_main == 'set-header' or input_main == 'sh':
  print(colored("[+] Request Header Settings [activated]\n","green"))
  
  
# Header Writing With Count
  note_head = []
  note_value = []
  header_count_l = []
  headers_i = []
  try:
   header_count = int(input("Header count[1,2,3,4,5]: "))
  except ValueError:
   try:
    header_count = header_count_l[0]
   except IndexError:
    pass
   else:
    print('')
   for i in range(0,header_count):
    input_header = input(f"Header{i+1}: ")
    if input_header == '':
     try:
      input_header == headers_i[0]
     except IndexError:
      pass
     else: 
      input_header == headers_i[0]
      pass
    else:
     input_value = input(f"Header{i+1}'s value: ")
     print(colored(f"Current Header{i+1} & value{i} set to > {input_header}: {input_value}","red"))
     note_head.append(f"{input_header}")
     note_value.append(f"{input_value}")
     req_header[input_header] = f"{input_value}"
  else:
   header_count_l.append(header_count)
   for i in range(0,header_count):
    input_header = input(f"Header{i+1}: ")
    if input_header == '':
     try:
      input_header == headers_i[0]
     except IndexError:
      pass
     else: 
      input_header == headers_i[0]
      pass
    else:
     input_value = input(f"Header{i+1}'s value: ")
     print(colored(f"Current Header{i+1} & value{i} set to > {input_header}: {input_value}","red"))
     note_head.append(f"{input_header}")
     note_value.append(f"{input_value}")
     req_header[input_header] = f"{input_value}"

# Request Headers Show Off
  try:
   acc = header_count
  except NameError:
   aba = "User-Agent: Python/3"
   pass
  else:
   try:
    if header_count == 1:
     aba = f"{note_head[0]}: {note_value[0]}"
    elif header_count == 2:
     aba = f"{note_head[0]}: {note_value[0]}\n{note_head[1]}: {note_value[1]}"
    elif header_count == 3:
     aba = f"{note_head[0]}: {note_value[0]}\n{note_head[1]}: {note_value[1]}\n{note_head[2]}: {note_value[2]}"
    elif header_count == 4:
     aba = f"""{note_head[0]}: {note_value[0]}\n{note_head[1]}: {note_value[1]}\n{note_head[2]}: {note_value[2]}\n{note_head[3]}: {note_value[3]}""" 
    elif header_count == 5:
     aba = f"""{note_head[0]}: {note_value[0]}\n{note_head[1]}: {note_value[1]}\n{note_head[2]}: {note_value[2]}\n{note_head[3]}: {note_value[3]}\n{note_head[4]}: {note_value[4]}""" 
   except UnboundLocalError or IndexError:
    pass
   else:
    print('')

# Json Request setting
 elif input_main == 'set-json' or input_main == 'sj':
  print(colored("[+] JSON Request Setting [activated]\n","green"))
  d_type = 'json'
  print(colored("[+]Current Data Type sets to [application/json]","red"))
  
# Get request option 
 elif input_main == 'get' or input_main == 'g':
  print(colored("[+] GET Request engine [activated]\n","green"))
  t_get()
  
# Post request option
 elif input_main == 'post' or input_main =='p':
  if d_type == 'json':
   t_post()
  else:
   try: 
    a = input_query1
    b = value_query1
   except NameError:
    print(colored("""[!]You need to specify Request Body Parameter using 'set-para' or 'spa' for [application/www-form-url-encoded] 'json' for [application/json] type body data \n""","cyan"))
    pass
   else:
    print(colored("[+] POST Request engine [activated]\n","green"))
    t_post()

# Delete request option
 elif input_main == 'delete' or input_main =='d':
  print(colored("[+] DELETE Request engine [activated]\n","green"))
  t_delete()
  
# Put request option
 elif input_main == 'put' or input_main =='P':
  if d_type == 'json':
   t_put()
  else:
   try: 
    a = input_query1
    b = value_query1
   except NameError:
    print(colored("""[!]You need to specify Request Body Parameter using 'set-para' or 'spa' for [application/www-form-url-encoded] 'json' for [application/json] type body data \n""","cyan"))
    pass
   else:
    print(colored("[+] PUT Request engine [activated]\n","green"))
    t_put()
  
# Option request option
 elif input_main == 'options' or input_main =='o':
  print(colored("[+] OPTIONS Request engine [activated]\n","green"))
  t_options()

# Head request option
 elif input_main == 'head' or input_main =='h':
  print(colored("[+] HEAD Request engine [activated]\n","green"))
  t_head()  
  
# Patch request option
 elif input_main == 'patch' or input_main =='pat':
  if d_type == 'json':
   t_patch()
  else:
   try: 
    a = input_query1
    b = value_query1
   except NameError:
    print(colored("""[!]You need to specify Request Body Parameter using 'set-para' or 'spa' for [application/www-form-url-encoded] 'json' for [application/json] type body data \n""","cyan"))
    pass
   else:
    print(colored("[+] PATCH Request engine [activated]\n","green"))
    t_patch()
  
# Else option to help
 else:
  print(colored("""
 help            - help mode
 exit            - exit from request engine
 show            - show current request  
 set-host / sh   - setting of http & host 
 set-header / sh - setting of headers
 set-path / sp   - setting of path
 set-para / spa  - setting of get parameter
 set-json / sj   - setting of json body [POST/PUT/PATCH]
 get / g        - get request engine
 post / p       - post request engine
 delete / d     - delete request engine
 put / P        - put request engine
 patch / pat    - patch request engine
 options / o    - options request engine
 head / h       - head request engine
  """,'yellow'))
