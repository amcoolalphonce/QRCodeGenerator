import qrcode

features = qrcode.QRCode(version=1, box_size=30, border = 3)
features.add_data('github.com/amcoolalphonce')
features.make(fit=True)
generated_image = features.make_image(fill_color = "red",back_color ="white")
generated_image.save('image4.png')
