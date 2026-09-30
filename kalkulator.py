import tkinter as tk

def tekan(nilai):
    layar.insert(tk.END, nilai)

def hapus():
    layar.delete(0, tk.END)

def backspace():
    isi = layar.get()

    if isi:
        layar.delete(len(isi) - 1, tk.END)

def hitung():
    try:
        ekspresi = layar.get()

        # eval digunakan untuk menghitung ekspresi
        hasil = eval(ekspresi)

        layar.delete(0, tk.END)
        layar.insert(0, hasil)

    except:
        layar.delete(0, tk.END)
        layar.insert(0, "Error")


root = tk.Tk()

root.title("Kalkulator")
root.geometry("350x500")
root.resizable(False, False)


layar = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10
)

layar.pack(
    padx=10,
    pady=20,
    fill="x"
)

frame_tombol = tk.Frame(root)

frame_tombol.pack(
    padx=10,
    pady=10
)

tombol = [
    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("/", 0, 3),

    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("*", 1, 3),

    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("-", 2, 3),

    ("0", 3, 0),
    (".", 3, 1),
    ("+", 3, 2),
    ("=", 3, 3),
]


for teks, baris, kolom in tombol:

    if teks == "=":

        tombol_baru = tk.Button(
            frame_tombol,
            text=teks,
            font=("Arial", 18),
            width=5,
            height=2,
            command=hitung
        )

    else:

        tombol_baru = tk.Button(
            frame_tombol,
            text=teks,
            font=("Arial", 18),
            width=5,
            height=2,
            command=lambda nilai=teks: tekan(nilai)
        )

    tombol_baru.grid(
        row=baris,
        column=kolom,
        padx=3,
        pady=3
    )



tombol_clear = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 14),
    width=10,
    command=hapus
)

tombol_clear.pack(
    side="left",
    padx=25,
    pady=10
)


tombol_backspace = tk.Button(
    root,
    text="⌫",
    font=("Arial", 14),
    width=10,
    command=backspace
)

tombol_backspace.pack(
    side="right",
    padx=25,
    pady=10
)


root.mainloop()