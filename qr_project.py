import qrcode
import webbrowser

website_url = "www.google.com"

qr = qrcode.QRCode(   #QRCode class
    version = 1,      #higher version = higher data storing capability
    error_correction = qrcode.constants.ERROR_CORRECT_L,   #higher version higher correction
    box_size = 20,            #size of qrcode box
    border = 2,               #white outer border size of qr code
)
qr.add_data(website_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("img.png")
