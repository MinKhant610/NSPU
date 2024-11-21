import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
from chat import chatRequest  # Ensure this imports correctly

# Create the main application window
root = tk.Tk()
root.title("NSPT Bot")
style = ttk.Style()
style.theme_use('default')
root.geometry("500x600")
root.configure(bg="white")

def handle_input():
    def fetch_response():
        user_input = user_entry.get().strip()
        if user_input:
            response_label.config(text="Processing your request...")
            try:
                response = chatRequest(user_input)
                text_area.configure(state='normal')
                text_area.insert(tk.END, f"You: {user_input}\n")
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
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 10), fg="white", bg="gray")
text_area.configure(state='disabled')
text_area.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

# Create the user entry widget
user_entry = tk.Entry(root, font=("Helvetica", 12), fg="#1e1e1e", width=40)
user_entry.pack(pady=10)

# Create a response label
response_label = tk.Label(root, text="", font=("Helvetica", 10), fg="#1e1e1e", bg="white")
response_label.pack()

# Create button frame
button_frame = tk.Frame(root, bg='white')
button_frame.pack(pady=10)

speak_button = ttk.Button(button_frame, text="Speak To NSPU", command=handle_input)
speak_button.grid(row=0, column=0, padx=5)

clear_button = ttk.Button(button_frame, text="Clear Response", command=lambda: text_area.configure(state='normal') or text_area.delete('1.0', tk.END) or text_area.configure(state='disabled'))
clear_button.grid(row=0, column=1, padx=5)

root.mainloop()
