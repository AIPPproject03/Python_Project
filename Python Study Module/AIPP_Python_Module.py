# This Is My Small Project For Studying Pyton
# Made By AIPPproject03 A.K.A A.Irwin Putra Pangesti
import os # Library For Clearscreen
import msvcrt # Library That Use By Windows For Readkey() Or Getch()
import readchar # Library That Often Use By Many System Operation For Readkey() or Getch()
import random # Library For Playing Games Or Just Making Logic Code For Randomize it
import math # Library For Math Solving Problems
from colorama import init, Fore, Back, Style # Library For Coloring The Font, Background And Style
init() # init(autoreset=True) ---> Biar Auto Reset Setelah Print Baru

intro =(Fore.GREEN+'''
  Hello And Wellcome To My Database Project Page
  This Is Just For Studying All About Python
  Let's Do This And Dont Forget To....
     \"KEEP YOUR SPIRIT RAISING\"\n ''')
print(intro)
print(" Press any key to continue...")
msvcrt.getch()
print(Style.RESET_ALL)
 

#==================================================================================================#
# Login Page...                                                                                    |
#==================================================================================================#
# Variables for login page :
name = ()
age = ()
password = ()
pattern = 112233

#=====( Process Input For Login )=====#
print(Back.LIGHTRED_EX)
os.system('cls' if os.name == 'nt' else 'clear') # nt jika os adalah Windows / clear jika os adalah Unix-compatible(Linux/macOs)
print(Style.BRIGHT+Fore.LIGHTRED_EX+"[-=-=-=-=-Login Page-=-=-=-=-=]")
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
os.system('cls')
print(" Press Any Key To Enter...")
readchar.readkey()
#-----( Output Of The Login Page )-----#
os.system('cls' if os.name == 'nt' else 'clear')
print(" Welcome  : " + name)
print(" Age      : " + str(age), end="")
if age == 1:
    print("st\n", end="")
elif age == 2:
    print("nd\n", end="")
elif age == 3:
    print("rd\n", end="")
else:
    print("th\n", end="")
print(" Password : " + str(password))
readchar.readkey()
print(Style.RESET_ALL)
#==================================================================================================#
# We're Going To The Main Program (AIPP_ZONE)...                                                   |
#==================================================================================================#
print(Style.BRIGHT+Fore.GREEN)
os.system('cls' if os.name == 'nt' else 'clear')
print(" Now We\'re At AIPPproject03 Zone...")
msvcrt.getch()
os.system('cls')
print(" You Can Do Anything Here...")
readchar.readkey()
os.system('cls')
print(" Press Any Key To Begin...")
msvcrt.getch()

#==================================================================================================#
# DATABASE FUNCTION AND PROCEDURE...                                                               |
#==================================================================================================#
database = {} # {} Sebagai Penanda Bahwa data-mahasiswa bersifat array
def input_data():
    code = input(" Enter The Code         : ")
    subject = input(" Enter The Subject Name : ")
    category = input(" Enter The Category     : ")
    database[code] = {"Subject": subject, "Category": category}
    print(" Data Has Been Accepted.")

def delete_data():
    if len(database) == 0:
        print(" There Is No Data")
    else:
        code = input(" Enter The Subject Code : ")
        if code in database:
            del database[code]
            print(" The Subject With Code", code, "Has Been Deleted.")
        else:
            print(" The Subject With Code", code, "Is Not Found.")

def edit_data():
    if len(database) == 0:
        print(" There Is No Data")
    else:
        code = input(" Enter The Subject Code : ")
        if code in database:
            print(" This Is The Current Data :")
            print(" Code     :", code)
            print(" Subject  :", database[code]["Subject"])
            print(" Category :", database[code]["Category"])

            subject = input(" Enter The New Subject  : ")
            category = input(" Enter The New Category : ")
            database[code]["Subject"] = subject
            database[code]["Category"] = category
            print(" Data Has Been Changed.")
        else:
            print(" The Subject With Code", code, "Is Not Found.")

def show_data():
    if len(database) > 0:
        print(" Database :")
        for code, data in database.items():
            print("|==============================|")
            print("| Code      :", code)
            print("| Subject   :", data["Subject"])
            print("| Jurusan   :", data["Category"])
            print("|==============================|")
    else:
        print(" There Is No Data")
#====================================[DATABASE PAGE END]===========================================#

#==================================================================================================#
# ALL ABOUT MATH FUNCTION AND PROCEDURE...                                                             |
#==================================================================================================#

def fibonacci(n):
    init_fibo = [0, 1]
    if n <= 0:
        return[]
    elif n == 1:
        return[0]
    elif n == 2:
        return init_fibo
    
    while len(init_fibo) < n:
        count_fibo = init_fibo[-1] + init_fibo[-2]
        init_fibo.append(count_fibo)
    return init_fibo

def calculator():
    while True:
        os.system("cls")
        print(" (+),(-),(*),(/)")
        operation = input("Enter The Operation: ")
        print()
        try:
            result_call = eval(operation)
            print(f"The Result Of {operation} = {result_call}")
            print()
        except:
            print("Invalid Expression. Please Enter A Valid Expression.")
            print()
            
        repeat = input("Do you want to repeat the program? (Y/N): ")
        if repeat.upper() == "N":
            break

