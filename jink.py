import tkinter as tk
from tkinter import messagebox

def sort_words():
    input_text = entry.get()  # Get input from the user
    words = input_text.split('-')  # Split by hyphen
    words.sort()  # Sort the list of words
    sorted_text = '-'.join(words)  # Join the sorted list back with hyphens
    messagebox.showinfo("Sorted Words", sorted_text)  # Display the result

# Create the main window
root = tk.Tk()
root.title("Word Sorter")

# Configure grid layout
root.geometry("400x200")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

# Create and place the input label
label = tk.Label(root, text="Enter hyphen-separated words:")
label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Create and place the input entry
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Create and place the sort button
sort_button = tk.Button(root, text="Sort Words", command=sort_words)
sort_button.grid(row=1, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
