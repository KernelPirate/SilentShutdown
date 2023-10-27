import os
import tkinter as tk
import tkinter.messagebox as mb


def shutdown():
    ip = ip_entry.get()
    message = message_entry.get()
    confirm = mb.askyesno("Confirmation", f"Are you sure you want to shutdown {ip}?\n\nMessage: {message}")
    if confirm:
        os.system(f"shutdown /s /m \\\\{ip} /t 30 /c \"{message}\"")


def restart():
    ip = ip_entry.get()
    message = message_entry.get()
    confirm = mb.askyesno("Confirmation", f"Are you sure you want to restart {ip}?\n\nMessage: {message}")
    if confirm:
        os.system(f"shutdown /r /m \\\\{ip} /t 30 /c \"{message}\"")


def open_url():
    ip = ip_entry.get()
    url = url_entry.get()
    confirm = mb.askyesno("Confirmation", f"Are you sure you want to open {url} on {ip}?")
    if confirm:
        os.system(f"start http://{ip}:8000")


# GUI
root = tk.Tk()
root.title("Remote Shutdown/Restart/Open URL")
root.geometry("400x300")

ip_label = tk.Label(root, text="IP Address:")
ip_label.pack()
ip_entry = tk.Entry(root)
ip_entry.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()
message_entry = tk.Entry(root)
message_entry.pack()

shutdown_button = tk.Button(root, text="Shutdown", command=shutdown)
shutdown_button.pack()

restart_button = tk.Button(root, text="Restart", command=restart)
restart_button.pack()

url_label = tk.Label(root, text="URL:")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

open_url_button = tk.Button(root, text="Open URL", command=open_url)
open_url_button.pack()

root.mainloop()
