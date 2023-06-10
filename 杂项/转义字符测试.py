# https://www.jianshu.com/p/17ae5776826f

import urllib.parse
import html
import base64

# URL编码
st = '字符'
enc_st = urllib.parse.quote(st)
print(enc_st)

enc_st = r'%E5%AD%97%E7%AC%A6'
dec_st = urllib.parse.unquote(enc_st)
print(dec_st)

# Unicode转义

enc_st = r'&#20170;&#22825;'
dec_st = html.unescape(enc_st)
print(dec_st)

#UTF-8编码
s = '\u4eca\u5929'
print(s)

# base64编码
str = '字符'
bytesStr = str.encode(encoding='utf-8')
b64str = base64.b64encode(bytesStr)
print(b64str)

# dec_str=base64.b64decode(b64str)
# print(dec_str)