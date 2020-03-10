def srr():
    stroka = input("Введите слово : ")
    word=stroka.split()
    long=0
    for i in range(len(word)):
        if len(word[long])<len(word[i]):
            long= i
        return(word[long])
print(srr())