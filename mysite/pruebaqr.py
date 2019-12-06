import pyqrcode

#s=("ROLL1A","ROLL1B","ROLL2A","ROLL2B","ROLL3A","ROLL3B","ROLL4A","ROLL4B","ROLL5A","ROLL5B")
s=("A01","A02","A03","A04","A05","A06","B01","B02","B03","B04","B05","B06","C01","C02","C03","C04","C05","C06","D01","D02","D03","D04","D05","D06")
for a in s:
    url= pyqrcode.create(a)

    url.svg(a+".svg",scale = 10)
