import random
import tkinter as tk
from PIL import Image, ImageTk

NUM_TYPES = 18

root = tk.Tk()

root.title('Type Quiz')
root.geometry('660x750')
root.resizable(False, False)

img_files = [
        "normal.png", "flare.png", "water.png", "electric.png", "grass.png", "ice.png",
        "fighting.png", "poison.png", "ground.png", "flying.png", "phychic.png", "bug.png",
        "rock.png", "ghost.png", "dragon.png", "dark.png", "steel.png", "fairy.png"
];

type_names = [
        "ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり",
        "かくとう", "どく", "じめん", "ひこう", "エスパー", "むし",
        "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー"
]

mul_tbl = ["0.4", "0.6", "1.0", "1.6"]

tbl = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-2, 0, 0,-1, 0],  # ノーマル (攻撃側)
    [ 0,-1,-1, 0, 1, 1, 0, 0, 0, 0, 0, 1,-1, 0,-1, 0, 1, 0],  # ほのお
    [ 0, 1,-1, 0,-1, 0, 0, 0, 1, 0, 0, 0, 1, 0,-1, 0, 0, 0],  # みず
    [ 0, 0, 1,-1,-1, 0, 0, 0,-2, 1, 0, 0, 0, 0,-1, 0, 0, 0],  # でんき
    [ 0,-1, 1, 0,-1, 0, 0,-1, 1,-1, 0,-1, 1, 0,-1, 0,-1, 0],  # くさ
    [ 0,-1,-1, 0, 1,-1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0,-1, 0],  # こおり
    [ 1, 0, 0, 0, 0, 1, 0,-1, 0,-1,-1,-1, 1,-2, 0, 1, 1,-1],  # かくとう
    [ 0, 0, 0, 0, 1, 0, 0,-1,-1, 0, 0, 0,-1,-1, 0, 0,-2, 1],  # どく
    [ 0, 1, 0, 1,-1, 0, 0, 1, 0,-2, 0,-1, 1, 0, 0, 0, 1, 0],  # じめん
    [ 0, 0, 0,-1, 1, 0, 1, 0, 0, 0, 0, 1,-1, 0, 0, 0,-1, 0],  # ひこう
    [ 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,-1, 0, 0, 0, 0,-2,-1, 0],  # エスパー
    [ 0,-1, 0, 0, 1, 0,-1,-1, 0,-1, 1, 0, 0,-1, 0, 1,-1,-1],  # むし
    [ 0, 1, 0, 0, 0, 1,-1, 0,-1, 1, 0, 1, 0, 0, 0, 0,-1, 0],  # いわ
    [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,-1, 0, 0],  # ゴースト
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,-1,-2],  # ドラゴン
    [ 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 1, 0, 0, 1, 0,-1, 0,-1],  # あく
    [ 0,-1,-1,-1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,-1, 1],  # はがね
    [ 0,-1, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 1, 1,-1, 0]   # フェアリー
]

q_list = list(range(0, NUM_TYPES))
random.shuffle(q_list)

cur_q = 0

imgs = []
ans_vars = []  #選択値格納用変数

def q_button_click():
    global cur_q

    if cur_q >= NUM_TYPES:
        return

    q_i = q_list[cur_q]

    msgs = []

    for i in range(0, NUM_TYPES):
        ans_v = ans_vars[i].get()
        if ans_v != tbl[i][q_i]:  # 回答が間違っている
            msgs.append("{0}は{1}じゃない".format(type_names[i], mul_tbl[ans_v + 2]))

    if len(msgs) > 0:
        q_msg['text'] = "\n".join(msgs)
    else:
        cur_q += 1

        q_img = Image.open("images\\" + img_files[q_list[cur_q]])
        q_img = ImageTk.PhotoImage(q_img)
        q_label_img.configure(image=q_img)
        q_label_img.image = q_img

        for k in range(0, NUM_TYPES):
            ans_vars[k].set(0)

        if cur_q >= NUM_TYPES:
            q_msg['text'] = "終了"
            q_button["state"] = "disable"
        else:
            q_msg['text'] = "{0}問目".format(cur_q + 1)

def btn_update(i):
    q_i = q_list[cur_q]
    ans_v = ans_vars[i].get()
    wrongs = 0

    for k in range(0, NUM_TYPES):
        if ans_vars[k].get() != tbl[k][q_i]:  # 回答が間違っている
            wrongs += 1

    if ans_v == tbl[i][q_i]:
        q_msg['text'] = "{0}: 正解     残り間違い: {1}".format(type_names[i], wrongs)
    else:
        q_msg['text'] = "{0}は{1}じゃない     残り間違い: {2}".format(type_names[i], mul_tbl[ans_v + 2], wrongs)

q_frame = tk.Frame(root, width=660, height=100)
q_frame.propagate(False)  # Frameサイズを固定
q_frame.grid(row=0, column=0)

q_def = tk.Label(q_frame, text="防御側が")
q_def.grid(row=0, column=0)

q_img = Image.open("images\\" + img_files[q_list[cur_q]])
q_img = ImageTk.PhotoImage(q_img)

q_label_img = tk.Label(q_frame, image=q_img)
q_label_img.grid(row=0, column=1)

q_button = tk.Button(q_frame, text="回答", padx=10, pady=10, command=q_button_click)
q_button.grid(row=0, column=2)

q_msg = tk.Label(q_frame, text="攻撃側を回答。1問目")
q_msg.grid(row=0, column=3)

ans_frame = tk.Frame(root, width=660, height=600)
ans_frame.propagate(False)  # Frameサイズを固定
ans_frame.grid(row=1, column=0)

cmds = [
        lambda: btn_update(0), lambda: btn_update(1), lambda: btn_update(2), lambda: btn_update(3),
        lambda: btn_update(4), lambda: btn_update(5), lambda: btn_update(6), lambda: btn_update(7),
        lambda: btn_update(8), lambda: btn_update(9), lambda: btn_update(10), lambda: btn_update(11),
        lambda: btn_update(12), lambda: btn_update(13), lambda: btn_update(14), lambda: btn_update(15),
        lambda: btn_update(16), lambda: btn_update(17)
]

for i, fname in enumerate(img_files):
    row = int(i / 6)
    col = i % 6

    ans_vars.append(tk.IntVar(root))

    frame = tk.Frame(ans_frame, width=110, height=200)
    frame.propagate(False)  # Frameサイズを固定
    frame.grid(row=row, column=col)

    img = Image.open("images\\" + fname)
    img = ImageTk.PhotoImage(img)
    imgs.append(img)

    label_img = tk.Label(frame, image=img)
    label_img.pack()

    r1 = tk.Radiobutton(frame, text="1.6", value=1, var=ans_vars[i], command=cmds[i])
    r1.pack()

    r2 = tk.Radiobutton(frame, text="1.0", value=0, var=ans_vars[i], command=cmds[i])
    r2.pack()

    r3 = tk.Radiobutton(frame, text="0.6", value=-1, var=ans_vars[i], command=cmds[i])
    r3.pack()

    r4 = tk.Radiobutton(frame, text="0.4", value=-2, var=ans_vars[i], command=cmds[i])
    r4.pack()

root.mainloop()
