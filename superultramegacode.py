import statistics as st
import os
from scipy.stats import shapiro, ttest_ind, ttest_rel, pearsonr
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd as pt
import scikit_posthocs as sp
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import tkinter as tk
os.system('color')


# code for graphs

def grafiki():
    my_imput = input("Введіть середнє значення через пробіл:")
    mean_data = [float(x.strip()) for x in my_imput.split(' ')]
    my_imput2 = input("Введіть SEM:")
    sem_data = [float(x.strip()) for x in my_imput2.split(' ')]
    vis_y = input("Введіть назву осі У:")
    vis_x = input("Введіть назви стовпчиків через пробіл:")
    nazvi = [(x.strip()) for x in vis_x.split(' ')]
    if len(mean_data) == len(nazvi):
        pass
    else:
        exit()
    fig, ax = plt.subplots()
    ax.bar(range(len(mean_data)), mean_data, yerr=sem_data, align='center', alpha=0.5, ecolor='black', capsize=10)
    ylabels = vis_y.split()
    ax.set_ylabel(' '.join(ylabels))
    ax.set_xticks(range(len(mean_data)))
    xlabels = nazvi
    ax.set_xticklabels(xlabels)
    plt.show()

# Code for data normality check
def normality():
    while True:
        x = input("\033[8mEnter data separated by spaces: \033[0m")
        try:
            data_float = [float(i.replace(",", ".")) for i in x.split(" ")]
            # Кількість даних
            n_d = len(data_float)
            if n_d < 10:
                print("Enter at least 10 values!")
            else:
                # Сортований ряд даних
                sort_d = sorted(data_float)
                # Min value
                min_d = min(data_float)
                # Max value
                max_d = max(data_float)
                # Average
                mean_d = st.mean(data_float)
                # Dyspercy
                var_d2 = sum((i - mean_d) ** 2 for i in data_float) / (n_d - 1)
                # SD
                sd_d2 = var_d2 ** 0.5
                # Shapiro Wilks test
                p_value = 0.05
                t_shap, p = shapiro(data_float)
                print(t_shap)
                shapirooo = {
                    10:  [0.842],
                    11: [0.850],
                    12: [0.859],
                    13: [0.866],
                    14: [0.874],
                    15: [0.881],
                    16: [0.887],
                }
                one_shapiro = shapirooo[n_d][0]
                if t_shap >= one_shapiro:
                    print(f"Shapiro-Wilk test shows that your data follows a normal distribution. p < {p_value}")
                else:
                    print(f"Shapiro-Wilk test shows that your data does NOT follow a normal distribution. p < {p_value}")
                (print
                 (f"Data count:  {n_d}\n"
                  f"Minimal value: {min_d}\n"
                  f"Shapiro critical: {round(one_shapiro, 3)}\n"
                  f"Shapiro measured: {round(t_shap, 3)}\n"
                  ))
                input_cycle = input("Do you need more data analysys? yes/no: ")
                if input_cycle.lower() == "no":
                    main_menu()
                elif input_cycle.lower() == "yes":
                    continue
        except ValueError:
            if "," in x:
                print("\033[91mStatistics is not for you\033[0m")
            elif ";" in x:
                print("\033[91mStatistics is not for you\033[0m")
            else:
                print("\033[1m\033[91mEnter only numbers!!!\033[0m")
        except KeyError:
            if n_d > 16:
                print("Use less values dumbass!")
            else:
                print("Stick to the rules")