def Figure_2D_3D():
    while True:
        os.system('cls')
        figMenu = 0
        print(" Welcome To Program Figure's Formula")
        print(" Choose 2D --> 2 or 3D ---> 3 ")
        figMenu = int(input(" Options : "))
        if figMenu == 1:
            print(" Invalid Instruction! Try Again")
        elif figMenu == 2:
            menu_2d = 0
            while menu_2d != 8:
                os.system('cls')
                print("|-----------[2D FIGURES]-----------|")
                print("| + |    Select The Figure's   | - |")
                print("|----------------------------------|")
                print("|[1] Square                        |")
                print("|[2] Rectangle                     |")
                print("|[3] Triangle                      |")
                print("|[4] Circle                        |")
                print("|[5] Parallelogram                 |")
                print("|[6] Rhombus                       |")
                print("|[7] Trapezoid                     |")
                print("|[8] Exit                          |")
                print("|==================================|")
                menu_2d = int(input(" You Choose : "))
                if menu_2d == 1:
                    Square()
                elif menu_2d == 2:
                    Rectangle()
                elif menu_2d == 3:
                    Triangle()
                elif menu_2d == 4:
                    Circle()
                elif menu_2d == 5:
                    Parallelogram()
                elif menu_2d == 6:
                    Rhombus()
                elif menu_2d == 7:
                    Trapezoid()
                elif menu_2d == 8:
                    print("Exit")
                    break
                msvcrt.getch()  
            break
        elif figMenu == 3:
            menu_3d = 0
            while menu_3d != 8:
                os.system('cls')
                print("|-----------[3D FIGURES]-----------|")
                print("| x |    Select The Figure's   | / |")
                print("|----------------------------------|")
                print("|[1] Cube                          |")
                print("|[2] Beam                          |")
                print("|[3] Ball                          |")
                print("|[4] Cylinder                      |")
                print("|[5] Cone                          |")
                print("|[6] Prism                         |")
                print("|[7] Pyramid                       |")
                print("|[8] Exit                          |")
                print("|==================================|")
                menu_3d = int(input(" You Choose : "))
                if menu_3d == 1:
                    Cube()
                elif menu_3d == 2:
                    Beam()
                elif menu_3d == 3:
                    Ball()
                elif menu_3d == 4:
                    Cylinder()
                elif menu_3d == 5:
                    Cone()
                elif menu_3d == 6:
                    Prism()
                elif menu_3d == 7:
                    Pyramid()
                elif menu_3d == 8:
                    print("Exit")
                    break
                msvcrt.getch()
            break
        else:
            print(" Invalid Options")
            
#[2D Figures]-[2D Figures]-[2D Figures]-[2D Figures]-[2D Figures]-[2D Figures]-[2D Figures]-[2D Figures]#
def Square():
    decimal = 2 # Batas angka belakang koma
    os.system('cls')
    print("|_____________________________________________|")
    print("|           *The Formula Of Square*           |")
    print("| Circumference = 4 x S                       |")
    print("| Area          = S x S                       |")
    print("| Diagonals     = S x sqrt(2)--> akar kuadrat |")
    print("|---------------------------------------------|")
    print(" Try It For Yourself!")
    print()
    
    s = int(input(" Input The Length Of The Square Side (s) : "))

    # The Counting Begin...
    K = 4 * s
    L = s * s
    D = s * (2 ** 0.5)
    D_format = "{:.{}f}".format(D, decimal)

    # The Output...
    print(" This Is The Result : ")
    print("[------------------------------------------------]")
    print(f"[ Circumference = {K}cm (Keliling)")
    print(f"[ Area          = {L}cm2 (Luas)")
    print(f"[ Diagonals     = {D_format} (Diagonal)")
    print("[------------------------------------------------]")

def Rectangle():
    decimal = 2 # Batas angka belakang koma
    os.system('cls')
    print("|_____________________________________________|")
    print("|         *The Formula Of Rectangle*          |")
    print("| Circumference = 2 ( p + l )                 |")
    print("| Area          = p x l                       |")
    print("| Diagonals     = ( p^2 + l^2 )sqrt(2)        |")
    print("|---------------------------------------------|")
    print(" Try It For Yourself!")
    print()

    p = int(input(" Input The Length Of The Rectangle (p) : "))
    l = int(input(" Input The Width Of The Rectangle (l)) : "))

    # The Counting Begin...
    K = 2 * (p + l)
    L = p * l
    D = (p ** 2 + l ** 2) ** 0.5
    D_format = "{:.{}f}".format(D, decimal)

    # The Output...
    print(" This Is The Result : ")
    print("[------------------------------------------------]")
    print(f"[ Circumference = {K}cm (Keliling)")
    print(f"[ Area          = {L}cm2 (Luas)")
    print(f"[ Diagonals     = {D_format} (Diagonal)")
    print("[------------------------------------------------]")

def Triangle():
    decimal = 2  # Batas angka belakang koma
    while True:
        os.system('cls')
        print("|_______________________________________________________|")
        print("|               *The Formula Of Triangle*               |")
        print("| Circumference = a + b + c                             |")
        print("| Semiperimeter = 1/2 * (a + b + c)                     |")
        print("| Area          = ((1/2) x b x t)                       |")
        print("| Area          or (sqrt(2)(s (s - a) (s - b) (s - c))) |")
        print("| Diagonals     = (a^2 + b^2) / 2                       |")
        print("|-------------------------------------------------------|")
        print(" Try It For Yourself!")
        print
        choice = input(" Choose The Calculation Method (s -> sisi or t -> tinggi): ")

        if choice == "s":
            a = int(input(" Input The Length Of Side a : "))
            b = int(input(" Input The Length Of Side b : "))
            c = int(input(" Input The Length Of Side c : "))

            # The Counting Begin...
            K = a + b + c
            s = (a + b + c) / 2  # Semiperimeter
            A = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Heron's formula
            D = (a ** 2 + b ** 2) / 2
            D_format = "{:.{}f}".format(D, decimal)

            # The Output...
            print("This Is The Result : ")
            print("[------------------------------------------------]")
            print(f"[ Circumference = {K}cm (Keliling)")
            print(f"[ Area          = {A}cm2 (Luas)")
            print(f"[ Diagonals     = {D_format} (Diagonal)")
            print("[------------------------------------------------]")
            break

        elif choice == "t":
            a = int(input(" Input The Length Of Side a : "))
            b = int(input(" Input The Length Of Side b : "))
            h = int(input(" Input The Height           : "))

            # The Counting Begin...
            K = a + b + (2 * ((a ** 2 + b ** 2) ** 0.5))
            A = (1/2) * b * h
            D = (a ** 2 + b ** 2) / 2
            D_format = "{:.{}f}".format(D, decimal)

            # The Output...
            print("This Is The Result : ")
            print("[------------------------------------------------]")
            print(f"[ Circumference = {K}cm (Keliling)")
            print(f"[ Area          = {A}cm2 (Luas)")
            print(f"[ Diagonals     = {D_format} (Diagonal)")
            print("[------------------------------------------------]")
            break

        else:
            print(" Invalid choice!")
            msvcrt.getch()

