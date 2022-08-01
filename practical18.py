f=open("C:\myfile.txt")
    file_data=f.read()
    f.close()

    print(file_data)
except FileNotFoundError:
     print("File Not exists")