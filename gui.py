# -*- coding:utf-8 -*-
import tkinter as tk

# rootフレームの設定
root = tk.Tk()
root.title("Naklab annotation")
root.geometry("800x400")

iconfile = './data/icon.ico'
root.iconbitmap(default=iconfile)


# センテンスのラベルとエントリーの設定
frame1 = tk.Frame(root,pady=10)
frame1.pack()
label2 = tk.Label(frame1,font=("",14),text="センテンス")
label2.pack(side="left")
entry1 = tk.Entry(frame1,font=("",14),justify="right",width=70)
entry1.pack(side="left")

# 開始タイムスタンプのラベルとエントリーの設定
frame2 = tk.Frame(root,pady=10)
frame2.pack()
label3 = tk.Label(frame2,font=("",14),text="開始タイムスタンプ")
label3.pack(side="left")
entry2 = tk.Entry(frame2,font=("",14),justify="center",width=15)
entry2.pack(side="left")

# 終了タイムスタンプのラベルとエントリーの設定
frame3 = tk.Frame(root,pady=10)
frame3.pack()
label4 = tk.Label(frame3,font=("",14),text="終了タイムスタンプ")
label4.pack(side="left")
entry3 = tk.Entry(frame3,font=("",14),justify="center",width=15)
entry3.pack(side="left")

# アペンド数のラベルとエントリーの設定
frame4 = tk.Frame(root,pady=10)
frame4.pack()
label5 = tk.Label(frame4,font=("",14),text="アペンド数")
label5.pack(side="left")
entry4 = tk.Entry(frame4,font=("",14),justify="center",width=15)
entry4.pack(side="left")

# 動画IDのラベルとエントリーの設定
frame5 = tk.Frame(root,pady=10)
frame5.pack()
label6 = tk.Label(frame5,font=("",14),text="動画ID")
label6.pack(side="left")
entry5 = tk.Entry(frame5,font=("",14),justify="center",width=15)
entry5.pack(side="left")
# clickイベント

def btn_click1():


    # テキスト取得
    st=entry1.get()
    ts=entry2.get()
    te=entry3.get()
    nm=entry4.get()
    f = open('./../template.txt', 'a') # ファイルを開く(該当ファイルがなければ新規作成)
    f.write('append%s = {\'sentence\':\'%s\',\'timestamp\':[%s,%s]}\n'%(nm,st,ts,te)) # 文字列を記載する
    f.close()

def btn_click2():


    # テキスト取得
    id=entry5.get()
    nm=entry4.get()
    f = open('./../template.txt', 'a') # ファイルを開く(該当ファイルがなければ新規作成)
    f.write('data[\"v_%s\"].append(append%s)\n'%(id,nm)) # 文字列を記載する
    f.close()



# ボタンの設定
button4 = tk.Button(root,text="テンプレ作成",font=("",16),width=12,bg="white",command=btn_click1)
button4.pack()
button5 = tk.Button(root,text="動画ID作成",font=("",16),width=12,bg="white",command=btn_click2)
button5.pack()


root.mainloop()
