from bs4 import BeautifulSoup
import requests as req

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

url_site="https://promoycar.ru/lichnyj-kabinet-footer/modeli-ts-i-kategorii.html"
path='VecityRu.txt'
def parseCarmoy(url):
    resp=req.get(url,verify=False)
    soup = BeautifulSoup(resp.content, 'html.parser')
    table=soup.find_all('tr')
    result=[]
    result.extend(table)
    print(result[7])

def openFile(path,path_out):
    fl=open(path, mode='r',encoding='utf8')
    st=""
    for line in fl.readlines():
        st=st+line
    #return st
    soup=BeautifulSoup(st,'xml')
    tables_marks=soup.find_all('td',{'class':'li4'})
    tables_models=soup.find_all('td',{'class':'li2'})
    #print(tables_models)
    marks=[]
    models=[]
    for mark in tables_marks:
        marks.append(delete_all_from_text(mark.text))
    for model in tables_models:
        models.append(delete_all_from_text(model.text))
    fl.close()
    out_fl=open(path_out, mode='w', encoding='utf8')
    out_fl.write('name;model;\n')
    for i in range(len(marks)):
        out_fl.write(marks[i]+';'+models[i]+';\n')
    out_fl.close()

    #print(marks)

openFile(path,"Table.csv")
#parseCarmoy(url_site)

