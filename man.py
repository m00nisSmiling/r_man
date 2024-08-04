import requests
import os
import json
from termcolor import colored
import sys

print(colored('''          +   REQUEST   +    ENGINE   +''','red'))
  
print(colored('''         000 111111111 111 111111111 000
        00000 1111111 11111 1111111 00000
       0000000 11111 1111111 11111 0000000
      000000000 111 111111111 111 000000000
                 +             +            ''','green'))
print(colored('''          [Developed By m00nissmiling]\n''','red'))



# OPTIONS REQUEST ENGINE
def t_options():
   
# Parameter Specify
 input_query = input("Parameter Data: ")
 try:
  if input_query[0]=="?":
   q_data = f"{input_query}"
  else:
   q_data = f"?{input_query}"
 except IndexError:
  q_data = ""
  pass
   
# Header Writing With Count
 req_header = {"User-Agent": "Python/3"}
 note_head = []
 note_value = []
 try:
  header_count = int(input("Header count[1,2,3,4,5]: "))
 except ValueError:
  pass
 else:
  if header_count=='':
   pass
  else:
   for i in range(0,header_count):
    input_header = input(f"Header{i}: ")
    if input_header == '':
     pass
    else:
     input_value = input(f"Header{i}'s value: ")
     note_head.append(f"{input_header}")
     note_value.append(f"{input_value}")
     req_header[input_header] = f"{input_value}"

# OPTIONS Request Start
 colb = f"{http_in}://{input_host}{path2}{q_data}"

 var1 = requests.options(f"{colb}", headers=req_header, allow_redirects=False)
 bo = var1.headers
 
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
 
# Request Headers Show Off
 try:
  if header_count == 1:
   aba = f"{note_head[0]}: {note_value[0]}"
  elif header_count == 2:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}"
  elif header_count == 3:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}"
  elif header_count == 4:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}""" 
  elif header_count == 5:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}\n {note_head[4]}: {note_value[4]}""" 
 except UnboundLocalError:
  pass
 else:
  print('')

# Request Conditions 
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f""" OPTIONS {path2}{q_data} {http_s}
 Host: {input_host}
 {aba}
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
  ""","blue"))
 except UnboundLocalError:
  print(colored(f""" OPTIONS {path2}{q_data} {http_s}
 Host: {input_host}
 User-Agent: Python/3
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
  ""","blue"))
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
 print(colored(f"{http_s} {bss}","blue"))
 print(colored(j,"blue"))
 print(var1.text)



# HEAD REQUEST ENGINE
def t_head():
# Parameter Specify
 input_query = input("Parameter Data: ")
 try:
  if input_query[0]=="?":
   q_data = f"{input_query}"
  else:
   q_data = f"?{input_query}"
 except IndexError:
  q_data = ""
  pass
   
# Header Writing With Count
 req_header = {"User-Agent": "Python/3"}
 note_head = []
 note_value = []
 try:
  header_count = int(input("Header count[1,2,3,4,5]: "))
 except ValueError:
  pass
 else:
  if header_count=='':
   pass
  else:
   for i in range(0,header_count):
    input_header = input(f"Header{i}: ")
    if input_header == '':
     pass
    else:
     input_value = input(f"Header{i}'s value: ")
     note_head.append(f"{input_header}")
     note_value.append(f"{input_value}")
     req_header[input_header] = f"{input_value}"

# HEAD Request Start
 colb = f"{http_in}://{input_host}{path2}{q_data}"

 var1 = requests.head(f"{colb}", headers=req_header, allow_redirects=False)
 bo = var1.headers
 
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
 
# Request Headers Show Off
 try:
  if header_count == 1:
   aba = f"{note_head[0]}: {note_value[0]}"
  elif header_count == 2:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}"
  elif header_count == 3:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}"
  elif header_count == 4:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}""" 
  elif header_count == 5:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}\n {note_head[4]}: {note_value[4]}""" 
 except UnboundLocalError:
  pass
 else:
  print('')

# Request Conditions 
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f""" HEAD {path2}{q_data} {http_s}
 Host: {input_host}
 {aba}
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
  ""","blue"))
 except UnboundLocalError:
  print(colored(f""" HEAD {path2}{q_data} {http_s}
 Host: {input_host}
 User-Agent: Python/3
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
  ""","blue"))
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
 print(colored(f"{http_s} {bss}","blue"))
 print(colored(j,"blue"))
 print(var1.text)




