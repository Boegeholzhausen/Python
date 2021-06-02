import tkinter as tk
import os
import matplotlib.pyplot as plt
import openpyxl
from PIL import Image, ImageTk
from tkinter.filedialog import Toplevel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import funcs.make_test as mt
import funcs.fill_excel as fe
import funcs.open_excel as oe
import funcs.graph_data as gd
import funcs.records as rc


# chance directory
os.chdir(r"C:\Python\Projects\WPMTracker")


def graphs():
    rc.wpm()
    rc.acc()
    rc.hits()
    gd.data()
    graphs = Toplevel(root) # mit root verbinden
    graphs.title("Graphs")
    graphs.iconbitmap(r"C:\Python\Projects\WPMTracker\icons\window_icon.ico")
    graphs.resizable(False, False)
    graphs.geometry("+-1910+130")
    canvas = tk.Canvas(graphs, width=1400, height=980, bg=background)
    canvas.grid(columnspan=3, rowspan=3)

    plt.figure
    plt.style.use("seaborn-deep")
    wpm_graph = plt.figure(figsize=(12,3))
    wpm_graph.patch.set_facecolor(background)
    wpmline = FigureCanvasTkAgg(wpm_graph, graphs)
    wpmline.get_tk_widget().grid(columnspan=2, column=0, row=0, sticky="NW", padx=10, pady=10)
    plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker (WPM)', data=gd.dfwpm)
    plt.xlabel("Nr.")
    plt.ylabel("WPM")
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.tight_layout()

    plt.figure
    plt.style.use("seaborn-deep")
    wpm_graph = plt.figure(figsize=(12,3))
    wpm_graph.patch.set_facecolor(background)
    wpmline = FigureCanvasTkAgg(wpm_graph, graphs)
    wpmline.get_tk_widget().grid(columnspan=2, column=0, row=1, sticky="NW", padx=10, pady=10)
    plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker (Accuracy)', data=gd.dfacc)
    plt.xlabel("Nr.")
    plt.ylabel("%")
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.tight_layout()

    plt.figure
    plt.style.use("seaborn-deep")
    wpm_graph = plt.figure(figsize=(12,3))
    wpm_graph.patch.set_facecolor(background)
    wpmline = FigureCanvasTkAgg(wpm_graph, graphs)
    wpmline.get_tk_widget().grid(columnspan=2, column=0, row=2, sticky="NW", padx=10, pady=10)
    plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker (Tastenanschläge)', data=gd.dfhits)
    plt.xlabel("Nr.")
    plt.ylabel("Tastenanschläge")
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.tight_layout()

    # WPM Record (Label)
    wpmrecord = tk.Label(graphs, text="WPM Record:")
    wpmrecord.grid(column=2, row=0, sticky="N", pady=100, padx=20)
    wpmrecord.config(bg=background, font=("Calibri bold", txtfontsize), fg="#1f262e")

    # WPM Record
    wpmrecord = tk.Label(graphs, text=str(rc.maxwpm))
    wpmrecord.grid(column=2, row=0)
    wpmrecord.config(bg=background, font=("Calibri bold", txtfontsize), fg="#0A4A1B")

    # ACC Record (Label)
    wpmrecord = tk.Label(graphs, text="Acc Record:")
    wpmrecord.grid(column=2, row=1, sticky="N", pady=100, padx=20)
    wpmrecord.config(bg=background, font=("Calibri bold", txtfontsize), fg="#1f262e")

    # ACC Record
    wpmrecord = tk.Label(graphs, text=str(rc.maxacc) + "%")
    wpmrecord.grid(column=2, row=1)
    wpmrecord.config(bg=background, font=("Calibri bold", txtfontsize), fg="#0A4A1B")

    # Hits Record (Label)
    wpmrecord = tk.Label(graphs, text="Hits Record:")
    wpmrecord.grid(column=2, row=2, sticky="N", pady=100, padx=20)
    wpmrecord.config(bg=background, font=("Calibri bold", txtfontsize), fg="#1f262e")

    # Hits Record
    wpmrecord = tk.Label(graphs, text=str(rc.maxhits))
    wpmrecord.grid(column=2, row=2)
    wpmrecord.config(bg=background, font=("Calibri bold", txtfontsize), fg="#0A4A1B")    


