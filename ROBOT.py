import tkinter as tk
from PIL import Image, ImageTk



from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")
from chatterbot.trainers import ChatterBotCorpusTrainer
bot = ChatBot('Candice')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.chinese")



window = tk.Tk()
window.title('ROBOT')
window.geometry('700x1000')
window.resizable(False,False)

#標題
div0 = tk.Frame(window,  width=80 , height=50 , bg='#6FB7B7')
div1 = tk.Frame(window,  width=540 , height=50 , bg='#6FB7B7')
div2 = tk.Frame(window,  width=80 , height=50 , bg='#6FB7B7')
#聊天室窗
div3_0 = tk.Frame(window,  width=700 , height=90 , bg='#FDFFFF')
div3_1 = tk.Frame(window,  width=700 , height=90 , bg='#FDFFFF')
div3_2 = tk.Frame(window,  width=700 , height=90 , bg='#FDFFFF')
div3_3 = tk.Frame(window,  width=700 , height=90 , bg='#FDFFFF')
div3_4 = tk.Frame(window,  width=700 , height=90 , bg='#FDFFFF')
div3_5 = tk.Frame(window,  width=700 , height=90 , bg='#FDFFFF')
div3_6 = tk.Frame(window,  width=700 , height=90 , bg='#FDFFFF')
div3_7 = tk.Frame(window,  width=700 , height=90 , bg='#FDFFFF')
div3_8 = tk.Frame(window,  width=700 , height=90 , bg='#FDFFFF')
div3_9 = tk.Frame(window,  width=700 , height=90 , bg='#FDFFFF')
#輸入區
div6 = tk.Frame(window,  width=80 , height=50 , bg='#6FB7B7')
div7 = tk.Frame(window,  width=540 , height=50 , bg='#6FB7B7')
div8 = tk.Frame(window,  width=80 , height=50 , bg='#6FB7B7')




div0.grid(column=0, row=0)
div1.grid(column=1, row=0)
div2.grid(column=2, row=0)

div3_0.grid(column=0, row=1 , columnspan=3)
div3_1.grid(column=0, row=2 , columnspan=3)
div3_2.grid(column=0, row=3 , columnspan=3)
div3_3.grid(column=0, row=4 , columnspan=3)
div3_4.grid(column=0, row=5 , columnspan=3)
div3_5.grid(column=0, row=6 , columnspan=3)
div3_6.grid(column=0, row=7 , columnspan=3)
div3_7.grid(column=0, row=8 , columnspan=3)
div3_8.grid(column=0, row=9 , columnspan=3)
div3_9.grid(column=0, row=10 , columnspan=3)

div6.grid(column=0, row=11)
div7.grid(column=1, row=11)
div8.grid(column=2, row=11)




 
#--------------分隔線---------------



#標題
title = tk.Label(window, text='竣任甜心陪聊機器人' , bg='#6FB7B7', fg='black', font=('Arial', 20))
title.grid(column=1, row=0)



#匯入圖片
imgju = Image.open('test.jpg')
imdog = Image.open('dog.jpg')
imwhite = Image.open('white.jpg')
imjuuse = ImageTk.PhotoImage(imgju.resize( (50, 50) ) )
imdoguse = ImageTk.PhotoImage(imdog.resize( (50, 50) ) )
imwhiteuse = ImageTk.PhotoImage(imwhite.resize((50,50)))




head = [imwhiteuse,imwhiteuse,imwhiteuse,imwhiteuse,imwhiteuse,imwhiteuse,imwhiteuse,imwhiteuse,imwhiteuse,imwhiteuse]
head2 = [imjuuse,imjuuse,imwhiteuse,imwhiteuse,imwhiteuse,imwhiteuse,imwhiteuse,imwhiteuse,imwhiteuse,imwhiteuse]


#大頭貼
head_0_1 = tk.Label(window, image=head[0], borderwidth=0)
head_0_1.grid(column=2, row=1)
head_0_2 = tk.Label(window, image=head2[0], borderwidth=0)
head_0_2.grid(column=0, row=1)

