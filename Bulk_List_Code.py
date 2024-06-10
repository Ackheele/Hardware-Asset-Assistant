import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
from tkinter import filedialog 

def add_asset(event=None):
    new_asset = asset_entry.get()
    if new_asset:  # Make sure the asset is not empty
        if len(new_asset) < 6:
            messagebox.showerror("Error", "String length must be at least 7 characters. Please edit the string.")
        else:
            # Split the entered string at "M" inclusively
            split_assets = []
            current_asset = ""
            for char in new_asset:
                if char == "M" and current_asset:
                    split_assets.append(current_asset)
                    current_asset = "M"
                else:
                    current_asset += char
            if current_asset:
                split_assets.append(current_asset)

            for asset in split_assets:
                asset_list.append(asset)
                display_area.insert(tk.END, asset + '\n')
    asset_entry.delete(0, tk.END)  # Clear the input field

def display_asset():
    final_str = ' "OR" '.join(asset_list)
    final_display_area.insert(tk.END, final_str + '\n')
    save_status.config(text="Bulk List Generated")

def copy_to_clipboard():
    final_str = ' "OR" '.join(asset_list)
    root.clipboard_clear()  # Clear clipboard contents
    root.clipboard_append(final_str)  # Append new text to clipboard
    save_status.config(text="Bulk List copied to clipboard!")

def save_to_file():
    # Open a file save dialog to get the file path where the user wants to save the file
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Save"
    )
    # Check if a file path was provided (i.e., the user did not cancel the dialog)
    if filepath:
        final_str = ' "OR" '.join(asset_list)
        with open(filepath, 'w') as file:
            file.write(final_str)
        save_status.config(text=f"Saved to {os.path.basename(filepath)}")
    else:
        save_status.config(text="Save cancelled.")

def clear_fields():
    global asset_list
    asset_list = []  # Reset the asset list
    asset_entry.delete(0, tk.END)  # Clear the entry widget
    display_area.delete('1.0', tk.END)  # Clear the main display area
    final_display_area.delete('1.0', tk.END)  # Clear the final display area
    save_status.config(text="All fields cleared!")  # Update the status label

def main():
    global root, asset_entry, display_area, final_display_area, save_status, asset_list
    root = tk.Tk()
    root.title("Bulk List Generator")

    asset_list = []

    # Entry widget to input assets
    asset_entry = tk.Entry(root, width=50)
    asset_entry.pack(pady=10)
    asset_entry.bind("<Return>", add_asset)

    # Button to add assets
    add_button = tk.Button(root, text="Add Asset", command=add_asset)
    add_button.pack(pady=5)

    # ScrolledText widget to display the assets
    display_area = scrolledtext.ScrolledText(root, width=60, height=10)
    display_area.pack(pady=10)

    # Button to generate list
    generate_button = tk.Button(root, text="Generate Bulk List", command=display_asset)
    generate_button.pack(pady=5)

    # Button to copy assets to clipboard
    copy_button = tk.Button(root, text="Copy Assets to Clipboard", command=copy_to_clipboard)
    copy_button.pack(pady=5)

    # Button to save file
    save_file_button = tk.Button(root, text="Save", command=save_to_file)
    save_file_button.pack(pady=5)

    # Button to clear fields
    clear_button = tk.Button(root, text="Clear", command=clear_fields)
    clear_button.pack(pady=5)

    # Label to show save status
    save_status = tk.Label(root, text="", fg="green")
    save_status.pack(pady=5)

    # ScrolledText widget to display new string
    final_display_area = scrolledtext.ScrolledText(root, width=60, height=10)
    final_display_area.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
