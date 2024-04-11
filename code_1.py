import requests
from bs4 import BeautifulSoup
urls = ["https://krittikaiitb.github.io"]
lis = set()
visited=set()
while(len(urls)!=0):
    #print(urls)
    url = urls.pop()
    visited.add(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.content,"html.parser")
    elements = soup.select("a[href]")
    elem = soup.select("a[src]")
    for j in elements:
        u = j['href']
        if u=='/':
            continue
        if u[0]=='/':
            u="https://krittikaiitb.github.io"+u
            if u not in visited and u not in urls:
                if ".pdf" not in u:
                    urls.append(u)
        lis.add(u)
    for j in elem:
        u = j['src']
        urls.append(u)
        if u=='/':
            continue 
        if u[0]=='/':
            u="https://krittikaiitb.github.io"+u
            if u not in visited and u not in urls:
                if ".pdf" not in u:
                    urls.append(u)
        lis.add(u)
#print(lis)
f = open('links.txt','w')
for h in lis:
    if h=='#':
        continue
    f.write(h)
    f.write('\n')
