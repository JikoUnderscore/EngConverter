from tkinter import *
from tkinter import font

def profile(fnc):
    import cProfile, pstats, io

    def iner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumtime'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return iner

class Chechboxes:
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n1301, n14, n15, n16, n17, n18, n19, n20 = \
        (IntVar() for i in range(21))
    n21, n22, n23, n24, n25, n26, n27, n28, n29, n30, n31, n32, n33, n34, n35, n36, n37, n38, n39 = \
        (IntVar() for iI in range(19))
    n40, n41, n42, nr1, nr2, nr3, nr4, n2601, nsp0 = (IntVar() for iII in range(9))

    t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t1301, t14, t15, t16, t17, t18, t19, t20 = \
        (StringVar() for ii in range(21))
    t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39 = \
        (StringVar() for iiI in range(19))
    t40, t41, t42, tr1, tr2, tr3, tr4, t2601, tsp0 = (StringVar() for iiII in range(9))
                                                                        #DEAD                                            DEAD
    tsp1, tsp2, tsp3, tsp4, tsp5, tsp6, tsp7, tsp8, tsp9, tsp10, tsp11, tsp12, tsp13, tsp14, tsp15, tsp16, tsp17, tsp18, tsp19, tsp20 = \
        (StringVar() for psp in range(20))
                                                                        #DEAD
    nsp1, nsp2, nsp3, nsp4, nsp5, nsp6, nsp7, nsp8, nsp9, nsp10, nsp11, nsp12, nsp13, nsp14, nsp15, nsp16, nsp17, nsp18, nsp19, nsp20, nsp21 = \
        (IntVar() for ipsp in range(21))

    def ch1(self):
        if self.n1.get() == 1:
            c1 = self.t1.get()
            return c1
        else:
            c2 = "o"
            return c2

    def ch2(self):
        if self.n2.get() == 1:
            c1 = self.t2.get()
            return c1
        else:
            c2 = "ä"
            return c2

    def ch3(self):
        if self.n3.get() == 1:
            c1 = self.t3.get()
            return c1
        else:
            c2 = "ü"
            return c2

    def ch4(self):
        if self.n4.get() == 1:
            c1 = self.t4.get()
            return c1
        else:
            c2 = "aw"
            return c2

    def ch5(self):
        if self.n5.get() == 1:
            c1 = self.t5.get()
            return c1
        else:
            c2 = "ow"
            return c2

    def ch6(self):
        if self.n6.get() == 1:
            c1 = self.t6.get()
            return c1
        else:
            c2 = "ie"
            return c2

    def ch7(self):
        if self.n7.get() == 1:
            c1 = self.t7.get()
            return c1
        else:
            c2 = "b"
            return c2

    def ch8(self):
        if self.n8.get() == 1:
            c1 = self.t8.get()
            return c1
        else:
            c2 = "ch"
            return c2

    def ch9(self):
        if self.n9.get() == 1:
            c1 = self.t9.get()
            return c1
        else:
            c2 = "d"
            return c2

    def ch10(self):
        if self.n10.get() == 1:
            c1 = self.t10.get()
            return c1
        else:
            c2 = "th"
            return c2

    def ch11(self):
        if self.n11.get() == 1:
            c1 = self.t11.get()
            return c1
        else:
            c2 = "e"
            return c2

    def ch12(self):
        if self.n12.get() == 1:
            c1 = self.t12.get()
            return c1
        else:
            c2 = "ur"
            return c2

    def ch13(self):
        if self.n13.get() == 1:
            c1 = self.t13.get()
            return c1
        else:
            c2 = "ai"
            return c2

    def ch1301(self):
        if self.n1301.get() == 1:
            c1 = self.t1301.get()
            return c1
        else:
            c2 = "ay"
            return c2

    def ch14(self):
        if self.n14.get() == 1:
            c1 = self.t14.get()
            return c1
        else:
            c2 = "f"
            return c2

    def ch15(self):
        if self.n15.get() == 1:
            c1 = self.t15.get()
            return c1
        else:
            c2 = "g"
            return c2

    def ch16(self):
        if self.n16.get() == 1:
            c1 = self.t16.get()
            return c1
        else:
            c2 = "h"
            return c2

    def ch17(self):
        if self.n17.get() == 1:
            c1 = self.t17.get()
            return c1
        else:
            c2 = "i"
            return c2

    def ch18(self):
        if self.n18.get() == 1:
            c1 = self.t18.get()
            return c1
        else:
            c2 = "ee"
            return c2

    def ch19(self):
        if self.n19.get() == 1:
            c1 = self.t19.get()
            return c1
        else:
            c2 = "j"
            return c2

    def ch20(self):
        if self.n20.get() == 1:
            c1 = self.t20.get()
            return c1
        else:
            c2 = "k"
            return c2

    def ch21(self):
        if self.n21.get() == 1:
            c1 = self.t21.get()
            return c1
        else:
            c2 = "l"
            return c2

    def ch22(self):
        if self.n22.get() == 1:
            c1 = self.t22.get()
            return c1
        else:
            c2 = "m"
            return c2

    def ch23(self):
        if self.n23.get() == 1:
            c1 = self.t23.get()
            return c1
        else:
            c2 = "n"
            return c2

    def ch24(self):
        if self.n24.get() == 1:
            c1 = self.t24.get()
            return c1
        else:
            c2 = "ng"
            return c2

    def ch25(self):
        if self.n25.get() == 1:
            c1 = self.t25.get()
            return c1
        else:
            c2 = "oa"
            return c2

    def ch26(self):
        if self.n26.get() == 1:
            c1 = self.t26.get()
            return c1
        else:
            c2 = "oy"
            return c2

    def ch2601(self):
        if self.n2601.get() == 1:
            c1 = self.t2601.get()
            return c1
        else:
            c2 = "oi"
            return c2

    def ch27(self):
        if self.n27.get() == 1:
            c1 = self.t27.get()
            return c1
        else:
            c2 = "p"
            return c2

    def ch28(self):
        if self.n28.get() == 1:
            c1 = self.t28.get()
            return c1
        else:
            c2 = "r"
            return c2

    def ch29(self):
        if self.n29.get() == 1:
            c1 = self.t29.get()
            return c1
        else:
            c2 = "s"
            return c2

    def ch30(self):
        if self.n30.get() == 1:
            c1 = self.t30.get()
            return c1
        else:
            c2 = "sh"
            return c2

    def ch31(self):
        if self.n31.get() == 1:
            c1 = self.t31.get()
            return c1
        else:
            c2 = "t"
            return c2

    def ch32(self):
        if self.n32.get() == 1:
            c1 = self.t32.get()
            return c1
        else:
            c2 = "thh"
            return c2

    def ch33(self):
        if self.n33.get() == 1:
            c1 = self.t33.get()
            return c1
        else:
            c2 = "uu"
            return c2

    def ch34(self):
        if self.n34.get() == 1:
            c1 = self.t34.get()
            return c1
        else:
            c2 = "oo"
            return c2

    def ch35(self):
        if self.n35.get() == 1:
            c1 = self.t35.get()
            return c1
        else:
            c2 = "v"
            return c2

    def ch36(self):
        if self.n36.get() == 1:
            c1 = self.t36.get()
            return c1
        else:
            c2 = "w"
            return c2

    def ch37(self):
        if self.n37.get() == 1:
            c1 = self.t37.get()
            return c1
        else:
            c2 = "y"
            return c2

    def ch38(self):
        if self.n38.get() == 1:
            c1 = self.t38.get()
            return c1
        else:
            c2 = "z"
            return c2

    def ch39(self):
        if self.n39.get() == 1:
            c1 = self.t39.get()
            return c1
        else:
            c2 = "zh"
            return c2

    def ch40(self):
        if self.n40.get() == 1:
            c1 = self.t40.get()
            return c1
        else:
            c2 = "i"
            return c2

    def ch41(self):
        if self.n41.get() == 1:
            c1 = self.t41.get()
            return c1
        else:
            c2 = "ə"
            return c2

    def ch42(self):
        if self.n42.get() == 1:
            c1 = self.t42.get()
            return c1
        else:
            c2 = "ər"
            return c2

    def air(self):
        if self.nr1.get() == 1:
            c1 = self.tr1.get()
            return c1
        else:
            c2 = "er"
            return c2

    def ar(self):
        if self.nr2.get() == 1:
            c1 = self.tr2.get()
            return c1
        else:
            c2 = "ar"
            return c2

    def eer(self):
        if self.nr3.get() == 1:
            c1 = self.tr3.get()
            return c1
        else:
            c2 = "eer"
            return c2

    def oor(self):
        if self.nr4.get() == 1:
            c1 = self.tr4.get()
            return c1
        else:
            c2 = "or"
            return c2

    #   ------------------------- SELECT ------------------------------------------------------
    def select_fillin(self):
        self.deselect_all()
        for i in range(45):
            if i == 1:
                if self.t1.get() != '':
                    self.n1.set(1)
            elif i == 2:
                if self.t2.get() != '':
                    self.n2.set(1)
            elif i == 3:
                if self.t3.get() != '':
                    self.n3.set(1)
            elif i == 4:
                if self.t4.get() != '':
                    self.n4.set(1)
            elif i == 5:
                if self.t5.get() != '':
                    self.n5.set(1)
            elif i == 6:
                if self.t6.get() != '':
                    self.n6.set(1)
            elif i == 7:
                if self.t7.get() != '':
                    self.n7.set(1)
            elif i == 8:
                if self.t8.get() != '':
                    self.n8.set(1)
            elif i == 9:
                if self.t9.get() != '':
                    self.n9.set(1)
            elif i == 10:
                if self.t10.get() != '':
                    self.n10.set(1)
            elif i == 11:
                if self.t11.get() != '':
                    self.n11.set(1)
            elif i == 12:
                if self.t12.get() != '':
                    self.n12.set(1)
            elif i == 13:
                if self.t13.get() != '':
                    self.n13.set(1)
            elif i == 14:
                if self.t1301.get() != '':
                    self.n1301.set(1)
            elif i == 15:
                if self.t14.get() != '':
                    self.n14.set(1)
            elif i == 16:
                if self.t15.get() != '':
                    self.n15.set(1)
            elif i == 17:
                if self.t16.get() != '':
                    self.n16.set(1)
            elif i == 18:
                if self.t17.get() != '':
                    self.n17.set(1)
            elif i == 19:
                if self.t18.get() != '':
                    self.n18.set(1)
            elif i == 20:
                if self.t19.get() != '':
                    self.n19.set(1)
            elif i == 21:
                if self.t20.get() != '':
                    self.n20.set(1)
            elif i == 22:
                if self.t21.get() != '':
                    self.n21.set(1)
            elif i == 23:
                if self.t22.get() != '':
                    self.n22.set(1)
            elif i == 24:
                if self.t23.get() != '':
                    self.n23.set(1)
            elif i == 25:
                if self.t24.get() != '':
                    self.n24.set(1)
            elif i == 26:
                if self.t25.get() != '':
                    self.n25.set(1)
            elif i == 27:
                if self.t26.get() != '':
                    self.n26.set(1)
            elif i == 28:
                if self.t2601.get() != '':
                    self.n2601.set(1)
            elif i == 29:
                if self.t27.get() != '':
                    self.n27.set(1)
            elif i == 30:
                if self.t28.get() != '':
                    self.n28.set(1)
            elif i == 31:
                if self.t29.get() != '':
                    self.n29.set(1)
            elif i == 32:
                if self.t30.get() != '':
                    self.n30.set(1)
            elif i == 33:
                if self.t31.get() != '':
                    self.n31.set(1)
            elif i == 34:
                if self.t32.get() != '':
                    self.n32.set(1)
            elif i == 35:
                if self.t33.get() != '':
                    self.n33.set(1)
            elif i == 36:
                if self.t34.get() != '':
                    self.n34.set(1)
            elif i == 37:
                if self.t35.get() != '':
                    self.n35.set(1)
            elif i == 38:
                if self.t36.get() != '':
                    self.n36.set(1)
            elif i == 39:
                if self.t37.get() != '':
                    self.n37.set(1)
            elif i == 40:
                if self.t38.get() != '':
                    self.n38.set(1)
            elif i == 41:
                if self.t39.get() != '':
                    self.n39.set(1)
            elif i == 42:
                if self.t40.get() != '':
                    self.n40.set(1)
            elif i == 43:
                if self.t41.get() != '':
                    self.n41.set(1)
            elif i == 44:
                if self.t42.get() != '':
                    self.n42.set(1)

    def select_all(self):
        self.nr1.set(1)
        self.nr2.set(1)
        self.nr3.set(1)
        self.nr4.set(1)
        self.n1.set(1)
        self.n2.set(1)
        self.n3.set(1)
        self.n4.set(1)
        self.n5.set(1)
        self.n6.set(1)
        self.n7.set(1)
        self.n8.set(1)
        self.n9.set(1)
        self.n10.set(1)
        self.n11.set(1)
        self.n12.set(1)
        self.n13.set(1)
        self.n1301.set(1)
        self.n14.set(1)
        self.n15.set(1)
        self.n16.set(1)
        self.n17.set(1)
        self.n18.set(1)
        self.n19.set(1)
        self.n20.set(1)
        self.n21.set(1)
        self.n22.set(1)
        self.n23.set(1)
        self.n24.set(1)
        self.n25.set(1)
        self.n26.set(1)
        self.n2601.set(1)
        self.n27.set(1)
        self.n28.set(1)
        self.n29.set(1)
        self.n30.set(1)
        self.n31.set(1)
        self.n32.set(1)
        self.n33.set(1)
        self.n34.set(1)
        self.n35.set(1)
        self.n36.set(1)
        self.n37.set(1)
        self.n38.set(1)
        self.n39.set(1)
        self.n40.set(1)
        self.n41.set(1)
        self.n42.set(1)

        self.nsp0.set(1)
        self.nsp1.set(1)
        self.nsp2.set(1)
        self.nsp3.set(1)
        self.nsp4.set(1)
        self.nsp5.set(1)
        self.nsp6.set(1)
        self.nsp7.set(1)
        self.nsp8.set(1)
        self.nsp9.set(1)
        self.nsp10.set(1)
        self.nsp11.set(1)
        self.nsp12.set(1)
        self.nsp13.set(1)
        self.nsp14.set(1)
        self.nsp15.set(1)
        self.nsp16.set(1)
        self.nsp17.set(1)
        self.nsp18.set(1)

    def deselect_all(self):
        self.nr1.set(0)
        self.nr2.set(0)
        self.nr3.set(0)
        self.nr4.set(0)
        self.n1.set(0)
        self.n2.set(0)
        self.n3.set(0)
        self.n4.set(0)
        self.n5.set(0)
        self.n6.set(0)
        self.n7.set(0)
        self.n8.set(0)
        self.n9.set(0)
        self.n10.set(0)
        self.n11.set(0)
        self.n12.set(0)
        self.n13.set(0)
        self.n1301.set(0)
        self.n14.set(0)
        self.n15.set(0)
        self.n16.set(0)
        self.n17.set(0)
        self.n18.set(0)
        self.n19.set(0)
        self.n20.set(0)
        self.n21.set(0)
        self.n22.set(0)
        self.n23.set(0)
        self.n24.set(0)
        self.n25.set(0)
        self.n26.set(0)
        self.n2601.set(0)
        self.n27.set(0)
        self.n28.set(0)
        self.n29.set(0)
        self.n30.set(0)
        self.n31.set(0)
        self.n32.set(0)
        self.n33.set(0)
        self.n34.set(0)
        self.n35.set(0)
        self.n36.set(0)
        self.n37.set(0)
        self.n38.set(0)
        self.n39.set(0)
        self.n40.set(0)
        self.n41.set(0)
        self.n42.set(0)

        self.nsp0.set(0)
        self.nsp1.set(0)
        self.nsp2.set(0)
        self.nsp3.set(0)
        self.nsp4.set(0)
        self.nsp5.set(0)
        self.nsp6.set(0)
        self.nsp7.set(0)
        self.nsp8.set(0)
        self.nsp9.set(0)
        self.nsp10.set(0)
        self.nsp11.set(0)
        self.nsp12.set(0)
        self.nsp13.set(0)
        self.nsp14.set(0)
        self.nsp15.set(0)
        self.nsp16.set(0)
        self.nsp17.set(0)
        self.nsp18.set(0)

    #   ------------------------- SPESHAL RULS -------------------------------------------------
    def sp_oundt(self):
        if self.nsp0.get() == 1:
            c1 = self.tsp0.get()
            return c1
        else:
            c2 = "ou"
            return c2

    def sp_kw(self):
        if self.nsp1.get() == 1:
            s = self.tsp1.get()
            return s
        else:
            s = 'qu'
            return s

    def sp_ngk(self):
        if self.nsp2.get() == 1:
            s = self.tsp2.get()
            return s
        else:
            s = 'nk'
            return s

    def sp_ago(self):
        if self.nsp3.get() == 1:
            s = self.tsp3.get()
            return s
        else:
            s = 'o'
            return s

    def sp_yoo(self):
        if self.nsp4.get() == 1:
            s = self.tsp4.get()
            return s
        else:
            s = 'yoo'
            return s

    def sp_ka_ko_ku(self):
        if self.nsp5.get() == 1:
            s = self.tsp5.get()
            return s
        else:
            s = 'c'
            return s

    def sp_tion(self):
        if self.nsp6.get() == 1:
            s = self.tsp6.get()
            return s
        else:
            s = 'shə'
            return s

    def sp_sion(self):
        if self.nsp7.get() == 1:
            s = self.tsp7.get()
            return s
        else:
            s = 'zhə'
            return s

    def sp_orro(self):
        if self.nsp8.get() == 1:
            s = self.tsp8.get()
            return s
        else:
            s = 'rr'
            return s

    def sp_egzx(self):
        if self.nsp9.get() == 1:
            s = self.tsp9.get()
            return s
        else:
            s = 'gz'
            return s

    def sp_a_bout(self):
        if self.nsp10.get() == 1:
            s = self.tsp10.get()
            return s
        else:
            s = 'ə'
            return s

    def sp_sof_a(self):
        if self.nsp11.get() == 1:
            s = self.tsp11.get()
            return s
        else:
            s = 'ə'
            return s
    # NOT USED
    def sp_offme(self):
        if self.nsp12.get() == 1:
            s = self.tsp12.get()
            return s
        else:
            s = 'üf'
            return s

    def sp_esz(self):
        if self.nsp13.get() == 1:
            s = self.tsp13.get()
            return s
        else:
            s = 'z'
            return s

    def sp_kxs(self):
        if self.nsp14.get() == 1:
            s = self.tsp14.get()
            return s
        else:
            s = 'ks'
            return s

    def sp_edd(self):
        if self.nsp15.get() == 1:
            s = self.tsp15.get()
            return s
        else:
            s = 'éd'
            return s

    def sp_ett(self):
        if self.nsp16.get() == 1:
            s = self.tsp16.get()
            return s
        else:
            s = 'éd'
            return s

    def sp_eedd(self):
        if self.nsp17.get() == 1:
            s = self.tsp17.get()
            return s
        else:
            s = 'éd'
            return s

    def sp_x_end(self):
        if self.nsp18.get() == 1:
            s = self.tsp18.get()
            return s
        else:
            s = 'ks'
            return s

    #   ------------------------- EXCLUDE -------------------------------------------------
    def excld(self):

        s = self.tsp20.get().lower()
        ss = s.replace(', ', ' ').replace(',', ' ')
        return ss.split()


