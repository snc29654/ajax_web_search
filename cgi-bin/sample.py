import cgi
import cgitb
import json
import sys
import io
import requests
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

zip_code=[]

def  data_print(url):
    global zip_code

    params = {'p':zip_code,
          'search.x':'1',
          'fr':'top_ga1_sa',
          'tid':'top_ga1_sa',
          'ei':'UTF-8',
          'aq':'',
          'oq':'',
          'afs':'',}

    r = requests.get(url, params=params)

    data = BeautifulSoup(r.content, 'html.parser')
    return(data)



cgitb.enable()
form=cgi.FieldStorage()
zip_code=form.getvalue("sent2")

find_data=data_print("http://search.yahoo.co.jp/search")




print("Content-type: text/html\n")
print(find_data)
