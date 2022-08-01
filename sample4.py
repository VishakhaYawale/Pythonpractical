"""
str1="Hello"
str2="Devesh"

#str3=" ".join([str1,str2])

#print("%s %s "%(str1,str2))

#print("{} {} ".format(str1,str2)
#str3="{} {}".format(str1,str2)

str3=str1+str2
print(str3)
"""
#__main__
try:
    f1=open("C:\python_programs\sam.txt","r")
    f2=open("C:\python_programs\copy.txt","w")
    list_obj=f1.readlines()
    f1.close()

    f2.writelines(list_obj)
    f2.close()
    print("File Copied")
except FileNotFoundError:
    print("File not exists")

    #end of try
    #end of __main__