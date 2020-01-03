import pyqrcode

#s=("ROLL1A","ROLL1B","ROLL2A","ROLL2B","ROLL3A","ROLL3B","ROLL4A","ROLL4B","ROLL5A","ROLL5B")
s=("D01","PTCAL")
for a in s:
    url= pyqrcode.create(a)

    url.svg("QRcodes/"+a+".svg",scale = 20)
