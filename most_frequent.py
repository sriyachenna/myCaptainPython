str=input()
def most_frequent(str):
    s1=set(str)
    d1={}
    s={}
    for x in s1:
        d1[x]=str.count(x)
    s = dict( sorted(d1.items(),key=lambda item: item[1],reverse=True))
    for i in s:
        print(i,"=",s[i],end=" ")
most_frequent(str.lower())
