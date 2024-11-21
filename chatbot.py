import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from chat import chatRequest

# Create the main application window
root = tk.Tk()
root.title("NSPT Bot")
style = ttk.Style()
style.theme_use('default')
root.geometry("500x600")
root.configure(bg="white")  

def handle_input():
    user_input = user_entry.get()
    if user_input.strip():
        response_label.config(text="Processing your request...")
        user_entry.delete(0, tk.END)
    else:
        response_label.config(text="Please enter a valid input.")

# Create a scrollable text widget for the meal plan display
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 10), fg="white", bg="gray")
# text_area.insert(tk.END, chatRequest(user_entry.get()))
text_area.configure(state='disabled')  
text_area.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)


user_entry = tk.Entry(root, font=("Helvetica", 12), fg="#1e1e1e", width=40)

user_entry.pack(pady=10)

if user_entry.get() == '':
    pass 
else:
    response_text = chatRequest(user_entry.get())
    if response_text:
        print('success')
        text_area.insert(tk.END, chatRequest(chat_text))

# Create a response label
response_label = tk.Label(root, text="", font=("Helvetica", 10), fg="#1e1e1e", bg="white")
response_label.pack()


button_frame = tk.Frame(root, bg='white')
button_frame.pack(pady=10)

speak_button = ttk.Button(button_frame, text="Speak To NSPU", command=handle_input)
speak_button.grid(row=0, column=0, padx=5)

clear_button = ttk.Button(button_frame, text="Clear Response", command=lambda: response_label.config(text=""))
clear_button.grid(row=0, column=1, padx=5)

root.mainloop()
