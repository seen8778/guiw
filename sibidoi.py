import requests
from bs4 import BeautifulSoup
import tkinter as tk

lottery_url = "https://www.lottery.co.th/small"
response = requests.get(lottery_url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")
buttons = soup.find_all("button", class_="btn-primary")
results = [btn.text.strip() for btn in buttons]
while len(results) < 6:
    results.append("-")
labels = [
    ("รางวัลที่ 1", results[0]),
    ("เลขท้าย 2 ตัว", results[1]),
    ("เลขท้าย 3 ตัว", f"{results[2]} / {results[3]}"),
    ("เลขท้าย 4 ตัว", f"{results[4]} / {results[5]}")
]
app = tk.Tk()
app.title("ตรวจผลสลากกินแบ่งรัฐบาล")
app.geometry("520x490")
app.configure(bg="#f9f9f9")

header = tk.Label(
    app, text="ผลสลากกินแบ่งรัฐบาล\nประจำวันที่ 1 กันยายน 2568",
    font=("Helvetica", 22, "bold"), fg="#333333", bg="#f9f9f9"
)
header.pack(pady=15)
canvas = tk.Canvas(app, width=500, height=300, bg="#f9f9f9", highlightthickness=0)
canvas.pack()

def create_rounded_box(x, y, w, h, r, fill, text="", text_font=("Helvetica", 16), text_color="black", shadow=True):
    if shadow:
        canvas.create_rectangle(x+2, y+2, x+w+2, y+h+2, fill="#e0e0e0", outline="")
    canvas.create_polygon(
        x+r, y,
        x+w-r, y,
        x+w, y,
        x+w, y+r,
        x+w, y+h-r,
        x+w, y+h,
        x+w-r, y+h,
        x+r, y+h,
        x, y+h,
        x, y+h-r,
        x, y+r,
        x, y,
        smooth=True,
        fill=fill,
        outline="#ccc"
    )
    canvas.create_text(x + w/2, y + h/2, text=text, font=text_font, fill=text_color)
box_width_left = 180
box_width_right = 260
box_height = 50
box_spacing = 15
start_y = 10

for i, (title, number) in enumerate(labels):
    y = start_y + i*(box_height + box_spacing)
    create_rounded_box(20, y, box_width_left, box_height, 15, "#6448E1", text=title, text_font=("Helvetica", 16, "bold"), text_color="#FFFFFF")
    create_rounded_box(220, y, box_width_right, box_height, 15, "#ffffff", text=number, text_font=("Helvetica", 16), text_color="black")

tk.Button(app, text="ออกจากโปรแกรม", command=app.quit,
          bg="#007AFF", fg="white", font=("Helvetica", 14, "bold"),
          activebackground="#005BBB", activeforeground="white",
          relief="flat", bd=0, padx=10, pady=8, width=25).pack(pady=15)

app.mainloop()