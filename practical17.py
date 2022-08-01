a=[1,2,3]
try:
    print("Second element=%d"%(a[1]))
    print("Fourth element=%d"%(a[3]))
except IndexError:
    print("An error occured")


print("\n Second Program")
a=[1,2,3]
try:
    print("Second element=%d"%(a[1]))
    print("Fourth element=%d"%(a[3]))
except(AttributeError,TypeError)as e:
    print("An errror occured:",e)