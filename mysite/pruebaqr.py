import pyqrcode

s="B01"

url= pyqrcode.create(s)

url.svg(s+".svg",scale = 10)
