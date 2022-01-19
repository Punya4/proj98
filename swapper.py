def custom():
    textInfile1=input("Enter file name 1 : ")
    textInfile2=input("Enter file name 2 : ")
    a= open(textInfile1,'r')
    b= open(textInfile2,'r')
    data_a=a.read()
    data_b=b.read()
    a=open(textInfile1,'w')
    b=open(textInfile2,'w')
    a.write(data_b)
    b.write(data_a)

custom()