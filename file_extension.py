myDict={
    "py":"Python",
    "java":"Java",
    "c":"C",
    "txt":"Text"}
fname= input("Enter the file name: ")
n=fname.split(".")
op=myDict[n[-1]]
print("the file extention is: "+op)
