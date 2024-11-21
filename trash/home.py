import tkinter as tk
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk  
from testing import create_chat_bot_frame

# Create the main window
root = tk.Tk()
root.title("Fix Waste")
# root.geometry("500x650")  # Set the size of the window
root.resizable(False, False)

# Set custom font
title_font = ("Arial", 20, "bold")
text_font = ("Arial", 14)

# Add the title
title_label = tk.Label(root, text="Waramly Welcome", font=title_font, fg="black")
title_label2 = tk.Label(root, text="Fix Waste", font=title_font, fg='#40DF4B')
title_label.pack()
title_label2.pack()

# Add the description
description = (
    "At Fix Waste, we specialize in innovative and sustainable waste "
    "management solutions.\nTogether, let's create a cleaner, greener future "
    "for generations to come."
)
desc_label = tk.Label(root, text=description, font=text_font, wraplength=400, justify="center", fg="gray")
desc_label.pack(pady=20)

# Add an image
try:
    image = Image.open('images/smarthome.png')
    image = image.resize((400, 400))
    image_tk = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error loading image: {e}")
    image_tk = None

# Create the Notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", pady=10)

# Create frames for each tab
home_frame = ttk.Frame(notebook)
chat_bot_frame = create_chat_bot_frame(notebook)
report_frame = ttk.Frame(notebook)

# Add frames to the Notebook
notebook.add(home_frame, text="Home")
notebook.add(chat_bot_frame, text="Chat Bot")
notebook.add(report_frame, text="Report")

# Add content to the Home tab
if image_tk:
    home_image_label = tk.Label(home_frame, image=image_tk)
    home_image_label.pack(pady=20)

home_text = tk.Label(
    home_frame, 
    text="Welcome to the Home tab!\nHere, you'll find general information.",
    font=text_font, 
    wraplength=400, 
    justify="center"
)
home_text.pack(pady=20)


# Add content to the Report tab
report_text = tk.Label(
    report_frame, 
    text="Welcome to the Report tab.\nView and manage reports here.",
    font=text_font, 
    wraplength=400, 
    justify="center"
)
report_text.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