def Circle():
    decimal = 2 # Batas angka belakang koma
    pi = 3.14159
    os.system('cls')
    print("|_____________________________________________|")
    print("|          *The Formula Of Circle*            |")
    print("| Circumference = 2 * pi * r                  |")
    print("| Area          = pi * r^2                    |")
    print("| Diameter      = 2 * r                       |")
    print("|---------------------------------------------|")
    print(" Try It For Yourself!")
    print()

    r = float(input(" Input The Radius Of The Circle (r) : "))

    # The Counting Begin...
    K = 2 * pi * r
    L = pi * (r ** 2)
    D = 2 * r
    K_format = "{:.{}f}".format(K, decimal)
    L_format = "{:.{}f}".format(L, decimal)

    # The Output...
    print(" This Is The Result : ")
    print("[------------------------------------------------]")
    print(f"[ Circumference = {K_format}cm (Keliling)")
    print(f"[ Area          = {L_format}cm2 (Luas)")
    print(f"[ Diameter      = {D}cm (Diameter)")
    print("[------------------------------------------------]")

def Parallelogram():
    decimal = 2  # Batas angka belakang koma
    os.system('cls')
    print("|______________________________________________|")
    print("|         *The Formula Of Parallelogram*       |")
    print("| Circumference = 2 * (a + b)                  |")
    print("| Area          = base * height                |")
    print("| Diagonals     = sqrt(a^2 + b^2 + 2ab * cosθ) |")
    print("|______________________________________________|")
    print(" Try It For Yourself!")
    print()

    a = float(input(" Input The Length Of Side A : "))
    b = float(input(" Input The Length Of Side B : "))
    t = float(input(" Input The Height : "))

    # The Counting Begins...
    K = 2 * (a + b)
    L = a * t
    D = math.sqrt((a ** 2) + (b ** 2) + (2 * a * b * math.cos(math.radians(180))))  # Sisi A dan Sisi B membentuk sudut 180 derajat
    diagonal_format = "{:.{}f}".format(D, decimal)

    # The Output...
    print(" This Is The Result : ")
    print("[------------------------------------------------]")
    print(f"[ Circumference = {K}cm (Keliling)")
    print(f"[ Area          = {L}cm2 (Luas)")
    print(f"[ Diagonal      = {diagonal_format} (Diagonal)")
    print("[------------------------------------------------]")

def Rhombus():
    decimal = 2  # Batas angka belakang koma
    os.system('cls')
    print("|______________________________________________|")
    print("|           *The Formula Of Rhombus*           |")
    print("| Circumference = s x 4                        |")
    print("| Area          = 1/2 x d1 x d2                |")
    print("| Diagonals 1   = 2 x L / d2                   |")
    print("| Diagonals 2   = 2 x L / d1                   |")
    print("|______________________________________________|")
    print(" Try It For Yourself!")
    print()

    s = float(input(" Input The Length Of Side (s): "))

    # The Counting Begins...
    K = s * 4
    d1 = 2 * s  # Diagonal 1
    d2 = 2 * s  # Diagonal 2
    L = 0.5 * d1 * d2
    diagonal1 = 2 * L / d2
    diagonal2 = 2 * L / d1

    K_format = "{:.{}f}".format(K, decimal-2)
    L_format = "{:.{}f}".format(L, decimal-2)
    d1_format = "{:.{}f}".format(diagonal1, decimal-2)
    d2_format = "{:.{}f}".format(diagonal2, decimal-2)

    # The Output...
    print(" This Is The Result : ")
    print("[------------------------------------------------]")
    print(f"[ Circumference = {K_format}cm (Keliling)")
    print(f"[ Area          = {L_format}cm2 (Luas)")
    print(f"[ Diagonal 1    = {d1_format} (Diagonal 1)")
    print(f"[ Diagonal 2    = {d2_format} (Diagonal 2)")
    print("[------------------------------------------------]")

def Trapezoid():
    decimal = 2  # Batas angka belakang koma
    os.system('cls')
    print("|______________________________________________|")
    print("|         *The Formula Of Trapezoid*           |")
    print("| Circumference = a + b + c + d                |")
    print("| Area          = 1/2 x (a + b) x t            |")
    print("| Height/t      = 2 x L / (a + b)              |")
    print("| Diagonal 1    = √(a^2 + c^2 - 2ac * cosθ)    |")
    print("| Diagonal 2    = √(b^2 + d^2 - 2bd * cosθ)    |")
    print("|______________________________________________|")
    print(" Try It For Yourself!")
    print()
    
    a = float(input(" Input The Length Of Side A (Upper Side): "))
    b = float(input(" Input The Length Of Side B (Base)      : "))
    t = float(input(" Input The Height Of The Trapezoid      : "))
    
    # Check if a > b
    if a > b:
        c = math.sqrt((a**2) - (((a-b)**2) + (t**2)) / (-2 * (a-b)))
        d = math.sqrt((b**2) - (((a-b)**2) + (t**2)) / (-2 * (a-b)))
        
        K = a + b + c + d
        L = 0.5 * (a + b) * t
        height = (2 * L) / (a + b)
        d1 = math.sqrt(a**2 + c**2 - 2*a*c*math.cos(math.radians(180)))
        d2 = math.sqrt(b**2 + d**2 - 2*b*d*math.cos(math.radians(180)))
        
        K_format = "{:.{}f}".format(K, decimal)
        L_format = "{:.{}f}".format(L, decimal)
        t_format = "{:.{}f}".format(height, decimal)
        d1_format = "{:.{}f}".format(d1, decimal)
        d2_format = "{:.{}f}".format(d2, decimal)
        
        # The Output...
        print(" This Is The Result : ")
        print("[------------------------------------------------]")
        print(f"[ Circumference = {K_format}cm (Keliling)")
        print(f"[ Area          = {L_format}cm2 (Luas)")
        print(f"[ Height        = {t_format}cm (Tinggi)")
        print(f"[ Diagonal 1    = {d1_format} (Diagonal 1)")
        print(f"[ Diagonal 2    = {d2_format} (Diagonal 2)")
        print("[------------------------------------------------]")
    else:
        print("Side A (Upper Side) should be greater than Side B (Base). Please try again.")


