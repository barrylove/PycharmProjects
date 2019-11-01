def wordNum():
    file = open("e:/test.txt","r")
    result = open("e:/result.txt","w")
    content = file.read()
    for i in range(0,len(content)):
        word = ""
        if content[i] != " ":
            word = word + content[i]
        else
            
            word =""