import pyqrcode 
from pyqrcode import QRCode 
  
s=input("enter url here")
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("QR.svg", scale = 8) 
print(url)