# Code to find data that is probably was just a mistake (test Shovene)
def misses():
    while True:
        x = input("\033[8mEnter data separated by spaces: \033[0m")
        try:
            data_float = [float(i.replace(",", ".")) for i in x.split(" ")]
            # Кількість даних
            n_d = len(data_float)
            if n_d < 4:
                print("Enter more data!")
            else:
                # Сортований ряд даних
                sort_d = sorted(data_float)
                # Мінімальне значення
                min_d = min(data_float)
                # Максимальне значення
                max_d = max(data_float)
                # Середнє арифметичне
                mean_d = st.mean(data_float)
                # Дисперсія (Додому формула)
                var_d2 = sum((i - mean_d) ** 2 for i in data_float) / (n_d - 1)
                # Стандартне відхилення (Додому формула)
                sd_d2 = var_d2 ** 0.5
                # Shovenist test
                shov_max = (max_d - mean_d)/sd_d2
                shov_min = (mean_d - min_d) / sd_d2
                shovi = {
                    4:  [1.64],
                    5: [1.68],
                    6: [1.73],
                    7: [1.79],
                    8: [1.86],
                    9: [1.92],
                    10: [1.96],
                    11: [2.00],
                    12: [2.03]
                }
                Shovi_out = shovi[n_d][0]
                if shov_max >= Shovi_out:
                    print(f"Shovene Test: max value - {max_d} - is an outlier")
                else:
                    print(f"Shovene Test: max value - {max_d} - is not an outlier")
                if shov_min >= Shovi_out:
                    print(f"Shovene Test: min value - {min_d} - is an outlier")
                else:
                    print(f"Shovene Test: min value - {min_d} - is not an outlier")
                (print
                 (f"Number of data:  {n_d}\n"
                  f"Max value: {max_d}\n"
                  f"Min value: {min_d}\n"
                  f"Shovene value for min: {round(shov_min, 2)}\n"
                  f"Shovene value for max: {round(shov_max, 2)}\n"
                  f"Shovene crit value: {Shovi_out}"))
                #Dikson test
                if n_d < 8:
                    d_min = (sort_d[1] - sort_d[0]) / (sort_d[-1] - sort_d[0])
                    d_max = (sort_d[-1] - sort_d[-2]) / (sort_d[-1] - sort_d[0])
                elif n_d == range(8, 10):
                    d_min = (sort_d[1] - sort_d[0]) / (sort_d[-2] - sort_d[0])
                    d_max = (sort_d[-1] - sort_d[-2]) / (sort_d[-1] - sort_d[1])
                # Dickson test
                dik_dic = {
                    4: [0.765],
                    5: [0.642],
                    6: [0.560],
                    7: [0.507],
                    8: [0.468],
                    9: [0.437],
                    10: [0.412]
                }
                dik_out = dik_dic[n_d][0]
                if max_d >= dik_out:
                    print(f"Dickson Test: max value - {max_d} - is an outlier")
                else:
                    print(f"Dickson Test: max value - {max_d} - is not an outlier")
                if min_d >= dik_out:
                    print(f"Dickson Test: min value - {min_d} - is an outlier")
                else:
                    print(f"Dickson Test: min value - {min_d} - is not an outlier")
                    (print
                     (f"Кількість даних:  {n_d}\n"
                      f"Мінімальне значення: {min_d}\n"
                      f"Dickson value for min: {round(min_d, 2)}\n"
                      f"Dickson value for max: {round(max_d, 2)}\n"
                      f"Dickson crit value: {dik_out}"))
                #Irvin test
                irvii_max = (max_d - sort_d[n_d - 1]) / sd_d2
                irvii = {
                    4: [2.00],
                    5: [1.87],
                    6: [1.77],
                    7: [1.69],
                    8: [1.63],
                    9: [1.58],
                    10: [1.54]
                }
                irvii_out = irvii[n_d][0]
                if irvii_max >= irvii_out:
                    print(f"Irvin Test: max value - {max_d} - is an outlier p = 0.05")
                else:
                    print(f"Irvin Test: max value - {max_d} - is not an outlier p = 0.05")
                (print
                 (f"Кількість даних:  {n_d}\n"
                  f"Мінімальне значення: {min_d}\n"
                  f"Irvin value: {round(irvii_max, 2)}\n"
                  f"Irvin crit value: {irvii_out}"))
                input_cycle = input("Do you need more data analysys? yes/no: ")
                if input_cycle.lower() == "no":
                    main_menu()
                elif input_cycle.lower() == "yes":
                    continue
        except ValueError:
            if "," in x:
                print("\033[91mStatistics is not for you\033[0m")
            elif ";" in x:
                print("\033[91mStatistics is not for you\033[0m")
            else:
                print("\033[1m\033[91mEnter only numbers!!!\033[0m")
        except KeyError:
            if n_d > 16:
                print("Use less values dumbass!")
            else:
                print("Stick to the rules")
