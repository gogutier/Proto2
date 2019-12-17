import pyqrcode

#s=("ROLL1A","ROLL1B","ROLL2A","ROLL2B","ROLL3A","ROLL3B","ROLL4A","ROLL4B","ROLL5A","ROLL5B")
s=("AN1","AN2","AN3","AN4","AN5","AN6","AN7")
for a in s:
    url= pyqrcode.create(a)

    url.svg("QRcodes/"+a+".svg",scale = 7)
