# with open('recnik_za_o.txt', "r", encoding='utf-8') as file:
#     list_malyk = file.read().split()
#

#
# import re
# # op_list_in = []
# # op_list_out = []
# # =-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-
# # dumi_za_upr = []
# #
# # for word in list_in:
# #     if word.endswith('ce'):
# #         nom = list_in.index(word)
# #         foneticna_duma = list_out[nom] + 'S'
# #         op_list_out[nom] = foneticna_duma
# #         dumi_za_upr.append(word)
# #
# #     elif word.endswith('ss'):
# #         nom2 = list_in.index(word)
# #         foneticna_duma2 = op_list_out[nom2] + 'S'
# #         op_list_out[nom2] = foneticna_duma2
# #         dumi_za_upr.append(word)
# #
# #
# #     elif word.endswith('se'):
# #         nom3 = list_in.index(word)
# #         foneticna_duma3 = list_out[nom3] + 'S'
# #         op_list_out[nom3] = foneticna_duma3
# #         dumi_za_upr.append(word)
# # =-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-
#
#
# # =-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-
# # for g in dumi_za_upr:
# #     for dumaa in list_in:
# #         if g in dumaa:
# #             # print(dumaa)
# #             nom = list_in.index(dumaa)
# #             foneticna_duma = list_out[nom]
# # op_list_in = []
# # op_list_out = list_out
# # for word in list_in:
# #     if '(1)' in word:
# #         nom = list_in.index(word)
# #         duma1 = list_out[nom-1]
# #         duma2 = list_out[nom]
# #         duma = f"{duma1}/{duma2}"
# #         op_list_out[nom-1] = duma
# #         op_list_in.append(word)
# #     elif '(2)' in word:
# #         nom = list_in.index(word)
# #         duma1 = list_out[nom-2]
# #         duma2 = list_out[nom]
# #         duma = f"{duma1}/{duma2}"
# #         op_list_out[nom-2] = duma
# #         op_list_in.append(word)
# #     elif '(3)' in word:
# #         nom = list_in.index(word)
# #         duma1 = list_out[nom-3]
# #         duma2 = list_out[nom]
# #         duma = f"{duma1}/{duma2}"
# #         op_list_out[nom-3] = duma
# #         op_list_in.append(word)
# #     else:
# #         op_list_in.append(word)
# # -=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-
# # =-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-
# # ss_dumi = []
# #
# # for word in list_in:
# #     if word.endswith('x'):
# #         wordindex = list_in.index(word)
# #         foniword = op_list_out[wordindex]
# #         if foniword.endswith('KS'):
# #             newfoni = re.sub(r"(KS$)|(KS/)", 'ɣ/', foniword)
# #
# #             op_list_out[wordindex] = newfoni
# #
# #         # elif foniword.endswith('T'):
# #         #     newfoni2 = re.sub(r"(T$)|(T/)", 'ђ/', foniword)
# #         #
# #         #     op_list_out[wordindex] = newfoni2
# #         # elif foniword.endswith('D'):
# #         #     newfoni3 = re.sub(r"(D$)|(D/)", 'ћ/', foniword)
# #         #
# #         #     op_list_out[wordindex] = newfoni3
# # =-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-
#
#
# #
# # with open('TEST_dumi.txt', "w", encoding='utf-8') as out1:
# #     out1.writelines("\n".join(list_in))
# import _pickle as pickle
# dik_lt = []
#
# for word in list_malyk:
#     if word in list_in:
#         nom = list_in.index(word)
#         foni = list_out[nom]
#         dik_lt.append(foni)
#
#
#
#
#


# import xlsxwriter
# workbook = xlsxwriter.Workbook('recnik_za_o.xlsx')
# worksheet = workbook.add_worksheet()
#
# korder = sorted(dik.keys())
# vorder = sorted(dik.values())
# row = 0
# col = 0
# for key in korder:
#
#     row += 1
#     # print(key)
#     worksheet.write(row, col,     key)
#
# row = 0
# col = 1
# for value in vorder:
#
#
#     row += 1
#     # print(value)
#     worksheet.write(row, col, value)
# workbook.close()
#
from tqdm import tqdm

with open('fonemi.txt', "r", encoding='utf-8') as file2:
    lst_vyn = file2.read().split()

with open('dumi.txt', "r", encoding='utf-8') as file:
    lst = file.read().split()

# lst = ["a", "am", "amß", "am's", "am'sß", "amabel", "amabelle", "amabile"]
# lst_vyn = ["ə", "ÆM/ÉɛM","ÉɛM","ÆMZ/ÉɛMZ","ÉɛMZ","ÆMəBɛL","ÆMəBəL","ɒMɒBəL"]

o_lst = []
o_lst_vyn = []

for word in tqdm(lst):
    nom = lst.index(word)
    duma = lst[nom - 1]
    dduma = lst[nom]
    foni = lst_vyn[nom - 1]
    ffoni = lst_vyn[nom]
    if "ß" not in word:
        o_lst.append(dduma)
        o_lst_vyn.append(ffoni)
    elif "/" in foni:
        o_lst.append(duma+'1')
        o_lst_vyn.append(foni.split('/')[0])
        if word.endswith('ß'):
            d = duma + '2'
            o_lst.append(d)
            o_lst_vyn.append(ffoni)

with open('test/TEST_V2_fonemi.txt', "w", encoding='utf-8') as out2:
    out2.writelines("\n".join(o_lst_vyn))

with open('test/TEST_V2_dumi.txt', "w", encoding='utf-8') as out2:
    out2.writelines("\n".join(o_lst))



print('>>done!<<')