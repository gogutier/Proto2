import pyqrcode

#s=("ROLL1A","ROLL1B","ROLL2A","ROLL2B","ROLL3A","ROLL3B","ROLL4A","ROLL4B","ROLL5A","ROLL5B")
s=("ZPASILLO","ZPICADO","ZPNC","FFG","FFW","DRO","TCY","HCR","WRD","DIM")
for a in s:
    url= pyqrcode.create(a)

    url.svg(a+".svg",scale = 5)