# GET REQUEST ENGINE
def t_get():
# Parameter Specify
 input_query = input("Parameter Data: ")
 try:
  if input_query[0]=="?":
   q_data = f"{input_query}"
  else:
   q_data = f"?{input_query}"
 except IndexError:
  q_data = ""
  pass
   
# Header Writing With Count
 req_header = {"User-Agent": "Python/3"}
 note_head = []
 note_value = []
 try:
  header_count = int(input("Header count[1,2,3,4,5]: "))
 except ValueError:
  pass
 else:
  if header_count=='':
   pass
  else:
   for i in range(0,header_count):
    input_header = input(f"Header{i}: ")
    if input_header == '':
     pass
    else:
     input_value = input(f"Header{i}'s value: ")
     note_head.append(f"{input_header}")
     note_value.append(f"{input_value}")
     req_header[input_header] = f"{input_value}"

# Get Request Start
 colb = f"{http_in}://{input_host}{path2}{q_data}"

 var1 = requests.get(f"{colb}", headers=req_header, allow_redirects=False)
 bo = var1.headers
 
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
 
# Request Headers Show Off
 try:
  if header_count == 1:
   aba = f"{note_head[0]}: {note_value[0]}"
  elif header_count == 2:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}"
  elif header_count == 3:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}"
  elif header_count == 4:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}""" 
  elif header_count == 5:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}\n {note_head[4]}: {note_value[4]}""" 
 except UnboundLocalError:
  pass
 else:
  print('')

# Request Conditions 
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f""" GET {path2}{q_data} {http_s}
 Host: {input_host}
 {aba}
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
  ""","blue"))
 except UnboundLocalError:
  print(colored(f""" GET {path2}{q_data} {http_s}
 Host: {input_host}
 User-Agent: Python/3
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
  ""","blue"))
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
 print(colored(f"{http_s} {bss}","blue"))
 print(colored(j,"blue"))
 print(var1.text)



# DELETE REQUEST ENGINE
def t_delete():
# Parameter Specify
 input_query = input("Parameter Data: ")
 try:
  if input_query[0]=="?":
   q_data = f"{input_query}"
  else:
   q_data = f"?{input_query}"
 except IndexError:
  q_data = ""
  pass
 
# Header Writing With Count  
 req_header = {"User-Agent": "Python/3"}
 note_head = []
 note_value = []
 try:
  header_count = int(input("Header count[1,2,3,4,5]: "))
 except ValueError:
  pass
 else:
  if header_count=='':
   pass
  else:
   for i in range(0,header_count):
    input_header = input(f"Header{i}: ")
    if input_header == '':
     pass
    else:
     input_value = input(f"Header{i}'s value: ")
     note_head.append(f"{input_header}")
     note_value.append(f"{input_value}")
     req_header[input_header] = f"{input_value}"

# DELETE Request Start
 colb = f"{http_in}://{input_host}{path2}{q_data}"

 var1 = requests.delete(f"{colb}", headers=req_header, allow_redirects=False)
 bo = var1.headers
 
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
 
# Request Headers Show Off
 try:
  if header_count == 1:
   aba = f"{note_head[0]}: {note_value[0]}"
  elif header_count == 2:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}"
  elif header_count == 3:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}"
  elif header_count == 4:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}""" 
  elif header_count == 5:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}\n {note_head[4]}: {note_value[4]}""" 
 except UnboundLocalError:
  pass
 else:
  print('')

# Request Conditions 
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f""" DELETE {path2}{q_data} {http_s}
 Host: {input_host}
 {aba}
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
  ""","blue"))
 except UnboundLocalError:
  print(colored(f""" DELETE {path2}{q_data} {http_s}
 Host: {input_host}
 User-Agent: Python/3
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
  ""","blue"))
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
 print(colored(f"{http_s} {bss}","blue"))
 print(colored(j,"blue"))
 print(var1.text)


# POST REQUEST ENGINE
def t_post():
# Header Writing With Count  
 req_header = {"User-Agent": "Python/3"}
 note_head = []
 note_value = []
 try:
  header_count = int(input("Header count[1,2,3,4,5]: "))
 except ValueError:
  pass
 else:
  if header_count=='':
   pass
  else:
   for i in range(0,header_count):
    input_header = input(f"Header{i}: ")
    if input_header == '':
     pass
    else:
     input_value = input(f"Header{i}'s value: ")
     note_head.append(f"{input_header}")
     note_value.append(f"{input_value}")
     req_header[input_header] = f"{input_value}"

