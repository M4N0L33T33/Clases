import qrcode

data = 'https://github.com/M4N0L33T33/Clases'

img = qrcode.make(data)

img.save('C:\\Users\\manue\\Pictures\\myllinking_qr.png')

print("listo")