#[3D Figures]-[3D Figures]-[3D Figures]-[3D Figures]-[3D Figures]-[3D Figures]-[3D Figures]-[3D Figures]#

def Cube():
    decimal = 2  # Batas angka belakang koma
    os.system('cls')
    print("|___________________________________________________|")
    print("|             *The Formula Of Cube*                 |")
    print("|______________________[3D]_________________________|")
    print("| Volume           = s x s x s or s^3               |")
    print("| Surface Area     = 6 x s x s                      |")
    print("| Diagonals Side   = s√(2)                          |")
    print("| Diagonals Space  = s√(3)                          |")
    print("| Diagonals Area   = s^2√(2)                        |")
    print("|___________________________________________________|")
    print(" Try It For Yourself!")
    print()

    s = float(input(" Input The Length Of Side (s): "))

    volume = s ** 3
    surface_area = 6 * s ** 2
    diagonal_side = s * math.sqrt(2)
    diagonal_space = s * math.sqrt(3)
    diagonal_area = s ** 2 * math.sqrt(2)

    volume_format = "{:.{}f}".format(volume, decimal)
    surface_area_format = "{:.{}f}".format(surface_area, decimal)
    diagonal_side_format = "{:.{}f}".format(diagonal_side, decimal)
    diagonal_space_format = "{:.{}f}".format(diagonal_space, decimal)
    diagonal_area_format = "{:.{}f}".format(diagonal_area, decimal)

    # The Output...
    print(" This Is The Result : ")
    print("[------------------------------------------------]")
    print(f"[ Volume              = {volume_format}cm3")
    print(f"[ Surface Area        = {surface_area_format}cm2")
    print(f"[ Diagonals Side      = {diagonal_side_format}cm")
    print(f"[ Diagonals Space     = {diagonal_space_format}cm")
    print(f"[ Diagonals Area      = {diagonal_area_format}cm2")
    print("[------------------------------------------------]")

def Beam():
    decimal = 2  # Batas angka belakang koma
    os.system('cls')
    print("|___________________________________________________|")
    print("|             *The Formula Of Beam*                 |")
    print("|______________________[3D]_________________________|")
    print("| Volume           = p x l x t                      |")
    print("| Surface Area     = 2 x (p x l + p x t + l + t)    |")
    print("| Diagonals Side   = a) ds1 = √(p^2 + l^2)          |")
    print("|                    b) ds2 = √(p^2 + t^2)          |")
    print("|                    c) ds3 = √(l^2 + t^2)          |")
    print("| Diagonals Space  = √(p^2 + l^2 + t^2)             |")
    print("| Diagonals Area   = a) da1 = ds1 x t               |")
    print("|                    b) da2 = ds2 x l               |")
    print("|                    c) da3 = ds3 x p               |")
    print("|___________________________________________________|")
    print(" Try It For Yourself!")
    print()

    p = float(input(" Input The Length Of Beam (p): "))
    l = float(input(" Input The Width Of Beam (l): "))
    t = float(input(" Input The Height Of Beam (t): "))

    volume = p * l * t
    surface_area = 2 * (p * l + p * t + l * t)
    diagonal_side_1 = math.sqrt(p ** 2 + l ** 2)
    diagonal_side_2 = math.sqrt(p ** 2 + t ** 2)
    diagonal_side_3 = math.sqrt(l ** 2 + t ** 2)
    diagonal_space = math.sqrt(p ** 2 + l ** 2 + t ** 2)
    diagonal_area_1 = diagonal_side_1 * t
    diagonal_area_2 = diagonal_side_2 * l
    diagonal_area_3 = diagonal_side_3 * p

    volume_format = "{:.{}f}".format(volume, decimal)
    surface_area_format = "{:.{}f}".format(surface_area, decimal)
    diagonal_side_1_format = "{:.{}f}".format(diagonal_side_1, decimal)
    diagonal_side_2_format = "{:.{}f}".format(diagonal_side_2, decimal)
    diagonal_side_3_format = "{:.{}f}".format(diagonal_side_3, decimal)
    diagonal_space_format = "{:.{}f}".format(diagonal_space, decimal)
    diagonal_area_1_format = "{:.{}f}".format(diagonal_area_1, decimal)
    diagonal_area_2_format = "{:.{}f}".format(diagonal_area_2, decimal)
    diagonal_area_3_format = "{:.{}f}".format(diagonal_area_3, decimal)

    # The Output...
    print(" This Is The Result : ")
    print("[------------------------------------------------]")
    print(f"[ Volume              = {volume_format}cm3")
    print(f"[ Surface Area        = {surface_area_format}cm2")
    print(f"[ Diagonal Side 1     = {diagonal_side_1_format}cm")
    print(f"[ Diagonal Side 2     = {diagonal_side_2_format}cm")
    print(f"[ Diagonal Side 3     = {diagonal_side_3_format}cm")
    print(f"[ Diagonal Space      = {diagonal_space_format}cm")
    print(f"[ Diagonal Area 1     = {diagonal_area_1_format}cm2")
    print(f"[ Diagonal Area 2     = {diagonal_area_2_format}cm2")
    print(f"[ Diagonal Area 3     = {diagonal_area_3_format}cm2")
    print("[------------------------------------------------]")

