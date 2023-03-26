import random
from v40_settings_for_linux import SettingBrowserClass
from v40_start_for_server import StartLoginQuit
from v40_setting_account import SettingAccount
from v40_like import UpVote
from v40_walker import Walker
from Data.data import user_setting_dict
from multiprocessing import Pool
import datetime
import time


class Mass:  # Класс для массовых действий

    def __init__(self):
        pass
    @staticmethod
    def start_mass_like(i):  # start for script # Старт основого скрипта
        my_like = Walker(i)
        url = 'https://www.reddit.com/r/DadWouldBeProud'
        sub_name = 'DadWouldBeProud'
        post_title_like = "I'm so playful today"

        try:
            my_like.start_browser()
            my_like.open_communities_url(url)
            my_like.random_subscribe()
            my_like.tab_new(sub_name)
            my_like.search_post_with_title_name(post_title_like)
            my_like.up_vote_random()
            my_like.save_or_share_or_pass()
            my_like.script_open_author()
            my_like.close_browser()

        except Exception as e:
            my_like.close_browser()
            print(f'Проблемы с масс.лайкингом: {e}')

    @staticmethod
    def start_mass_dislike(i):  # Cтарт масс дизлайк
        my_like = UpVote(i)
        url = 'https://www.reddit.com/r/ass'
        post_title_dis = 'Can my warm butt make your soldier stand up'
        try:
            my_like.start_browser()
            my_like.open_communities_url(url)
            my_like.random_subscribe()
            my_like.search_post_with_title_name(post_title_dis)
            my_like.down_vote_random()
            my_like.close_browser()

        except Exception as e:
            my_like.close_browser()
            print(f'Проблемы с масс.ДИЗлайкингом: {e}')

    @staticmethod
    def start_mass_walker(i):
        bot = Walker(i)
        start_time = time.time()
        try:
            bot.walking_start()
            while time.time() - start_time < 900:
                random_num = random.random()
                bot.scrolling_and_open_post()

                if random_num < 0.15:
                    bot.script_like_post_and_save()
                if 0.15 < random_num < 0.5:
                    bot.close_post()
                if 0.5 < random_num < 0.85:
                    bot.script_open_author()
                if 0.85 < random_num < 1:
                    bot.script_like_post_and_open_author()

            print(f"Account{bot.count}: {datetime.datetime.now()}:: [+]  Закончил гулять!")
            bot.close_browser()
        except Exception as e:
            bot.close_browser()
            print(f"Account{bot.count}: {datetime.datetime.now()}: [-]  Вылетел с прогули")

    @staticmethod
    def start_mass_random_like(i):  # start for script # Старт основого скрипта
        my_like = UpVote(i)
        url = 'https://www.reddit.com/r/IRLgirls'
        sub_name = 'IRLgirls'
        post_title = ['Gorgeous blonde in her bikini (IUTR)', '1243', '124']

        try:
            my_like.start_browser()
            # my_like.open_sub_random(sub_name, url)
            my_like.open_communities_url(url)
            my_like.random_subscribe()
            my_like.tab_new(sub_name)
            my_like.search_post_with_title_name(random.choice(post_title))
            my_like.up_vote_random()
            my_like.save_or_share_or_pass()
            my_like.close_browser()

        except Exception as e:
            my_like.start_menu()
            print(f'Проблемы с масс.лайкингом: {e}')

    @staticmethod   # Старт основого скрипта
    def start_mass_setting_account(i):  # start for script
        my_like = SettingAccount(i)
        try:
            my_like.start_browser()
            my_like.setting_nsfw()
            my_like.close_browser()
        except Exception as e:
            my_like.start_menu()
            print(f'Проблемы с настройками аккаунтов: {e}')

    @staticmethod   # Старт основого скрипта
    def start_mass_auth(i):  # start for script
        my_mass_bot = StartLoginQuit(i)
        my_mass_bot.start_browser()

    @staticmethod
    def setting_one_account_hard(i):
        my_like = UpVote(i)
        try:
            my_like.start_browser()
            time.sleep(1000)
            my_like.close_browser()
        except Exception as e:
             print(f'Проблемы с настройками аккаунтов: {e}')

    @staticmethod
    def check_acc(i):
        my_like = UpVote(i)
        login_list = [user_setting_dict[key]['login'] for key in user_setting_dict.keys()]

        try:
            my_like.start_browser()
            for login in login_list:
                # загрузка страницы пользователя
                my_like.browser.execute_script(f"window.open('https://www.reddit.com/user/{login}');")
            time.sleep(1000)
            my_like.close_browser()

        except Exception as e:
            print(f'Проблемы с чекером: {e}')

    @staticmethod   # Старт проверки настроек драйвера
    def test_driver_settings(i):
        try:
            te1st = SettingBrowserClass(i)
            browser = te1st.setting_browser_bot()
            browser.get('https://whoer.net/ru')
            time.sleep(100)

        except Exception as e:
            print(f'Проблемы с тестом настроек: {e}')