def hgraphs():
    rc.hwpm()
    rc.hacc()
    rc.hhits()
    gd.hdata()
    graphs = Toplevel(root) # mit root verbinden
    graphs.title("Graphs")
    graphs.iconbitmap(r"C:\Python\Projects\WPMTracker\icons\window_icon.ico")
    graphs.resizable(False, False)
    graphs.geometry("+-1910+130")
    canvas = tk.Canvas(graphs, width=1400, height=980, bg=background)
    canvas.grid(columnspan=3, rowspan=3)

    plt.figure
    plt.style.use("seaborn-deep")
    wpm_graph = plt.figure(figsize=(12,3))
    wpm_graph.patch.set_facecolor(background)
    wpmline = FigureCanvasTkAgg(wpm_graph, graphs)
    wpmline.get_tk_widget().grid(columnspan=2, column=0, row=0, sticky="NW", padx=10, pady=10)
    plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker (WPM) [Hard]', data=gd.dfhwpm)
    plt.xlabel("Nr.")
    plt.ylabel("WPM")
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.tight_layout()

    plt.figure
    plt.style.use("seaborn-deep")
    wpm_graph = plt.figure(figsize=(12,3))
    wpm_graph.patch.set_facecolor(background)
    wpmline = FigureCanvasTkAgg(wpm_graph, graphs)
    wpmline.get_tk_widget().grid(columnspan=2, column=0, row=1, sticky="NW", padx=10, pady=10)
    plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker (Accuracy) [Hard]', data=gd.dfhacc)
    plt.xlabel("Nr.")
    plt.ylabel("%")
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.tight_layout()

    plt.figure
    plt.style.use("seaborn-deep")
    wpm_graph = plt.figure(figsize=(12,3))
    wpm_graph.patch.set_facecolor(background)
    wpmline = FigureCanvasTkAgg(wpm_graph, graphs)
    wpmline.get_tk_widget().grid(columnspan=2, column=0, row=2, sticky="NW", padx=10, pady=10)
    plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker (Tastenanschläge) [Hard]', data=gd.dfhhits)
    plt.xlabel("Nr.")
    plt.ylabel("Tastenanschläge")
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.tight_layout()

    # WPM Record (Label)
    wpmrecord = tk.Label(graphs, text="WPM Record:")
    wpmrecord.grid(column=2, row=0, sticky="N", pady=100, padx=20)
    wpmrecord.config(bg=background, font=("Calibri bold", txtfontsize), fg="#1f262e")

    # WPM Record
    wpmrecord = tk.Label(graphs, text=str(rc.maxhwpm))
    wpmrecord.grid(column=2, row=0)
    wpmrecord.config(bg=background, font=("Calibri bold", txtfontsize), fg="#920000")

    # ACC Record (Label)
    wpmrecord = tk.Label(graphs, text="Acc Record:")
    wpmrecord.grid(column=2, row=1, sticky="N", pady=100, padx=20)
    wpmrecord.config(bg=background, font=("Calibri bold", txtfontsize), fg="#1f262e")

    # ACC Record
    wpmrecord = tk.Label(graphs, text=str(rc.maxhacc) + "%")
    wpmrecord.grid(column=2, row=1)
    wpmrecord.config(bg=background, font=("Calibri bold", txtfontsize), fg="#920000")

    # Hits Record (Label)
    wpmrecord = tk.Label(graphs, text="Hits Record:")
    wpmrecord.grid(column=2, row=2, sticky="N", pady=100, padx=20)
    wpmrecord.config(bg=background, font=("Calibri bold", txtfontsize), fg="#1f262e")

    # Hits Record
    wpmrecord = tk.Label(graphs, text=str(rc.maxhhits))
    wpmrecord.grid(column=2, row=2)
    wpmrecord.config(bg=background, font=("Calibri bold", txtfontsize), fg="#920000")   


# GUI
root = tk.Tk()
root.title("WPM Tracker")
root.iconbitmap(r"C:\Python\Projects\WPMTracker\icons\window_icon.ico")
background = "#97D5FF"
root.resizable(False, False)
root.geometry("+-500+200")


canvas = tk.Canvas(root, width=460, height= 750, bg=background)
canvas.grid(columnspan=2, rowspan=9)


## TK Window
# heights & widths
btnh = 1
btnw = 17
btnfontsize = 14
txtfontsize = 18

