from tkinter import *
from tkinter import (messagebox, filedialog, colorchooser)
import re
import win32com.client as wc
from threading import Timer
import subprocess as subpc
from datetime import datetime
import os


def zaseci(f):
    from time import time
    def wrp(*args, **kwargs):
        start = time()
        rf = f(*args, **kwargs)
        total = time() - start
        print("RUN TIME:", total)
        return rf
    return wrp

class PrevodGovor:

    def govorene(self):
        speaker_number = 3
        spk = wc.Dispatch("SAPI.SpVoice")
        vcs = spk.GetVoices()
        # print(vcs.Item(speaker_number).GetAttribute("Name"))  # speaker name
        spk.Voice
        spk.SetVoice(vcs.Item(speaker_number))
        spk.Speak(mw.ent_txt.get("1.0", 'end-1c'))

    def prevod(self):
        kraj = ""
        try:
            pyrvicen_tekst = mw.ent_txt.get("0.0", 'end-1c').lower()

            with open('data/dumi.txt', "r", encoding='utf-8') as file:
                recnik = {k: v for v, k in enumerate(file.read().split())}

            with open('data/fonemi.txt', "r", encoding='utf-8') as file2:
                recnik_out = dict(enumerate(file2.read().split()))

            punctuation = '''"'!@#█$%^&*(){}[]|._-`/?:;\,~ \n'''

            spisyk_ot_dumi = re.findall(r"[\w']+|\W", str(pyrvicen_tekst))

            broj_dumi = int(len(spisyk_ot_dumi))

            for x in range(broj_dumi):
                word = spisyk_ot_dumi[x]
                # print(f'{word=}')
                if word in punctuation:
                    kraj += word
                else:
                    wordnumber = (recnik.get(word))
                    each_word = (recnik_out.get(wordnumber))
                    if each_word is None:
                        ss = ""
                        ss += word + '\n'
                        with open("MISSING_WORDS/word_dump.txt", "a+") as f:
                            f.write(ss)

                        with open("MISSING_WORDS/missing_word_list.txt", "w") as fw:
                            ff = open("MISSING_WORDS/word_dump.txt", "r")
                            fw.writelines(set(ff))
                        kraj += '█' + word + '█'
                    else:
                        from checkboxes import chw
                        if chw.nsp19.get() == 1:
                            print('checked')
                            z = bool(re.compile(r"(se(s1$|s2$|s3$|$|s))|(ss$)|(ce$)").findall(word))
                            zs = bool(each_word.endswith('S'))

                            if z and zs is True:
                                print('in')
                                kraj += each_word + 'S'
                            elif z is True:
                                if '/' in each_word:
                                    print('/in2', each_word)
                                    spl = each_word.split('/')
                                    for index, wrd in enumerate(spl, start=1):  # XɔRSəZ/XɔRSIZ
                                        print(index)
                                        newstr = wrd[::-1].replace("S"[::-1], "SS"[::-1], 1)[::-1]
                                        if index < len(spl):
                                            kraj += newstr + '/'
                                        else:
                                            kraj += newstr
                                else:
                                    print('in2', each_word)
                                    kraj += each_word
                            else:
                                print('out')
                                kraj += each_word
                        else:
                            print('not checked')
                            kraj += each_word

            return kraj
        except Exception as err:
            # mw.textbox2.insert(0.0, err)
            kraj += f" \n ERROR: {err}."
            return kraj

    @zaseci
    def prevod2(self, *args):

        try:

            from checkboxes import chw

            ogtext = self.prevod()

            p043 = re.sub('ɛR', chw.air(), ogtext)
            p044 = re.sub('ɒR', chw.ar(), p043)
            p045 = re.sub('IR', chw.eer(), p044)
            p046 = re.sub('ɔR', chw.oor(), p045)

            p047 = re.sub(r'([©BDGLMNVÝəIÑ])(Z\b)', fr'\1{chw.sp_esz()}', p046)

            p1 = re.sub('ɒ', chw.ch1(), p047)
            p2 = re.sub('Æ', chw.ch2(), p1)
            p3 = re.sub('ʌ', chw.ch3(), p2)
            p4 = re.sub('ɔ', chw.ch4(), p3)
            p501 = re.sub('(Á)(NT|ND|T)', fr"{chw.sp_oundt()}\2", p4)
            p5 = re.sub('Á', chw.ch5(), p501)
            p6 = re.sub('Í', chw.ch6(), p5)
            p7 = re.sub('B', chw.ch7(), p6)
            p8 = re.sub('Ç', chw.ch8(), p7)
            p9 = re.sub('D', chw.ch9(), p8)
            p10 = re.sub('Ð', chw.ch10(), p9)
            p11 = re.sub('ɛ', chw.ch11(), p10)
            p12 = re.sub('®', chw.ch12(), p11)

            p13 = re.sub('(É)(\W)', fr"{chw.ch13()}\2", p12)
            p1301 = re.sub('(É)(\w)', fr"{chw.ch1301()}\2", p13)
            p14 = re.sub('F', chw.ch14(), p1301)
            p15 = re.sub('G', chw.ch15(), p14)
            p16 = re.sub('X', chw.ch16(), p15)
            p17 = re.sub('I', chw.ch17(), p16)
            p18 = re.sub('Ï', chw.ch18(), p17)
            p19 = re.sub('J', chw.ch19(), p18)
            p20 = re.sub('K', chw.ch20(), p19)
            p21 = re.sub('L', chw.ch21(), p20)
            p22 = re.sub('M', chw.ch22(), p21)
            p23 = re.sub('N', chw.ch23(), p22)
            p24 = re.sub('Ñ', chw.ch24(), p23)
            p25 = re.sub('Ö', chw.ch25(), p24)
            p26 = re.sub(r'(µ)(\W)', fr"{chw.ch26()}\2", p25)
            p2601 = re.sub(r'(µ)(\w)', fr"{chw.ch2601()}\2", p26)
            p27 = re.sub('P', chw.ch27(), p2601)
            p28 = re.sub('R', chw.ch28(), p27)
            p29 = re.sub('S', chw.ch29(), p28)
            p30 = re.sub('ʃ', chw.ch30(), p29)
            p31 = re.sub('T', chw.ch31(), p30)
            p32 = re.sub('θ', chw.ch32(), p31)
            p33 = re.sub('U', chw.ch33(), p32)
            p34 = re.sub('Ú', chw.ch34(), p33)
            p35 = re.sub('V', chw.ch35(), p34)

            p36 = re.sub('W', chw.ch36(), p35)
            p37 = re.sub('Y', chw.ch37(), p36)
            p38 = re.sub('Z', chw.ch38(), p37)
            p39 = re.sub('ʒ', chw.ch39(), p38)
            p40 = re.sub('Ý', chw.ch40(), p39)
            p41 = re.sub('©', chw.ch42(), p40)

            pl1 = re.sub('kw', chw.sp_kw(), p41)
            pl2 = re.sub('ngk', chw.sp_ngk(), pl1)
            pl3 = re.sub(r'oa\b', fr"{chw.sp_ago()}", pl2)
            pl4 = re.sub(r'(\w)(yoo)', fr"\1{chw.sp_yoo()}", pl3)
            pl5 = re.sub(fr"({chw.ch20()})([a|əouärtl])", fr"{chw.sp_ka_ko_ku()}\2", pl4)
            pl6 = re.sub(r'sh(\w)(.)\b', fr"{chw.sp_tion()}\2", pl5)
            pl7 = re.sub(r'zh(\w)(.)\b', fr"{chw.sp_sion()}\2", pl6)
            pl8 = re.sub(r'([əouwieya])r([əouwieya])', fr"\1{chw.sp_orro()}\2", pl7)
            pl9 = re.sub(r'(gz)(\w)', fr"{chw.sp_egzx()}\2", pl8)
            pl10 = re.sub(r'\bə', fr"{chw.sp_a_bout()}", pl9)
            pl11 = re.sub(r'([a-z][a-z][a-z])(ə\b)', fr"\1{chw.sp_sof_a()}", pl10)
            pl12 = re.sub(r'ks(\w)', fr'{chw.sp_kxs()}\1', pl11)
            pl13 = re.sub(r'ɣ', chw.sp_x_end(), pl12)

            p41001 = re.sub('ə', chw.ch41(), pl13)
            p41002 = re.sub(r'\büv\b', fr'{chw.sp_offme()}', p41001)
            p41003 = re.sub(r"ʔћ", chw.sp_eedd(), p41002)
            p41004 = re.sub(r"ђ", chw.sp_ett(), p41003)
            p41005 = re.sub(r"ћ", chw.sp_edd(), p41004)

                # TODO: " 's " da se izpisva v prevoda, i da moze da se promenja. Zamestvane v fajla ili nov kod
                # TODO: "ss,se,ce," v kraja da dumata da se oromenjat v "ss"

            nummmm = mw.remove_dash()
            regex = r"(\w+)(/(\w+))(/(\w+)/)((\w+))|(\w+)(/(\w+))(/(\w+))|(\w+)(/(\w+))"
            if nummmm == 0:
                ogtext1 = p41005
            elif nummmm == 3:
                ogtext1 = re.sub(regex, r"\1\8\13", p41005)
            elif nummmm == 2:
                ogtext1 = re.sub(regex, r"\3\10\15", p41005)
            elif nummmm == 4:
                ogtext1 = re.sub(regex, r"\5\12\15", p41005)
            elif nummmm == 1:
                ogtext1 = re.sub(regex, r"\7\12\15", p41005)

            # removing_extra_spaces = re.sub("([a-z]|[A-Z])\s([.,!?:;█])", r"\1\2", pl4)

            end_text = re.sub("(^|[.\n?!])\s*([a-zA-Z])", lambda p: p.group(0).upper(), ogtext1)

            mw.textbox2.delete(0.0, END)
            mw.textbox2.insert(0.0, end_text)
            return "break"
        except Exception as ero:
            mw.textbox2.insert(0.0, ero)