def Ball():
    decimal = 2  # Batas angka belakang koma
    pi = 3.14159
    while True:
        os.system('cls')
        print("|___________________________________________________|")
        print("|             *The Formula Of Ball*                 |")
        print("|______________________[3D]_________________________|")
        print("| Volume           = 4/3 x pi x r^3                 |")
        print("| Surface Area     = 4 x pi x r^2                   |")
        print("| Radius With V    = ∛(3 x V / (4 x pi))            |")
        print("| Radius With SA   = √(SA / (4 x pi))               |")
        print("|___________________________________________________|")
        print(" Try It For Yourself!")
        print()

        option = int(input(" Choose an option: \n 1. Calculate using Radius (Find Volume and Surface Area) \n 2. Calculate using Volume (Find Radius) \n Enter your choice (1 or 2): "))

        if option == 1:
            radius = float(input(" Input The Radius (r): "))

            volume = (4/3) * pi * (radius ** 3)
            surface_area = 4 * pi * (radius ** 2)

            volume_format = "{:.{}f}".format(volume, decimal)
            surface_area_format = "{:.{}f}".format(surface_area, decimal)

            print(" This Is The Result : ")
            print("[------------------------------------------------]")
            print(f"[ Volume              = {volume_format}cm3")
            print(f"[ Surface Area        = {surface_area_format}cm2")
            print("[------------------------------------------------]")
            break
        elif option == 2:
            volume = float(input(" Input The Volume: "))

            radius_with_volume = (3 * volume / (4 * pi)) ** (1/3)
            radius_with_surface_area = math.sqrt(volume / (4 * pi))

            radius_with_volume_format = "{:.{}f}".format(radius_with_volume, decimal)
            radius_with_surface_area_format = "{:.{}f}".format(radius_with_surface_area, decimal)

            print(" This Is The Result : ")
            print("[------------------------------------------------]")
            print(f"[ Radius With Volume      = {radius_with_volume_format}cm")
            print(f"[ Radius With Surface Area = {radius_with_surface_area_format}cm")
            print("[------------------------------------------------]")
            break
        else:
            print(" Invalid option!")
            msvcrt.getch()

def Cylinder():
    decimal = 2  # Batas angka belakang koma
    pi = 3.14159
    while True:
        os.system('cls')
        print("|___________________________________________________|")
        print("|            *The Formula Of Cylinder*              |")
        print("|______________________[3D]_________________________|")
        print("| Volume             = pi x r^2 x t                 |")
        print("| Surface Area       = 2 x pi x r x (r + t)         |")
        print("| Cover Area         = 2 x pi x r x t               |")
        print("| Base Area          = pi x r x r                   |")
        print("| Radius With Volume = √(V / (pi x t))              |")
        print("| Height With Volume = V / (pi x r^2)               |")
        print("|___________________________________________________|")
        print(" Try It For Yourself!")
        print()

        option = int(input(" Choose an option: \n 1. (Find Volume, Surface Area, Cover Area, and Base Area) \n 2. (Find Radius) \n 3. (Find Height) \n Enter your choice (1, 2, or 3): "))

        if option == 1:
            radius = float(input(" Input The Radius (r): "))
            height = float(input(" Input The Height (t): "))

            volume = pi * (radius ** 2) * height
            surface_area = 2 * pi * radius * (radius + height)
            cover_area = 2 * pi * radius * height
            base_area = pi * (radius ** 2)

            volume_format = "{:.{}f}".format(volume, decimal)
            surface_area_format = "{:.{}f}".format(surface_area, decimal)
            cover_area_format = "{:.{}f}".format(cover_area, decimal)
            base_area_format = "{:.{}f}".format(base_area, decimal)

            print(" This Is The Result : ")
            print("[------------------------------------------------]")
            print(f"[ Volume         = {volume_format} cm3")
            print(f"[ Surface Area   = {surface_area_format} cm2")
            print(f"[ Cover Area     = {cover_area_format} cm2")
            print(f"[ Base Area      = {base_area_format} cm2")
            print("[------------------------------------------------]")
            break

        elif option == 2:
            volume = float(input(" Input The Volume: "))
            height = float(input(" Input The Height (t): "))

            radius_with_volume = math.sqrt(volume / (pi * height))

            radius_with_volume_format = "{:.{}f}".format(radius_with_volume, decimal)

            print(" This Is The Result : ")
            print("[------------------------------------------------]")
            print(f"[ Radius With Volume = {radius_with_volume_format} cm")
            print("[------------------------------------------------]")
            break

        elif option == 3:
            radius = float(input(" Input The Radius (r): "))
            volume = float(input(" Input The Volume: "))

            height_with_volume = volume / (pi * (radius ** 2))

            height_with_volume_format = "{:.{}f}".format(height_with_volume, decimal)

            print(" This Is The Result : ")
            print("[------------------------------------------------]")
            print(f"[ Height With Volume = {height_with_volume_format} cm")
            print("[------------------------------------------------]")
            break

        else:
            print(" Invalid option!")
            msvcrt.getch()

def Cone():
    decimal = 2  # Batas angka belakang koma
    pi = 3.14159
    while True:
        os.system('cls')
        print("|___________________________________________________|")
        print("|             *The Formula Of Cone*                 |")
        print("|______________________[3D]_________________________|")
        print("| Volume             = 1/3 x pi x r^2 x t           |")
        print("| S (Pynthagoras)    = √(r^2 + t^2)                 |")
        print("| Surface Area       = (pi x r^2) + (pi x r x s)    |")
        print("| Base Area          = pi x r^2                     |")
        print("| Cover Area         = pi x r x s                   |")
        print("| Radius With Volume = √(3 x V / (pi x t))          |")
        print("| Height With Volume = 3 x V / (pi x r^2)           |")
        print("|___________________________________________________|")
        print(" Try It For Yourself!")
        print()

        option = int(input(" Choose an option: \n 1. (Find Volume, Surface Area, Base Area, and Cover Area) \n 2. (Find Radius) \n 3. (Find Height) \n Enter your choice (1, 2, or 3): "))

        if option == 1:
            radius = float(input(" Input The Radius (r): "))
            height = float(input(" Input The Height (t): "))

            volume = (1/3) * pi * (radius ** 2) * height
            s = math.sqrt((radius ** 2) + (height ** 2))
            surface_area = (pi * (radius ** 2)) + (pi * radius * s)
            base_area = pi * (radius ** 2)
            cover_area = pi * radius * s

            volume_format = "{:.{}f}".format(volume, decimal)
            surface_area_format = "{:.{}f}".format(surface_area, decimal)
            base_area_format = "{:.{}f}".format(base_area, decimal)
            cover_area_format = "{:.{}f}".format(cover_area, decimal)

            print(" This Is The Result : ")
            print("[------------------------------------------------]")
            print(f"[ Volume         = {volume_format} cm3")
            print(f"[ Surface Area   = {surface_area_format} cm2")
            print(f"[ Base Area      = {base_area_format} cm2")
            print(f"[ Cover Area     = {cover_area_format} cm2")
            print("[------------------------------------------------]")
            break

        elif option == 2:
            volume = float(input(" Input The Volume: "))
            height = float(input(" Input The Height (t): "))

            radius_with_volume = math.sqrt((3 * volume) / (pi * height))

            radius_with_volume_format = "{:.{}f}".format(radius_with_volume, decimal)

            print(" This Is The Result : ")
            print("[------------------------------------------------]")
            print(f"[ Radius With Volume = {radius_with_volume_format} cm")
            print("[------------------------------------------------]")
            break

        elif option == 3:
            radius = float(input(" Input The Radius (r): "))
            volume = float(input(" Input The Volume: "))

            height_with_volume = (3 * volume) / (pi * (radius ** 2))

            height_with_volume_format = "{:.{}f}".format(height_with_volume, decimal)

            print(" This Is The Result : ")
            print("[------------------------------------------------]")
            print(f"[ Height With Volume = {height_with_volume_format} cm")
            print("[------------------------------------------------]")
            break

        else:
            print(" Invalid option.")
            msvcrt.getch()
            
