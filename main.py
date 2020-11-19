import tkinter as tk
from functools import partial
import os
import operator
import Pmw, sys


def main():
    def login():
        username = User_name_value.get()
        password = Password_value.get()
        if username == 'rohan' and password == 'rohan':
            Password_value.delete(0, tk.END)
            root.destroy()
            login_success()
        else:
            root.destroy()
            login_failed()

    root = tk.Tk()
    root.title('Login')
    root.geometry("250x100")

    User_name = tk.Label(root, text="USER NAME : ")
    User_name.grid(row=2, column=0)

    User_name_value = tk.Entry(root, bg='white')
    User_name_value.grid(row=2, column=1)

    Password_label = tk.Label(root, text="PASSWORD : ")
    Password_label.grid(row=4, column=0)

    Password_value = tk.Entry(root, show="*", bg='white')
    Password_value.grid(row=4, column=1)

    submit = tk.Button(root, text="SUBMIT", width=10, command=lambda: login(), fg='blue')
    submit.grid(row=5, column=1)

    root.mainloop()


def login_failed():
    root = tk.Tk()
    root.title('LOGIN FAILED')
    root.geometry("250x100")
    message = tk.Label(root, text="LOGIN FAILED TRY AGAIN!!!!")
    message.grid(row=1, column=1)
    root.mainloop()