# Descriptive statistics
def describe_st():
    while True:
        x = input("\033[8mВведіть дані через пробіл: \033[0m")
        try:
            data_float = [float(i) for i in x.split(" ")]
            # Кількість даних
            n_d = len(data_float)
            if n_d < 4:
                print("Enter more data!")
            else:
                # Сортований ряд даних
                sort_d = sorted(data_float)
                # Мінімальне значення
                min_d = min(data_float)
                # Максимальне значення
                max_d = max(data_float)
                # Медіана
                median_d = st.median(data_float)
                # Середнє арифметичне
                mean_d = st.mean(data_float)
                # Мода
                mode_d = st.multimode(data_float)
                if len(data_float) == len(mode_d):
                    print("Моди немає")
                else:
                    print("Мода: ", mode_d)
                # Дисперсія (Додому формула)
                var_d2 = sum((i - mean_d)**2 for i in data_float) / (n_d-1)
                # Стандартне відхилення (Додому формула)
                sd_d2 = var_d2**0.5
                # SEM
                sem_d4 = sd_d2 / (n_d**0.5)
                # Квартиль 25 50 75
                q_d = st.quantiles(data_float)
                (print
                (f"Кількість даних:  {n_d}\n"
                f"Сортований ряд даних: {sort_d}\n" 
                f"Мінімальне значення: {min_d}\n"
                f"Максимальне значення: {max_d}\n" 
                f"Медіана: {median_d}\n"
                f"Середнє арифметичне: {mean_d: .3f}\n"
                f"SEM4: {round(sem_d4, 3)}\n"
                f"Дисперсія 2: {var_d2}\n"
                f"Стандартне відхилення 2: {sd_d2}\n"
                f"Квантилі 25 50 75: {q_d}"))
                input_cycle = input("Do you need more data analisys? yes/no: ")
                if input_cycle.lower() == "no":
                    main_menu()
                elif input_cycle.lower() == "yes":
                    continue
        except ValueError:
            if "," in x:
                print("\033[91mStatistics is not for you\033[0m")
            elif ";" in x:
                print("\033[91mStatistics is not for you\033[0m")
            else:
                print("\033[1m\033[91mEnter only numbers!!!\033[0m")
        except KeyError:
                if n_d > 16:
                    print("Use less values dumbass!")
                else:
                    print("Stick to the rules")


def norm_ttest():
    while True:
        x1 = input("\033[8mEnter data for group 1 separated by spaces: \033[0m")
        x2 = input("\033[8mEnter data for group 1 separated by spaces: \033[0m")
        try:
            data_float1 = [float(i.replace(",", ".")) for i in x1.split(" ")]
            data_float2 = [float(i.replace(",", ".")) for i in x2.split(" ")]
            # Кількість даних
            n_d1 = len(data_float1)
            n_d2 = len(data_float2)

            if n_d1 < 4 or n_d2 < 4:
                print("Enter at least 4 values!")
            else:
                # Сортований ряд даних
                sort_d1 = sorted(data_float1)
                sort_d2 = sorted(data_float2)
                p_value = 0.05
                df = n_d1 + n_d2 - 2
                ttest_norm, p = ttest_ind(data_float1, data_float2)
                print(ttest_norm)
                crits_t = {
                    6: [2.45],
                    7: [2.37],
                    8: [2.31],
                    9: [2.26],
                    10: [2.23],
                    11: [2.20],
                    12: [2.18],
                    13: [2.16],
                    14: [2.15],
                    15: [2.13],
                }
                crit_t = crits_t[df][0]
                (print
                 (f"Data count group 1:  {n_d1}\n"
                  f"Data count group 2:  {n_d2}\n"
                  f"Sorted data 1  {sort_d1}\n"
                  f"Sorted data 2  {sort_d2}\n"
                  f"Student  {abs(round(ttest_norm, 3))}\n"
                  f"Critical Student  {crit_t}\n"
                  ))
                if abs(ttest_norm) > crit_t:
                    print(f"There is a statistically significant difference between the groups with p = {p}")
                else:
                    print(f"There is no statistically significant difference between the groups with p = {p}")
                input_cycle = input("Do you need more data analysys? yes/no: ")
                if input_cycle.lower() == "no":
                    main_menu()
                elif input_cycle.lower() == "yes":
                    continue
        except ValueError:
            if "," in x1 or "," in x2:
                print("\033[91mStatistics is not for you\033[0m")
            elif ";" in x1 or "," in x2:
                print("\033[91mBe aware of your background door becallo\033[0m")
            else:
                print("\033[1m\033[91mUse only numbers!!!\033[0m")


