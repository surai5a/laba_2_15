# 18 var - 18 zad
# !/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    with open("ind1.txt", "r", encoding="utf-8") as f:
        sentences = f.readlines()

    mas1 = []
    mas2 = []

    for sentence in sentences:
        if len(sentence.split()[0]) == 1:
            mas1.append(sentence)
        else:
            mas2.append(sentence)

    for i in mas1:
        print(i)
    for i in mas2:
        print(i)