head_1_1 = tk.Label(window, image=head[1], borderwidth=0)
head_1_1.grid(column=2, row=2)
head_1_2 = tk.Label(window, image=head2[0], borderwidth=0)
head_1_2.grid(column=0, row=2)

head_2_1 = tk.Label(window, image=head[2], borderwidth=0)
head_2_1.grid(column=2, row=3)
head_2_2 = tk.Label(window, image=head2[2], borderwidth=0)
head_2_2.grid(column=0, row=3)

head_3_1 = tk.Label(window, image=head[3], borderwidth=0)
head_3_1.grid(column=2, row=4)
head_3_2 = tk.Label(window, image=head2[3], borderwidth=0)
head_3_2.grid(column=0, row=4)

head_4_1 = tk.Label(window, image=head[4], borderwidth=0)
head_4_1.grid(column=2, row=5)
head_4_2 = tk.Label(window, image=head2[4], borderwidth=0)
head_4_2.grid(column=0, row=5)

head_5_1 = tk.Label(window, image=head[5], borderwidth=0)
head_5_1.grid(column=2, row=6)
head_5_2 = tk.Label(window, image=head2[5], borderwidth=0)
head_5_2.grid(column=0, row=6)

head_6_1 = tk.Label(window, image=head[6], borderwidth=0)
head_6_1.grid(column=2, row=7)
head_6_2 = tk.Label(window, image=head2[6], borderwidth=0)
head_6_2.grid(column=0, row=7)

head_7_1 = tk.Label(window, image=head[7], borderwidth=0)
head_7_1.grid(column=2, row=8)
head_7_2 = tk.Label(window, image=head2[7], borderwidth=0)
head_7_2.grid(column=0, row=8)

head_8_1 = tk.Label(window, image=head[8], borderwidth=0)
head_8_1.grid(column=2, row=9)
head_8_2 = tk.Label(window, image=head2[8], borderwidth=0)
head_8_2.grid(column=0, row=9)

head_9_1 = tk.Label(window, image=head[9], borderwidth=0)
head_9_1.grid(column=2, row=10)
head_9_2 = tk.Label(window, image=head2[9], borderwidth=0)
head_9_2.grid(column=0, row=10)


'''
#歡迎詞
welcome_0 = tk.Label(window, text='歡迎來到竣任甜心陪聊機器人', bg='#FDFFFF', fg='#263238', font=('Arial', 16))
welcome_0.grid(column=1, row=1,  sticky=tk.W)
welcome_1 = tk.Label(window, text='請輸入指令', bg='#FDFFFF', fg='#263238', font=('Arial', 16))
welcome_1.grid(column=1, row=2, sticky=tk.W)
'''

chat = ['歡迎來到竣任甜心陪聊機器人','請輸入指令','','','','','','','','']


#輸入區
entry = tk.Entry()
entry.grid(column=1, row=11)


aling = [tk.W, tk.W, tk.E, tk.E, tk.E, tk.E, tk.E, tk.E, tk.E, tk.E]



#聊天區(10區)
chat_0 = tk.Label(window, text=chat[0], bg='#FDFFFF', fg='#263238', font=('Arial', 16))
chat_0.grid(column=1, row=1, sticky=aling[0])

chat_1 = tk.Label(window, text=chat[1], bg='#FDFFFF', fg='#263238', font=('Arial', 16))
chat_1.grid(column=1, row=2, sticky=aling[1])

chat_2 = tk.Label(window, text=chat[2], bg='#FDFFFF', fg='#263238', font=('Arial', 16))
chat_2.grid(column=1, row=3, sticky=aling[2])

chat_3 = tk.Label(window, text=chat[3], bg='#FDFFFF', fg='#263238', font=('Arial', 16))
chat_3.grid(column=1, row=4, sticky=aling[3])

chat_4 = tk.Label(window, text=chat[4], bg='#FDFFFF', fg='#263238', font=('Arial', 16))
chat_4.grid(column=1, row=5, sticky=aling[4])

chat_5 = tk.Label(window, text=chat[5], bg='#FDFFFF', fg='#263238', font=('Arial', 16))
chat_5.grid(column=1, row=6, sticky=aling[5])

chat_6 = tk.Label(window, text=chat[6], bg='#FDFFFF', fg='#263238', font=('Arial', 16))
chat_6.grid(column=1, row=7, sticky=aling[6])