def pair_ttest():
    while True:
        x1 = input("\033[8mВведіть дані групи 1 через пробіл: \033[0m")
        x2 = input("\033[8mВведіть дані групи 2 через пробіл: \033[0m")
        try:
            data_float1 = [float(i.replace(",", ".")) for i in x1.split(" ")]
            data_float2 = [float(i.replace(",", ".")) for i in x2.split(" ")]
            # Кількість даних
            n_d1 = len(data_float1)
            n_d2 = len(data_float2)
            if n_d1 < 4 or n_d2 < 4:
                print("Enter at least 4 values!")
            else:
                # Сортований ряд даних
                sort_d1 = sorted(data_float1)
                sort_d2 = sorted(data_float2)
                p_value = 0.05
                df = n_d1 - 1
                ttest_norm, p = ttest_rel(data_float1, data_float2)
                print(ttest_norm)
                crits_t = {
                    5: [2.57],
                    6: [2.45],
                    7: [2.37],
                    8: [2.31],
                    9: [2.26],
                    10: [2.23],
                    11: [2.20],
                    12: [2.18],
                    13: [2.16],
                    14: [2.15],
                    15: [2.13],
                }
                crit_t = crits_t[df][0]
                (print
                 (f"Data count group 1:  {n_d1}\n"
                  f"Data count group 2:  {n_d2}\n"
                  f"Sorted data 1  {sort_d1}\n"
                  f"Sorted data 2  {sort_d2}\n"
                  f"Student  {abs(round(ttest_norm, 3))}\n"
                  f"Critical Student  {crit_t}\n"
                  ))
                if abs(ttest_norm) > crit_t:
                    print(f"There is a statistically significant difference between the groups with p = {p}")
                else:
                    print(f"There is no statistically significant difference between the groups with p = {p}")
                input_cycle = input("Do you need more data analysys? yes/no: ")
                if input_cycle.lower() == "no":
                    main_menu()
                elif input_cycle.lower() == "yes":
                    continue
        except ValueError:
            if "," in x1 or "," in x2:
                print("\033[91mStatistics is not for you\033[0m")
            elif ";" in x1 or "," in x2:
                print("\033[91mBe aware of your background door becallo\033[0m")
            else:
                print("\033[1m\033[91mUse only numbers!!!\033[0m")




def tukey_test():
    while True:
        x1 = x2 = x3 = x4 = x5 = x6 = ""
        groups_data = input("Вкажіть кількість Груп для порівняння: ")
        if groups_data == "3":
            x1 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x2 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x3 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
        elif groups_data == "4":
            x1 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x2 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x3 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x4 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
        elif groups_data == "5":
            x1 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x2 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x3 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x4 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x5 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
        elif groups_data == "6":
            x1 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x2 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x3 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x4 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x5 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
            x6 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
        else:
            print("This test compare from 3 to 6 groups each others")
        try:
            data_float1 = [float(i.replace(",", ".")) for i in x1.split(" ")] if x1 else []
            data_float2 = [float(i.replace(",", ".")) for i in x2.split(" ")] if x2 else []
            data_float3 = [float(i.replace(",", ".")) for i in x3.split(" ")] if x3 else []
            data_float4 = [float(i.replace(",", ".")) for i in x4.split(" ")] if x4 else []
            data_float5 = [float(i.replace(",", ".")) for i in x5.split(" ")] if x5 else []
            data_float6 = [float(i.replace(",", ".")) for i in x6.split(" ")] if x6 else []

            # Кількість даних
            n_d1 = len(data_float1)
            n_d2 = len(data_float2)
            n_d3 = len(data_float3)
            n_d4 = len(data_float4)
            n_d5 = len(data_float5)
            n_d6 = len(data_float6)

            all_data = np.concatenate([data_float1, data_float2, data_float3, data_float4, data_float5, data_float6])
            groups = (
                ["Група 1"] * n_d1 +
                ["Група 2"] * n_d2 +
                ["Група 3"] * n_d3 +
                ["Група 4"] * n_d4 +
                ["Група 5"] * n_d5 +
                ["Група 6"] * n_d6
                )
            tukey_test = pt(all_data, groups)
            print(f"Tukey test: {tukey_test}")
            input_cycle = input("Do you need more data analysys? yes/no: ")
            if input_cycle.lower() == "no":
                    main_menu()
            elif input_cycle.lower() == "yes":
                    continue
        except ValueError:
            if "," in x1 or "," in x2:
                print("\033[91mStatistics is not for you\033[0m")
            elif ";" in x1 or "," in x2:
                print("\033[91mBe aware of your background door becallo\033[0m")
            else:
                print("\033[1m\033[91mUse only numbers!!!\033[0m")


