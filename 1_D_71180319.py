string=input("Masukkan string: ")

def cekString(string):
    if string.isdigit():
        bil=int(string)
        if bil%2==0:
            bil=int(bil/2)
            print(bil)
        else:
            bil=int((bil+5)/2)
            print(bil)
    else:
       str=str[::-1]
       print(string)
cekString(string)