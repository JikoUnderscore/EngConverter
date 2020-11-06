# # # with open('cmuwords.txt', "r", encoding='utf-8') as file:
# # #     list = file.read().split()
# # #
# # # with open('cmuphomes.txt', "r", encoding='utf-8') as file2:
# # #     list_out = file2.read().split()
# # #
# #
# #
# # list_in = ['i', 'am', 'a', 'cat']
# #
# # list_out = ['ie',  'äm', 'ə', 'cät']
# #
# #
# #
# # prv_izrecenie = input("Enter text? \n>").lower().split() #обработва първичен текст от потребитела
# #
# # broj_dumi = int(len(prv_izrecenie))         #броя да думи
# #
# #
# #
# #
# # recnik_out = dict(enumerate(list_out))
# # recnik = {k: v for v, k in enumerate(list_in)}
# #
# #
# #
# # recnik_out[0] = f"{recnik_out.get(0)}/ye"
# # print(f"{recnik_out=}")
# #
# # kraj = ""
# # kraj2 = ""
# # for x in range(broj_dumi):               #Проверява броя думи. Взима им индекса и го сравнява с индикса на изходящият списък. Извлича думата от изходящият индекс
# #     word = prv_izrecenie[x]
# #     wordnumber = (recnik.get(word))
# #     eat_word = (recnik_out.get(wordnumber))
# #     kraj2 += eat_word + " "
# #
# #     if word in list_in:
# #         indeksnaduma = list_in.index(word)
# #         novduma = list_out[indeksnaduma]
# #         kraj += novduma + " "
# #     else:
# #         print('not ok')
# #
# # print(f"list method: {kraj}")
# # print(f"dic method: {kraj2}")
# #
# # #
# # #
# # #
# # # with open('pet.txt', "r", encoding='utf-8') as file_nocool:
# # #     list = file_nocool.read()
# # #
# # # with open('coolpet.txt', "r", encoding='utf-8') as file_cool:
# # #     cool_list = file_cool.read()
# # #
# # #
# # # ko = input('teck for a word: \n>')
# # #
# # # if ko in list:
# # #     print(list)
# # #
# # #
# #
# # #
# # # with open('data/New folder/cmu_words2.txt', "r", encoding='utf-8') as file:
# # #     list_in = file.read().split()
# # #
# # # with open('data/New folder/cmuphomesCopy2.txt', "r", encoding='utf-8') as file2:
# # #     list_out = file2.read().split()
# # #
# # # # recnik_out = dict(enumerate(list_out))
# # # # recnik = {k: v for v, k in enumerate(list_in)}
# # # # def seart(myDict, seart1):
# # # #     seart = ""
# # # #     for key, value in myDict.items():
# # # #         if seart1 in key:
# # # #             seart += key
# # # #             print(value)
# # # #             return seart
# # # #
# # # # print(seart(recnik, 'baba(1)'))
# # #
# # # matters = ['(1)', '(2)']
# # # # matting = [s for s in list_in if any(xs in s for xs in matters)]
# # #
# # # if any(matters) in list_in:
# # #     print('found')
# # # else:
# # #     print('not found')
# # #
# #
# #
# # # list_in = ['abducting', 'abducting(1)', 'abduction', 'abduction(1)', 'abductions', 'abductions(1)', 'abductor', 'abductor(1)', 'abductors', 'abductors(1)', 'abducts', 'abdul', 'abdulaziz', 'abdulla', 'abdullah', 'abe']
# # #
# # # list_out = ['ÆBDʌKTIÑ',  'əBDʌKTIÑ',    'ÆBDʌKʃəN',   'əBDʌKʃəN',     'ÆBDʌKʃəNZ',   'əBDʌKʃəNZ',   'ÆBDʌKT©',   'əBDʌKT©',    'ÆBDʌKT©Z',    'əBDʌKT©Z',   'ÆBDʌKTS',  'ÆBDÚL', 'ÆBDÚLəZÏZ', 'ɒBDÚLə', 'ÆBDʌLə',   'ÉB']
# # #
# #
# #
#
# cislo = 49562546250
#
# print(f"tova e cisloto {type(cislo)} = {cislo}")
#
#
# class tekstovne(object):
#
#     def _na(self, *args):
#         print(self)
#         txt = args
#         osnova = f"{txt}"
#         return osnova
#
#     def na(*args):
#         o = f"{args}"
#         return o[1:-1]
#
#
#
# tip = tekstovne()                                        # str()
# nov_tkst = tekstovne.na(25252,25252,2528)                 # str(cislo)
#
#
#
# print(f"vece e texk {type(tip)} = {nov_tkst}")
#
#
#
# from tkinter import *
#
# root = Tk()
#
#
# class App:
#     def __init__(self, master):
#         scrollbar = Scrollbar(master, orient=VERTICAL)
#         self.b1 = Text(master, yscrollcommand=scrollbar.set)
#         self.b2 = Text(master, yscrollcommand=scrollbar.set)
#         scrollbar.config(command=self.yview)
#         scrollbar.pack(side=RIGHT, fill=Y)
#         self.b1.pack(side=LEFT, fill=BOTH, expand=1)
#         self.b2.pack(side=LEFT, fill=BOTH, expand=1)
#
#     def yview(self, *args):
#         self.b1.yview(*args)
#         self.b2.yview(*args)
#
#
# app = App(root)
# for item in range(0, 40):
#     for i in range(item):
#         it = str(i) + ' '
#         app.b1.insert(1.0, it)
#         app.b2.insert(1.0, it)
#     app.b1.insert(1.0, '\n')
#     app.b2.insert(1.0, '\n')
#
# root.mainloop()

from tqdm import tqdm
from time import sleep
from tkinter import *



# with tqdm(total=100) as pogrbr:
#     for i in range(10):
#         sleep(0.2)
#         pogrbr.update(10)
#     print('10 % kod')

from lenta import LentaGUI


def start():
    win.destroy()
    def useit(x):
        herer = Toplevel()
        lnt = LentaGUI(x, herer)
        for i in range(x):
            print('zzz for 0.1 seconds for the', i, 'time')
            sleep(0.1)
            lnt.update_with(i+1)
        herer.destroy()

    def getshit():
        nm = int(entt.get())
        useit(nm)

    root = Tk()
    dfg = Label(root, text='start working')
    dfg.pack()
    root.geometry("200x100")
    varrr = StringVar()
    entt = Entry(root, text='type a num')
    entt.pack()
    entt.insert(END,'10')

    Button(root,text='get shit done', command=getshit).pack()

win = Tk()

bar = LentaGUI(10,win)
bar.update_with(1)
bar.update_with(0)
sleep(1.0)
print('here1')
bar.update_with(1)
sleep(1.0)
bar.update_with(9.6)

sleep(1.0)
print('here2')
bar.update_with(4.2)

sleep(1.0)
print('here3')
bar.update_with(6.9)

sleep(1.0)
print('here4')
bar.update_with(4.2)
bar.update_with(0)
sleep(0.5)
bar.update_with(9.9)
sleep(0.5)
bar.update_with(0)
sleep(0.5)
bar.update_with(9.9)
sleep(0.5)
bar.update_with(0)
sleep(1.0)
print('here5')
bar.update_with(6.9)
sleep(0.5)
bar.update_with(10)
win.after(1, start())





win.mainloop()




