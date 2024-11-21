import tkinter as tk
from tkinter import scrolledtext
import threading
from chat import chatRequest
from PIL import Image, ImageTk
from tkinter.font import Font
from ttkbootstrap import ttk
from ttkbootstrap.dialogs import Messagebox
from report import showReport
from report import recycleReward

def reportNow():
    user_name_entry.delete(0, 'end')
    user_phone_entry.delete(0, 'end')
    location_code_entry.delete(0, 'end')
    Messagebox.show_info(title='Report Status', message='Record Successfully', alert=True)


root = tk.Tk()
root.title("Fix Waste")
root.geometry("600x900")
root.configure(bg="white")

notebook = ttk.Notebook(root, bootstyle='success')
notebook.pack(expand=True, fill=tk.BOTH, pady=10)

# --- Home Frame ---
home_frame = ttk.Frame(notebook)
notebook.add(home_frame, text="Home")

# Add content to the Home Frame
title_font = ("Arial", 20, "bold")
text_font = ("Arial", 14)

title_label = ttk.Label(home_frame, text='Innovation for sustainable living', font=title_font, bootstyle='dark')
title_label.pack(pady=10)


description = (
    "At Fix Waste, we specialize in innovative and sustainable waste management solutions.\n"
    "Together, let's create a cleaner, greener future for generations to come"
)
desc_label = tk.Label(home_frame, text=description, font=text_font, wraplength=400, justify="center", fg="gray")
desc_label.pack(pady=15)

try:
    image = Image.open('images/smarthome.png')
    image = image.resize((400, 400))
    image_tk = ImageTk.PhotoImage(image)

    image_label = tk.Label(home_frame, image=image_tk)
    image_label.image = image_tk  
    image_label.pack(pady=20)
except Exception as e:
    print(f"Error loading image: {e}")

# top level button
all_report_btn = ttk.Button(home_frame, text='All reports', command=showReport)
all_report_btn.place(x=150, y=600)

recycle_rewards = ttk.Button(home_frame, text='Recyle rewards', command=recycleReward)
recycle_rewards.place(x=400, y=600)


# --- Chat Bot Frame ---
chat_bot_frame = ttk.Frame(notebook)
notebook.add(chat_bot_frame, text="Chat Bot")

# Chatbot functionality
def handle_input():
    def fetch_response():
        user_input = user_entry.get().strip()
        if user_input:
            response_label.config(text="Processing your request...")
            try:
                response = chatRequest(user_input)
                text_area.configure(state='normal')
                text_area.insert(tk.END, f"You: {user_input}\n \n")
                text_area.insert(tk.END, f"Bot: {response}\n\n")
                text_area.configure(state='disabled')
                text_area.see(tk.END)
                response_label.config(text="Response received.")
            except Exception as e:
                response_label.config(text=f"Error: {str(e)}")
            user_entry.delete(0, tk.END)
        else:
            response_label.config(text="Please enter a valid input.")
    threading.Thread(target=fetch_response).start()

# Create a scrollable text widget for the conversation display
text_area = scrolledtext.ScrolledText(chat_bot_frame, wrap=tk.WORD, font=("Courier", 18), fg="black", bg="white")
text_area.configure(state='disabled')
text_area.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

# User entry widget
user_entry = tk.Entry(chat_bot_frame, font=("Helvetica", 12), fg="#1e1e1e", width=40)
user_entry.pack(pady=10)

# Response label
response_label = tk.Label(chat_bot_frame, text="", font=("Helvetica", 10), fg='white', bg='black')
response_label.pack()

# Button frame
button_frame = tk.Frame(chat_bot_frame)
button_frame.pack(pady=10)

speak_button = ttk.Button(button_frame, text="Ask AI", command=handle_input, bootstyle='success')
speak_button.grid(row=0, column=0, padx=5)

clear_button = ttk.Button(button_frame, text="Clear Response", command=lambda: text_area.configure(state='normal') or text_area.delete('1.0', tk.END) or text_area.configure(state='disabled'))
clear_button.grid(row=0, column=1, padx=5)


# report frame
report_frame = ttk.Frame(notebook)
notebook.add(report_frame, text='Report')

entry_font = Font(family='Helvetica', size=16)

get_logo = Image.open('images/report.png').resize((250, 250), Image.Resampling.LANCZOS)
mc_logo = ImageTk.PhotoImage(get_logo)

ttk.Label(report_frame, image=mc_logo).pack()
title = ttk.Label(report_frame, text='Report or disscus local problem', font=('Helvetica', 24, 'bold'))
title.pack(pady=5)

user_name = ttk.Label(report_frame, text='Name')
user_name.pack(anchor='nw', padx=50, pady=5)
user_name_entry = ttk.Entry(report_frame, width=30)
user_name_entry.pack(anchor='nw', padx=50, pady=5)

user_phone = ttk.Label(report_frame, text='Phone')
user_phone.pack(anchor='nw', padx=50, pady=5)
user_phone_entry = ttk.Entry(report_frame, width=30)
user_phone_entry.pack(anchor='nw', padx=50, pady=5)

location_code = ttk.Label(report_frame, text='Location Code')
location_code.pack(anchor='nw', padx=50, pady=5)
location_code_entry = ttk.Entry(report_frame, width=30)
location_code_entry.pack(anchor='nw', padx=50, pady=5)

categroy = ttk.Label(report_frame, text='Choose Categroy')
categroy.pack(anchor='nw', padx=50, pady=5)

wastes = []
variable = tk.StringVar()
waste_type= open('wastes.txt')

for waste in waste_type:
    waste = waste.rstrip('\n')
    wastes.append(waste)
variable.set(wastes[0])

waste_type = ttk.OptionMenu(
    report_frame,
    variable,
    wastes[0],
    *wastes,
    bootstyle='dark',
)

waste_type.pack(anchor='nw', padx=50, pady=5)
waste_type.configure(width=26)

# Report Status
report = ttk.Label(report_frame, text='Report Status')
report.pack(anchor='nw', padx=50, pady=5)
report_list = ['Open', 'NotFixed']
report_var = tk.StringVar()

report_watste = ttk.OptionMenu(
    report_frame,
    report_var,
    report_list[0],
    *report_list,
    bootstyle='dark'
)
report_watste.pack(anchor='nw', padx=50, pady=5)
report_watste.configure(width=26)

report_btn = ttk.Button(report_frame, text='Report Now', bootstyle='success', command=reportNow)

report_btn.pack(anchor='nw', padx=150, pady=5)


# Start the Tkinter main loop
root.mainloop()
