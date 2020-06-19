

import math
import numpy as np
import matplotlib.pyplot as plt

def func_e(x, n):   # x = number that e gets raised to, n = number of terms
    e_approx = 0
    for i in range(n):
        e_approx += x**i/math.factorial(i)
    return e_approx

def func_cos(x, n):
    cos_approx = 0
    for i in range(n):
        coefficient = (-1) ** i                      # coefficient of the function
        nominator = x ** (2 * i)                     # nominator of the function
        denominator = math.factorial(2 * i)          # denominator of the function
        cos_approx += coefficient * (nominator / denominator)

    return cos_approx

angle_rad = (math.radians(45))
cos_angle = func_cos(angle_rad,5)

out = math.cos(angle_rad)




def func_sin(x, n):
    sin_approx = 0
    for i in range(n):
        coefficient = (-1) ** i                       # coefficient of the function
        nominator = x**(2*i + 1)                      # nominator of the function
        denominator = math.factorial(2*i + 1)         # denominator of the function
        sin_approx += coefficient * (nominator / denominator)

    return sin_approx

#
# sin_angle = func_sin(angle_rad,5)
# print(sin_angle)
#
# sin_angle = math.sin(angle_rad)
# print(sin_angle)
#
#

def show_e(n):

    angles = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
    p_e = np.exp(angles)

    fig, ax = plt.subplots()
    ax.plot(angles, p_e)
    plt.title("Taylor Series cos(x)")

    # add lines for for each term in the Taylor Series
    for i in range(1, int(n) + 1):
        t_e = [func_e(angle, i) for angle in angles]
        ax.plot(angles, t_e)

    ax.set_ylim([-7, 4])

    # set up legend
    legend_lst = ['e^x() function']
    for i in range(1, int(n) + 1):
        legend_lst.append(f'{i} terms')
    ax.legend(legend_lst, loc='upper right')

    plt.show()


def show_cos(n):

    angles = np.arange(-2*np.pi,2*np.pi,0.1)
    p_cos = np.cos(angles)

    fig, ax = plt.subplots()
    ax.plot(angles,p_cos)
    plt.title("Taylor Series cos(x)")

    # add lines for for each term in the Taylor Series
    for i in range(1,int(n)+1):
        t_cos = [func_cos(angle,i) for angle in angles]
        ax.plot(angles,t_cos)

    ax.set_ylim([-7,4])

    # set up legend
    legend_lst = ['cos() function']
    for i in range(1,int(n)+1):
        legend_lst.append(f'Taylor Series - {i} terms')
    ax.legend(legend_lst, loc=3)

    plt.show()


def show_sin(n):
    angles = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
    p_sin = np.sin(angles)

    fig, ax = plt.subplots()
    ax.plot(angles,p_sin)
    plt.title("Taylor Series sin(x)")

    # add lines for for each term in the Taylor Series
    for i in range(1,int(n)+1):
        t_sin = [func_sin(angle,i) for angle in angles]
        ax.plot(angles,t_sin)

    ax.set_ylim([-7,4])

    # set up legend
    legend_lst = ['sin() function']
    for i in range(1,int(n)+1):
        legend_lst.append(f'Taylor Series - {i} terms')
    ax.legend(legend_lst, loc=3)


    plt.show()


def main():
    ans = True
    while ans:
        print("\n\t\t\t\t\t\t\t\t\t\t\t\tCOMPUTATIONAL MATHEMATICS FINAL PROJECT")
        print("\t\t\t\t ===============================================================================================")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTAYLOR SERIES")
        print("\t\t\t\t ===============================================================================================")

        print("""
        \t\t\t\t\t\t\t\t\t\t\t\t  SELECT AN OPTION:
        \t\t\t\t\t\t\t\t\t\t\t\t ==================
        \t\t\t\t\t\t\t\t\t\t\t\t  1.Visualize e^x
        \t\t\t\t\t\t\t\t\t\t\t\t  2.Visualize sin(x)
        \t\t\t\t\t\t\t\t\t\t\t\t  3.Visualize cos(x)
        \t\t\t\t\t\t\t\t\t\t\t\t  4.Exit
        \t\t\t\t\t\t\t\t\t\t\t\t ===================
        """""
              )
        ans = input("=>")

        if ans == "1":
            n = input("Choose number of terms: ")
            x = 5
            print("\t\t\t\t\t\t\t\tTAYLOR FUNCTION : e^x")
            print("\t\t\t---------------------------------------------------------------")
            for i in range(1, int(n)+1):
                e_approx = func_e(x, i)
                e_exp = math.exp(x)
                e_error = abs(e_approx - e_exp)
                print(f'{i} terms: Approximation= {e_approx}, \tTrue Value= {e_exp}, \tError = {e_error}')
            print("\n\n")
            show_e(n)

        elif ans == "2":
            n = input("Choose number of terms: ")
            x = 5
            print("\t\t\t\t\t\t\t\tTAYLOR FUNCTION : sin(x)")
            print("\t\t\t---------------------------------------------------------------")
            for i in range(1, int(n)+1):
                sin_approx = func_sin(x, i)
                sin_exp = math.sin(x * 2 * math.pi / 180)
                sin_error = abs(sin_approx - sin_exp)
                print(f'{i} terms: Approximation= {sin_approx}, \tTrue Value= {sin_exp}, \tError = {sin_error}')
            print("\n\n")
            show_sin(n)

        elif ans == "3":
            n = input("Choose number of terms: ")
            x = 5
            print("\t\t\t\t\t\t\t\tTAYLOR FUNCTION : cos(x)")
            print("\t\t\t---------------------------------------------------------------")
            for i in range(1, int(n)+1):
                cos_approx = func_cos(x, i)
                cos_exp = math.cos(x * 2 * math.pi / 180)
                cos_error = abs(cos_approx - cos_exp)
                print(f'{i} terms: Approximation= {cos_approx}, \tTrue Value= {cos_exp}, \tError = {cos_error}')
            print("\n\n")
            show_cos(n)

        elif ans == "4":
            break

        elif ans != "":
            print("\n Not Valid Choice Try again")


if __name__ == "__main__":
    main()
