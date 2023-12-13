import qrcode

features = qrcode.QRCode(version=1, box_size=30, border = 3)
generated_image = qrcode.make("AmcoolGithub")
generated_image.save('image1.png')
