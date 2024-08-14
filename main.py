import tkinter
import ttkbootstrap as tkk

FONT = "Calibri 24 bold"


def compare():
    entry_1 = entry_1_str.get()
    entry_2 = entry_2_str.get()
    result = False
    if entry_1 == entry_2:
        result = True

    output_string.set("Same" if result else "not Same")


# window
window = tkk.Window(themename="darkly")
window.title("Compare")
window.geometry("500x200")


# title
title_label = tkk.Label(master=window, text="Compare", font=FONT)
title_label.pack()

# input fields
input_frame = tkinter.Frame(window)
entry_1_str = tkinter.StringVar()
entry_2_str = tkinter.StringVar()
entry = tkk.Entry(input_frame, textvariable=entry_1_str)
entry_2 = tkk.Entry(input_frame, textvariable=entry_2_str)
button = tkk.Button(input_frame, text="Vergleichen", command=compare)
entry.pack(padx=5, side="left")
entry_2.pack(padx=10, side="left")
button.pack(side="bottom")

input_frame.pack()


# output
output_string = tkinter.StringVar()
output_label = tkk.Label(window, text="Output", font="Calibri 24", textvariable=output_string)
output_label.pack(pady=5)

# run
window.mainloop()
