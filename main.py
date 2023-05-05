from tkinter import *

dictionary = []
with open('words.txt', 'r') as file:
    for line in file.readlines():
        for word in line.split():
            dictionary.append(word)


def getTextInput():
    result = textExample.get("1.0", "end")
    a[0] = result


def str_to_ASC():
    word_length = len(a[0])
    word_given = a[0]
    for i in range(word_length-1):
        buff = word_given[i]
        asc_buff = ord(buff)
        # at this point we have decimal code of the word
        asc_binary = format(asc_buff, '08b')
        new = list(asc_binary)
        new += " 0"
        new.reverse()
        asc_binary = "".join(new)
        asc_binary += " 11 "
        char_table.append(asc_binary)


def ASC_to_str():
    for i in range(len(char_table)):
        word_buf = char_table[i]
        new = list(word_buf)
        new[0] = ""
        new[1] = ""
        new.reverse()
        for j in range(3):
            new[j] = ""
        binary = "".join(new)
        character = int(binary, 2)
        character = chr(character)
        decoded_message[0] += character


def show_decoded_ASC(new_window):
    czy = 0
    string_cover = ""
    for i in range(len(dictionary)):
        if decoded_message[0] == dictionary[i]:
            czy = 1
            length = len(decoded_message[0])
            for j in range(length):
                string_cover += "*"
    if czy == 0:
        label_send = Label(new_window, text="Word encoded:   " + decoded_message[0], fg="black")
    elif czy == 1:
        label_send = Label(new_window, text="Word encoded:   " + string_cover, fg="black")
    label_send.place(x=45, y=186)


def show_ASC(i):
    label_show_ASC = Label(text=char_table[i], fg="black")
    label_show_ASC.place(x=250, y=20+20*i)


def show_ASC_all():
    for i in range(len(char_table)):
        show_ASC(i)


def clear_message():
    for i in range(len(char_table)):
        label_show_ASC = Label(text="", fg="black", width=200)
        label_show_ASC.place(x=250, y=20 + 20 * i)
    char_table.clear()


def clear_ASC_message(new_window):
    decoded_message[0] = ""
    label_send = Label(new_window, text="", fg="black", width=200)
    label_send.place(x=135, y=186)


def open_window():
    new_window = Toplevel(root)
    new_window.geometry("420x250")
    new_window.title("Second window")

    label_1 = Label(new_window, text="Receiving information")
    label_1.pack()

    button_ASC_to_str = Button(new_window, text="Convert ASCII to string", command=lambda: ASC_to_str())
    button_ASC_to_str.place(x=45, y=36)

    button_str_show = Button(new_window, text="Show string", command=lambda: show_decoded_ASC(new_window))
    button_str_show.place(x=45, y=86)

    button_str_clear = Button(new_window, text="Clear message", command=lambda: clear_ASC_message(new_window))
    button_str_clear.place(x=45, y=136)

    label_send = Label(new_window, text="Word encoded:   " + b[0], fg="black")
    label_send.place(x=45, y=186)


a = [" "]
b = [" "]
char_table = []
char_received = []
decoded_message = [""]

root = Tk()

label_home = Label(text="Sending information")
label_home.pack()

button_1 = Button(root, text="Open second window", command=open_window)
button_1.place(x=45, y=40)

textExample = Text(root, height=1, width=20)
textExample.place(x=45, y=100)

button_str_to_ASC = Button(root, text="Convert word to ASCII", command=lambda: str_to_ASC())
button_str_to_ASC.place(x=45, y=200)

button_show_message = Button(root, text="Show coded message", command=lambda: show_ASC_all())
button_show_message.place(x=45, y=250)

button_clear = Button(root, text="Clear coded message", command=lambda: clear_message())
button_clear.place(x=45, y=300)

btnRead = Button(root, height=1, width=10, text="Read string", command=getTextInput)
btnRead.place(x=45, y=150)


root.geometry("420x400")
root.title("Main window")
root.mainloop()
