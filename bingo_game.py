from tkinter import *
import tkinter.font
import PIL
from PIL import ImageTk, Image , ImageDraw
import random
import time
import threading
from functools import partial
import pygame

root = Tk()
root.title("빙고게임")
root.geometry("1024x750")
root.configure(bg = 'white')
font = tkinter.font.Font(family = "맑은고딕", size = 30, weight = "bold")
big_font = tkinter.font.Font(family = "맑은고딕", size = 140, weight = "bold")
btn_font = tkinter.font.Font(family="맑은 고딕", size=10 , weight = "bold")
bingo_image = Image.open("./image/bingo.png")
bingo_image = bingo_image.resize((200,80), PIL.Image.ANTIALIAS)
bingo_image = ImageTk.PhotoImage(bingo_image)


list_image = Image.open("./image/list.png")
list_image = list_image.resize((200,60), PIL.Image.ANTIALIAS)
list_image = ImageTk.PhotoImage(list_image)

Label(root, text = " ",bg = "white").grid(row =0, column = 0)


##-----------------------------sample make ----------------------------------------
global sampleList
global count
global set_list
set_list = []
count = 0

def command_args(arg):
    global get_range
    get_range = arg

## random generate의 경우에는 1~75까지의 숫자를 random하게 배치한다.
def random_generate():
    global sampleList
    list = []
    for i in range(75):
        list.append(i+1)
    sampleList= random.sample(list,75)

## reset의 경우 전체 sampleList를 초기화 시키고 set_list또한 초기화 시킴
def reset():
    global count
    global set_list
    random_generate()
    for i in range(0,count):
        globals()['Num{}'.format(i)]["text"] = " "
        globals()['Num{}'.format(i)]["image"] = photo_b
    set_list = []
    random_num["text"] = " "
    count = 0
    for i in range(0,25):
        globals()['button{}'.format(i)]["bg"] = "white"

    btn_get_num_1["state"] = tkinter.NORMAL
    btn_get_num_2["state"] = tkinter.NORMAL
    btn_get_num_3["state"] = tkinter.NORMAL
    btn_get_num_4["state"] = tkinter.NORMAL
    btn_get_num_0["state"] = tkinter.NORMAL


pygame.mixer.init()

## set num == 번호뽑기를 통해서 random한 번호를 추출하기
def get_num():
    global sampleList
    global set_list
    global count
    temp = 10
    btn_get_num["state"] = tkinter.DISABLED
    count_list = random.sample(sampleList,10)
    pygame.mixer.music.load("./image/1.mp3")
    pygame.mixer.music.play()
    while temp:
        time.sleep(0.1)
        random_num["text"] = sampleList[temp]
        random_num.update()
        temp -= 1
    pygame.mixer.music.stop()
    pygame.mixer.music.load("./image/2.mp3")
    pygame.mixer.music.play()
    globals()['Num{}'.format(count)]["image"] = photo
    set_list.append(sampleList[count])
    set_list.sort()
    for i in range(0,count+1):
        globals()['Num{}'.format(i)]["text"] = set_list[i]
    random_num["text"] = sampleList[count]
    count += 1
    btn_get_num["state"] = tkinter.NORMAL

