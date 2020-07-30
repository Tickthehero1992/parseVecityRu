from bs4 import BeautifulSoup
import requests as req

url_site_main="https://auto.vercity.ru/catalog/auto/"
url_default="https://auto.vercity.ru"

def delete_all_from_text(text):
    st_out=""
    for c in text:
        if c not in ['\n','\t','\r']:
            st_out=st_out+c
    ss=st_out.split(' ')
    st_out=""

    for s in ss:
        if s!='':
           st_out=st_out+s+' '
    if st_out[-1]==' ':
        return st_out[:-1]
    else:
        return st_out


def Parse_main(url,class_name='sections_letter-brands'):
    resp=req.get(url,verify=False)
    #print(resp.content)
    soup=BeautifulSoup(resp.content, 'html.parser')
    list_marks=soup.find_all('ul',{'class':class_name})
    result=[]
    for l_m in list_marks:
        result.extend(l_m.find_all('a'))
    Names=[]
    Refs=[]
    for r in result:
        p=str(r)
        soup2=BeautifulSoup(p,'xml')
        Names.append(delete_all_from_text(soup2.text))
        Refs.append(soup2.a['href'])

    return Names, Refs

def Parse_model(url,Name=None,path_out=None):
    #resp = req.get(url_default+url, verify=False)
    #soup = BeautifulSoup(resp.content, 'html.parser')
    #list_models=soup.find_all('ul',{'class':'page_model-ranges'})
    #fl=open(path_out,mode='a',encoding='utf8')
    print(Parse_main(url,'page_model-ranges'))


print(Parse_main(url_site_main))
print(Parse_model('https://auto.vercity.ru/catalog/auto/avanti/'))