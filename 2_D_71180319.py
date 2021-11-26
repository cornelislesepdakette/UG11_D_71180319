string=input("Masukkan sebuah kata/kalimat: ")
sisip=input("Masukkan karakter yang ingin disisipkan: ")

def sisipHuruf(string,sisip):
    kapital=string.upper()
    print(sisip.join(list(kapital)))
def sisipKata(string,sisip):
    kapital=string.title()
    print(sisip.join(kapital.split()))

sisipHuruf(string,sisip)
sisipKata(string,sisip)