def main():
    try:  # Переменные для пула
        print('Привет, что будем делать?! \n 1. Проверка прокси \n 2. Настройка аккаунтов \n 3. Лайки один диап.  \n 4. Ручное управление аккаунтом  \n 5. Чекер аккаунтов  \n 6. Сканер диапазонов(баги) \n 7. Запуск по цепочке \n 8. Дизлайк в один диапазон \n 9. Гулялка(15-20 минут)')
        start_question = input("Сделай выбор и напиши цифру(без точки): ")

        if start_question == '1':
            min_num_account = int(input('Введи диапазон аккаунтов, для лайкинга! \n С какого аккаунта стартуем? (Напиши цифру): '))
            max_num_account = int(input('На каком аккаунте закончим? (Напиши цифру): ')) + 1
            number_of_active_profiles = int(max_num_account - min_num_account)

            loading_profile_data = [i for i in range(min_num_account, max_num_account)]  # Генерация списка аккаунтов

            if loading_profile_data is not None:
                with Pool(number_of_active_profiles) as p:  # МУЛЬТИПРОЦЕССИНГ
                    p.map(Mass.test_driver_settings, loading_profile_data)

        if start_question == '2':
            min_num_account = int(input('Введи диапазон аккаунтов, для лайкинга! \n С какого аккаунта стартуем? (Напиши цифру): '))
            max_num_account = int(input('На каком аккаунте закончим? (Напиши цифру): ')) + 1
            number_of_active_profiles = int(max_num_account - min_num_account)
            a = int(number_of_active_profiles + 1)
            loading_profile_data = [i for i in range(min_num_account, max_num_account)]  # Генерация списка аккаунтов

            if loading_profile_data is not None:
                with Pool(number_of_active_profiles) as p:  # МУЛЬТИПРОЦЕССИНГ
                    p.map(Mass.start_mass_setting_account, loading_profile_data)

        if start_question == '3':

            min_num_account = int(input('Введи диапазон аккаунтов, для лайкинга! \n С какого аккаунта стартуем? (Напиши цифру): '))
            max_num_account = int(input('На каком аккаунте закончим? (Напиши цифру): ')) + 1
            number_of_active_profiles = int(max_num_account - min_num_account)

            loading_profile_data = [i for i in range(min_num_account, max_num_account)]  # Генерация списка аккаунтов

            if loading_profile_data is not None:
                with Pool(number_of_active_profiles) as p:  # МУЛЬТИПРОЦЕССИНГ
                    p.map(Mass.start_mass_like, loading_profile_data)

        if start_question == '4':

            number_account = int(input('Введите номер аккаунта для ручного управления: '))
            Mass.setting_one_account_hard(number_account)

        if start_question == '5':
            Mass.check_acc(1)

        if start_question == '6':
            min_num_account = int(input('Введи диапазон аккаунтов, для лайкинга! \n С какого аккаунта стартуем? (Напиши цифру): '))
            max_num_account = int(input('На каком аккаунте закончим? (Напиши цифру): ')) + 1
            number_of_active_profiles = int(max_num_account - min_num_account)

            loading_profile_data = [i for i in range(min_num_account, max_num_account)]  # Генерация списка аккаунтов

            if loading_profile_data is not None:
                with Pool(number_of_active_profiles) as p:  # МУЛЬТИПРОЦЕССИНГ
                    p.map(Mass.setting_one_account_hard, loading_profile_data)

        if start_question == '7':
            # Список диапазонов аккаунтов
            ranges = [(1, 15), (16, 30), (46, 60), (61, 75), (76, 90), (91, 102)]
            random.shuffle(ranges)
            print(ranges)

            for start, end in ranges:
                number_of_active_profiles = end - start + 1
                loading_profile_data = [i for i in range(start, end)]

                if loading_profile_data is not None:
                    with Pool(number_of_active_profiles) as p:
                        p.map(Mass.start_mass_like, loading_profile_data)

        if start_question == '8':
            min_num_account = int(input('Введи диапазон аккаунтов, для лайкинга! \n С какого аккаунта стартуем? (Напиши цифру): '))
            max_num_account = int(input('На каком аккаунте закончим? (Напиши цифру): ')) + 1
            number_of_active_profiles = int(max_num_account - min_num_account)

            loading_profile_data = [i for i in range(min_num_account, max_num_account)]  # Генерация списка аккаунтов

            if loading_profile_data is not None:
                with Pool(number_of_active_profiles) as p:  # МУЛЬТИПРОЦЕССИНГ
                    p.map(Mass.start_mass_dislike, loading_profile_data)

        if start_question == '9':
            # Список диапазонов аккаунтов
            ranges = [(1, 15), (16, 30), (46, 60), (61, 75), (76, 90), (91, 102)]
            random.shuffle(ranges)
            print(ranges)
            for start, end in ranges:
                number_of_active_profiles = end - start + 1
                loading_profile_data = [i for i in range(start, end)]

                if loading_profile_data is not None:
                    with Pool(number_of_active_profiles) as p:
                        p.map(Mass.start_mass_walker, loading_profile_data)

    except Exception as e:
        print(f'Проблемы с мультипроцессингом: {e}')


if __name__ == '__main__':
    main()

