from tqdm import tqdm


with open('dumi.txt', "r", encoding='utf-8') as file:
    spisyk_v = file.read().split()


with open('fonemi.txt', "r", encoding='utf-8') as file2:
    spisyk_vyn = file2.read().split()


for i, w in enumerate(spisyk_v):
    if 'oy' in w:

        wrd = spisyk_vyn[i].replace('µ', 'λ')
        spisyk_vyn[i] = wrd



with open('NEWdumi.txt', "w", encoding='utf-8') as f:
    for wt in spisyk_v:
        f.write(f"{wt}\n")


with open('NEWfonemi.txt', "w", encoding='utf-8') as f2:
    for wt2 in spisyk_vyn:
        f2.write(f"{wt2}\n")



print('>>> DONE <<<')