import qrcode
image = qrcode.make('www.facebook.com')
image.save('qr.png', 'PNG')