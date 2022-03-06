
from tkinter import filedialog


# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("png files","*.png*"),("jpg files","*jpg")))
    return filename


print(browseFiles())