class MenuBar:
    def __init__(self, rodi):
        menubar = Menu(rodi.window)
        rodi.window.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Save rules', accelerator="Ctrl+S", command=self.seva_now)
        filemenu.add_command(label='Show in explorer save folder', command=self.seva_folder)
        filemenu.add_separator()
        filemenu.add_command(label='Save rules as...', command=self.save_var)
        filemenu.add_command(label='Load rules as...', command=self.load_var)
        filemenu.add_separator()
        filemenu.add_command(label='Open...', command=rodi.open_new)
        filemenu.add_command(label='Save output txt as...',)  # TODO: napravi koda tuka
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda: root.destroy())
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", accelerator="Ctrl+X",
                             command=lambda: root.focus_get().event_generate('<<Cut>>'))
        editmenu.add_command(label="Copy", accelerator="Ctrl+C",
                             command=lambda: root.focus_get().event_generate('<<Copy>>'))
        editmenu.add_command(label="Paste", accelerator="Ctrl+V",
                             command=lambda: root.focus_get().event_generate('<<Paste>>'))
        editmenu.add_command(label="Select all", accelerator="Ctrl+A",
                                     command=lambda: root.focus_get().tag_add("sel", "1.0", "end"))
        editmenu.add_separator()
        editmenu.add_command(label="Undo", accelerator="Ctrl+Z", command=rodi.ent_txt.edit_undo)
        editmenu.add_command(label="Redo", accelerator="Ctrl+Y", command=rodi.ent_txt.edit_redo)
        menubar.add_cascade(label="Edit", menu=editmenu)

        # View = Menu(menubar, tearoff=0)
        #
        # menubar.add_cascade(label="View", menu=View)

        Manage = Menu(menubar, tearoff=0)
        Manage.add_command(label='Update dump number !!!', command=rodi.dump_filen_update)
        Manage.add_command(label='Open dump file...', command=rodi.otvori_dump_file)
        Manage.add_separator()
        Manage.add_checkbutton(label='enable auto converter', var=rodi.ccc, command=self.ssttaartt)
        Manage.add_separator()
        Manage.add_checkbutton(label='Synchronize vertical scrolling', command=rodi.sinc_scroll, var=rodi.sinc_gh)
        menubar.add_cascade(label="Options", menu=Manage)

        somenu = Menu(menubar, tearoff=0)
        somenu.add_command(label="Do nothing...", command=rodi.mnoff)
        somenu.add_command(label="color", command=rodi.izberi_color)
        menubar.add_cascade(label="So...", menu=somenu)

        elp = Menu(menubar, tearoff=0)
        elp.add_command(label='get to programing')  # TODO: i kod tuka
        mee = Menu(elp, tearoff=0)
        mee.add_command(label='What a does')
        mee.add_command(label='What b does')
        mee.add_command(label='What c does')
        mee.add_command(label='What d does')
        elp.add_cascade(label='Explain', menu=mee)
        menubar.add_cascade(label="HELP", menu=elp)

        root.bind('<Control-s>', self.seva_now)

    def ssttaartt(self):
        mw.auto_prev()
        mw.lnta["text"] = 'Welcome to text converter 9000 - AUTOMATIC CONVERTER IS ACTIVE'
        mw.lnta["bg"] = '#9b3335'

    def seva_folder(self):
        mjasto = os.path.abspath(os.curdir)
        os.startfile(f"{mjasto}\\data\\saved")

    def seva_now(self, e):
        from checkboxes import chw
        tm = str(datetime.now().strftime("%Y-%m-%d h%H%M%S"))
        fajl_ime = "data/saved/saved at %s.dat" % tm
        print(e)
        with open(fajl_ime, "w", encoding='utf-8') as s:
            s.write(str(chw.ch1()) + ' ')
            s.write(str(chw.n1.get()) + '\n')
            s.write(str(chw.ch2()) + ' ')
            s.write(str(chw.n2.get()) + '\n')
            s.write(str(chw.ch3()) + ' ')
            s.write(str(chw.n3.get()) + '\n')
            s.write(str(chw.ch4()) + ' ')
            s.write(str(chw.n4.get()) + '\n')
            s.write(str(chw.ch5()) + ' ')
            s.write(str(chw.n5.get()) + '\n')
            s.write(str(chw.ch6()) + ' ')
            s.write(str(chw.n6.get()) + '\n')
            s.write(str(chw.ch7()) + ' ')
            s.write(str(chw.n7.get()) + '\n')
            s.write(str(chw.ch8()) + ' ')
            s.write(str(chw.n8.get()) + '\n')
            s.write(str(chw.ch9()) + ' ')
            s.write(str(chw.n9.get()) + '\n')
            s.write(str(chw.ch10()) + ' ')
            s.write(str(chw.n10.get()) + '\n')
            s.write(str(chw.ch11()) + ' ')
            s.write(str(chw.n11.get()) + '\n')
            s.write(str(chw.ch12()) + ' ')
            s.write(str(chw.n12.get()) + '\n')
            s.write(str(chw.ch13()) + ' ')
            s.write(str(chw.n13.get()) + '\n')
            s.write(str(chw.ch1301()) + ' ')
            s.write(str(chw.n1301.get()) + '\n')
            s.write(str(chw.ch14()) + ' ')
            s.write(str(chw.n14.get()) + '\n')
            s.write(str(chw.ch15()) + ' ')
            s.write(str(chw.n15.get()) + '\n')
            s.write(str(chw.ch16()) + ' ')
            s.write(str(chw.n16.get()) + '\n')
            s.write(str(chw.ch17()) + ' ')
            s.write(str(chw.n17.get()) + '\n')
            s.write(str(chw.ch18()) + ' ')
            s.write(str(chw.n18.get()) + '\n')
            s.write(str(chw.ch19()) + ' ')
            s.write(str(chw.n19.get()) + '\n')
            s.write(str(chw.ch20()) + ' ')
            s.write(str(chw.n20.get()) + '\n')
            s.write(str(chw.ch21()) + ' ')
            s.write(str(chw.n21.get()) + '\n')
            s.write(str(chw.ch22()) + ' ')
            s.write(str(chw.n22.get()) + '\n')
            s.write(str(chw.ch23()) + ' ')
            s.write(str(chw.n23.get()) + '\n')
            s.write(str(chw.ch24()) + ' ')
            s.write(str(chw.n24.get()) + '\n')
            s.write(str(chw.ch25()) + ' ')
            s.write(str(chw.n25.get()) + '\n')
            s.write(str(chw.ch26()) + ' ')
            s.write(str(chw.n26.get()) + '\n')
            s.write(str(chw.ch2601()) + ' ')
            s.write(str(chw.n2601.get()) + '\n')
            s.write(str(chw.ch27()) + ' ')
            s.write(str(chw.n27.get()) + '\n')
            s.write(str(chw.ch28()) + ' ')
            s.write(str(chw.n28.get()) + '\n')
            s.write(str(chw.ch29()) + ' ')
            s.write(str(chw.n29.get()) + '\n')
            s.write(str(chw.ch30()) + ' ')
            s.write(str(chw.n30.get()) + '\n')
            s.write(str(chw.ch31()) + ' ')
            s.write(str(chw.n31.get()) + '\n')
            s.write(str(chw.ch32()) + ' ')
            s.write(str(chw.n32.get()) + '\n')
            s.write(str(chw.ch33()) + ' ')
            s.write(str(chw.n33.get()) + '\n')
            s.write(str(chw.ch34()) + ' ')
            s.write(str(chw.n34.get()) + '\n')
            s.write(str(chw.ch35()) + ' ')
            s.write(str(chw.n35.get()) + '\n')
            s.write(str(chw.ch36()) + ' ')
            s.write(str(chw.n36.get()) + '\n')
            s.write(str(chw.ch37()) + ' ')
            s.write(str(chw.n37.get()) + '\n')
            s.write(str(chw.ch38()) + ' ')
            s.write(str(chw.n38.get()) + '\n')
            s.write(str(chw.ch39()) + ' ')
            s.write(str(chw.n39.get()) + '\n')
            s.write(str(chw.ch40()) + ' ')
            s.write(str(chw.n40.get()) + '\n')
            s.write(str(chw.ch41()) + ' ')
            s.write(str(chw.n41.get()) + '\n')
            s.write(str(chw.ch42()) + ' ')
            s.write(str(chw.n42.get()) + '\n')
            s.write(str(chw.air()) + ' ')
            s.write(str(chw.nr1.get()) + '\n')
            s.write(str(chw.ar()) + ' ')
            s.write(str(chw.nr2.get()) + '\n')
            s.write(str(chw.eer()) + ' ')
            s.write(str(chw.nr3.get()) + '\n')
            s.write(str(chw.oor()) + ' ')
            s.write(str(chw.nr4.get()) + '\n')
            s.write(str(chw.sp_oundt()) + ' ')
            s.write(str(chw.nsp0.get()) + '\n')
            s.write(str(chw.sp_kw()) + ' ')
            s.write(str(chw.nsp1.get()) + '\n')
            s.write(str(chw.sp_ngk()) + ' ')
            s.write(str(chw.nsp2.get()) + '\n')
            s.write(str(chw.sp_ago()) + ' ')
            s.write(str(chw.nsp3.get()) + '\n')
            s.write(str(chw.sp_yoo()) + ' ')
            s.write(str(chw.nsp4.get()) + '\n')
            s.write(str(chw.sp_ka_ko_ku()) + ' ')
            s.write(str(chw.nsp5.get()) + '\n')
            s.write(str(chw.sp_tion()) + ' ')
            s.write(str(chw.nsp6.get()) + '\n')
            s.write(str(chw.sp_sion()) + ' ')
            s.write(str(chw.nsp7.get()) + '\n')
            s.write(str(chw.sp_orro()) + ' ')
            s.write(str(chw.nsp8.get()) + '\n')
            s.write(str(chw.sp_egzx()) + ' ')
            s.write(str(chw.nsp9.get()) + '\n')
            s.write(str(chw.sp_a_bout()) + ' ')
            s.write(str(chw.nsp10.get()) + '\n')
            s.write(str(chw.sp_sof_a()) + ' ')
            s.write(str(chw.nsp11.get()) + '\n')
            s.write(str(chw.sp_offme()) + ' ')
            s.write(str(chw.nsp12.get()) + '\n')
            s.write(str(chw.sp_esz()) + ' ')
            s.write(str(chw.nsp13.get()) + '\n')
            s.write(str(chw.sp_kxs()) + ' ')
            s.write(str(chw.nsp14.get()) + '\n')
            s.write(str(chw.sp_edd()) + ' ')
            s.write(str(chw.nsp15.get()) + '\n')
            s.write(str(chw.sp_ett()) + ' ')
            s.write(str(chw.nsp16.get()) + '\n')
            s.write(str(chw.sp_eedd()) + ' ')
            s.write(str(chw.nsp17.get()) + '\n')
            s.write(str(chw.sp_x_end()) + ' ')
            s.write(str(chw.nsp18.get()) + '\n')

    def save_var(self):
        from checkboxes import chw
        sf = filedialog.asksaveasfilename(
                initialfile="Untitle.dat",
                defaultextension=".dat",
                filetypes=[("All files", "*.*"),
                       ("Data files", "*.dat")])
        with open(sf, "w", encoding='utf-8') as s:
            s.write(str(chw.ch1()) + ' ')
            s.write(str(chw.n1.get()) + '\n')
            s.write(str(chw.ch2()) + ' ')
            s.write(str(chw.n2.get()) + '\n')
            s.write(str(chw.ch3()) + ' ')
            s.write(str(chw.n3.get()) + '\n')
            s.write(str(chw.ch4()) + ' ')
            s.write(str(chw.n4.get()) + '\n')
            s.write(str(chw.ch5()) + ' ')
            s.write(str(chw.n5.get()) + '\n')
            s.write(str(chw.ch6()) + ' ')
            s.write(str(chw.n6.get()) + '\n')
            s.write(str(chw.ch7()) + ' ')
            s.write(str(chw.n7.get()) + '\n')
            s.write(str(chw.ch8()) + ' ')
            s.write(str(chw.n8.get()) + '\n')
            s.write(str(chw.ch9()) + ' ')
            s.write(str(chw.n9.get()) + '\n')
            s.write(str(chw.ch10()) + ' ')
            s.write(str(chw.n10.get()) + '\n')
            s.write(str(chw.ch11()) + ' ')
            s.write(str(chw.n11.get()) + '\n')
            s.write(str(chw.ch12()) + ' ')
            s.write(str(chw.n12.get()) + '\n')
            s.write(str(chw.ch13()) + ' ')
            s.write(str(chw.n13.get()) + '\n')
            s.write(str(chw.ch1301()) + ' ')
            s.write(str(chw.n1301.get()) + '\n')
            s.write(str(chw.ch14()) + ' ')
            s.write(str(chw.n14.get()) + '\n')
            s.write(str(chw.ch15()) + ' ')
            s.write(str(chw.n15.get()) + '\n')
            s.write(str(chw.ch16()) + ' ')
            s.write(str(chw.n16.get()) + '\n')
            s.write(str(chw.ch17()) + ' ')
            s.write(str(chw.n17.get()) + '\n')
            s.write(str(chw.ch18()) + ' ')
            s.write(str(chw.n18.get()) + '\n')
            s.write(str(chw.ch19()) + ' ')
            s.write(str(chw.n19.get()) + '\n')
            s.write(str(chw.ch20()) + ' ')
            s.write(str(chw.n20.get()) + '\n')
            s.write(str(chw.ch21()) + ' ')
            s.write(str(chw.n21.get()) + '\n')
            s.write(str(chw.ch22()) + ' ')
            s.write(str(chw.n22.get()) + '\n')
            s.write(str(chw.ch23()) + ' ')
            s.write(str(chw.n23.get()) + '\n')
            s.write(str(chw.ch24()) + ' ')
            s.write(str(chw.n24.get()) + '\n')
            s.write(str(chw.ch25()) + ' ')
            s.write(str(chw.n25.get()) + '\n')
            s.write(str(chw.ch26()) + ' ')
            s.write(str(chw.n26.get()) + '\n')
            s.write(str(chw.ch2601()) + ' ')
            s.write(str(chw.n2601.get()) + '\n')
            s.write(str(chw.ch27()) + ' ')
            s.write(str(chw.n27.get()) + '\n')
            s.write(str(chw.ch28()) + ' ')
            s.write(str(chw.n28.get()) + '\n')
            s.write(str(chw.ch29()) + ' ')
            s.write(str(chw.n29.get()) + '\n')
            s.write(str(chw.ch30()) + ' ')
            s.write(str(chw.n30.get()) + '\n')
            s.write(str(chw.ch31()) + ' ')
            s.write(str(chw.n31.get()) + '\n')
            s.write(str(chw.ch32()) + ' ')
            s.write(str(chw.n32.get()) + '\n')
            s.write(str(chw.ch33()) + ' ')
            s.write(str(chw.n33.get()) + '\n')
            s.write(str(chw.ch34()) + ' ')
            s.write(str(chw.n34.get()) + '\n')
            s.write(str(chw.ch35()) + ' ')
            s.write(str(chw.n35.get()) + '\n')
            s.write(str(chw.ch36()) + ' ')
            s.write(str(chw.n36.get()) + '\n')
            s.write(str(chw.ch37()) + ' ')
            s.write(str(chw.n37.get()) + '\n')
            s.write(str(chw.ch38()) + ' ')
            s.write(str(chw.n38.get()) + '\n')
            s.write(str(chw.ch39()) + ' ')
            s.write(str(chw.n39.get()) + '\n')
            s.write(str(chw.ch40()) + ' ')
            s.write(str(chw.n40.get()) + '\n')
            s.write(str(chw.ch41()) + ' ')
            s.write(str(chw.n41.get()) + '\n')
            s.write(str(chw.ch42()) + ' ')
            s.write(str(chw.n42.get()) + '\n')
            s.write(str(chw.air()) + ' ')
            s.write(str(chw.nr1.get()) + '\n')
            s.write(str(chw.ar()) + ' ')
            s.write(str(chw.nr2.get()) + '\n')
            s.write(str(chw.eer()) + ' ')
            s.write(str(chw.nr3.get()) + '\n')
            s.write(str(chw.oor()) + ' ')
            s.write(str(chw.nr4.get()) + '\n')
            s.write(str(chw.sp_oundt()) + ' ')
            s.write(str(chw.nsp0.get()) + '\n')
            s.write(str(chw.sp_kw()) + ' ')
            s.write(str(chw.nsp1.get()) + '\n')
            s.write(str(chw.sp_ngk()) + ' ')
            s.write(str(chw.nsp2.get()) + '\n')
            s.write(str(chw.sp_ago()) + ' ')
            s.write(str(chw.nsp3.get()) + '\n')
            s.write(str(chw.sp_yoo()) + ' ')
            s.write(str(chw.nsp4.get()) + '\n')
            s.write(str(chw.sp_ka_ko_ku()) + ' ')
            s.write(str(chw.nsp5.get()) + '\n')
            s.write(str(chw.sp_tion()) + ' ')
            s.write(str(chw.nsp6.get()) + '\n')
            s.write(str(chw.sp_sion()) + ' ')
            s.write(str(chw.nsp7.get()) + '\n')
            s.write(str(chw.sp_orro()) + ' ')
            s.write(str(chw.nsp8.get()) + '\n')
            s.write(str(chw.sp_egzx()) + ' ')
            s.write(str(chw.nsp9.get()) + '\n')
            s.write(str(chw.sp_a_bout()) + ' ')
            s.write(str(chw.nsp10.get()) + '\n')
            s.write(str(chw.sp_sof_a()) + ' ')
            s.write(str(chw.nsp11.get()) + '\n')
            s.write(str(chw.sp_offme()) + ' ')
            s.write(str(chw.nsp12.get()) + '\n')
            s.write(str(chw.sp_esz()) + ' ')
            s.write(str(chw.nsp13.get()) + '\n')
            s.write(str(chw.sp_kxs()) + ' ')
            s.write(str(chw.nsp14.get()) + '\n')
            s.write(str(chw.sp_edd()) + ' ')
            s.write(str(chw.nsp15.get()) + '\n')
            s.write(str(chw.sp_ett()) + ' ')
            s.write(str(chw.nsp16.get()) + '\n')
            s.write(str(chw.sp_eedd()) + ' ')
            s.write(str(chw.nsp17.get()) + '\n')
            s.write(str(chw.sp_x_end()) + ' ')
            s.write(str(chw.nsp18.get()) + '\n')

    def load_var(self):
        from checkboxes import chw
        lf = filedialog.askopenfilename(
            defaultextension=".dat",
            filetypes=[("All files", "*.*"),
                       ("Text files", "*.dat")])
        with open(lf, "r", encoding='utf-8') as l:
            ll = l.readlines()
            for i in range(0, len(ll)):
                if i == 0:
                    chw.t1.set(ll[i].split()[0])
                    chw.n1.set(ll[i].split()[1])
                elif i == 1:
                    chw.t2.set(ll[i].split()[0])
                    chw.n2.set(ll[i].split()[1])
                elif i == 2:
                    chw.t3.set(ll[i].split()[0])
                    chw.n3.set(ll[i].split()[1])
                elif i == 3:
                    chw.t4.set(ll[i].split()[0])
                    chw.n4.set(ll[i].split()[1])
                elif i == 4:
                    chw.t5.set(ll[i].split()[0])
                    chw.n5.set(ll[i].split()[1])
                elif i == 5:
                    chw.t6.set(ll[i].split()[0])
                    chw.n6.set(ll[i].split()[1])
                elif i == 6:
                    chw.t7.set(ll[i].split()[0])
                    chw.n7.set(ll[i].split()[1])
                elif i == 7:
                    chw.t8.set(ll[i].split()[0])
                    chw.n8.set(ll[i].split()[1])
                elif i == 8:
                    chw.t9.set(ll[i].split()[0])
                    chw.n9.set(ll[i].split()[1])
                elif i == 9:
                    chw.t32.set(ll[i].split()[0])
                    chw.n32.set(ll[i].split()[1])
                elif i == 10:
                    chw.t11.set(ll[i].split()[0])
                    chw.n11.set(ll[i].split()[1])
                elif i == 11:
                    chw.t12.set(ll[i].split()[0])
                    chw.n12.set(ll[i].split()[1])
                elif i == 12:
                    chw.t13.set(ll[i].split()[0])
                    chw.n13.set(ll[i].split()[1])
                elif i == 13:
                    chw.t1301.set(ll[i].split()[0])
                    chw.n1301.set(ll[i].split()[1])
                elif i == 14:
                    chw.t14.set(ll[i].split()[0])
                    chw.n14.set(ll[i].split()[1])
                elif i == 15:
                    chw.t15.set(ll[i].split()[0])
                    chw.n15.set(ll[i].split()[1])
                elif i == 16:
                    chw.t16.set(ll[i].split()[0])
                    chw.n16.set(ll[i].split()[1])
                elif i == 17:
                    chw.t17.set(ll[i].split()[0])
                    chw.n17.set(ll[i].split()[1])
                elif i == 18:
                    chw.t18.set(ll[i].split()[0])
                    chw.n18.set(ll[i].split()[1])
                elif i == 19:
                    chw.t19.set(ll[i].split()[0])
                    chw.n19.set(ll[i].split()[1])
                elif i == 20:
                    chw.t20.set(ll[i].split()[0])
                    chw.n20.set(ll[i].split()[1])
                elif i == 21:
                    chw.t21.set(ll[i].split()[0])
                    chw.n21.set(ll[i].split()[1])
                elif i == 22:
                    chw.t22.set(ll[i].split()[0])
                    chw.n22.set(ll[i].split()[1])
                elif i == 23:
                    chw.t23.set(ll[i].split()[0])
                    chw.n23.set(ll[i].split()[1])
                elif i == 24:
                    chw.t24.set(ll[i].split()[0])
                    chw.n24.set(ll[i].split()[1])
                elif i == 25:
                    chw.t25.set(ll[i].split()[0])
                    chw.n25.set(ll[i].split()[1])
                elif i == 26:
                    chw.t26.set(ll[i].split()[0])
                    chw.n26.set(ll[i].split()[1])
                elif i == 27:
                    chw.t2601.set(ll[i].split()[0])
                    chw.n2601.set(ll[i].split()[1])
                elif i == 28:
                    chw.t27.set(ll[i].split()[0])
                    chw.n27.set(ll[i].split()[1])
                elif i == 29:
                    chw.t28.set(ll[i].split()[0])
                    chw.n28.set(ll[i].split()[1])
                elif i == 30:
                    chw.t29.set(ll[i].split()[0])
                    chw.n29.set(ll[i].split()[1])
                elif i == 31:
                    chw.t30.set(ll[i].split()[0])
                    chw.n30.set(ll[i].split()[1])
                elif i == 32:
                    chw.t31.set(ll[i].split()[0])
                    chw.n31.set(ll[i].split()[1])
                elif i == 33:
                    chw.t10.set(ll[i].split()[0])
                    chw.n10.set(ll[i].split()[1])
                elif i == 34:
                    chw.t33.set(ll[i].split()[0])
                    chw.n33.set(ll[i].split()[1])
                elif i == 35:
                    chw.t34.set(ll[i].split()[0])
                    chw.n34.set(ll[i].split()[1])
                elif i == 36:
                    chw.t35.set(ll[i].split()[0])
                    chw.n35.set(ll[i].split()[1])
                elif i == 37:
                    chw.t36.set(ll[i].split()[0])
                    chw.n36.set(ll[i].split()[1])
                elif i == 38:
                    chw.t37.set(ll[i].split()[0])
                    chw.n37.set(ll[i].split()[1])
                elif i == 39:
                    chw.t38.set(ll[i].split()[0])
                    chw.n38.set(ll[i].split()[1])
                elif i == 40:
                    chw.t39.set(ll[i].split()[0])
                    chw.n39.set(ll[i].split()[1])
                elif i == 41:
                    chw.t40.set(ll[i].split()[0])
                    chw.n40.set(ll[i].split()[1])
                elif i == 42:
                    chw.t41.set(ll[i].split()[0])
                    chw.n41.set(ll[i].split()[1])
                elif i == 43:
                    chw.t42.set(ll[i].split()[0])
                    chw.n42.set(ll[i].split()[1])
                elif i == 44:
                    chw.tr1.set(ll[i].split()[0])
                    chw.nr1.set(ll[i].split()[1])
                elif i == 45:
                    chw.tr2.set(ll[i].split()[0])
                    chw.nr2.set(ll[i].split()[1])
                elif i == 46:
                    chw.tr3.set(ll[i].split()[0])
                    chw.nr3.set(ll[i].split()[1])
                elif i == 47:
                    chw.tr4.set(ll[i].split()[0])
                    chw.nr4.set(ll[i].split()[1])
                elif i == 48:
                    chw.tsp0.set(ll[i].split()[0])
                    chw.nsp0.set(ll[i].split()[1])
                elif i == 49:
                    chw.tsp1.set(ll[i].split()[0])
                    chw.nsp1.set(ll[i].split()[1])
                elif i == 50:
                    chw.tsp2.set(ll[i].split()[0])
                    chw.nsp2.set(ll[i].split()[1])
                elif i == 51:
                    chw.tsp3.set(ll[i].split()[0])
                    chw.nsp3.set(ll[i].split()[1])
                elif i == 52:
                    chw.tsp4.set(ll[i].split()[0])
                    chw.nsp4.set(ll[i].split()[1])
                elif i == 53:
                    chw.tsp5.set(ll[i].split()[0])
                    chw.nsp5.set(ll[i].split()[1])
                elif i == 54:
                    chw.tsp6.set(ll[i].split()[0])
                    chw.nsp6.set(ll[i].split()[1])
                elif i == 55:
                    chw.tsp7.set(ll[i].split()[0])
                    chw.nsp7.set(ll[i].split()[1])
                elif i == 56:
                    chw.tsp8.set(ll[i].split()[0])
                    chw.nsp8.set(ll[i].split()[1])
                elif i == 57:
                    chw.tsp9.set(ll[i].split()[0])
                    chw.nsp9.set(ll[i].split()[1])
                elif i == 58:
                    chw.tsp10.set(ll[i].split()[0])
                    chw.nsp10.set(ll[i].split()[1])
                elif i == 59:
                    chw.tsp11.set(ll[i].split()[0])
                    chw.nsp11.set(ll[i].split()[1])
                elif i == 60:
                    chw.tsp12.set(ll[i].split()[0])
                    chw.nsp12.set(ll[i].split()[1])
                elif i == 61:
                    chw.tsp13.set(ll[i].split()[0])
                    chw.nsp13.set(ll[i].split()[1])
                elif i == 62:
                    chw.tsp14.set(ll[i].split()[0])
                    chw.nsp14.set(ll[i].split()[1])
                elif i == 63:
                    chw.tsp15.set(ll[i].split()[0])
                    chw.nsp15.set(ll[i].split()[1])
                elif i == 64:
                    chw.tsp16.set(ll[i].split()[0])
                    chw.nsp16.set(ll[i].split()[1])
                elif i == 65:
                    chw.tsp17.set(ll[i].split()[0])
                    chw.nsp17.set(ll[i].split()[1])
                elif i == 66:
                    chw.tsp18.set(ll[i].split()[0])
                    chw.nsp18.set(ll[i].split()[1])


