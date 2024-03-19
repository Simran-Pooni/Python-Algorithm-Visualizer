import tkinter as tk
import random
import time

# Bubble-Sort Algorithmus
def bubble_sort(arr, canvas):
    for passes_left in range(len(arr) - 1, 0, -1):
        for i in range(passes_left):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                darstBalken(canvas, arr)
                canvas.update()
                time.sleep(0.1)


# Hauptfunktion
def darstBalken(canvas, arr):
    canvas.delete("all")
    canvas_breite = 500
    canvas_höhe = 300
    balkenbreite = canvas_breite / len(arr)
    max_value = max(arr)

    for i in range(len(arr)):       # Iteriert über die Indizes der Liste
        value = arr[i]
        balken_höhe = (value / max_value) * canvas_höhe

        # x-Koordinaten
        x_links = i * balkenbreite   # linke seite des balkens
        x_rechts = (i + 1) * balkenbreite  # rechte seite des balkens

        # y-Koordinaten
        y_oben = canvas_höhe - balken_höhe   # obere seite des balkens
        y_unten = canvas_höhe           # untere seite des balkens

        # Zeichnet den Balken auf dem Canvas mit den berechneten Koordinaten
        canvas.create_rectangle(x_links, y_oben, x_rechts, y_unten, fill="lightpink")


def sort_list():
    user_eingabe = eingabe.get().split()
    user_list = []

    for each in user_eingabe:
        user_list.append(int(each))
    bubble_sort(user_list, canvas)


# Hauptfenster mw
mw = tk.Tk()
mw.title("Algorithm Visualizer")

# Eingabefeld
eingabe = tk.Entry(mw, width=60)
eingabe.pack(pady=10)

# "Sortieren" Button
sortBut = tk.Button(mw, text="Sortieren", command=sort_list)
sortBut.pack()

# Fläche (canvas) für Visualisierung
canvas = tk.Canvas(mw, width=500, height=300)
canvas.pack()

mw.mainloop()


