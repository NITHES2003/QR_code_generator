import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qrcode():
    text = text_entry.get()
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "White")
    img.show() 

window = tk.Tk()
window.title("QR code generator")
text_label = tk.Label(window, text="Enter a the link: ")
text_label.pack()
text_entry = tk.Entry(window, width=50)
text_entry.pack()
button = tk.Button(window, text="Generate QR", command=generate_qrcode)
button.pack()
window.mainloop()


