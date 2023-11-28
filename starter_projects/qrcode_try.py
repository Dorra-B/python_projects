import qrcode

img = qrcode.make('Some data here')
img.save("somefile.png")
type(img)