# POST Request Start
 colb = f"{http_in}://{input_host}{path2}"
 
# Parameter Specify

 input_queryType = input("Post Data Type[json/www]: ")
 q_data = {}
 note_jquery = []
 note_jvalue = []
 if input_queryType =='www':
  input_query = input("Parameter: ")
  q_data = input_query
  var1 = requests.post(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)
  bo = var1.headers
 elif input_queryType =='json' or input_queryType =='j':
  input_query_count = int(input("Json Keypair Count[1,2,3,4,5]: "))
  for i in range(0,input_query_count):
   input_jquery = input(f"Json Key {i}: ")
   note_jquery.append(input_jquery)
   input_jvalue = input(f"Json Value {i}: ")
   note_jvalue.append(input_jvalue)
   q_data[input_jquery] = input_jvalue
  var1 = requests.post(f"{colb}", headers=req_header, json=q_data, allow_redirects=False)
  bo = var1.headers
 else:
  input_query = input("Parameter: ")
  q_data = input_query
  var1 = requests.post(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)
  bo = var1.headers
  
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
 
# Request Headers Show Off
 try:
  if header_count == 1:
   aba = f"{note_head[0]}: {note_value[0]}"
  elif header_count == 2:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}"
  elif header_count == 3:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}"
  elif header_count == 4:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}""" 
  elif header_count == 5:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}\n {note_head[4]}: {note_value[4]}""" 
 except UnboundLocalError:
  pass
 else:
  print('')
  
# Request Conditions  
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f""" POST {path2} {http_s}
 Host: {input_host}
 {aba}
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
 {q_data}""","blue"))
 except UnboundLocalError:
  print(colored(f""" POST {path2} {http_s}
 Host: {input_host}
 User-Agent: Python/3
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
 {q_data}""","blue"))
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
 print(colored(f"{http_s} {bss}","blue"))
 print(colored(j,"blue"))
 print(var1.text)



def t_patch():
# Header Writing With Count  
 req_header = {"User-Agent": "Python/3"}
 note_head = []
 note_value = []
 try:
  header_count = int(input("Header count[1,2,3,4,5]: "))
 except ValueError:
  pass
 else:
  if header_count=='':
   pass
  else:
   for i in range(0,header_count):
    input_header = input(f"Header{i}: ")
    if input_header == '':
     pass
    else:
     input_value = input(f"Header{i}'s value: ")
     note_head.append(f"{input_header}")
     note_value.append(f"{input_value}")
     req_header[input_header] = f"{input_value}"

# PATCH Request Start
 colb = f"{http_in}://{input_host}{path2}"
 
# Parameter Specify

 input_queryType = input("Post Data Type[json/www]: ")
 q_data = {}
 note_jquery = []
 note_jvalue = []
 if input_queryType =='www':
  input_query = input("Parameter: ")
  q_data = input_query
  var1 = requests.patch(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)
  bo = var1.headers
 elif input_queryType =='json' or input_queryType =='j':
  input_query_count = int(input("Json Keypair Count[1,2,3,4,5]: "))
  for i in range(0,input_query_count):
   input_jquery = input(f"Json Key {i}: ")
   note_jquery.append(input_jquery)
   input_jvalue = input(f"Json Value {i}: ")
   note_jvalue.append(input_jvalue)
   q_data[input_jquery] = input_jvalue
  var1 = requests.patch(f"{colb}", headers=req_header, json=q_data, allow_redirects=False)
  bo = var1.headers
 else:
  input_query = input("Parameter: ")
  q_data = input_query
  var1 = requests.patch(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)
  bo = var1.headers
  
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
 
# Request Headers Show Off
 try:
  if header_count == 1:
   aba = f"{note_head[0]}: {note_value[0]}"
  elif header_count == 2:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}"
  elif header_count == 3:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}"
  elif header_count == 4:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}""" 
  elif header_count == 5:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}\n {note_head[4]}: {note_value[4]}""" 
 except UnboundLocalError:
  pass
 else:
  print('')
  
