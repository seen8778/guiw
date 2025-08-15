import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("แบบฟอร์ม ชื่อ-ชั้น-เลขที่")
root.geometry("360x220")

def show_result():
    name = name_var.get().strip()
    grade = grade_var.get().strip()
    no = no_var.get().strip()
    text = f"ชื่อ : {name}\nชั้น : {grade}\nเลขที่ : {no}"
    messagebox.showinfo("ผลลัพธ์", text)

name_var = tk.StringVar()
grade_var = tk.StringVar()
no_var = tk.StringVar()

ttk.Label(root, text="ชื่อ :").grid(row=0, column=0, padx=10, pady=10, sticky="e")
ttk.Entry(root, textvariable=name_var, width=25).grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="ชั้น :").grid(row=1, column=0, padx=10, pady=10, sticky="e")
ttk.Entry(root, textvariable=grade_var, width=25).grid(row=1, column=1, padx=10, pady=10)

ttk.Label(root, text="เลขที่ :").grid(row=2, column=0, padx=10, pady=10, sticky="e")
ttk.Entry(root, textvariable=no_var, width=25).grid(row=2, column=1, padx=10, pady=10)

ttk.Button(root, text="แสดงผล", command=show_result).grid(row=3, column=0, columnspan=2, pady=15)

root.mainloop()