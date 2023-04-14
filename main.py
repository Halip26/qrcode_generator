import qrcode
from datetime import datetime

print("Input your URL to Generate the QRCode.. ") 
input_URL = str(input(": "))

QR = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

QR.add_data(input_URL)
QR.make(fit=True)

img = QR.make_image(fill_color="black", back_color="white")
img.save('output/url_qrcode-%s.png'%datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

print(QR.data_list)