class Rule_window(Chechboxes):

    def toggle_window(self):
        # novprozorec = self.open_window()
        x = str(novprozorec.winfo_exists())
        if x == '0':
            self.open_window()
        elif x == '1':
            novprozorec.destroy()

    @profile
    def open_window(self):
        global novprozorec

        try:
            if novprozorec.state() == 'normal':
                novprozorec.focus()

        except:
            novprozorec = Toplevel()
            novprozorec.title("Custom letters")
            novprozorec.bind('<Escape>', lambda e: novprozorec.destroy())
            novprozorec.focus()
            novprozorec.iconbitmap('data/ico/icon2.ico')

            f_i = "#606060"
            novprozorec['bg'] = f_i
            self.pod_proz = Frame(novprozorec, bg=f_i, height=20, width=800)
            self.pod_proz.grid(row=21, column=0, columnspan=30)
            self.sysht = Label(self.pod_proz, text='0')
            self.sysht.pack()  # place() # relx=0, rely=0

            big_font = font.Font(family="Cooper Black", size="12", weight="normal")

            spec_btn = Button(novprozorec, command=self.runmerun, text='EXPAND RULES', font=big_font, bg=f_i)
            spec_btn.grid(row=20, column=10, columnspan=3)
            # spec_btn.place(height=30, width=110, anchor=S, relx=0.50, rely=0.99)

            sel_ckt = Button(novprozorec, text='select only filled in', command=self.select_fillin, bg=f_i)
            sel_ckt.grid(row=18, column=17, columnspan=10)
            selec_btn = Button(novprozorec, text="select all", command=self.select_all, height=1, width=9,
                               font=big_font, bd=5, bg=f_i)
            selec_btn.grid(row=19, column=17, columnspan=10)
            deselec_btn = Button(novprozorec, text="deselect all", command=self.deselect_all, height=1, width=9,
                                 font=big_font,
                                 bd=5, bg=f_i)
            deselec_btn.grid(row=20, column=17, columnspan=10)

            nula = 0
            edno = 1
            dve = 2
            tri = 3
            cetiri = 4
            pet = 5

            e_w = 3  # entry_width

            # ------------------ Vowel sounds - short -----------------------------------------
            Label(novprozorec, text='Short vowels', font=big_font, bg=f_i).grid(row=0, column=10)
                                                                        # TODO: s 'TAB' da se mesti migastijyt kursor
            Label(novprozorec, text='"a" as in AT', bg=f_i).grid(row=1, column=10)
            Entry(novprozorec, textvariable=self.t2, width=e_w).grid(row=1, column=11)
            Checkbutton(novprozorec, var=self.n2, bg=f_i).grid(row=1, column=12)

            Label(novprozorec, text='"e" as in ED', bg=f_i).grid(row=2, column=10)
            Entry(novprozorec, textvariable=self.t11, width=e_w).grid(row=2, column=11)
            Checkbutton(novprozorec, var=self.n11, bg=f_i).grid(row=2, column=12)

            Label(novprozorec, text='"i" as in IT', bg=f_i).grid(row=3, column=10)
            Entry(novprozorec, textvariable=self.t17, width=e_w).grid(row=3, column=11)
            Checkbutton(novprozorec, var=self.n17, bg=f_i).grid(row=3, column=12)

            Label(novprozorec, text='"o" as in ODD', bg=f_i).grid(row=4, column=10)
            Entry(novprozorec, textvariable=self.t1, width=e_w).grid(row=4, column=11)
            Checkbutton(novprozorec, var=self.n1, bg=f_i).grid(row=4, column=12)

            Label(novprozorec, text='"u" as in HUT', bg=f_i).grid(row=5, column=10)
            Entry(novprozorec, textvariable=self.t3, width=e_w).grid(row=5, column=11)
            Checkbutton(novprozorec, var=self.n3, bg=f_i).grid(row=5, column=12)

            # ------------------ Vowel sounds - long -----------------------------------------

            Label(novprozorec, text='Long vowels', font=big_font, bg=f_i).grid(row=6, column=10)
            Label(novprozorec, text='"a" as in CATE', bg=f_i).grid(row=7, column=10)
            Entry(novprozorec, textvariable=self.t13, width=e_w).grid(row=7, column=11)
            Checkbutton(novprozorec, var=self.n13, bg=f_i).grid(row=7, column=12)

            Label(novprozorec, text='"ay" as in PAYDAY', bg=f_i).grid(row=7, column=13)
            Entry(novprozorec, textvariable=self.t1301, width=e_w).grid(row=7, column=14)
            Checkbutton(novprozorec, var=self.n1301, bg=f_i).grid(row=7, column=15)

            Label(novprozorec, text='"ea" as in EAT', bg=f_i).grid(row=8, column=10)
            Entry(novprozorec, textvariable=self.t18, width=e_w).grid(row=8, column=11)
            Checkbutton(novprozorec, var=self.n18, bg=f_i).grid(row=8, column=12)

            Label(novprozorec, text='"i" as in HIDE', bg=f_i).grid(row=9, column=10)
            Entry(novprozorec, textvariable=self.t6, width=e_w).grid(row=9, column=11)
            Checkbutton(novprozorec, var=self.n6, bg=f_i).grid(row=9, column=12)

            Label(novprozorec, text='"oa" as in FLOAT', bg=f_i).grid(row=10, column=10)
            Entry(novprozorec, textvariable=self.t25, width=e_w).grid(row=10, column=11)
            Checkbutton(novprozorec, var=self.n25, bg=f_i).grid(row=10, column=12)

            Label(novprozorec, text='"oo" as in TOO', bg=f_i).grid(row=11, column=10)
            Entry(novprozorec, textvariable=self.t34, width=e_w).grid(row=11, column=11)
            Checkbutton(novprozorec, var=self.n34, bg=f_i).grid(row=11, column=12)

            Label(novprozorec, text='"oy" as in TOY', bg=f_i).grid(row=12, column=10)
            Entry(novprozorec, textvariable=self.t26, width=e_w).grid(row=12, column=11)
            Checkbutton(novprozorec, var=self.n26, bg=f_i).grid(row=12, column=12)

            Label(novprozorec, text='"oi" as in OIL', bg=f_i).grid(row=12, column=13)
            Entry(novprozorec, textvariable=self.t2601, width=e_w).grid(row=12, column=14)
            Checkbutton(novprozorec, var=self.n2601, bg=f_i).grid(row=12, column=15)

            Label(novprozorec, text='"ough" as in OUGHT', bg=f_i).grid(row=13, column=10)
            Entry(novprozorec, textvariable=self.t4, width=e_w).grid(row=13, column=11)
            Checkbutton(novprozorec, var=self.n4, bg=f_i).grid(row=13, column=12)

            Label(novprozorec, text='"ow" as in COW', bg=f_i).grid(row=14, column=10)
            Entry(novprozorec, textvariable=self.t5, width=e_w).grid(row=14, column=11)
            Checkbutton(novprozorec, var=self.n5, bg=f_i).grid(row=14, column=12)

            Label(novprozorec, text='"e" as in GIVEN', bg=f_i).grid(row=1, column=13)
            Entry(novprozorec, textvariable=self.t41, width=e_w).grid(row=1, column=14)
            Checkbutton(novprozorec, var=self.n41, bg=f_i).grid(row=1, column=15)

            Label(novprozorec, text='"oo" as in HOOD', bg=f_i).grid(row=2, column=13)
            Entry(novprozorec, textvariable=self.t33, width=e_w).grid(row=2, column=14)
            Checkbutton(novprozorec, var=self.n33, bg=f_i).grid(row=2, column=15)

            Label(novprozorec, text='"y" as in SIMPLY', bg=f_i).grid(row=3, column=13)
            Entry(novprozorec, textvariable=self.t40, width=e_w).grid(row=3, column=14)
            Checkbutton(novprozorec, var=self.n40, bg=f_i).grid(row=3, column=15)

            # ------------------ Rhotic vowels -----------------------------------------

            Label(novprozorec, text='Rhotic vowels', font=big_font, bg=f_i).grid(row=0, column=16)
            Label(novprozorec, text='"air" as in HAIR', bg=f_i).grid(row=1, column=16)
            Entry(novprozorec, textvariable=self.tr1, width=e_w).grid(row=1, column=17)
            Checkbutton(novprozorec, var=self.nr1, bg=f_i).grid(row=1, column=18)

            Label(novprozorec, text='"ar" as in HARD', bg=f_i).grid(row=2, column=16)
            Entry(novprozorec, textvariable=self.tr2, width=e_w).grid(row=2, column=17)
            Checkbutton(novprozorec, var=self.nr2, bg=f_i).grid(row=2, column=18)

            Label(novprozorec, text='"eer" as in BEER', bg=f_i).grid(row=3, column=16)
            Entry(novprozorec, textvariable=self.tr3, width=e_w).grid(row=3, column=17)
            Checkbutton(novprozorec, var=self.nr3, bg=f_i).grid(row=3, column=18)

            Label(novprozorec, text='"or" as in FORD', bg=f_i).grid(row=4, column=16)
            Entry(novprozorec, textvariable=self.tr4, width=e_w).grid(row=4, column=17)
            Checkbutton(novprozorec, var=self.nr4, bg=f_i).grid(row=4, column=18)

            Label(novprozorec, text='"er" stressed', bg=f_i).grid(row=5, column=16)
            Entry(novprozorec, textvariable=self.t12, width=e_w).grid(row=5, column=17)
            Checkbutton(novprozorec, var=self.n12, bg=f_i).grid(row=5, column=18)

            Label(novprozorec, text='"er" unstressed', bg=f_i).grid(row=6, column=16)
            Entry(novprozorec, textvariable=self.t42, width=e_w).grid(row=6, column=17)
            Checkbutton(novprozorec, var=self.n42, bg=f_i).grid(row=6, column=18)

            # ------------------ Consonant sounds -----------------------------------------

            Label(novprozorec, text='Consonant', font=big_font, bg=f_i).grid(row=0, column=0)
            Label(novprozorec, text='"b" as in BE', bg=f_i).grid(row=1, column=nula)
            Entry(novprozorec, textvariable=self.t7, width=e_w).grid(row=1, column=edno)
            Checkbutton(novprozorec, var=self.n7, bg=f_i).grid(row=1, column=dve)

            Label(novprozorec, text='"ch" as in CHEESE', bg=f_i).grid(row=2, column=nula)
            Entry(novprozorec, textvariable=self.t8, width=e_w).grid(row=2, column=edno)
            Checkbutton(novprozorec, var=self.n8, bg=f_i).grid(row=2, column=dve)

            Label(novprozorec, text='"d" as in DEE', bg=f_i).grid(row=3, column=nula)
            Entry(novprozorec, textvariable=self.t9, width=e_w).grid(row=3, column=edno)
            Checkbutton(novprozorec, var=self.n9, bg=f_i).grid(row=3, column=dve)

            Label(novprozorec, text='"f" as in FEE', bg=f_i).grid(row=4, column=nula)
            Entry(novprozorec, textvariable=self.t14, width=e_w).grid(row=4, column=edno)
            Checkbutton(novprozorec, var=self.n14, bg=f_i).grid(row=4, column=dve)

            Label(novprozorec, text='"g" as in GREEN', bg=f_i).grid(row=5, column=nula)
            Entry(novprozorec, textvariable=self.t15, width=e_w).grid(row=5, column=edno)
            Checkbutton(novprozorec, var=self.n15, bg=f_i).grid(row=5, column=dve)

            Label(novprozorec, text='"h" as in HE', bg=f_i).grid(row=6, column=nula)
            Entry(novprozorec, textvariable=self.t16, width=e_w).grid(row=6, column=edno)
            Checkbutton(novprozorec, var=self.n16, bg=f_i).grid(row=6, column=dve)

            Label(novprozorec, text='"j" as in JAM', bg=f_i).grid(row=7, column=nula)
            Entry(novprozorec, textvariable=self.t19, width=e_w).grid(row=7, column=edno)
            Checkbutton(novprozorec, var=self.n19, bg=f_i).grid(row=7, column=dve)

            Label(novprozorec, text='"k" as in KEY', bg=f_i).grid(row=8, column=0)
            Entry(novprozorec, textvariable=self.t20, width=e_w).grid(row=8, column=1)
            Checkbutton(novprozorec, var=self.n20, bg=f_i).grid(row=8, column=2)

            Label(novprozorec, text='"l" as in LEE', bg=f_i).grid(row=9, column=0)
            Entry(novprozorec, textvariable=self.t21, width=e_w).grid(row=9, column=1)
            Checkbutton(novprozorec, var=self.n21, bg=f_i).grid(row=9, column=2)

            Label(novprozorec, text='"m" as in ME', bg=f_i).grid(row=10, column=0)
            Entry(novprozorec, textvariable=self.t22, width=e_w).grid(row=10, column=1)
            Checkbutton(novprozorec, var=self.n22, bg=f_i).grid(row=10, column=2)

            Label(novprozorec, text='"n" as in NICE', bg=f_i).grid(row=11, column=0)
            Entry(novprozorec, textvariable=self.t23, width=e_w).grid(row=11, column=1)
            Checkbutton(novprozorec, var=self.n23, bg=f_i).grid(row=11, column=2)

            Label(novprozorec, text='"ng" as in PING', bg=f_i).grid(row=12, column=0)
            Entry(novprozorec, textvariable=self.t24, width=e_w).grid(row=12, column=1)
            Checkbutton(novprozorec, var=self.n24, bg=f_i).grid(row=12, column=2)

            Label(novprozorec, text='"p" as in PEE', bg=f_i).grid(row=13, column=0)
            Entry(novprozorec, textvariable=self.t27, width=e_w).grid(row=13, column=1)
            Checkbutton(novprozorec, var=self.n27, bg=f_i).grid(row=13, column=2)

            Label(novprozorec, text='"r" as in READ', bg=f_i).grid(row=14, column=0)
            Entry(novprozorec, textvariable=self.t28, width=e_w).grid(row=14, column=1)
            Checkbutton(novprozorec, var=self.n28, bg=f_i).grid(row=14, column=2)

            Label(novprozorec, text='"s" as in SEA', bg=f_i).grid(row=15, column=0)
            Entry(novprozorec, textvariable=self.t29, width=e_w).grid(row=15, column=1)
            Checkbutton(novprozorec, var=self.n29, bg=f_i).grid(row=15, column=2)

            Label(novprozorec, text='"sh" as in SHE', bg=f_i).grid(row=1, column=tri)
            Entry(novprozorec, textvariable=self.t30, width=e_w).grid(row=1, column=cetiri)
            Checkbutton(novprozorec, var=self.n30, bg=f_i).grid(row=1, column=pet)

            Label(novprozorec, text='"t" as in TEA', bg=f_i).grid(row=2, column=tri)
            Entry(novprozorec, textvariable=self.t31, width=e_w).grid(row=2, column=cetiri)
            Checkbutton(novprozorec, var=self.n31, bg=f_i).grid(row=2, column=pet)

            Label(novprozorec, text='"th" as in THAT', bg=f_i).grid(row=3, column=tri)
            Entry(novprozorec, textvariable=self.t32, width=e_w).grid(row=3, column=cetiri)
            Checkbutton(novprozorec, var=self.n32, bg=f_i).grid(row=3, column=pet)

            Label(novprozorec, text='"th" as in THIN', bg=f_i).grid(row=4, column=tri)
            Entry(novprozorec, textvariable=self.t10, width=e_w).grid(row=4, column=cetiri)
            Checkbutton(novprozorec, var=self.n10, bg=f_i).grid(row=4, column=pet)

            Label(novprozorec, text='"v" as in VEE', bg=f_i).grid(row=5, column=tri)
            Entry(novprozorec, textvariable=self.t35, width=e_w).grid(row=5, column=cetiri)
            Checkbutton(novprozorec, var=self.n35, bg=f_i).grid(row=5, column=pet)

            Label(novprozorec, text='"w" as in WE', bg=f_i).grid(row=6, column=tri)
            Entry(novprozorec, textvariable=self.t36, width=e_w).grid(row=6, column=cetiri)
            Checkbutton(novprozorec, var=self.n36, bg=f_i).grid(row=6, column=pet)

            Label(novprozorec, text='"y" as in YIELD', bg=f_i).grid(row=7, column=tri)
            Entry(novprozorec, textvariable=self.t37, width=e_w).grid(row=7, column=cetiri)
            Checkbutton(novprozorec, var=self.n37, bg=f_i).grid(row=7, column=pet)

            Label(novprozorec, text='"z" as in ZEE', bg=f_i).grid(row=8, column=tri)
            Entry(novprozorec, textvariable=self.t38, width=e_w).grid(row=8, column=cetiri)
            Checkbutton(novprozorec, var=self.n38, bg=f_i).grid(row=8, column=pet)

            Label(novprozorec, text='"z" as in SEIZURE', bg=f_i).grid(row=9, column=tri)
            Entry(novprozorec, textvariable=self.t39, width=e_w).grid(row=9, column=cetiri)
            Checkbutton(novprozorec, var=self.n39, bg=f_i).grid(row=9, column=pet)

            # Label(novprozorec).grid(row=19, column=0)
            novprozorec.resizable(height=0, width=0)
            # menubarnov = Menu(novprozorec)
            # editmenu = Menu(menubarnov, tearoff=0)
            # editmenu.add_command(label="Cut", accelerator="Ctrl+X",
            #                      command=lambda: novprozorec.focus_get().event_generate('<<Cut>>'))
            # editmenu.add_command(label="Copy", accelerator="Ctrl+C",
            #                      command=lambda: novprozorec.focus_get().event_generate('<<Copy>>'))
            # editmenu.add_command(label="Paste", accelerator="Ctrl+V",
            #                      command=lambda: novprozorec.focus_get().event_generate('<<Paste>>'))
            # menubarnov.add_cascade(label="Edit", menu=editmenu)
            #

            #
            # novprozorec.bind("<Escape>", exit)

    def spec(self):
        global specialni_pravila

        try:
            if specialni_pravila.state() == 'normal':
                specialni_pravila.focus()
        except:
            specialni_pravila = Toplevel()
            specialni_pravila.title('EXPANDED RULES')
            specialni_pravila.focus()
            specialni_pravila.iconbitmap('data/ico/icon2.ico')
            specialni_pravila.bind('<Escape>', lambda e: specialni_pravila.destroy())
            f_i = "#606060"

            self.expandrules(specialni_pravila)

            Button(specialni_pravila, height=1, width=19, text='CLOSE', command=self.close_popout_window, bg=f_i). \
                place(relx=0, rely=0)  # grid(row=0, column=0, sticky=NW)
            specialni_pravila.resizable(height=0, width=0)

    def close_popout_window(self):
        if specialni_pravila.state() == 'normal':
            specialni_pravila.destroy()
            ruw.sysht.config(text='0')

    def runmerun(self):
        if self.sysht.cget("text") == '0':
            self.expandrules(self.pod_proz)
            self.sysht.config(text='1')
        elif self.sysht.cget("text") == '3':
            specialni_pravila.destroy()
            self.sysht.config(text='1')
            self.expandrules(self.pod_proz)

    @staticmethod
    def expandrules(xx):
        f_i = "#606060"
        row_one = Frame(xx, bg=f_i)
        row_one.pack()
        e_w = 3  # entry_width

        def izkoci_pop():
            ruw.spec()
            ruw.sysht.config(text='3')
            row_one.destroy()
            xx.config(height=20, width=800)

        def zatvori_pop():
            row_one.destroy()
            xx.config(height=20, width=800)
            ruw.sysht.config(text='0')

        Button(row_one, text='POPOUT', command=izkoci_pop, bg=f_i).grid(row=0, column=0)
        Button(row_one, text='Close', command=zatvori_pop, bg=f_i).grid(row=0, column=0, sticky=W)

        Label(row_one, text='CHAGE "qu-" to', bg=f_i).grid(row=1, column=0)
        Entry(row_one, textvar=chw.tsp1, width=e_w).grid(row=1, column=1)
        Checkbutton(row_one, var=chw.nsp1, bg=f_i).grid(row=1, column=2)

        Label(row_one, text='CHAGE "-nk" to', bg=f_i).grid(row=1, column=3)
        Entry(row_one, textvar=chw.tsp2, width=e_w).grid(row=1, column=4)
        Checkbutton(row_one, var=chw.nsp2, bg=f_i).grid(row=1, column=5)

        Label(row_one, text='CHAGE "-o" as in ago to', bg=f_i).grid(row=1, column=6)
        Entry(row_one, textvar=chw.tsp3, width=e_w).grid(row=1, column=7)
        Checkbutton(row_one, var=chw.nsp3, bg=f_i).grid(row=1, column=8)

        Label(row_one, text='CHAGE "ou-" before "nd/nt/t/l"', bg=f_i).grid(row=2, column=0)
        Entry(row_one, textvariable=chw.tsp0, width=e_w).grid(row=2, column=1)
        Checkbutton(row_one, var=chw.nsp0, bg=f_i).grid(row=2, column=2)

        Label(row_one, text='CHAGE "schwa"/ə/ in beginig to', bg=f_i).grid(row=3, column=0)
        Entry(row_one, textvar=chw.tsp10, width=e_w).grid(row=3, column=1)
        Checkbutton(row_one, var=chw.nsp10, bg=f_i).grid(row=3, column=2)

        Label(row_one, text='/ə/ in the end(longer than 3 letters)', bg=f_i).grid(row=4, column=0)
        Entry(row_one, textvar=chw.tsp11, width=e_w).grid(row=4, column=1)
        Checkbutton(row_one, var=chw.nsp11, bg=f_i).grid(row=4, column=2)

        Label(row_one, text='CHAGE "-еu(yoo)" to', bg=f_i).grid(row=2, column=3)
        Entry(row_one, textvar=chw.tsp4, width=e_w).grid(row=2, column=4)
        Checkbutton(row_one, var=chw.nsp4, bg=f_i).grid(row=2, column=5)

        Label(row_one, text='CHAGE "k-" before "a,ə,o,u,ä,r,t,l" to', bg=f_i).grid(row=2, column=6)
        Entry(row_one, textvar=chw.tsp5, width=e_w).grid(row=2, column=7)
        Checkbutton(row_one, var=chw.nsp5, bg=f_i).grid(row=2, column=8)

        Label(row_one, text='CHAGE "rr" in "marry" to', bg=f_i).grid(row=3, column=3)
        Entry(row_one, textvar=chw.tsp8, width=e_w).grid(row=3, column=4)
        Checkbutton(row_one, var=chw.nsp8, bg=f_i).grid(row=3, column=5)

        Label(row_one, text='CHAGE "x"/gz/ in "exact" to', bg=f_i).grid(row=3, column=6)
        Entry(row_one, textvar=chw.tsp9, width=e_w).grid(row=3, column=7)
        Checkbutton(row_one, var=chw.nsp9, bg=f_i).grid(row=3, column=8)

        Label(row_one, text='CHAGE -z plurals to', bg=f_i).grid(row=4, column=3)
        Entry(row_one, textvar=chw.tsp13, width=e_w).grid(row=4, column=4)
        Checkbutton(row_one, var=chw.nsp13, bg=f_i).grid(row=4, column=5)

        Label(row_one, text='CHAGE "tio" in "-tion" to', bg=f_i).grid(row=5, column=3)
        Entry(row_one, textvar=chw.tsp6, width=e_w).grid(row=5, column=4)
        Checkbutton(row_one, var=chw.nsp6, bg=f_i).grid(row=5, column=5)

        Label(row_one, text='CHAGE "sio" in "-sion" to', bg=f_i).grid(row=6, column=3)
        Entry(row_one, textvar=chw.tsp7, width=e_w).grid(row=6, column=4)
        Checkbutton(row_one, var=chw.nsp7, bg=f_i).grid(row=6, column=5)

        Label(row_one, text='CHAGE -x-/ks/ to', bg=f_i).grid(row=4, column=6)
        Entry(row_one, textvar=chw.tsp14, width=e_w).grid(row=4, column=7)
        Checkbutton(row_one, var=chw.nsp14, bg=f_i).grid(row=4, column=8)

        Label(row_one, text='CHAGE -ed /voiced/ to', bg=f_i).grid(row=6, column=0)
        Entry(row_one, textvar=chw.tsp15, width=e_w).grid(row=6, column=1)
        Checkbutton(row_one, var=chw.nsp15, bg=f_i).grid(row=6, column=2)

        Label(row_one, text='CHAGE -ed /voiceless/ to', bg=f_i).grid(row=5, column=0)
        Entry(row_one, textvar=chw.tsp16, width=e_w).grid(row=5, column=1)
        Checkbutton(row_one, var=chw.nsp16, bg=f_i).grid(row=5, column=2)

        Label(row_one, text='CHAGE -ed /vowle+voiced/ to', bg=f_i).grid(row=7, column=0)
        Entry(row_one, textvar=chw.tsp17, width=e_w).grid(row=7, column=1)
        Checkbutton(row_one, var=chw.nsp17, bg=f_i).grid(row=7, column=2)

        Label(row_one, text='CHAGE -x/ks/ to', bg=f_i).grid(row=5, column=6)
        Entry(row_one, textvar=chw.tsp18, width=e_w).grid(row=5, column=7)
        Checkbutton(row_one, var=chw.nsp18, bg=f_i).grid(row=5, column=8)

        Label(row_one, text='......', bg=f_i).grid(row=6, column=6)
        Entry(row_one, textvar=chw.tsp12, width=e_w).grid(row=6, column=7)
        Checkbutton(row_one, var=chw.nsp12, bg=f_i).grid(row=6, column=8)

        Label(row_one, text='ENTER excludet words', bg=f_i).grid(row=8, column=0)
        Entry(row_one, textvar=chw.tsp20, width=35).grid(row=9, column=0, columnspan=3)
        Checkbutton(row_one, var=chw.nsp20, bg=f_i).grid(row=8, column=1)

        Checkbutton(row_one, var=chw.nsp19, text="doble the 's' at the end of words/RichSpell/", bg=f_i).grid(row=10, column=0, columnspan=3)
        Checkbutton(row_one, var=chw.nsp21, text="Long vowel rule/RichSpell/", bg=f_i).grid(row=11, column=0, columnspan=3)


chw = Chechboxes()
ruw = Rule_window()
