# Python_Project
Just Some Library For My Python Project...

<h1 align="center">Phyton Study Module</h1>
First you must install this library at your terminal :

```
.\ pip install readchar
.\ pip install colorama
```

But in optional, this is the library that i use to make this project :

```python
import os
import msvcrt
import readchar
import random
import math
from colorama import init, Fore, Back, Style
```

Oh i forgot, hehe before begin you must insert this password : "112233"
Because i make a login page from this coding :

```python
while True:
    name = input("[ What Is Your Name  : ")
    if len(name.strip()) == 0:  # Memeriksa apakah input kosong setelah menghapus spasi di awal dan akhir
        print(" Please Insert Your Name!")
    else:
        break
while True:
    try:
        age = int(input("[ How Old Are You    : "))
        break
    except ValueError:
        print(" Invalid Input. Please Enter A Valid Integer For Age !\n")
while True:
        password = int(input("[ Enter The Password : "))
        if password == pattern:
            os.system('cls')
            print(" Password Accepted!")
            break
        else:
            os.system('cls')
            print(" Incorrect Password!")
```
