# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задача: написать программу, создающую структуру каталогов
# в выбранном каталоге
# bin
#   images
#       png
#       jpeg
#   filters
#   dlls

import os
import sys

# Проверка на кол-во аргументов
if len(sys.argv) < 2:
    print(f"Дано аргументов {len(sys.argv) - 1}. Нужен один.")
    exit(1)
# Проверка на существование пути
if not os.path.exists(sys.argv[1]):
    print("Путь не существует.")
    exit(1)


# Функция создания структуры
def make_directory():
    os.mkdir(sys.argv[1] + "\\bin")
    os.mkdir(sys.argv[1] + "\\bin" + "\\filter")
    os.mkdir(sys.argv[1] + "\\bin" + "\\dlls")
    os.mkdir(sys.argv[1] + "\\bin" + "\\images")
    os.mkdir(sys.argv[1] + "\\bin" + "\\images" + "\\png")
    os.mkdir(sys.argv[1] + "\\bin" + "\\images" + "\\jpeg")


# Опциональная функция для просмотра созданной структуры
def check_directory():
    path = sys.argv[1] + "\\bin"
    print("Created structure:")
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(sub_indent, f))


try:
    make_directory()
    check_directory()
except FileExistsError:  # Проверка на уже имеющуюся структуру в данном каталоге
    print("Path already exist.")
    exit(1)

# print(list(os.scandir(sys.argv[1])))
