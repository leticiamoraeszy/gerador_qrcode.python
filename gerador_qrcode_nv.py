import qrcode

class Gerar:
    def msg(self):
        data = "https://drive.google.com/file/d/1BM0nQPihR4tF4T3fTPtY8gOFquXP205K/view?usp=sharing"
        qr = qrcode.QRCode()
        qr.add_data(data)
        qr.make()
        img = qr.make_image()
        img.save('qrcode.png')
        
a = Gerar()
a.msg()

        
