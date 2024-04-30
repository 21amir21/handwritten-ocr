# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk


# def browse_file():
#     filename = filedialog.askopenfilename(
#         filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")]
#     )
#     if filename:
#         display_image(filename)


# def display_image(filename):
#     image = Image.open(filename)
#     image.thumbnail((500, 500))  # Resize image to fit in the window
#     photo = ImageTk.PhotoImage(image)

#     # Create a new window to display the image
#     window = tk.Toplevel(root)
#     window.title("Selected Photo")

#     # Display the image in a label
#     label = tk.Label(window, image=photo)
#     label.image = photo  # Keep a reference to the image to prevent garbage collection
#     label.pack()

#     # Add an empty text field below the image
#     text_entry = tk.Entry(window)
#     text_entry.pack(pady=10)


# # Create the main application window
# root = tk.Tk()
# root.title("Photo Browser")
# root.geometry("600x400")  # Set initial window size

# # Create a button to browse for a photo
# browse_button = tk.Button(root, text="Browse Photo", command=browse_file)
# browse_button.pack(pady=10)

# # Start the Tkinter event loop
# root.mainloop()

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def browse_file():
    filename = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")]
    )
    if filename:
        display_image(filename)


def display_image(filename):
    image = Image.open(filename)
    image.thumbnail((500, 500))  # Resize image to fit in the window
    photo = ImageTk.PhotoImage(image)

    # Display the image in a label
    label.config(image=photo)
    label.image = photo  # Keep a reference to the image to prevent garbage collection

    # Clear the text field
    text_entry.delete(0, tk.END)


# Create the main application window
root = tk.Tk()
root.title("Photo Browser")
root.geometry("800x600")  # Set initial window size

# Create a button to browse for a photo
browse_button = tk.Button(root, text="Browse Photo", command=browse_file)
browse_button.pack(pady=10)

# Create a label to display the photo
label = tk.Label(root)
label.pack()

# Add an empty text field below the image
text_entry = tk.Entry(root)
text_entry.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