# logo
logo = Image.open(r"C:\Python\Projects\WPMTracker\icons\logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(root, image=logo, borderwidth=2)
logo_label.image = logo
logo_label.grid(columnspan=3, column=0, row=0)

# Instuction 1
instructions2 = tk.Label(root, text="Make the Test")
instructions2.grid(columnspan=2, column=0, row=1)
instructions2.config(bg=background, font=("Calibri bold", txtfontsize))

test_icon = Image.open(r"C:\Python\Projects\WPMTracker\icons\test1.png")
test_icon = ImageTk.PhotoImage(test_icon)
test_icon_label = tk.Label(root, image=test_icon, bg = background)
test_icon_label.image = test_icon
test_icon_label.grid(columnspan=1, column=1, row=1, padx=30, sticky="E")
test_icon = Image.open(r"C:\Python\Projects\WPMTracker\icons\test2.png")
test_icon = ImageTk.PhotoImage(test_icon)
test_icon_label = tk.Label(root, image=test_icon, bg = background)
test_icon_label.image = test_icon
test_icon_label.grid(columnspan=1, column=0, row=1, padx=30, sticky="W")

# Button easy & hard speed
speed_btn = tk.Button(root, text="Easy Test", command=lambda:mt.open_browser())
speed_btn.grid(column=0, row=2)
speed_btn.config(bg="#0A4A1B", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hspeed_btn = tk.Button(root, text="Hard Test", command=lambda:mt.open_browser_hard())
hspeed_btn.grid(column=1, row=2)
hspeed_btn.config(bg="#920000", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

# Button Ergebniss einlesen
result_btn = tk.Button(root, text="Copy Results", command=lambda:fe.getValues())
result_btn.grid(column=0, row=3)
result_btn.config(bg="#0A4A1B", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hresult_btn = tk.Button(root, text="Copy Results", command=lambda:fe.gethValues())
hresult_btn.grid(column=1, row=3)
hresult_btn.config(bg="#920000", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

# Instuction 2
instructions2= tk.Label(root, text="Excel Files")
instructions2.grid(columnspan=3, column=0, row=4)
instructions2.config(bg=background, font=("Calibri bold", txtfontsize))

# Excel_Icon 1
excel_icon = Image.open(r"C:\Python\Projects\WPMTracker\icons\excel2.png")
excel_icon = ImageTk.PhotoImage(excel_icon)
excel_icon_label = tk.Label(root, image=excel_icon, bg = background)
excel_icon_label.image = excel_icon
excel_icon_label.grid(columnspan=1, column=1, row=4, padx=30, sticky="E")
# Excel_Icon 2
excel_icon = Image.open(r"C:\Python\Projects\WPMTracker\icons\excel1.png")
excel_icon = ImageTk.PhotoImage(excel_icon)
excel_icon_label = tk.Label(root, image=excel_icon, bg = background)
excel_icon_label.image = excel_icon
excel_icon_label.grid(columnspan=1, column=0, row=4, padx=30, sticky="W")

# Button easy & hard excel
easy_btn = tk.Button(root, text="Easy", command=lambda:oe.open_easy())
easy_btn.grid(column=0, row=5)
easy_btn.config(bg="#0A4A1B", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=4)

hard_btn = tk.Button(root, text="Hard", command=lambda:oe.open_hard())
hard_btn.grid(column=1, row=5)
hard_btn.config(bg="#920000", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=4)

# Instuction 3
instructions3 = tk.Label(root, text="Graphs & Records")
instructions3.grid(columnspan=2, column=0, row=6)
instructions3.config(bg=background, font=("Calibri bold", txtfontsize))

# Graph_Icon
graph_icon = Image.open(r"C:\Python\Projects\WPMTracker\icons\trophy.png")
graph_icon = ImageTk.PhotoImage(graph_icon)
graph_icon_label = tk.Label(root, image=graph_icon, bg = background)
graph_icon_label.image = graph_icon
graph_icon_label.grid(columnspan=1, column=1, row=6, padx=30, sticky="E")

# Trophy_icon
trophy_icon = Image.open(r"C:\Python\Projects\WPMTracker\icons\graph.png")
trophy_icon = ImageTk.PhotoImage(trophy_icon)
trophy_icon_label = tk.Label(root, image=trophy_icon, bg = background)
trophy_icon_label.image = trophy_icon
trophy_icon_label.grid(columnspan=1, column=0, row=6, padx=30, sticky="W")

# #16465E darkblue
# Button easy&hard graph
records_btn = tk.Button(root, text = "Easy", command=lambda:graphs())
records_btn.grid(column=0, row=7)
records_btn.config(bg="#85C98B", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hrecords_btn = tk.Button(root, text = "Hard", command=lambda:hgraphs())
hrecords_btn.grid(column=1, row=7)
hrecords_btn.config(bg="#FF5050", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

root.mainloop()