def Dunn_test():
    def dunn_test():
        varlist = []
        lenlist = []
        groups = []
        numnum = 0
        groups_data = int(input("Enter how many groups do you want to compare: "))
        try:
            for i in range(1, groups_data + 1):
                x = input(f"Data for group {i}: ")
                data_float = [float(j.replace(",", ".")) for j in x.split(" ")]
                varlist.append(data_float)
            if any(number < 4 for number in lenlist):
                print("Be watchful of your data, some of your data feels lonely.\n"
                      " To use this technique you need more than that")
            else:
                print(varlist)
                dunn_test = sp.posthoc_dunn(varlist, p_adjust='holm')
                print(
                    f"Test of mister Dunn:\n {dunn_test}"
                )
        except ValueError:
            if "," in x:
                print("\033[91mStatistics is not for you\033[0m")
            elif ";" in x:
                print("\033[91mBe aware of your background door becallo\033[0m")
            else:
                print("\033[1m\033[91mUse only numbers!!!\033[0m")



def mantest():
    while True:
        x1 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
        x2 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
        try:
            data_float1 = [float(i.replace(",", ".")) for i in x1.split(" ")]
            data_float2 = [float(i.replace(",", ".")) for i in x2.split(" ")]
            # Кількість даних
            n_d1 = len(data_float1)
            n_d2 = len(data_float2)
            if n_d1 < 4 or n_d2 < 4:
                print("Enter at least 4 values!")
            else:
                all_data = [data for data in [data_float1, data_float2]]
                witney = sp.posthoc_mannwhitney(all_data, p_adjust='holm')

                (print
                 (f"Data count group 1:  {n_d1}\n"
                  f"Data count group 2:  {n_d2}\n"
                  f"Test Witney: \n {witney}\n"))

                input_cycle = input("Do you need more data analysys? yes/no: ")
                if input_cycle.lower() == "no":
                    main_menu()
                elif input_cycle.lower() == "yes":
                    continue
        except ValueError:
            if "," in x1 or "," in x2:
                print("\033[91mStatistics is not for you\033[0m")
            elif ";" in x1 or "," in x2:
                print("\033[91mBe aware of your background door becallo\033[0m")
            else:
                print("\033[1m\033[91mUse only numbers!!!\033[0m")





def wilkonsonnnn():
    while True:
        x1 = input("\033[8mEnter data for the first group separated by spaces: \033[0m")
        x2 = input("\033[8mEnter data for the second group separated by spaces: \033[0m")
        try:
            data_float1 = [float(i.replace(",", ".")) for i in x1.split(" ")]
            data_float2 = [float(i.replace(",", ".")) for i in x2.split(" ")]
            # Кількість даних
            n_d1 = len(data_float1)
            n_d2 = len(data_float2)
            if n_d1 < 4 or n_d2 < 4:
                print("Enter at least 4 values!")
            else:
                all_data = [data for data in [data_float1, data_float2]]
                wilktest = sp.posthoc_wilcoxon(all_data, p_adjust='holm')
                (print
                 (f"Data count group 1:  {n_d1}\n"
                  f"Data count group 2:  {n_d2}\n"
                  f"Test Wilcoxona: \n {wilktest}\n"))
                input_cycle = input("Do you need more data analysys? yes/no: ")
                if input_cycle.lower() == "no":
                    main_menu()
                elif input_cycle.lower() == "yes":
                    continue
        except ValueError:
            if "," in x1 or "," in x2:
                print("\033[91mStatistics is not for you\033[0m")
            elif ";" in x1 or "," in x2:
                print("\033[91mBe aware of your background door becallo\033[0m")
            else:
                print("\033[1m\033[91mUse only numbers!!!\033[0m")

