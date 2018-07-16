import tkinter as tk
from tkinter import font
import pickle
import random

with open('use_form.pickle','rb') as f:
 form = pickle.load(f)

with open('use_word.pickle','rb') as f:
 word = pickle.load(f)

# lbl['text']=tmp

def generate():
    h=''
    f=random.choice(form)
    for w in f.split():
        if w[0]!='.':
            h+=w
        else:
            h+=random.choice(word[w[1]][int(w[2])])
    lbl['text']=h
rt = tk.Tk()
rt.title('俳句自動生成')
rt.geometry('600x400+600+0')
lbl = tk.Label(rt,text = 'hello',font=font.Font(size=40))
frm = tk.Frame(rt)
btn = tk.Button(frm,text='再生成',font=font.Font(size=100),command=generate)
lbl.pack(fill='x',expand=1)#grid(row=1,column=1,sticky=tk.W+tk.E)
btn.pack(side='bottom',fill='y',expand=1)
frm.pack(fill='both',expand=1)
generate()


rt.mainloop()
