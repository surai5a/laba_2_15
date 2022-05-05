# 18 var - 3 zad
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Не даны имена файлов!", file=sys.stderr)
        sys.exit(1)
    mas = []
    for i in range(1, len(sys.argv)):
        try:
            with open(sys.argv[i], "r", encoding="utf-8") as f:
                text = f.readlines()
                for j in text:
                    mas.append(j.rstrip())
        except FileNotFoundError:
            print(f'{sys.argv[i]} не удалось открыть.')
            continue

    print(' '.join(mas))
