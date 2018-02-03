#!/usr/bin/python3
# coding: utf-8

from lib import step,alf

s1 = input('Введите текст: ')
res = u''
for c in s1:
    if c not in alf:
        res += c
        continue
    i = alf.index(c)
    i -= step
    res += alf[i]
print(res)
