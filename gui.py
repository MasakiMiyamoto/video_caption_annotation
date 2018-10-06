# -*- coding:utf-8 -*-
import sys
sys.getrecursionlimit()
import tkinter as tk
import random
import tkinter.messagebox as tkmsg
'''
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
'''
# rootフレームの設定
root = tk.Tk()
root.title("Naklab annotation")
root.geometry("800x600")

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
entry2 = tk.Entry(frame2,font=("",14),justify="center",width=7)
entry2.pack(side="left")
label6 = tk.Label(frame2,font=("",14),text="分")
label6.pack(side="left")
entry6 = tk.Entry(frame2,font=("",14),justify="center",width=7)
entry6.pack(side="left")
label7 = tk.Label(frame2,font=("",14),text="秒")
label7.pack(side="left")

# 終了タイムスタンプのラベルとエントリーの設定
frame3 = tk.Frame(root,pady=10)
frame3.pack()
label4 = tk.Label(frame3,font=("",14),text="終了タイムスタンプ")
label4.pack(side="left")
entry3 = tk.Entry(frame3,font=("",14),justify="center",width=7)
entry3.pack(side="left")
label8 = tk.Label(frame3,font=("",14),text="分")
label8.pack(side="left")
entry7 = tk.Entry(frame3,font=("",14),justify="center",width=7)
entry7.pack(side="left")
label9 = tk.Label(frame3,font=("",14),text="秒")
label9.pack(side="left")

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
frame6 = tk.Frame(root,pady=10)
frame6.pack()
label7 = tk.Label(frame6,font=("",14),text="*タイムスタンプは全部のエントリーを記入しないと出力されない")
label7.pack(side="left")
# clickイベント



def btn_click1():

    entry8.delete(0,100)
    # テキスト取得
    st=entry1.get()
    tsm=entry2.get()
    tss=entry6.get()
    tem=entry3.get()
    tes=entry7.get()
    nm=entry4.get()
    if tsm=='':
        ts=float(tss)
    if tsm!='':
        ts=int(tsm)*60+float(tss)
    if tem=='':
        te=float(tes)
    if tem!='':
        te=int(tem)*60+float(tes)
    f = open('./../template.txt', 'a') # ファイルを開く(該当ファイルがなければ新規作成)
    bun1='append%s = {\'sentence\':\'%s\',\'timestamp\':[%s,%s]}'%(nm,st,'%02.2f' % ts,'%02.2f' % te)
    f.write(bun1+'\n') # 文字列を記載する
    f.close()
    entry8.insert(tk.END,bun1)
    rm=random.randrange(1, 101)
    if rm==1 or rm==11 or rm==21 or rm==31 or rm==41 or rm==51:


        b=tkmsg.showinfo('うんち！','ちんちん！')
        '''
        img = cv2.imread("./data/hasu.jpg")
        cv2.imshow('ero gazou', img)
        '''
def btn_click2():
    entry8.delete(0,100)
    '''
    with open('./data/kazu.txt','r',encoding='utf-8') as f:
        kazu=f.read()
        nmr=int(kazu)
    '''
    # テキスト取得
    id=entry5.get()
    nm=entry4.get()
    f = open('./../template.txt', 'a') # ファイルを開く(該当ファイルがなければ新規作成)
    bun2='data[\"v_%s\"].append(append%s)'%(id,nm)
    f.write(bun2+'\n') # 文字列を記載する
    f.close()
    entry8.insert(tk.END,bun2)
    '''
    nmr+=1
    w = open('./data/kazu.txt', 'w')
    w.write('%d',nmr)
    '''
def btn_click3():

    entry8.delete(0,100)

    # テキスト取得
    id=entry5.get()
    f = open('./../template.txt', 'a') # ファイルを開く(該当ファイルがなければ新規作成)
    bun3='data[\"v_%s\"] = []'%(id)
    f.write(bun3+'\n') # 文字列を記載する
    f.close()
    entry8.insert(tk.END,bun3)

def kesu():
    entry1.delete(0,100)
    entry2.delete(0,100)
    entry3.delete(0,100)
    entry7.delete(0,100)
    entry6.delete(0,100)
    #entry8.delete(0,100)

def btn_click4():
    entry1.insert(tk.END,"画面のと画面のが衝突します")
# ボタンの設定
def btn_click5():
    entry1.insert(tk.END,"画面のが危険")


frame7 = tk.Frame(root,pady=0)
frame7.pack()

button4 = tk.Button(frame7,text="テンプレ作成",font=("",16),width=12,bg="white",command=btn_click1)
button4.pack(side="left")
button7 = tk.Button(frame7,text="若宮のわがまま",font=("",16),width=12,bg="white",command=kesu)
button7.pack(side="left")
frame8 = tk.Frame(root,pady=0)
frame8.pack()
button5 = tk.Button(frame8,text="動画ID作成",font=("",16),width=12,bg="white",command=btn_click2)
button5.pack(side="left")

button8 = tk.Button(frame8,text="楽々ボタン1",font=("",16),width=12,bg="white",command=btn_click4)
button8.pack(side="left")
button9 = tk.Button(frame8,text="楽々ボタン2",font=("",16),width=12,bg="white",command=btn_click5)
button9.pack(side="left")

'''
with open('./data/kazu.txt','r',encoding='utf-8') as f:
    kazu=f.read()
'''
frame9 = tk.Frame(root,pady=0)
frame9.pack()
button6 = tk.Button(frame9,text="最初のやつ",font=("",16),width=12,bg="white",command=btn_click3)
button6.pack(side="left")
'''
entry8= tk.Entry(frame9,font=("",14),justify="center",width=5)
entry8.pack(side="left")

label9 = tk.Label(frame9,font=("",14),text="回")
label9.pack(side="left")
entry8.insert(tk.END,kazu)
'''
'''
root.bind( '<Key-Delete>', kesu)
'''
frame10 = tk.Frame(root,pady=10)
frame10.pack()
frame11 = tk.Frame(root,pady=10)
frame11.pack()
frame12 = tk.Frame(root,pady=10)
frame12.pack()
label8 = tk.Label(frame12,font=("",14),text="v0.51")
label8.pack(side="left")

label8 = tk.Label(frame10,font=("",14),text="出力結果")
label8.pack(side="left")

entry8 = tk.Entry(frame11,font=("",14),justify="right",width=60)
entry8.pack(side="left")
root.mainloop()
