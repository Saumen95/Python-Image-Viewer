from PIL import Image, ImageTk


def Tk_image(path, w, h):
    img = Image(path)
    img = img.resize((w, h))
    storeobj = ImageTk.PhotoImage(img)
    return storeobj
