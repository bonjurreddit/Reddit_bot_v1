import random
import time

min_num_account1 = int(input('Введи диапазон аккаунтов, для лайкинга! \n С какого аккаунта стартуем? (Напиши цифру): '))
max_num_account1 = int(input('На каком аккаунте закончим? (Напиши цифру): ')) + 1
number_of_active_profiles1 = int(max_num_account1 - min_num_account1)

min_num_account2 = int(input('Введи диапазон аккаунтов, для лайкинга! \n С какого аккаунта стартуем? (Напиши цифру): '))
max_num_account2 = int(input('На каком аккаунте закончим? (Напиши цифру): ')) + 1
number_of_active_profiles2 = int(max_num_account2 - min_num_account2)

min_num_account3 = int(input('Введи диапазон аккаунтов, для лайкинга! \n С какого аккаунта стартуем? (Напиши цифру): '))
max_num_account3 = int(input('На каком аккаунте закончим? (Напиши цифру): ')) + 1
number_of_active_profiles3 = int(max_num_account3 - min_num_account3)

min_num_account4 = int(input('Введи диапазон аккаунтов, для лайкинга! \n С какого аккаунта стартуем? (Напиши цифру): '))
max_num_account4 = int(input('На каком аккаунте закончим? (Напиши цифру): ')) + 1
number_of_active_profiles4 = int(max_num_account4 - min_num_account4)

min_num_account5 = int(input('Введи диапазон аккаунтов, для лайкинга! \n С какого аккаунта стартуем? (Напиши цифру): '))
max_num_account5 = int(input('На каком аккаунте закончим? (Напиши цифру): ')) + 1
number_of_active_profiles5 = int(max_num_account5 - min_num_account5)



loading_profile_data1 = [i for i in range(min_num_account1, max_num_account1)]  # Генерация списка аккаунтов
loading_profile_data2 = [i for i in range(min_num_account1, max_num_account1)]  # Генерация списка аккаунтов
loading_profile_data3 = [i for i in range(min_num_account1, max_num_account1)]  # Генерация списка аккаунтов
loading_profile_data4 = [i for i in range(min_num_account1, max_num_account1)]  # Генерация списка аккаунтов
loading_profile_data5 = [i for i in range(min_num_account1, max_num_account1)]  # Генерация списка аккаунтов

if loading_profile_data is not None:
    with Pool(number_of_active_profiles1) as p:  # МУЛЬТИПРОЦЕССИНГ
    p.map(Mass.setting_one_account_hard, loading_profile_data1)
time.sleep(random.randit(175, 190))
if loading_profile_data is not None:
    with Pool(number_of_active_profiles2) as p:  # МУЛЬТИПРОЦЕССИНГ
    p.map(Mass.setting_one_account_hard, loading_profile_data2)
time.sleep(random.randit(175, 190))
if loading_profile_data is not None:
    with Pool(number_of_active_profiles3) as p:  # МУЛЬТИПРОЦЕССИНГ
    p.map(Mass.setting_one_account_hard, loading_profile_data3)
time.sleep(random.randit(175, 190))
if loading_profile_data is not None:
    with Pool(number_of_active_profiles4) as p:  # МУЛЬТИПРОЦЕССИНГ
    p.map(Mass.setting_one_account_hard, loading_profile_data4)
time.sleep(random.randit(175, 190))
if loading_profile_data is not None:
    with Pool(number_of_active_profiles5) as p:  # МУЛЬТИПРОЦЕССИНГ
    p.map(Mass.setting_one_account_hard, loading_profile_data5)
