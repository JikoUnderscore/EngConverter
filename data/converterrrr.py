from tqdm import tqdm
import pickle

with open('dumi.txt', "r", encoding='utf-8') as file:
    spisyk_v = file.read().split()


with open('fonemi.txt', "r", encoding='utf-8') as file2:
    spisyk_vyn = file2.read().split()


recnik = dict(zip(spisyk_v, spisyk_vyn))


recnik_abc = {'a':{}, 'b':{},'c':{},'d':{},'e':{},'f':{},'g':{},'h':{},'i':{},'j':{},'k':{},'l':{},'m':{},'n':{},'o':{},
              'p':{},'q':{},'r':{},'s':{},'t':{},'u':{},'v':{},'w':{},'x':{},'y':{},'z':{}}


for key in tqdm(recnik_abc.keys()):
    for k, v in recnik.items():
        if k.startswith(key):
            recnik_abc[key][k] = v


with open('filename.pkl', 'wb') as handle:
    pickle.dump(recnik_abc, handle, protocol=pickle.HIGHEST_PROTOCOL)

print('>>> DONE <<<')