#this is for vowpal wabbit

from collections import Counter
from hazm import sent_tokenize
#import hazm
import math

def readData(fileName):
    file = open(fileName, 'r')
    data = file.read().split(u".")
    sample_set = []
    for sample in data:
        if sample.__len__() > 1:
            sample_set.append(sample)
    return sample_set

file=open("result.txt","w")
#reading data
file1 = 'Ahmadinejad.txt'
file2 = "mosavi.txt"
sample_set1 = readData(file1)
sample_set2=readData(file2)

print('************* SENTENCE TOKENIZATION ***************')
all_sentences1 = []
for sample in sample_set1:
    sentences1 = sent_tokenize(sample)
    all_sentences1.extend(sentences1)
#print(all_sentences)

print('************* SENTENCE TOKENIZATION ***************')
all_sentences2 = []
for sample in sample_set2:
    sentences2 = sent_tokenize(sample)
    all_sentences2.extend(sentences2)

size2=all_sentences2.__len__()
size1=all_sentences1.__len__()

if(size1> size2):
        num = size2
elif(size1< size2):
        num = size1


all_words = {}
cnt1 =1
cnt2 = 0
print(num)
for s in all_sentences1:
    all_words[cnt1] = s
    cnt1 += 2
    if (cnt1 > 2*num):
        break

for s in all_sentences2:
    all_words[cnt2] = s
    cnt2 += 2
    if (cnt2 > 2*num):
        break

for k , v in all_words.items():
    m = divmod(k,2)
    if m[1]==0:
       # m==-1
        file.write("-1" + '|' + v + "\n")
    else:
        file.write(str(m[1]) + '|' + v + "\n")

file.close()