def Prism():
    decimal = 2  # Batas angka belakang koma
    pi = 3.14159
    while True:
        os.system('cls')
        print("|____________________________________________________________________|")
        print("|                        *The Formula Of Prism*                      |")
        print("|_________________________________[3D]_______________________________|")
        print("| Base Area (BA)   = Adjust The Shape Of The Prism                   |")
        print("| Volume           = BA x t                                          |")
        print("| Surface Area     = t x (base circumference) x (2 x BA)             |")
        print("| Area of 3-prism  = t x ( a1 + a2 + a3) + (2 x BA)                  |")
        print("| Area of 4-prism  = t x ( a1 + a2 + a3 + 4a) + (2 x BA)             |")
        print("| Area of 5-prism  = t x ( a1 + a2 + a3 + 4a + 5a) + (2 x BA)        |")
        print("| Area of 6-prism  = t x ( a1 + a2 + a3 + a4 + a5 + a6) + (2 x BA)   |")
        print("|____________________________________________________________________|")
        print(" Try It For Yourself!")
        print()

        option = int(input(" Choose the number of sides of the prism (3-6): "))

        if option < 3 or option > 6:
            print(" Invalid option. Please choose a number between 3 and 6.")
            msvcrt.getch()
            continue

        base_area = 0.0
        if option == 3:
            a1 = float(input(" Input side length a1: "))
            a2 = float(input(" Input side length a2: "))
            a3 = float(input(" Input side length a3: "))

            base_area = 0.5 * a1 * a2

        elif option == 4:
            a1 = float(input(" Input side length a1: "))
            a2 = float(input(" Input side length a2: "))
            a3 = float(input(" Input side length a3: "))
            a = float(input(" Input side length a: "))

            base_area = a * a

        elif option == 5:
            a1 = float(input(" Input side length a1: "))
            a2 = float(input(" Input side length a2: "))
            a3 = float(input(" Input side length a3: "))
            a = float(input(" Input side length a: "))

            base_area = 0.25 * (a1 * a2 * a3) * (1 / (a ** 2))

        elif option == 6:
            a1 = float(input(" Input side length a1: "))
            a2 = float(input(" Input side length a2: "))
            a3 = float(input(" Input side length a3: "))
            a4 = float(input(" Input side length a4: "))
            a5 = float(input(" Input side length a5: "))
            a6 = float(input(" Input side length a6: "))

            base_area = (1 / 4) * (3 * (a1 * a2) + 2 * (a2 * a3 + a3 * a4 + a4 * a5 + a5 * a6))

        height = float(input(" Input the height of the prism: "))

        volume = base_area * height
        surface_area = height * (2 * base_area)

        volume_format = "{:.{}f}".format(volume, decimal)
        surface_area_format = "{:.{}f}".format(surface_area, decimal)
        base_area_format = "{:.{}f}".format(base_area, decimal)

        print(" This Is The Result : ")
        print("[------------------------------------------------]")
        print(f"[ Volume         = {volume_format} cm3")
        print(f"[ Surface Area   = {surface_area_format} cm2")
        print(f"[ Base Area      = {base_area_format} cm2")
        print("[------------------------------------------------]")
        break

def Pyramid():
    decimal = 2  # Batas angka belakang koma
    pi = 3.14159
    while True:
        os.system('cls')
        print("|____________________________________________________________________|")
        print("|                      *The Formula Of Pyramid*                      |")
        print("|________________________________[3D]________________________________|")
        print("| A) 3-Side Pyramid :                                                |")
        print("|    > Volume                    = 1/3 x BA x t                      |")
        print("|    > Height                    = 6 x V / BTB x HTB                 |")
        print("|    > Surface Area              = BA + L ΔI + L ΔII + L ΔIII        |")
        print("|    > Base Area                 = 1/2 x BTB x HTB                   |")
        print("|    > Base Triangle Base(BTB)   = 6 x V / HTB x t                   |")
        print("|    > Height Triangle Base(HTB) = 6 x V / BTB x t                   |")
        print("|    > L ΔI                      = 1/2 x a Δ1 x t Δ1                 |")
        print("|    > L ΔII                     = 1/2 x a Δ2 x t Δ2                 |")
        print("|    > L ΔIII                    = 1/2 x a Δ3 x t Δ3                 |")
        print("|____________________________________________________________________|")
        print(" Try It For Yourself!")
        print()
        
        option = input("Pilih opsi rumus yang ingin dihitung (1-3): ")
        
        if option == "1":
            # Rumus untuk 3-Side Pyramid
            BA = float(input(" Input Base Area (BA): "))
            t = float(input(" Input Height (t): "))
            
            volume = (1/3) * BA * t
            height = (6 * volume) / (BA * t)
            surface_area = BA + (3 * BA * t)
            
            volume_format = "{:.{}f}".format(volume, decimal)
            height_format = "{:.{}f}".format(height, decimal)
            surface_area_format = "{:.{}f}".format(surface_area, decimal)
            
            print(" Hasil Perhitungan (3-Side Pyramid) : ")
            print("[------------------------------------------------]")
            print(f"[ Volume         = {volume_format}cm3")
            print(f"[ Height         = {height_format}cm")
            print(f"[ Surface Area   = {surface_area_format}cm2")
            print("[------------------------------------------------]")
            break

        elif option == "2":
            # Ongoing....
            pass
        
        elif option == "3":
            # Ongoing....
            pass
        
        else:
            print(" Invalid Option.")
            msvcrt.getche()
            continue