def login_success():
    charcaters = {
        10: '!', 11: '"', 12: '#', 13: '$',
        14: '%', 15: '&', 16: '(', 17: ')',
        18: '*', 19: '+', 20: ',', 21: '-',
        22: '.', 23: '/', 24: '0', 25: '1',
        26: '2', 27: '3', 28: '4', 29: '5',
        30: '6', 31: '7', 32: '8', 33: '9',
        34: ':', 35: ';', 36: '<', 37: '=',
        38: '>', 39: '?', 40: '@', 41: 'A',
        42: 'B', 43: 'C', 44: 'D', 45: 'E',
        46: 'F', 47: 'G', 48: 'H', 49: 'I',
        50: 'J', 51: 'K', 52: 'L', 53: 'M',
        54: 'N', 55: 'O', 56: 'P', 57: 'Q',
        58: 'R', 59: 'S', 60: 'T', 61: 'U',
        62: 'V', 63: 'W', 64: 'X', 65: 'Y',
        66: 'Z', 67: '[', 68: ']', 69: '^',
        70: '_', 71: 'a', 72: 'b', 73: 'c',
        74: 'd', 75: 'e', 76: 'f', 77: 'g',
        78: 'h', 79: 'i', 80: 'j', 81: 'k',
        82: 'l', 83: 'm', 84: 'n', 85: 'o',
        86: 'p', 87: 'q', 88: 'r', 89: 's',
        90: 't', 91: 'u', 92: 'v', 93: 'w',
        94: 'x', 95: 'y', 96: 'z', 97: '{',
        98: '|', 99: '}'}

    decript_characters ={
        10	:	'!',    11	:	'"',    12	:	'#',    13	:	'$',
        14	:	'%',    15	:	'&',    16	:	'(',    17	:	')',
        18	:	'*',    19	:	'+',    20	:	',',    21	:	'-',
        22	:	'.',    23	:	'/',    24	:	'0',    25	:	'1',
        26	:	'2',    27	:	'3',    28	:	'4',    29	:	'5',
        30	:	'6',    31	:	'7',    32	:	'8',    33	:	'9',
        34	:	':',    35	:	';',    36	:	'<',    37	:	'=',
        38	:	'>',    39	:	'?',    40	:	'@',    41	:	'A',
        42	:	'B',    43	:	'C',    44	:	'D',    45	:	'E',
        46	:	'F',    47	:	'G',    48	:	'H',    49	:	'I',
        50	:	'J',    51	:	'K',    52	:	'L',    53	:	'M',
        54	:	'N',    55	:	'O',    56	:	'P',    57	:	'Q',
        58	:	'R',    59	:	'S',    60	:	'T',    61	:	'U',
        62	:	'V',    63	:	'W',    64	:	'X',    65	:	'Y',
        66	:	'Z',    67	:	'[',    68	:	']',    69	:	'^',
        70	:	'_',    71	:	'a',    72	:	'b',    73	:	'c',
        74	:	'd',    75	:	'e',    76	:	'f',    77	:	'g',
        78	:	'h',    79	:	'i',    80	:	'j',    81	:	'k',
        82	:	'l',    83	:	'm',    84	:	'n',    85	:	'o',
        86	:	'p',    87	:	'q',    88	:	'r',    89	:	's',
        90	:	't',    91	:	'u',    92	:	'v',    93	:	'w',
        94	:	'x',    95	:	'y',    96	:	'z',    97	:	'{',
        98	:	'|',    99	:	'}' , ' ':' '  }    

    def get_key(val):
        for key, value in charcaters.items():
            if val == value:
                return key

    def get_val(kee):
        for key, value in decript_characters.items():
            if key == kee:
                return value

    def create_file():
        path = os.path.dirname(__file__)
        f = open(f"{path}\secure.txt", "a+")
        username = User_name_value.get()
        password = Password_value.get()

        username_encript = ""

        for i in username:
            a = get_key(i)
            username_encript = username_encript + str(a)

        password_encript = ""

        for j in password:
            b = get_key(j)
            password_encript = password_encript + str(b)

        f.write(username_encript + " " + password_encript)
        f.write('\n')
        f.close()
        User_name_value.delete(0, tk.END)
        Password_value.delete(0, tk.END)

    def terminate_box():
        root.destroy()

    def show_decript():
        # root.destroy()
        # dump = tk.Tk()
        # dump.title('SAVED DETAILS')
        # dump.geometry("300x100")
        # dump.mainloop()
        filename = "PASSWORDS"
        decript_canvas = tk.Tk()            
        top = tk.Frame(decript_canvas); top.pack(side='top')
        text = Pmw.ScrolledText(top,
            borderframe=5, 
            vscrollmode='dynamic', 
            hscrollmode='dynamic',
            labelpos='n', 
            label_text='SAVED  %s' % filename,
            text_width=40, 
            text_height=4,
            text_wrap='none',
            )
        text.pack()

        path=os.path.dirname(__file__)
        f=open(f"{path}\secure.txt","r")
        for i in f:
            message_1=i
            message_2=message_1.replace(' ','00')
            translator_1=""
            transilator_2=""
            for s in map(operator.add, message_2[::2], message_2[1::2]):
                a=get_val(int(s))
                translator_1 = translator_1 + str(a)
            transilator_2=translator_1.replace('None',' ')
            g=open(f"{path}\decript.txt","a+")
            g.write(transilator_2)
            g.write('\n')

            text.insert('end', transilator_2 )
            text.insert('end','\n')
        g.truncate(0)
        g.close()
        f.close()

        if os.path.exists(f"{path}\decript.txt"):
            os.remove(f"{path}\decript.txt")

        tk.Button(top, text='Quit', command=decript_canvas.destroy).pack(pady=15)

        decript_canvas.mainloop()

    root = tk.Tk()
    root.title('save')

    root.geometry("300x100")

    User_name = tk.Label(root, text="USER NAME : ")
    User_name.grid(row=2, column=0)

    User_name_value = tk.Entry(root, bg='white')
    User_name_value.grid(row=2, column=1)

    Password_label = tk.Label(root, text="PASSWORD : ")
    Password_label.grid(row=4, column=0)

    Password_value = tk.Entry(root, bg='white')
    Password_value.grid(row=4, column=1)

    save = tk.Button(root, text="SAVE", command=lambda: create_file(), width=10, fg='blue')
    save.grid(row=5, column=0)

    teminate = tk.Button(root, text="EXIT", command=lambda: terminate_box(), width=10, fg='blue')
    teminate.grid(row=5, column=1)

    show_saved = tk.Button(root, text="SHOW_SAVED", command=lambda: show_decript(), width=10, fg='blue')
    show_saved.grid(row=5, column=2)

    root.mainloop()


if __name__ == "__main__":
    main()