def get_rangenum(range_num):
    global sampleList
    global set_list
    global count
    temp = 10
    buf = 0
    eval(f"btn_get_num_{range_num}")['state'] = tkinter.DISABLED
    count_list = random.sample(sampleList,10)
    pygame.mixer.music.load("./image/1.mp3")
    pygame.mixer.music.play()
    while temp:
        time.sleep(0.1)
        random_num["text"] = sampleList[temp]
        random_num.update()
        temp -= 1
    pygame.mixer.music.stop()
    pygame.mixer.music.load("./image/2.mp3")
    pygame.mixer.music.play()

    print(count)

    for i in range(count,75):
            ## 나눈 결과의 몫을 가져오므로 range 구분이 가능함
        if((sampleList[i]) // 15 == range_num):
            temp = sampleList[i]
            sampleList[i] = sampleList[count]
            sampleList[count] = temp
            random_num["text"] = sampleList[count]
            set_list.append(sampleList[count])
            set_list.sort()
            globals()['Num{}'.format(count)]["image"] = photo
            count += 1
            break;
        elif(i == 74):
            random_num["text"] = "-"
            eval(f"btn_get_num_{range_num}")['state'] = tkinter.DISABLED
            return

    for i in range(0,count):
        globals()['Num{}'.format(i)]["text"] = set_list[i]

    eval(f"btn_get_num_{range_num}")['state'] = tkinter.NORMAL


## 프로그램이 시작하면 기본적으로 random_generate를 실행
random_generate()


## -----------------------   frmae ------------------------------------------------------

frame_button = Frame(root, relief="solid",bg = "white")
frame_button.grid(row = 1, column =1)

frame_board = Frame(root, relief="solid", bd = 5,bg = "white")
frame_board.grid(row = 1, column = 2,columnspan = 5)


Label(root, image = list_image,bg = "white",font = font).grid(row =4, column = 0,columnspan = 2)
frame_numlist = Frame(root, relief="solid", bd = 2,bg = "white")
frame_numlist.grid(row = 5,column=0, columnspan=5)

##-------------------------------------------------------------------------------------
big_photo = PhotoImage(file = "./image/b.png")
random_num = Label(root,text = " ",image = big_photo,bg = "white",font = big_font)
random_num.grid(row = 1,column = 0)
random_num["compound"] = "center"

##--------------------------------- frame board----------------------------------------

def bt_c1(k):
    if globals()['button{}'.format(k)]["bg"] == "white":
        globals()['button{}'.format(k)]["bg"] = "blue"
    else:
        globals()['button{}'.format(k)]["bg"] = "white"
    print( globals()['button{}'.format(k)]["bg"])

k = 0
for i in range(5):
    globals()['button{}'.format(i)] = Button(frame_board, padx = 30, pady = 30, text = "  ", bg = "white", borderwidth = 2)
    globals()['button{}'.format(i)].grid(row = 1, column = k)
    globals()['button{}'.format(i)].configure(command = partial(bt_c1,i))
    Label(frame_board, text = "\n\n",bg = "white").grid(row =1, column = k+1)
    k = k+2

Label(frame_board, text = " ",bg = "white").grid(row =2, column = 1,columnspan = 9)

k = 0
for i in range(5,10):
    globals()['button{}'.format(i)] = Button(frame_board, padx = 30, pady = 30, text = "  ", bg = "white", borderwidth = 2)
    globals()['button{}'.format(i)].grid(row = 3, column = k)
    globals()['button{}'.format(i)].configure(command = partial(bt_c1,i))
    Label(frame_board, text = "\n\n",bg = "white").grid(row =3, column = k+1)
    k = k+2

Label(frame_board, text = " ",bg = "white").grid(row =4, column = 1,columnspan = 9)

k = 0
for i in range(10,15):
    globals()['button{}'.format(i)] = Button(frame_board, padx = 30, pady = 30, text = "  ", bg = "white", borderwidth = 2)
    globals()['button{}'.format(i)].grid(row = 5, column = k)
    globals()['button{}'.format(i)].configure(command = partial(bt_c1,i))
    Label(frame_board, text = "\n\n",bg = "white").grid(row =5, column = k+1)
    k = k+2

Label(frame_board, text = " ",bg = "white").grid(row =6, column = 1,columnspan = 9)

k = 0
for i in range(15,20):
    globals()['button{}'.format(i)] = Button(frame_board, padx = 30, pady = 30, text = "  ", bg = "white", borderwidth = 2)
    globals()['button{}'.format(i)].grid(row = 7, column = k)
    globals()['button{}'.format(i)].configure(command = partial(bt_c1,i))
    Label(frame_board, text = "\n\n",bg = "white").grid(row =7, column = k+1)
    k = k+2

Label(frame_board, text = " ",bg = "white").grid(row =8, column = 1,columnspan = 9)

k = 0
for i in range(20,25):
    globals()['button{}'.format(i)] = Button(frame_board, padx = 30, pady = 30, text = "  ", bg = "white", borderwidth = 2)
    globals()['button{}'.format(i)].grid(row = 9, column = k)
    globals()['button{}'.format(i)].configure(command = partial(bt_c1,i))
    Label(frame_board, text = "\n\n",bg = "white").grid(row =9, column = k+1)
    k = k+2


##  ----------------------------  frame button  -----------------------------------------

btn_get_num = Button(frame_button,padx=50,pady=10,font=btn_font,bg="#FDF5E6",fg="#464646" ,relief="ridge"  ,text = "번호 뽑기",command = get_num)
btn_get_num.grid(row = 1, column=0,columnspan=4)

Label(frame_button, text = "\n",bg = "white").grid(row =2, column = 0)

reset_board = Button(frame_button,padx=5,pady=10, font=btn_font,bg="#FDF5E6",fg="#464646" ,relief="ridge",text = "   지우기   ",command = reset)
reset_board.grid(row = 3, column = 0,columnspan=4)


Label(frame_button, text = "\n",bg = "white").grid(row =4, column = 0)

btn_get_num_0 = Button(frame_button,padx=4,pady=10, font=btn_font,bg="#FDF5E6",fg="#464646" ,relief="ridge", text = "  첫번째줄  ",command = lambda : get_rangenum(0))
btn_get_num_0.grid(row = 5, column=0)
btn_get_num_1 = Button(frame_button,padx=4,pady=10, font=btn_font,bg="#FDF5E6",fg="#464646" ,relief="ridge", text = " 두번째줄 ",command = lambda : get_rangenum(1))
btn_get_num_1.grid(row = 5, column=1)
btn_get_num_2 = Button(frame_button,padx=4,pady=10, font=btn_font,bg="#FDF5E6",fg="#464646" ,relief="ridge", text = " 세번째줄 ",command = lambda : get_rangenum(2))
btn_get_num_2.grid(row = 5, column=2)
btn_get_num_3 = Button(frame_button,padx=4,pady=10, font=btn_font,bg="#FDF5E6",fg="#464646" ,relief="ridge", text = " 네번째줄 ",command = lambda : get_rangenum(3))
btn_get_num_3.grid(row = 5, column=3)
btn_get_num_4 = Button(frame_button,padx=4,pady=10, font=btn_font,bg="#FDF5E6",fg="#464646" ,relief="ridge", text = " 다섯번째줄 ",command = lambda : get_rangenum(4))
btn_get_num_4.grid(row = 6, column=0)



## Label(frame_button, text = "\n\n\n\n\n\n",bg = "white").grid(row =4, column = 0)

Label(frame_button,font = font,bg = "white",image = bingo_image).grid(row=0,column = 0,columnspan=3)


##------------------------------------------list------------------------------------------


photo = Image.open("./image/num.png")
photo = photo.resize((50,50), PIL.Image.ANTIALIAS)
photo = ImageTk.PhotoImage(photo)

photo_b = Image.open("./image/num_b.png")
photo_b = photo_b.resize((50,50), PIL.Image.ANTIALIAS)
photo_b = ImageTk.PhotoImage(photo_b)

random_num.config(image = big_photo)


for i in range(25):
    globals()['Num{}'.format(i)] = Label(frame_numlist, text = " " ,image = photo_b,font = font,bg = "white")
    globals()['Num{}'.format(i)].grid(row = 0, column = i)
    globals()['Num{}'.format(i)]["compound"] = "center"
for i in range(25,50):
    globals()['Num{}'.format(i)] = Label(frame_numlist, text = " " ,image = photo_b,font = font,bg = "white")
    globals()['Num{}'.format(i)].grid(row = 1, column = i-25)
    globals()['Num{}'.format(i)]["compound"] = "center"
for i in range(50,75):
    globals()['Num{}'.format(i)] = Label(frame_numlist, text = " " ,image = photo_b,font = font,bg = "white")
    globals()['Num{}'.format(i)].grid(row = 2, column = i-50)
    globals()['Num{}'.format(i)]["compound"] = "center"

##--------------------------------------------------------------------------------------------------
root.mainloop()
