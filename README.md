# r_man
Manual Request Engine For Termux / Linux / Windows 


# Installation
#### $ git clone https://github.com/m00nisSmiling/r_man.git
#### $ cd r_man
#### $ python requirements.py
#### $ python man.py

# Usage 
#### - Easily specify http/host/path/
#### - In [engine] : you can write your request method name [ options/head/get/put/patch/post/delete ]
#### - You can manually specify your [ headers:values, parameters:values, request data in json ]

# Engine Commands
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
