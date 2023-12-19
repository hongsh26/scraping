import requests
from bs4 import BeautifulSoup
import pyautogui

while(1):
    keyword=pyautogui.prompt("검색어를 입력하세요")
    if(keyword == None):
        break
    lastPage=pyautogui.prompt("마지막 페이지 번호를 입력해주세요")
    try:
        int(lastPage)
    except:
        break
    fileName=pyautogui.prompt("파일 이름을 입력해주세요")
    if(fileName.isalpha() == False):
        pyautogui.alert("다시하셈.")
        break
    permission=pyautogui.confirm("만일 파일이 이미 존재한다면 기존 내용에 덮어씁니다.",buttons=["확인","취소"])
    f=open("{}.txt".format(fileName),'w')
    f.close()
    pageNum=1
    if(permission == "취소"):
        break
    output=[]
    count=1
    for i in range(1,int(lastPage)*10,10):
        print(f"{pageNum}페이지 입니다.================================")
        response=requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}") #keyword위치에 검색어 들어감 i는 페이지
        html=response.text
        soup=BeautifulSoup(html,'html.parser')
        links=soup.select(".news_tit")  #결과는 리스트
        for link in links:
            title=link.text  #태그 안에 텍스트요소를 가져온다
            url=link.attrs['href']  #href의 속성값(attrs)을 가져온다
            output.append(str(count)+'번째: '+title+''+url)
            count+=1
        pageNum+=1
    for link in output:
        f=open("{}.txt".format(fileName),'a')
        f.write(link+"\n")
        print(link)
    f.close()
    str=''
    f=open("{}.txt".format(fileName),'r')
    for i in range(int(lastPage)*10):
        content=f.readline()
        str+=content
    f.close()
    pyautogui.alert("가져올 정보를 골라주세요!")
    pyautogui.alert(str)
    num=pyautogui.prompt("가져올 번호를 입력해주세요.\n 예시:1,2,5")
    index_num=num.split(",")
    result=[]
    for i in index_num:
        result.append(output[int(i)-1])
    f=open("{}.txt".format(fileName),'w')
    f.close()
    f=open("{}.txt".format(fileName),'a')
    for i in result:
        f.write(i+"\n")
    f.close()
    break