class MainWindow:
    jj = 0
    def __init__(self, window):
        window.title("Text converter - INPROGRESS BUILD")
        window.geometry("1280x630+150+100")
        window.iconbitmap('data/ico/icon2.ico')
        self.img2 = PhotoImage(file='data/speaker2.png')
        self.window = window
        self.r_d = IntVar()
        self.ccc = IntVar()
        self.sinc_gh = IntVar()
        font_specs = ("ubuntu", 14, "bold")

        self.f_i = "#606060"
        window.config(bg=self.f_i)

        self.pyrvi_red = Frame(window, bg=self.f_i)     #, bg='red'
        self.pyrvi_red.pack(fill=X, side=TOP)
        self.vtori_red = Frame(window, bg=self.f_i)      #, bg='black'
        self.vtori_red.pack(fill=X, side=TOP)
        self.treti_red = Frame(window, bg=self.f_i)     # , bg='blue'
        self.treti_red.pack(side=TOP)
        self.cetvyrti_red = Frame(window, bg=self.f_i)    # , bg='yellow'
        self.cetvyrti_red.pack(fill=X, side=TOP)

        Label(self.pyrvi_red, text="Enter Text Below:", font=font_specs, bg=self.f_i).pack(expand=True, side=LEFT, anchor=SE)
        self.b1 = Button(self.pyrvi_red, state=NORMAL, text="Enter!", command=pr.prevod2, height=1, width=8, font=("Times New Roman", 16, "bold"), bg=self.f_i)
        self.b1.pack(expand=True, side=LEFT)

        Label(self.pyrvi_red, text="Output Text Below:", font=font_specs, bg=self.f_i).pack(expand=True, side=LEFT, anchor=SW)

        self.ent_txt = Text(self.vtori_red, undo=True, wrap=WORD)    # ,  width=78, height=24,
        self.ent_txt.pack(expand=True, side=LEFT, anchor=E)
        self.scr_br = Scrollbar(self.vtori_red, orient="vertical")
        self.scr_br.pack(side=LEFT, fill=Y)
        Button(master=self.ent_txt, text='SPEAK!', command=pr.govorene, image=self.img2, bg=self.f_i).place(relx=0.956, rely=0.926)
        self.textbox2 = Text(self.vtori_red, wrap=WORD)
        self.textbox2.pack(expand=True, side=LEFT, anchor=W)

        Label(self.treti_red, text="word1/word2/word3/word4", bg=self.f_i).grid(row=1, column=5, columnspan=4)
        Label(self.treti_red, text="Apply choses word to all words with dashes!", bg=self.f_i).grid(row=1, column=0, columnspan=2)
        Label(self.treti_red, text="default", bg=self.f_i).grid(row=2, column=0, sticky=E)
        Radiobutton(self.treti_red, var=self.r_d, value=0, bg=self.f_i).grid(row=2, column=1, sticky=W)
        Radiobutton(self.treti_red, var=self.r_d, value=3, bg=self.f_i).grid(row=2, column=5)
        Radiobutton(self.treti_red, var=self.r_d, value=2, bg=self.f_i).grid(row=2, column=6)
        Radiobutton(self.treti_red, var=self.r_d, value=1, bg=self.f_i).grid(row=2, column=8)
        Radiobutton(self.treti_red, var=self.r_d, value=4, bg=self.f_i).grid(row=2, column=7)
        self.v_dump = StringVar()
        self.dump = Label(self.treti_red, text="Dump:(number)   //Manage -> Update dump count//", bg=self.f_i)
        self.dump.grid(row=1, column=20, sticky=E, padx=200)

        # Label(self.cetvyrti_red, text="Raw Text Below:").pack(side=LEFT)
        Button(self.cetvyrti_red, text="Show raw text!", command=lambda: [self.textboxraw.delete(0.0, END), self.textboxraw.insert(0.0, pr.prevod())], bg=self.f_i).pack(side=LEFT)
        self.textboxraw = Text(self.cetvyrti_red, width=50, height=2, wrap=WORD)
        self.textboxraw.pack(side=LEFT)
        from checkboxes import ruw
        self.cbt = Button(self.cetvyrti_red, text="Open custom \n letters window!", command=lambda: [ruw.open_window(), self.tgl_btn()], font=("Times New Roman", 12, "bold"), bg=self.f_i)
        self.cbt.pack(side=RIGHT)

        self.desen_buton = Menu(window, tearoff=False)
        self.desen_buton.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: root.focus_get().event_generate('<<Cut>>'))
        self.desen_buton.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: root.focus_get().event_generate('<<Copy>>'))
        self.desen_buton.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: root.focus_get().event_generate('<<Paste>>'))
        self.desen_buton.add_command(label="Select all", accelerator="Ctrl+A", command=lambda: root.focus_get().tag_add("sel", "1.0", "end"))

        self.ent_txt.bind('<Button-3>', self.desen_btn)
        self.textbox2.bind('<Button-3>', self.desen_btn)
        self.textboxraw.bind('<Button-3>', self.desen_btn)
        self.ent_txt.bind('<Shift-Return>', lambda x: print(x))
        self.ent_txt.bind('<Return>', pr.prevod2)

        self.lnta = Label(window, text='Welcome to text converter 9000', relief=SUNKEN, anchor=W, bg=self.f_i)
        self.lnta.place(anchor=S, relx=0.50, rely=1, relwidth=1)
        self.menubar = MenuBar(self)

    def desen_btn(self, ev):
        self.desen_buton.tk_popup(ev.x_root, ev.y_root)

    def izberi_color(self):
        fonnen_cvjat = colorchooser.askcolor()[1]
        print(fonnen_cvjat)
        self.window.configure(bg=f"{fonnen_cvjat}")
        self.pyrvi_red.configure(bg=f"{fonnen_cvjat}")
        self.vtori_red.configure(bg=f"{fonnen_cvjat}")
        self.treti_red.configure(bg=f"{fonnen_cvjat}")
        self.cetvyrti_red.configure(bg=f"{fonnen_cvjat}")

    def tgl_btn(self):
        from checkboxes import ruw
        self.cbt.config(text='Toggle custom \n letters window!', command=ruw.toggle_window)

    def auto_prev(self):
        if self.ccc.get() == 1:
            self.jj += 1
            self.ent_txt.unbind('<Return>')
            self.ent_txt.unbind('<Shift-Return>')
            # self.b1.config(state=DISABLED)
            pr.prevod2()
            Timer(0.1, self.auto_prev).start()
            print('..RUNNING..', self.jj)
        else:
            self.ent_txt.bind('<Shift-Return>', lambda x: print(x))
            self.ent_txt.bind('<Return>', pr.prevod2)
            # self.b1.config(state=NORMAL)
            self.lnta["text"] = 'Welcome to text converter 9000 - AUTOMATIC CONVERTER IS DISABLED'
            self.lnta["bg"] = '#606060'
            print('not runnig')

    def remove_dash(self):
        a = self.r_d.get()
        return a

    def otvori_dump_file(self):
        subpc.Popen(["Notepad.exe", "MISSING_WORDS/missing_word_list.txt"])

    def dump_filen_update(self):
        with open("MISSING_WORDS/word_dump.txt", "r") as llc:
            c = len(list(llc))
            self.dump.config(text=f"Dump file size is {c} lines long")

    def mnoff(self):
        for c in range(0, 100):
            if messagebox.askretrycancel(title="WOT", message=str(c) + " |What did you expext") is True:
                messagebox.showwarning(title="WARNING", message="you dun goofed")
            else:
                if messagebox.askyesno(title="HAHAHAHAHAHAHA", message="DO YOU WANT TO ~QUIT~") is True:
                    quit()
                else:
                    messagebox.showwarning(title="WARNING", message="you dun goofed AGAIN")
            c += 1

    def open_new(self):
        self.fname = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All files", "*.*"),
                       ("Text files", "*.txt")])
        if self.fname:
            self.ent_txt.delete(1.0, END)
            with open(self.fname, "r") as f:
                self.ent_txt.insert(1.0, f.read())

    def sinc_scroll(self):
        if self.sinc_gh.get() == 0:
            print('sinhron ne raboti')
        else:
            self.ent_txt.config(yscrollcommand=self.scr_br.set)
            self.textbox2.config(yscrollcommand=self.scr_br.set)
            self.scr_br.config(command=lambda *args: [self.ent_txt.yview(*args), self.textbox2.yview(*args)])
            # self.ent_txt.unbind("<MouseWheel>", lambda e: print(e))
            # self.textbox2.unbind("<MouseWheel>", lambda e: print(e))

            # self.textbox2.config(command=self.ent_txt.yview)
            # def OnMouseWheel(e):
            #     self.scr_br.yview(-1*(e.delta/120), "units")
            # self.ent_txt.bind('<MouseWheel>', OnMouseWheel)

            print('sinhron raboti')


if __name__ == "__main__":
    root = Tk()
    pr = PrevodGovor()
    mw = MainWindow(root)
    root.mainloop()
