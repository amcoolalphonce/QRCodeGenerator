import qrcode

features = qrcode.QRCode(version=1, box_size=30, border = 3)
features.add_data('github.com/amcoolalphonce')
features.make(fit=True)
generated_image = features.make_image()
generated_image.save('image1.png')