#======================================= END Of Figures =======================================#

def Temperature():
    tmp_menu = 0
    while tmp_menu != 6:
        os.system("cls")
        print("|========================================|")
        print("|      Welcome To Temperature Zone       |")
        print("|========================================|")
        print("|[1] Convert Celsius (°C)                |")
        print("|[2] Convert Fahrenheit (°F)             |")
        print("|[3] Convert Kelvin (°K)                 |")
        print("|[4] Convert Reamur (°R)                 |")
        print("|[5] Convert Rankine (°Ra)               |")
        print("|[6] Exit                                |")
        print("|========================================|")
        tmp_menu = int(input("| Choose : "))
        if tmp_menu == 1:
            Conv_Celsius()
            msvcrt.getch()
        elif tmp_menu == 2:
            Conv_Fahrenheit()
            msvcrt.getch()
        elif tmp_menu == 3:
            Conv_Kelvin()
            msvcrt.getch()
        elif tmp_menu == 4:
            Conv_Reamur()
            msvcrt.getch()
        elif tmp_menu == 5:
            Conv_Rankine()
            msvcrt.getch()
        elif tmp_menu == 6:
            print(" Exit...")
            msvcrt.getch()
            break
        else:
            print(" Invalid Option.")
            msvcrt.getch()

def Conv_Celsius():
    os.system('cls')
    celsius = float(input(" Input Celsius : "))
    # The Formula...
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    reamur = celsius * 4/5
    rankine = (celsius + 273.15) * 9/5
    # The Result...
    print("|============================>")
    print("| The Result ||--->[°C]<---><>")
    print("|============================>")
    print(f"| From : {celsius}°C")
    print(f"| --> {fahrenheit}°F")
    print(f"| --> {kelvin}°K")
    print(f"| --> {reamur}°R")
    print(f"| --> {rankine}°Ra")
    print("|=============================>")

def Conv_Fahrenheit():
    os.system('cls')
    fahrenheit = float(input("Input Fahrenheit: "))
    # The Formula...
    celsius = (fahrenheit - 32) * 5/9
    kelvin = (fahrenheit + 459.67) * 5/9
    reamur = (fahrenheit - 32) * 4/9
    rankine = fahrenheit + 459.67
    # The Result...
    print("|============================>")
    print("| The Result ||--->[°F]<---><>")
    print("|============================>")
    print(f"| From: {fahrenheit}°F")
    print(f"| --> {celsius}°C")
    print(f"| --> {kelvin}°K")
    print(f"| --> {reamur}°R")
    print(f"| --> {rankine}°Ra")
    print("|=============================>")

def Conv_Kelvin():
    os.system('cls')
    kelvin = float(input("Input Kelvin: "))
    # The Formula...
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    reamur = (kelvin - 273.15) * 4/5
    rankine = kelvin * 9/5
    # The Result...
    print("|============================>")
    print("| The Result ||--->[°K]<---><>")
    print("|============================>")
    print(f"| From: {kelvin}°K")
    print(f"| --> {celsius}°C")
    print(f"| --> {fahrenheit}°F")
    print(f"| --> {reamur}°R")
    print(f"| --> {rankine}°Ra")
    print("|=============================>")

def Conv_Reamur():
    os.system('cls')
    reamur = float(input("Input Reamur: "))
    # The Formula...
    celsius = reamur * 5/4
    fahrenheit = (reamur * 9/4) + 32
    kelvin = (reamur * 5/4) + 273.15
    rankine = (reamur * 9/4) + 491.67
    # The Result...
    print("|============================>")
    print("| The Result ||--->[°R]<---><>")
    print("|============================>")
    print(f"| From: {reamur}°R")
    print(f"| --> {celsius}°C")
    print(f"| --> {fahrenheit}°F")
    print(f"| --> {kelvin}°K")
    print(f"| --> {rankine}°Ra")
    print("|=============================>")


def Conv_Rankine():
    os.system('cls')
    rankine = float(input("Input Rankine: "))
    # The Formula...
    celsius = (rankine - 491.67) * 5/9
    fahrenheit = rankine - 459.67
    kelvin = rankine * 5/9
    reamur = (rankine - 491.67) * 4/9
    # The Result...
    print("|============================>")
    print("| The Result ||--->[°Ra]<---><>")
    print("|============================>")
    print(f"| From: {rankine}°Ra")
    print(f"| --> {celsius}°C")
    print(f"| --> {fahrenheit}°F")
    print(f"| --> {kelvin}°K")
    print(f"| --> {reamur}°R")
    print("|=============================>")
#====================================[ALL ABOUT MATH PAGE END]=========================================#

#==================================================================================================#
# SIMPLE GAME FUNCTION AND PROCEDURE...                                                            |
#==================================================================================================#

# THE GAME OF ROCK, PAPER AND SCISSORS !__!__!__!__!__!__!__!__!
def get_user_choice():
    choices = {
        "r": "rock",
        "p": "paper",
        "s": "scissors"
    }
    user_choice = input("| Enter your choice (r for rock, p for paper, s for scissors): ").lower()
    while user_choice not in choices.keys():
        user_choice = input("| Invalid choice. Please enter r, p, or s: ").lower()
    return choices[user_choice]
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "| It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "| You win!"
    else:
        return "| Computer wins!"
def play():
    play = input("| Do you want to play again? (y/n): ").lower()
    return play == ("y")

