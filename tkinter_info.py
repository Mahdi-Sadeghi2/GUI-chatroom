import tkinter
from tkinter import BOTH, StringVar, END

# Define window
root = tkinter.Tk()
root.title("Let's stay in touch")
# Add icon for the aplication
root.iconbitmap("blue_talk.ico")
# Set size of the window app
root.geometry("400x600")
# Make app unresizeable
root.resizable(0, 0)

# Defince colors
root_color = "#535657"
input_color = "#4f646f"
output_color = "#EFF78A"
# Set background color
root.config(bg=root_color)


# Define functions
def send_message():
    """
      Send the users message to output frame

    """
    message_label = tkinter.Label(
        output_frame, text=message_entry.get(), fg=text_color.get(), bg=output_color, font=("Helvetica bold", 12))
    message_label.pack()

    # Clear the entry field for next message
    message_entry.delete(0, END)


# Define GUI layout
# Make input window
input_frame = tkinter.LabelFrame(root, bg=input_color)
# Make output window
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0, 10), fill=BOTH, expand=True)

# Define widgets/buttons
message_entry = tkinter.Entry(
    input_frame, text="Enter a message", width=30, font=("Helvetica bold", 12))
send_button = tkinter.Button(
    input_frame, text="Send", bg=output_color, command=send_message)
message_entry.grid(row=0, columnspan=3, column=0, padx=10, pady=10)
send_button.grid(row=0, column=3, rowspan=1,
                 padx=10, pady=10, ipadx=20, ipady=5)
text_color = StringVar()
text_color.set("#ff0000")
red_button = tkinter.Radiobutton(
    input_frame, text="Red", variable=text_color, value="#ff0000", bg=input_color)
green_button = tkinter.Radiobutton(
    input_frame, text="Green", variable=text_color, value="#09b303", bg=input_color)
blue_button = tkinter.Radiobutton(
    input_frame, text="Blue", variable=text_color, value="#158af8", bg=input_color)
red_button.grid(row=1, column=0)
green_button.grid(row=1, column=1)
blue_button.grid(row=1, column=2)

output_label = tkinter.Label(output_frame, text="--- Stored Messages ---",
                             fg=input_color, bg=output_color, font=("Helvetica bold", 18))
output_label.pack(pady=15)

# Run the root windows mainloop
root.mainloop()
