import tkinter as tk
from threading import Thread
from voice_assistant import conversation  

def send_message():
    user_msg = entry.get()
    if not user_msg.strip():
        return
    chat_box.insert(tk.END, f"You: {user_msg}")
    entry.delete(0, tk.END)

    def get_response():
        try:
            # Replacing this with actual Elevenlabs call if different callback
            response = conversation.send_message(user_msg)
            chat_box.insert(tk.END, f"AI: {response}")
        except Exception as e:
            chat_box.insert(tk.END, f"Error: {str(e)}")

    Thread(target=get_response).start()  # running the thread

# Create Tkinter window
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("600x500")

chat_box = tk.Listbox(root, width=80, height=25)
chat_box.pack(padx=10, pady=10)

entry = tk.Entry(root, width=60)
entry.pack(side=tk.LEFT, padx=10)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(side=tk.RIGHT, padx=10)

root.mainloop()
