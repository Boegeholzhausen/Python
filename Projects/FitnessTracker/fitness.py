import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import Toplevel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import funcs.get_data as gd


# chance directory
os.chdir(r"C:\Python\Projects\FitnessTracker")


root = tk.Tk()
root.title("Fitness Tracker")
root.iconbitmap(r"C:\Python\Projects\FitnessTracker\icons\fitness_icon.ico")
background = "#488953"
root.resizable(False, False)
root.geometry("+500+300")

canvas = tk.Canvas(root, width=500, height=500, bg=background)
canvas.grid(columnspan=2, rowspan=2)

# Logo
logo = Image.open(r"C:\Python\Projects\FitnessTracker\icons\fitness.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(root, image=logo, bg=background)
logo_label.image = logo
logo_label.grid(columnspan=2, column=0, row=0)

# Button für Trainingsplanauswahl
btnh = 2
btnw = 17
btnfontsize = 14
txtfontsize = 18

workout1_btn = tk.Button(root, text="Ring Workout", command=lambda:[workout_1_tabel(), workout_1_graph()])
workout1_btn.grid(column=0, row=1)
workout1_btn.config(bg="#3C58A0", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

workout2_btn = tk.Button(root, text="Muscle Growth", command=lambda:workout_2())
workout2_btn.grid(column=1, row=1)
workout2_btn.config(bg="#3C58A0", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)


def workout_1_tabel():
    workout_1_tabel = Toplevel(root)
    workout_1_tabel.title("Ring Workout")
    workout_1_tabel.iconbitmap(r"C:\Python\Projects\FitnessTracker\icons\fitness_icon.ico")
    workout_1_tabel.resizable(False, False)
    canvas_1 = tk.Canvas(workout_1_tabel, width=1100, height=500, bg=background)
    canvas_1.grid(columnspan=5, rowspan=8)
    workout_1_tabel.geometry("+50+50")

    tablecolor = "white"
    textcolor = "black"
    # Trainingsplan (Tabelle) anzeigen
    plan = tk.Label(workout_1_tabel, text="Übung", borderwidth=2, relief="solid")
    plan.grid(columnspan=1, rowspan=1, column=0, row=0, sticky="N", padx=30, pady=20, ipady=15, ipadx=50)
    plan.config(bg=tablecolor, font=("Calibri bold", txtfontsize), fg=textcolor)
#
    set1 = tk.Label(workout_1_tabel, text="Set 1", borderwidth=2, relief="solid")
    set1.grid(columnspan=1, rowspan=1, column=1, row=0, sticky="N", pady=20, ipady=15, ipadx=50)
    set1.config(bg=tablecolor, font=("Calibri bold", txtfontsize), fg=textcolor)
#
    set2 = tk.Label(workout_1_tabel, text="Set 2", borderwidth=2, relief="solid")
    set2.grid(columnspan=1, rowspan=1, column=2, row=0, sticky="N", pady=20, ipady=15, ipadx=50)
    set2.config(bg=tablecolor, font=("Calibri bold", txtfontsize), fg=textcolor)
#
    set3 = tk.Label(workout_1_tabel, text="Set 3", borderwidth=2, relief="solid")
    set3.grid(columnspan=1, rowspan=1, column=3, row=0, sticky="N", pady=20, ipady=15, ipadx=50)
    set3.config(bg=tablecolor, font=("Calibri bold", txtfontsize), fg=textcolor)

    for i in range(1,7):
        exercise = tk.Label(workout_1_tabel, text=str(gd.exer), borderwidth=2, relief="solid")
        exercise.grid(columnspan=1, rowspan=1, column=0, row=i, sticky="N", pady=1, ipady=10, ipadx=50)
        exercise.config(bg=tablecolor, font=("Calibri bold", txtfontsize), fg=textcolor)

    for i in range(1,7):
        for x in range(1,4):
            rep = tk.Label(workout_1_tabel, text="1", borderwidth=2, relief="solid")
            rep.grid(columnspan=1, rowspan=1, column=x, row=i, sticky="N", pady=1, ipady=10, ipadx=50)
            rep.config(bg=tablecolor, font=("Calibri bold", txtfontsize), fg=textcolor)
            # print(gd.exer + " [Set " + str(i) + "]")


    # Eingabe für die Reps
    entry_btn = tk.Button(workout_1_tabel, text="Wiederholungen eingeben")
    entry_btn.grid(column=4, row=0, sticky="S", pady=10, padx=10)
    entry_btn.config(bg="#8380c2", font=("Calibri bold", txtfontsize), fg="white")    

    entry = tk.Entry(workout_1_tabel) 
    entry.grid(column=4, row=1, sticky="N", pady=10, padx=10, ipadx=20)
    entry.config(bg="#20272F", font=("Calibri bold", txtfontsize), fg="white")

    # Nächste Übung anzeigen


def workout_1_graph():
    workout_1_graph = Toplevel(root)
    workout_1_graph.title("Ring Workout")
    workout_1_graph.iconbitmap(r"C:\Python\Projects\FitnessTracker\icons\fitness_icon.ico")
    workout_1_graph.resizable(False, False)
    canvas_1 = tk.Canvas(workout_1_graph, width=1600, height=500, bg=background)
    canvas_1.grid(columnspan=1, rowspan=2)
    workout_1_graph.geometry("+50+800")

    # Graph anzeigen
    exercises = plt.figure(figsize=(15,4))
    exercises.patch.set_facecolor(background)
    line = FigureCanvasTkAgg(exercises, workout_1_graph)
    line.get_tk_widget().grid(columnspan=1, rowspan=1, column=0, row=1, sticky="NW", padx=10, pady=10)
    plt.plot('xvalues', 'yvalues', color="#8380c2", linewidth=3, label=gd.exer + " [Set 1]", data = gd.dfset1)
    plt.plot('xvalues', 'yvalues', color="#33a3cc", linewidth=3, label=gd.exer + " [Set 2]", data = gd.dfset2)
    plt.plot('xvalues', 'yvalues', color="#09046c", linewidth=3, label=gd.exer + " [Set 3]", data = gd.dfset3)
    plt.xlabel("Nr.")
    plt.ylabel("Reps")
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.tight_layout()


def workout_2():
    workout_2 = Toplevel(root)
    workout_2.title("Ring Workout")
    canvas_1 = tk.Canvas(workout_2, width=2440, height=1200, bg=background)
    canvas_1.grid(columnspan=2, rowspan=2)
    workout_2.geometry("+50+50")

root.mainloop()