# THE GAME OF GUESS THE NUMBER !__!__!__!__!__!__!__!__!
def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome To Guess The Number Game!")
    print("I'm Thinking Of A Number From 1 To 100!")

    while True:
        try:
            # Ask the player for a guess
            guess = int(input("Take A Guess : "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            print("Congratulations! You Guessed The Number In", attempts, "Attempts.")
            break

    print("Thanks For Playing!")

# THE GAME OF TIC TAC TOE !__!__!__!__!__!__!__!__!
def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = "X"

    def display_board():
        print(f"\n {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")

    def is_winner(player):
        winning_combinations = (
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        )

        for combo in winning_combinations:
            if all(board[i] == player for i in combo):
                return True

        return False

    def is_board_full():
        return all(cell != " " for cell in board)

    def switch_player():
        nonlocal current_player
        current_player = "O" if current_player == "X" else "X"

    def make_move():
        if current_player == "X":
            while True:
                move = int(input("Choose a position (1-9): ")) - 1

                if move >= 0 and move <= 8 and board[move] == " ":
                    board[move] = current_player
                    break
                else:
                    print("Invalid move. Try again.")
        else:
            while True:
                move = random.randint(0, 8)
                if board[move] == " ":
                    board[move] = current_player
                    break

    while True:
        display_board()
        make_move()

        if is_winner(current_player):
            display_board()
            if current_player == "X":
                print("Congratulations! You win!")
            else:
                print("The computer wins!")
            break
        elif is_board_full():
            display_board()
            print("It's a tie!")
            break

        switch_player()

#====================================[SIMPLE GAME PAGE END]========================================#


#-_-_-_-_-_-_-_-_-[A_I_P_P_p_r_o_j_e_c_t_0_3]-_-_-_- THE MAIN MENU -_-_-_-[A_I_P_P_p_r_o_j_e_c_t_0_3]-_-_-_-_-_-_-_-_-_-#
menu = [1,2,3,4]
for pilih in menu:
    os.system('cls')
    print(" User Right Now :")
    print(" |----------------------|")
    print(" | Name : "+name)
    print(" | Age  : "+str(age), end="")
    if age == 1:
        print("st\n", end="")
    elif age == 2:
        print("nd\n", end="")
    elif age == 3:
        print("rd\n", end="")
    else:
        print("th\n", end="")
    print(" |----------------------|\n")
    print("|======================================|")
    print("|    WELLCOME TO AIPPproject03 ZONE    |")
    print("|======================================|")
    print("| 1) AIPP Database                     |")
    print("| 2) AIPP Math Zone                    |")
    print("| 3) AIPP Simple Games                 |")
    print("| 4) Exit                              |")
    print("|======================================|")
    pilih = int(input(" Choose Your Way : "))
#====================( MENU 1 "DATABASE" )====================#
    if pilih == 1:
        menu1 = 0
        while menu1 != 5:
            os.system('cls')
            print("|======================================|")
            print("|         AIPP DATABASE ZONE           |")
            print("|======================================|")
            print("| 1) Input Data                        |")
            print("| 2) Delete Data                       |")
            print("| 3) Edit Data                         |")
            print("| 4) Show Data                         |")
            print("| 5) Exit                              |")
            print("|======================================|")
            menu1 = int(input(" Choose : "))
            if menu1 == 1:
                input_data()
            elif menu1 == 2:
                delete_data()
            elif menu1 == 3:
                edit_data()
            elif menu1 == 4:
                show_data()
            elif menu1 == 5:
                print(" Exit To Main Menu")
                break
            msvcrt.getch()
#====================( MENU 2 "ALL ABOUT MATH" )====================#
    elif pilih == 2:
        menu2 = 0
        while menu2 != 5:
            os.system('cls')
            print("|======================================|")
            print("|         ALL ABOUT MATH ZONE          |")
            print("|======================================|")
            print("| 1) Fibonacci                         |")
            print("| 2) Calculator                        |")
            print("| 3) 2D and 3D Figures                 |")
            print("| 4) Temperature                       |")
            print("| 5) Exit                              |")
            print("|======================================|")
            menu2 = int(input(" Choose : "))
            if menu2 == 1:
                os.system("cls")
                print("[FIBONACCI COUNTING]")
                n = int(input(" How Many Numbers Do Your Need : "))
                init_fibo = fibonacci(n)
                print(" This Is The Answer : ",init_fibo)
            elif menu2 == 2:
                os.system("cls")
                print(" Welcome To The Simple Calculator")
                print(" Feel Free To Write Your Formula...")
                msvcrt.getch()
                os.system("cls")
                calculator()
            elif menu2 == 3:
                Figure_2D_3D()
            elif menu2 == 4:
                Temperature()
            elif menu2 == 5:
                print(" Exit To Main Menu")
                break
            msvcrt.getch()
#====================( MENU 3 "SIMPLE GAME" )====================#
    elif pilih == 3:
        menu3 = 0;
        while menu3 != 4:
            os.system("cls")
            print("|======================================|")
            print("|           SIMPLE GAME ZONE           |")
            print("|======================================|")
            print("| 1) Rock, Paper, Scissors             |")
            print("| 2) Guess The Number                  |")
            print("| 3) Tic Tac Toe                       |")
            print("| 4) Exit                              |")
            print("|======================================|")
            menu3 = int(input(" Choose : "))
            if menu3 == 1:
                while True:
                    os.system("cls")
                    print("[ ROCK PAPER SCISSORS GAMELOGIC ]")
                    print("[       By AIPPproject03        ]\n")
                    user_choice = get_user_choice()
                    computer_choice = get_computer_choice()
                    print("|==================================================|")
                    print("| You chose      :", user_choice)
                    print("| Computer chose :", computer_choice)
                    result = determine_winner(user_choice, computer_choice)
                    print(result)
                    if not play():
                        print("| Thank You For Playing")
                        print("|==================================================|")
                        break
                    print("| Let\'s do this again bruh!")
                    msvcrt.getch()
            elif menu3 == 2:
                guess_number()
            elif menu3 == 3:
                play_game()
            elif menu3 == 4:
                print(" Exit To Main Menu")
                break
            msvcrt.getch()
#====================( "EXIT" )====================#
    elif pilih == 4:
        print(" Exit...")
        break
    else:
        print(" Invalid Command")
        