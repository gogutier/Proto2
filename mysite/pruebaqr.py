import pyqrcode

s="Hola q tal"

url= pyqrcode.create(s)

url.svg("myqr.svg",scale = 8)