chat_7 = tk.Label(window, text=chat[7], bg='#FDFFFF', fg='#263238', font=('Arial', 16))
chat_7.grid(column=1, row=8, sticky=aling[7])

chat_8 = tk.Label(window, text=chat[8], bg='#FDFFFF', fg='#263238', font=('Arial', 16))
chat_8.grid(column=1, row=9, sticky=aling[8])

chat_9 = tk.Label(window, text=chat[9], bg='#FDFFFF', fg='#263238', font=('Arial', 16))
chat_9.grid(column=1, row=10, sticky=aling[9])



i=2



#enter按鈕
def button():
    xx=entry.get()
    global i,head_0_1,head_1_1,head_2_1,head_3_1,head_4_1,head_5_1,head_6_1,head_7_1,head_8_1,head_9_1,head_0_2,head_1_2,head_2_2,head_3_2,head_4_2,head_5_2,head_6_2,head_7_2,head_8_2,head_9_2
    if i<10:
        chat[i]=entry.get()
        head[i]=imdoguse
        head2[i]=imwhiteuse
        aling[i]=tk.E
        
        
        head_0_1 = tk.Label(window, image=head[0], borderwidth=0)
        head_0_1.grid(column=2, row=1)
        head_0_2 = tk.Label(window, image=head2[0], borderwidth=0)
        head_0_2.grid(column=0, row=1)       
        head_1_1 = tk.Label(window, image=head[1], borderwidth=0)
        head_1_1.grid(column=2, row=2)
        head_1_2 = tk.Label(window, image=head2[1], borderwidth=0)
        head_1_2.grid(column=0, row=2)        
        head_2_1 = tk.Label(window, image=head[2], borderwidth=0)
        head_2_1.grid(column=2, row=3)
        head_2_2 = tk.Label(window, image=head2[2], borderwidth=0)
        head_2_2.grid(column=0, row=3)        
        head_3_1 = tk.Label(window, image=head[3], borderwidth=0)
        head_3_1.grid(column=2, row=4)
        head_3_2 = tk.Label(window, image=head2[3], borderwidth=0)
        head_3_2.grid(column=0, row=4)        
        head_4_1 = tk.Label(window, image=head[4], borderwidth=0)
        head_4_1.grid(column=2, row=5)
        head_4_2 = tk.Label(window, image=head2[4], borderwidth=0)
        head_4_2.grid(column=0, row=5)        
        head_5_1 = tk.Label(window, image=head[5], borderwidth=0)
        head_5_1.grid(column=2, row=6)
        head_5_2 = tk.Label(window, image=head2[5], borderwidth=0)
        head_5_2.grid(column=0, row=6)    
        head_6_1 = tk.Label(window, image=head[6], borderwidth=0)
        head_6_1.grid(column=2, row=7)
        head_6_2 = tk.Label(window, image=head2[6], borderwidth=0)
        head_6_2.grid(column=0, row=7)     
        head_7_1 = tk.Label(window, image=head[7], borderwidth=0)
        head_7_1.grid(column=2, row=8)
        head_7_2 = tk.Label(window, image=head2[7], borderwidth=0)
        head_7_2.grid(column=0, row=8)      
        head_8_1 = tk.Label(window, image=head[8], borderwidth=0)
        head_8_1.grid(column=2, row=9)
        head_8_2 = tk.Label(window, image=head2[8], borderwidth=0)
        head_8_2.grid(column=0, row=9)
        head_9_1 = tk.Label(window, image=head[9], borderwidth=0)
        head_9_1.grid(column=2, row=10)
        head_9_2 = tk.Label(window, image=head2[9], borderwidth=0)
        head_9_2.grid(column=0, row=10)
        
        chat_0.grid(column=1, row=1, sticky=aling[0])
        chat_1.grid(column=1, row=2, sticky=aling[1])
        chat_2.grid(column=1, row=3, sticky=aling[2])
        chat_3.grid(column=1, row=4, sticky=aling[3])
        chat_4.grid(column=1, row=5, sticky=aling[4])
        chat_5.grid(column=1, row=6, sticky=aling[5])
        chat_6.grid(column=1, row=7, sticky=aling[6])
        chat_7.grid(column=1, row=8, sticky=aling[7])
        chat_8.grid(column=1, row=9, sticky=aling[8])
        chat_9.grid(column=1, row=10, sticky=aling[9])
        chat_2.configure(text=chat[2])
        chat_3.configure(text=chat[3])
        chat_4.configure(text=chat[4])
        chat_5.configure(text=chat[5])
        chat_6.configure(text=chat[6])
        chat_7.configure(text=chat[7])
        chat_8.configure(text=chat[8])
        chat_9.configure(text=chat[9])
        
    else:
        chat.pop(0)
        chat.append(entry.get())
        
        aling.pop(0)
        aling.append(tk.E)
        
        head.pop(0)
        head2.pop(0)
        head.append(imdoguse)
        head2.append(imwhiteuse)
        
        head_0_1 = tk.Label(window, image=head[0], borderwidth=0)
        head_0_1.grid(column=2, row=1)
        head_0_2 = tk.Label(window, image=head2[0], borderwidth=0)
        head_0_2.grid(column=0, row=1)       
        head_1_1 = tk.Label(window, image=head[1], borderwidth=0)
        head_1_1.grid(column=2, row=2)
        head_1_2 = tk.Label(window, image=head2[1], borderwidth=0)
        head_1_2.grid(column=0, row=2)        
        head_2_1 = tk.Label(window, image=head[2], borderwidth=0)
        head_2_1.grid(column=2, row=3)
        head_2_2 = tk.Label(window, image=head2[2], borderwidth=0)
        head_2_2.grid(column=0, row=3)        
        head_3_1 = tk.Label(window, image=head[3], borderwidth=0)
        head_3_1.grid(column=2, row=4)
        head_3_2 = tk.Label(window, image=head2[3], borderwidth=0)
        head_3_2.grid(column=0, row=4)        
        head_4_1 = tk.Label(window, image=head[4], borderwidth=0)
        head_4_1.grid(column=2, row=5)
        head_4_2 = tk.Label(window, image=head2[4], borderwidth=0)
        head_4_2.grid(column=0, row=5)        
        head_5_1 = tk.Label(window, image=head[5], borderwidth=0)
        head_5_1.grid(column=2, row=6)
        head_5_2 = tk.Label(window, image=head2[5], borderwidth=0)
        head_5_2.grid(column=0, row=6)    
        head_6_1 = tk.Label(window, image=head[6], borderwidth=0)
        head_6_1.grid(column=2, row=7)
        head_6_2 = tk.Label(window, image=head2[6], borderwidth=0)
        head_6_2.grid(column=0, row=7)     
        head_7_1 = tk.Label(window, image=head[7], borderwidth=0)
        head_7_1.grid(column=2, row=8)
        head_7_2 = tk.Label(window, image=head2[7], borderwidth=0)
        head_7_2.grid(column=0, row=8)      
        head_8_1 = tk.Label(window, image=head[8], borderwidth=0)
        head_8_1.grid(column=2, row=9)
        head_8_2 = tk.Label(window, image=head2[8], borderwidth=0)
        head_8_2.grid(column=0, row=9)
        head_9_1 = tk.Label(window, image=head[9], borderwidth=0)
        head_9_1.grid(column=2, row=10)
        head_9_2 = tk.Label(window, image=head2[9], borderwidth=0)
        head_9_2.grid(column=0, row=10)
        chat_0.grid(column=1, row=1, sticky=aling[0])
        chat_1.grid(column=1, row=2, sticky=aling[1])
        chat_2.grid(column=1, row=3, sticky=aling[2])
        chat_3.grid(column=1, row=4, sticky=aling[3])
        chat_4.grid(column=1, row=5, sticky=aling[4])
        chat_5.grid(column=1, row=6, sticky=aling[5])
        chat_6.grid(column=1, row=7, sticky=aling[6])
        chat_7.grid(column=1, row=8, sticky=aling[7])
        chat_8.grid(column=1, row=9, sticky=aling[8])
        chat_9.grid(column=1, row=10, sticky=aling[9])
        chat_0.configure(text=chat[0])
        chat_1.configure(text=chat[1])
        chat_2.configure(text=chat[2])
        chat_3.configure(text=chat[3])
        chat_4.configure(text=chat[4])
        chat_5.configure(text=chat[5])
        chat_6.configure(text=chat[6])
        chat_7.configure(text=chat[7])
        chat_8.configure(text=chat[8])
        chat_9.configure(text=chat[9])
    
    i+=1   
    
    if(i<10):
        chat[i]=chatbot.get_response(xx)
        head[i]=imwhiteuse
        head2[i]=imjuuse
        aling[i]=tk.W
        
        head_0_1 = tk.Label(window, image=head[0], borderwidth=0)
        head_0_1.grid(column=2, row=1)
        head_0_2 = tk.Label(window, image=head2[0], borderwidth=0)
        head_0_2.grid(column=0, row=1)       
        head_1_1 = tk.Label(window, image=head[1], borderwidth=0)
        head_1_1.grid(column=2, row=2)
        head_1_2 = tk.Label(window, image=head2[1], borderwidth=0)
        head_1_2.grid(column=0, row=2)        
        head_2_1 = tk.Label(window, image=head[2], borderwidth=0)
        head_2_1.grid(column=2, row=3)
        head_2_2 = tk.Label(window, image=head2[2], borderwidth=0)
        head_2_2.grid(column=0, row=3)        
        head_3_1 = tk.Label(window, image=head[3], borderwidth=0)
        head_3_1.grid(column=2, row=4)
        head_3_2 = tk.Label(window, image=head2[3], borderwidth=0)
        head_3_2.grid(column=0, row=4)        
        head_4_1 = tk.Label(window, image=head[4], borderwidth=0)
        head_4_1.grid(column=2, row=5)
        head_4_2 = tk.Label(window, image=head2[4], borderwidth=0)
        head_4_2.grid(column=0, row=5)        
        head_5_1 = tk.Label(window, image=head[5], borderwidth=0)
        head_5_1.grid(column=2, row=6)
        head_5_2 = tk.Label(window, image=head2[5], borderwidth=0)
        head_5_2.grid(column=0, row=6)    
        head_6_1 = tk.Label(window, image=head[6], borderwidth=0)
        head_6_1.grid(column=2, row=7)
        head_6_2 = tk.Label(window, image=head2[6], borderwidth=0)
        head_6_2.grid(column=0, row=7)     
        head_7_1 = tk.Label(window, image=head[7], borderwidth=0)
        head_7_1.grid(column=2, row=8)
        head_7_2 = tk.Label(window, image=head2[7], borderwidth=0)
        head_7_2.grid(column=0, row=8)      
        head_8_1 = tk.Label(window, image=head[8], borderwidth=0)
        head_8_1.grid(column=2, row=9)
        head_8_2 = tk.Label(window, image=head2[8], borderwidth=0)
        head_8_2.grid(column=0, row=9)
        head_9_1 = tk.Label(window, image=head[9], borderwidth=0)
        head_9_1.grid(column=2, row=10)
        head_9_2 = tk.Label(window, image=head2[9], borderwidth=0)
        head_9_2.grid(column=0, row=10)
        
        chat_0.grid(column=1, row=1, sticky=aling[0])
        chat_1.grid(column=1, row=2, sticky=aling[1])
        chat_2.grid(column=1, row=3, sticky=aling[2])
        chat_3.grid(column=1, row=4, sticky=aling[3])
        chat_4.grid(column=1, row=5, sticky=aling[4])
        chat_5.grid(column=1, row=6, sticky=aling[5])
        chat_6.grid(column=1, row=7, sticky=aling[6])
        chat_7.grid(column=1, row=8, sticky=aling[7])
        chat_8.grid(column=1, row=9, sticky=aling[8])
        chat_9.grid(column=1, row=10, sticky=aling[9])
        chat_2.configure(text=chat[2])
        chat_3.configure(text=chat[3])
        chat_4.configure(text=chat[4])
        chat_5.configure(text=chat[5])
        chat_6.configure(text=chat[6])
        chat_7.configure(text=chat[7])
        chat_8.configure(text=chat[8])
        chat_9.configure(text=chat[9])
    else:
        chat.pop(0)
        chat.append(chatbot.get_response(xx))
        
        aling.pop(0)
        aling.append(tk.W)
        
        head.pop(0)
        head2.pop(0)
        head.append(imwhiteuse)
        head2.append(imjuuse)
        
        head_0_1 = tk.Label(window, image=head[0], borderwidth=0)
        head_0_1.grid(column=2, row=1)
        head_0_2 = tk.Label(window, image=head2[0], borderwidth=0)
        head_0_2.grid(column=0, row=1)       
        head_1_1 = tk.Label(window, image=head[1], borderwidth=0)
        head_1_1.grid(column=2, row=2)
        head_1_2 = tk.Label(window, image=head2[1], borderwidth=0)
        head_1_2.grid(column=0, row=2)        
        head_2_1 = tk.Label(window, image=head[2], borderwidth=0)
        head_2_1.grid(column=2, row=3)
        head_2_2 = tk.Label(window, image=head2[2], borderwidth=0)
        head_2_2.grid(column=0, row=3)        
        head_3_1 = tk.Label(window, image=head[3], borderwidth=0)
        head_3_1.grid(column=2, row=4)
        head_3_2 = tk.Label(window, image=head2[3], borderwidth=0)
        head_3_2.grid(column=0, row=4)        
        head_4_1 = tk.Label(window, image=head[4], borderwidth=0)
        head_4_1.grid(column=2, row=5)
        head_4_2 = tk.Label(window, image=head2[4], borderwidth=0)
        head_4_2.grid(column=0, row=5)        
        head_5_1 = tk.Label(window, image=head[5], borderwidth=0)
        head_5_1.grid(column=2, row=6)
        head_5_2 = tk.Label(window, image=head2[5], borderwidth=0)
        head_5_2.grid(column=0, row=6)    
        head_6_1 = tk.Label(window, image=head[6], borderwidth=0)
        head_6_1.grid(column=2, row=7)
        head_6_2 = tk.Label(window, image=head2[6], borderwidth=0)
        head_6_2.grid(column=0, row=7)     
        head_7_1 = tk.Label(window, image=head[7], borderwidth=0)
        head_7_1.grid(column=2, row=8)
        head_7_2 = tk.Label(window, image=head2[7], borderwidth=0)
        head_7_2.grid(column=0, row=8)      
        head_8_1 = tk.Label(window, image=head[8], borderwidth=0)
        head_8_1.grid(column=2, row=9)
        head_8_2 = tk.Label(window, image=head2[8], borderwidth=0)
        head_8_2.grid(column=0, row=9)
        head_9_1 = tk.Label(window, image=head[9], borderwidth=0)
        head_9_1.grid(column=2, row=10)
        head_9_2 = tk.Label(window, image=head2[9], borderwidth=0)
        head_9_2.grid(column=0, row=10)
        chat_0.grid(column=1, row=1, sticky=aling[0])
        chat_1.grid(column=1, row=2, sticky=aling[1])
        chat_2.grid(column=1, row=3, sticky=aling[2])
        chat_3.grid(column=1, row=4, sticky=aling[3])
        chat_4.grid(column=1, row=5, sticky=aling[4])
        chat_5.grid(column=1, row=6, sticky=aling[5])
        chat_6.grid(column=1, row=7, sticky=aling[6])
        chat_7.grid(column=1, row=8, sticky=aling[7])
        chat_8.grid(column=1, row=9, sticky=aling[8])
        chat_9.grid(column=1, row=10, sticky=aling[9])
        chat_0.configure(text=chat[0])
        chat_1.configure(text=chat[1])
        chat_2.configure(text=chat[2])
        chat_3.configure(text=chat[3])
        chat_4.configure(text=chat[4])
        chat_5.configure(text=chat[5])
        chat_6.configure(text=chat[6])
        chat_7.configure(text=chat[7])
        chat_8.configure(text=chat[8])
        chat_9.configure(text=chat[9])

    i+=1
    


btn = tk.Button(window, text='ENTER', command=button, font=('Arial', 12))
btn.grid(column=2, row=11)




window.mainloop()