# Request Conditions  
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f""" PATCH {path2} {http_s}
 Host: {input_host}
 {aba}
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
 {q_data}""","blue"))
 except UnboundLocalError:
  print(colored(f""" PATCH {path2} {http_s}
 Host: {input_host}
 User-Agent: Python/3
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
 {q_data}""","blue"))
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
 print(colored(f"{http_s} {bss}","blue"))
 print(colored(j,"blue"))
 print(var1.text)



# PUT REQUEST ENGINE
def t_put():
# Header Writing With Count  
 req_header = {"User-Agent": "Python/3"}
 note_head = []
 note_value = []
 try:
  header_count = int(input("Header count[1,2,3,4,5]: "))
 except ValueError:
  pass
 else:
  if header_count=='':
   pass
  else:
   for i in range(0,header_count):
    input_header = input(f"Header{i}: ")
    if input_header == '':
     pass
    else:
     input_value = input(f"Header{i}'s value: ")
     note_head.append(f"{input_header}")
     note_value.append(f"{input_value}")
     req_header[input_header] = f"{input_value}"

# PUT Request Start
 colb = f"{http_in}://{input_host}{path2}"
 
# Parameter Specify

 input_queryType = input("Post Data Type[json/www]: ")
 q_data = {}
 note_jquery = []
 note_jvalue = []
 if input_queryType =='www':
  input_query = input("Parameter: ")
  q_data = input_query
  var1 = requests.put(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)
  bo = var1.headers
 elif input_queryType =='json' or input_queryType =='j':
  input_query_count = int(input("Json Keypair Count[1,2,3,4,5]: "))
  for i in range(0,input_query_count):
   input_jquery = input(f"Json Key {i}: ")
   note_jquery.append(input_jquery)
   input_jvalue = input(f"Json Value {i}: ")
   note_jvalue.append(input_jvalue)
   q_data[input_jquery] = input_jvalue
  var1 = requests.put(f"{colb}", headers=req_header, json=q_data, allow_redirects=False)
  bo = var1.headers
 else:
  input_query = input("Parameter: ")
  q_data = input_query
  var1 = requests.put(f"{colb}", headers=req_header, data=q_data, allow_redirects=False)
  bo = var1.headers
  
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
 