def cor_test():
    while True:
        x1 = input("\033[93mВведіть дані незалежної Групи через пробіл: \033[0m")
        x2 = input("\033[93mВведіть дані залежної Групи через пробіл: \033[0m")

        try:
            data1 = [float(i) for i in x1.split(" ")]
            data2 = [float(i) for i in x2.split(" ")]

            # Кількість даних
            n1 = len(data1)
            n2 = len(data2)

            if n1 < 10 or n2 < 10:
                print("\033[91mВведіть більше ніж дев'ять значень!!!\033[0m")
                continue
            elif n1 != n2:
                print("\033[91mВведіть одинакову кількість даних у вибірках!!!\033[0m")
                continue
            else:

                value_p = 0.05

                t_crits = {
                    8: [2.31],
                    9: [2.26],
                    10: [2.23],
                    11: [2.20],
                    12: [2.18],
                    13: [2.16],
                    14: [2.15],
                    15: [2.13],
                    16: [2.12],
                    17: [2.11],
                    18: [2.10],
                    19: [2.09],
                    20: [2.09]
                }

                # Ступінь свободи
                df = n1 - 2

                t_crit = t_crits[df][0]

                corr_d, p = pearsonr(data1, data2)

                corr_stat = (corr_d / ((1 - corr_d**2)**0.5)) * df**0.5

                (print
                 (f"Кількість даних Групи 1: {n1}\n"
                  f"Кількість даних Групи 2: {n2}\n"
                  f"Коефіцієнт кореляції Пірсона: {round(corr_d, 3)}\n"
                  f"Коефіцієнт детермінації: {round(corr_d**2*100)}\n"
                  f"Критичне значення Стьюдента: {t_crit}\n"
                  f"Рівень статистичної значущості коефіцієнта кореляції: {p}\n"
                  f"Ступінь свободи: {df}\n"
                  f"Значущість коефіцієнта кореляції r за допомогою t критерію Стьюдента: {round(corr_stat, 3)}"))
                if corr_stat > t_crit:
                    print(f"\033[91mДані Групи 1 і Групи 2 взаємозалежні на {round(corr_d**2*100)}%,\n"
                          f"оскільки {value_p} >  {p},\n"
                          f"а також Значущість коефіцієнта кореляції {round(corr_stat, 3)} є більшою за критичне значення {t_crit} \033[0m\n")
                else:
                    print(f"Дані Групи 1 і Групи 2 не взаємозалежні")

                plt.scatter(data1, data2)
                plt.title("Кореляційне поле")
                plt.xlabel("Незалежна група")
                plt.ylabel("Залежна група")
                plt.show()
        except ValueError:
            if "," in x1 or "," in x2:
                print("\033[91mStatistics is not for you\033[0m")
            elif ";" in x1 or "," in x2:
                print("\033[91mBe aware of your background door becallo\033[0m")
            else:
                print("\033[1m\033[91mUse only numbers!!!\033[0m")
        input_cycle = input("Do you need more data analysys? yes/no: ")
        if input_cycle.lower() == "no":
            main_menu()
        elif input_cycle.lower() == "yes":
            continue
def main_menu():
    (print
        (f"\033[1m\033[92m         Main Menu\033[0m\n"
        f"\033[91m[1]\033[0m\033[1m Finding Misses\033[0m\n" 
        f"\033[91m[2]\033[0m\033[1m Desciptive statistics\033[0m\n"
        f"\033[91m[3]\033[0m\033[1m Normality Check\033[0m\n" 
        f"\033[91m[4]\033[0m\033[1m Student`s test for independent data\033[0m\n"
        f"\033[91m[5]\033[0m\033[1m Mann's Witney test for non-parametric data\033[0m\n"
        f"\033[91m[6]\033[0m\033[1m Pairwise Student`s test\033[0m\n"
        f"\033[91m[7]\033[0m\033[1m Non parametric test Wilkins\033[0m\n"
        f"\033[91m[8]\033[0m\033[1m Tukey test for more than 2\033[0m\n"
        f"\033[91m[9]\033[0m\033[1m Dann`s test\033[0m\n"
        f"\033[91m[10]\033[0m\033[1m Correlation analysis\033[0m\n"
        f"\033[91m[11]\033[0m\033[1m Exit\033[0m"))
    input_menu = input("\033[33mEnter option num: \033[0m")
    if input_menu == "1":
        misses()
    elif input_menu == "2":
        describe_st()
    elif input_menu == "3":
        normality()
    elif input_menu == "4":
        norm_ttest()
    elif input_menu == "5":
        mantest()
    elif input_menu == "6":
        pair_ttest()
    elif input_menu == "7":
        wilkonsonnnn()
    elif input_menu == "8":
        tukey_test()
    elif input_menu == "9":
        Dunn_test()
    elif input_menu == "10":
        cor_test()
    elif input_menu == "11":
        grafiki()
main_menu()
