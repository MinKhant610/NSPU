import tkinter as tk
from tkinter import ttk, scrolledtext
from chat import chatRequest  # Import your chatbot logic

def create_chat_bot_frame(parent):
    chat_frame = ttk.Frame(parent)
    
    def handle_input():
        user_input = user_entry.get()
        if user_input.strip():
            response_label.config(text="Processing your request...")
            try:
                # Call the chatRequest function
                response_text = chatRequest(user_input)
                
                # Enable the text area to update the conversation
                text_area.configure(state='normal')
                text_area.insert(tk.END, f"You: {user_input}\n")
                text_area.insert(tk.END, f"Bot: {response_text}\n\n")
                text_area.configure(state='disabled')  # Lock it again
                
                # Clear the entry field
                user_entry.delete(0, tk.END)
                response_label.config(text="Response received.")
            except Exception as e:
                response_label.config(text=f"Error: {str(e)}")
        else:
            response_label.config(text="Please enter a valid input.")

    text_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, font=("Courier", 12), fg="white", bg="gray")
    text_area.configure(state='disabled')
    text_area.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

    # User entry widget
    user_entry = tk.Entry(chat_frame, font=("Helvetica", 12), fg="#1e1e1e", width=40)
    user_entry.pack(pady=10)

    # Response label
    response_label = tk.Label(chat_frame, text="", font=("Helvetica", 10), fg="#1e1e1e", bg="white")
    response_label.pack()

    # Button frame
    button_frame = tk.Frame(chat_frame, bg='white')
    button_frame.pack(pady=10)

    # Buttons
    speak_button = ttk.Button(button_frame, text="Speak To NSPU", command=handle_input)
    speak_button.grid(row=0, column=0, padx=5)

    clear_button = ttk.Button(button_frame, text="Clear Response", command=lambda: text_area.configure(state='normal') or text_area.delete('1.0', tk.END) or text_area.configure(state='disabled'))
    clear_button.grid(row=0, column=1, padx=5)

    return chat_frame
