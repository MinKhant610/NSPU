import tkinter as tk
from ttkbootstrap import ttk
from PIL import Image
from PIL import ImageTk
from ttkbootstrap.dialogs import Messagebox

def showReport():
    report_window = tk.Toplevel()
    report_window.title("Report")

    get_img = Image.open('images/waste.jpg')
    img = ImageTk.PhotoImage(get_img)

    label = ttk.Label(report_window, image=img)
    label.image = img  
    label.pack()


def recycleReward():
    choices = {
        "plastic": 0,
        "paper": 0,
        "glass": 0,
        "aluminum": 0
    }

    def update_choice(item, weight):
        choices[item] += weight
        Messagebox.show_info(title='Recycle Status', message=f'You saved {weight}kg of {item}!')
        Messagebox.show_info(title='Reward Status', message=f'You can withdraw {weight*10} kyats')

    report_window = tk.Toplevel()
    report_window.title("Recycle Reward")

    recycle_frame = ttk.Labelframe(report_window, text='Choose Recycle Items', bootstyle='dark')
    recycle_frame.grid(row=0, column=0, pady=10, padx=10)

    plastic_btn = ttk.Button(recycle_frame, 
        text='Plastic Bottle (0.3kg)',
        command=lambda: update_choice('plastic', 0.3)
    )
    plastic_btn.grid(row=0, column=0, pady=10, padx=10)

    paper_btn = ttk.Button(recycle_frame, 
        text='Paper (0.1kg)',
        command=lambda: update_choice('paper', 0.1)
    )
    paper_btn.grid(row=0, column=1, pady=10, padx=10)

    glass_btn = ttk.Button(recycle_frame, 
        text='Glass Bottle (0.5kg)',
        command=lambda: update_choice('glass', 0.5)
    )
    glass_btn.grid(row=1, column=0, pady=10, padx=10)

    aluminum_btn = ttk.Button(recycle_frame, 
        text='Aluminum Can (0.2kg)',
        command=lambda: update_choice('aluminum', 0.2)
    )
    aluminum_btn.grid(row=1, column=1, pady=10, padx=10)

    report_window.mainloop()


