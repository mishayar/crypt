#!/usr/bin/python3
# coding: utf-8

step = 4
alf = u'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
s1 = input('Введите текст: ')
res = u''
for c in s1:
    if c not in alf:
        res += c
        continue
    i = alf.index(c)
    i += step
    if i >= len(alf):
        i = i - len(alf)
    res += alf[i]
print(res)
