# -*- coding: utf-8 -*-
"""
 
@author: user
"""
from email.parser import BytesParser
class HTTP_Parser:
    
    def __init__(self):
        '''Constructor'''
        self.data = (
                  b'GET /who/ken/trust.html HTTP/1.1\r\n'
                  b'Host: cm.bell-labs.com\r\n'
                  b'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\r\n'
                  b'Accept: text/html;q=0.9,text/plain\r\n'
                  b'\n\n'
                  b'<html>\r\n'
                  b'    <body>\r\n'
   
                  b'       <h1>Hello, World!</h1>\r\n'
   
                  b'    </body>\r\n'
                  b'</html>\r\n'
             )
        self.req_line=""
        self.headers={}
        
        
    
    def parse_request_line(self):
        '''Method to parse request line'''
        request_line, headers_alone, = self.data.split(b'\r\n', 1)
        req_line = BytesParser().parsebytes(request_line)
        self.req_line=str(req_line)
        method,path,rest = self.req_line.split(' ')
        print(req_line)
        print('Method:',method)
        print('Path:',path)
        print('Version:',rest)
        
    def parse_headers(self):
        '''Method to parse headers'''
        _, headers_alone = self.data.split(b'\r\n', 1)
        head,_=headers_alone.split(b'\n\n',1)
        header = BytesParser().parsebytes(head)
        self.headers=dict( header)
        print(header)
        print("Header_dict:",self.headers)
       
        
    def parse_body(self):
        '''Method to parse body'''
        _,body= self.data.split(b'\n\n',1)
        body_alone = BytesParser().parsebytes(body)
        print(body_alone)
        

if __name__=='__main__':
    http=HTTP_Parser()
    print("Request line:")
    http.parse_request_line()
    print("\n")
    print("Http headers:")
    http.parse_headers()
    print("\n")
    print("Http Body:")
    http.parse_body()

        
    