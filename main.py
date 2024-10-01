import qrcode
from datetime import datetime

print("Input your URL link to Generate the QRCode.. ")
# for example : https://blog-halip26.thedev.id/
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
img.save("output/url_qrcode-%s.png" % datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

# another alternatif
# img.save('url_qrcode.png')

print("The URL link: ", QR.data_list)
