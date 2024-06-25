import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk  # Import ImageTk here
import os


def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img = img.convert("RGBA")
        img_tk = ImageTk.PhotoImage(img)
        lbl_image.config(image=img_tk)
        lbl_image.image = img_tk
        lbl_image.file_path = file_path


def add_watermark():
    if not hasattr(lbl_image, 'file_path'):
        messagebox.showwarning("Warning", "Please upload an image first")
        return

    watermark_text = entry_watermark.get()
    if not watermark_text:
        messagebox.showwarning("Warning", "Please enter a watermark text")
        return

    original = Image.open(lbl_image.file_path).convert("RGBA")
    txt = Image.new("RGBA", original.size, (255, 255, 255, 0))

    font = ImageFont.truetype("arial.ttf", 40)
    draw = ImageDraw.Draw(txt)

    width, height = original.size
    textwidth, textheight = draw.textsize(watermark_text, font)

    x = width - textwidth - 10
    y = height - textheight - 10

    draw.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)
    watermarked = Image.alpha_composite(original, txt)

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[
                                             ("PNG files", "*.png"), ("All files", "*.*")])
    if save_path:
        watermarked.convert("RGB").save(save_path)
        messagebox.showinfo("Info", f"Watermarked image saved as {
                            os.path.basename(save_path)}")


# Create main application window
root = tk.Tk()
root.title("Watermark Application")

# Create and place widgets
lbl_image = tk.Label(root)
lbl_image.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

btn_upload = tk.Button(root, text="Upload Image", command=upload_image)
btn_upload.grid(row=1, column=0, padx=10, pady=10)

entry_watermark = tk.Entry(root, width=30)
entry_watermark.grid(row=2, column=0, padx=10, pady=10)
entry_watermark.insert(0, "Enter watermark text")

btn_add_watermark = tk.Button(
    root, text="Add Watermark", command=add_watermark)
btn_add_watermark.grid(row=2, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