# Request Headers Show Off
 try:
  if header_count == 1:
   aba = f"{note_head[0]}: {note_value[0]}"
  elif header_count == 2:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}"
  elif header_count == 3:
   aba = f"{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}"
  elif header_count == 4:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}""" 
  elif header_count == 5:
   aba = f"""{note_head[0]}: {note_value[0]}\n {note_head[1]}: {note_value[1]}\n {note_head[2]}: {note_value[2]}\n {note_head[3]}: {note_value[3]}\n {note_head[4]}: {note_value[4]}""" 
 except UnboundLocalError:
  pass
 else:
  print('')
  
# Request Conditions  
 try:
  print(colored("=================[Request]===================","red"))
  print(colored(f""" PUT {path2} {http_s}
 Host: {input_host}
 {aba}
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
 {q_data}""","blue"))
 except UnboundLocalError:
  print(colored(f""" PUT {path2} {http_s}
 Host: {input_host}
 User-Agent: Python/3
 Accept-Encoding: gzip, deflate, br
 Accept: */*
 Connection: keep-alive
 
 {q_data}""","blue"))
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
 print(colored(f"{http_s} {bss}","blue"))
 print(colored(j,"blue"))
 print(var1.text)
 
 
# SET HOST AND PATH
input_http = input("http or https : ")
if input_http =='' or input_http=='http':
 http_in = 'http'
 http_s = 'HTTP/1.1'
   
elif input_http =='HTTPS' or input_http=='https':
 http_in = 'https'
 http_s = 'HTTP/2'

else:
 http_in = 'http'
 http_s = 'HTTP/1.1'

print(colored(f"Current Protocol Set To : {http_s}","magenta")) 
input_host = input("Hostname: ")
print(colored(f"Current Hostname Set To : {input_host}","magenta"))
input_path = input("Path: ")
try:
 if input_path[0] == '/':
  path2 = input_path
 else:
  path_te = input_path[1:]
  path2 = f"/{path_te}"
except IndexError:
 path2 = f"/{input_path}"
 pass

print(colored(f"Current Path Set To : {path2}","magenta"))

while True:
 input_main = input(colored("""[engine] > """,'blue'))
 if input_main == 'help' :
  print(colored("""
   help        - info about command and caller mode 
   exit        - exit from request engine 
   get / g     - get request engine
   post / p    - post request engine
   delete / d  - delete request engine
   put / P     - put request engine
   patch / pat - patch request engine
   options/o   - options request engine
   head / h    - head request engine
  """,'yellow'))
 elif input_main == 'exit' or input_main == 'e':
  sys.exit()
  
 elif input_main == 'setting' or input_main == 'rset':
  print(colored("[+] SETTINGS Request engine [activated]\n","green"))
  print(colored(f"\n- Current HTTP version : {http_s}","magenta"))
  print(colored(f"- Current Host : {input_host}","magenta"))
  print(colored(f"- Current Path : {path2} \n","magenta"))
  # SET HOST AND PATH
  input_http = input("http or https : ")
  if input_http =='' or input_http=='http':
   http_in = 'http'
   http_s = 'HTTP/1.1'
   
  elif input_http =='HTTPS' or input_http=='https':
   http_in = 'https'
   http_s = 'HTTP/2'

  else:
   http_in = 'http'
   http_s = 'HTTP/1.1'
  
  input_host = input("Hostname: ")
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
  print(colored(f"\n- Current HTTP version : {http_s}","red"))
  print(colored(f"- Current Host : {input_host}","red"))
  print(colored(f"- Current Path : {path2} \n","red"))
  
 elif input_main == 'get' or input_main == 'rg':
  print(colored("[+] GET Request engine [activated]\n","green"))
  print(colored(f"\n- Current HTTP version : {http_s}","magenta"))
  print(colored(f"- Current Host : {input_host}","magenta"))
  print(colored(f"- Current Path : {path2} \n","magenta"))
  t_get()
  
 elif input_main == 'post' or input_main =='rp':
  print(colored("[+] POST Request engine [activated]\n","green"))
  print(colored(f"\n- Current HTTP version : {http_s}","magenta"))
  print(colored(f"- Current Host : {input_host}","magenta"))
  print(colored(f"- Current Path : {path2} \n","magenta"))
  t_post()

 elif input_main == 'delete' or input_main =='rd':
  print(colored("[+] DELETE Request engine [activated]\n","green"))
  print(colored(f"\n- Current HTTP version : {http_s}","magenta"))
  print(colored(f"- Current Host : {input_host}","magenta"))
  print(colored(f"- Current Path : {path2} \n","magenta"))
  t_delete()
  
 elif input_main == 'put' or input_main =='rP':
  print(colored("[+] PUT Request engine [activated]\n","green"))
  print(colored(f"\n- Current HTTP version : {http_s}","magenta"))
  print(colored(f"- Current Host : {input_host}","magenta"))
  print(colored(f"- Current Path : {path2} \n","magenta"))
  t_put()
  
 elif input_main == 'options' or input_main =='ro':
  print(colored("[+] OPTIONS Request engine [activated]\n","green"))
  print(colored(f"\n- Current HTTP version : {http_s}","magenta"))
  print(colored(f"- Current Host : {input_host}","magenta"))
  print(colored(f"- Current Path : {path2} \n","magenta"))
  t_options()

 elif input_main == 'head' or input_main =='rh':
  print(colored("[+] HEAD Request engine [activated]\n","green"))
  print(colored(f"\n- Current HTTP version : {http_s}","magenta"))
  print(colored(f"- Current Host : {input_host}","magenta"))
  print(colored(f"- Current Path : {path2} \n","magenta"))
  t_head()  
  
 elif input_main == 'patch' or input_main =='rpat':
  print(colored("[+] PATCH Request engine [activated]\n","green"))
  print(colored(f"\n- Current HTTP version : {http_s}","magenta"))
  print(colored(f"- Current Host : {input_host}","magenta"))
  print(colored(f"- Current Path : {path2} \n","magenta"))
  t_patch()
  
 else:
  print(colored("""
   help          - info about command and caller mode 
   exit          - exit from request engine 
   setting / set - setting of engine [http/host/path]
   get / g       - get request engine
   post / p      - post request engine
   delete / d    - delete request engine
   put / P       - put request engine
   patch / pat   - patch request engine
   options/o     - options request engine
   head / h      - head request engine   
  """,'yellow'))
