import pyqrcode

#s=("ROLL1A","ROLL1B","ROLL2A","ROLL2B","ROLL3A","ROLL3B","ROLL4A","ROLL4B","ROLL5A","ROLL5B")
s=("E01","E02","E03","E04","C09","C10","C11","C12","C13")
for a in s:
    url= pyqrcode.create(a)

    url.svg("QRcodes/"+a+".svg",scale = 10)
