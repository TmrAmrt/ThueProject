import random
import tkinter as tk
from tkinter import simpledialog, END
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    filepath = askopenfilename(
        filetypes=[("Thue Files", "*.thue"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    rules_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        rules_edit.insert(tk.END, text)
    window.title(f"Thue Language Interpreter - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension="thue",
        filetypes=[("Thue File", "*.thue"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = rules_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Thue Language Interpreter - {filepath}")


class Rule:
    left = ""
    right = ""

    def __init__(self, lh, rh):
        self.left = lh
        self.right = rh

    def __repr__(self):
        return "Rule(%s,%s)" % (repr(self.left), repr(self.right))


def load_rules():
    rules = []
    for line in rules_edit.get("1.0", "end-1c").split("\n"):
        s = line.replace(" ", "")
        splitee = s.split("::=", 1)
        if len(splitee) == 2:
            lhs = splitee[0]
            rhs = splitee[1]
            rules.append(Rule(lhs, rhs))
    return rules


def findall(s, pattern):
    i = -1
    indexes = []
    while 1:
        i = s.find(pattern, i+1)
        if i >= 0:
            indexes.append(i)
            i += 1
        else:
            break
    return indexes


def step(rules):
    matches = []
    indexes = []
    data = text_edit.get("1.0", "end-1c")
    print(data)
    newdata = ""
    for rule in rules:
        indexes = findall(data, rule.left)
        for i in indexes:
            matches.append((i, rule))
    if len(matches) == 0:
        text_edit.delete("1.0", END)
        text_edit.insert("1.0", data)
        lbl_initialText.config(text="Processed Text :")
        return 0
    # choix au hasard d'un des match
    select = matches[random.randint(0, len(matches) - 1)]
    position = select[0]
    selectedrule = select[1]
    endpos = position+len(selectedrule.left)
    if data[position:endpos] == select[1].left:

        if select[1].right[:1] == "~":
            result_display.insert(END, select[1].right[1:])
        elif select[1].right == ":::":
            newdata = tk.simpledialog.askstring("Enter text", "please input your added text")
        else:
            newdata = select[1].right
        data = data[:position] + newdata + data[endpos:]
        text_edit.delete("1.0", END)
        text_edit.insert("1.0", data)
        return 1


def run_prog():
    rules = load_rules()
    notfinished = 1
    while notfinished == 1:
        notfinished = step(rules)


window = tk.Tk()

window.title("Thue Language Interpreter")
window.rowconfigure(0, minsize=200, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, minsize=200, weight=1)

rules_edit = tk.Text(bd=4, height=15, width=70)
text_edit = tk.Text(bd=4, height=1, width=25)
result_display = tk.Text(bd=4, height=1, width=25)

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
fr_buttons2 = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Load Rule File", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save Rules As...", command=save_file)
btn_etienne = tk.Button(window, text="Execute", command=run_prog)
lbl_initialText = tk.Label(text=" Text to process :")
lbl_results = tk.Label(text=" Results :")

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_etienne.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, rowspan=3, column=0, sticky="ns")
lbl_initialText.grid(row=1, column=1, sticky="w")
lbl_results.grid(row=2, column=1, sticky="w")
rules_edit.grid(row=0, column=1, columnspan=2, sticky="nsew")
text_edit.grid(row=1, column=2, sticky="new", padx=10, pady=5)
result_display.grid(row=2, column=2, sticky="new", pady=20, padx=10)
window.mainloop()


