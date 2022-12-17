import qrcode
from PIL import Image
link=input("Enter Your Link: ")
name=input("Enter name of the file for save: ")
c1=input("Enter color of code: ")
c2=input("Enter code's backgroung color: ")
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data(f'{link}')
qr.make(fit=True)
img=qr.make_image(fill_color=(f'{c1}'),back_color=(f'{c2}'))
img.save(f'{name}.png')
