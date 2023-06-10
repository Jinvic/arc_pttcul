import urllib.parse

enc_st=input()
dec_st = urllib.parse.unquote(enc_st)
print(dec_st)