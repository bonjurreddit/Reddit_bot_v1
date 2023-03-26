import random
import datetime
from v40_walker import Walker
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from multiprocessing import Pool


class SmartBot(Walker):

    def __init__(self, count):
        super().__init__(count)
        self.post_id = None
        self.flag_check_post  = None

    def smart_dis(self):
        try:
            elements = self.browser.find_elements(By.CSS_SELECTOR, self.random_post)
            index = - 1
            for element in elements:
                index += 1
                class_name = element.get_attribute("class")
                if self.post_id in class_name:
                    self.browser.back()
                    self.move_and_click_element_ls(elements[index - 1])
                    if random.random() < 0.5:
                        self.down_vote_random()
                        print(f'Account{self.count}: [+] Поставил Дизлайк')
                    self.random_time_sleep_large()
                    break
        except NoSuchElementException:
            print(f'Account{self.count}: [-] Проблемы с ДизЛайком')

    def check_post_in_page(self, post_title):
        try:
            scroll = self.browser.find_element(By.PARTIAL_LINK_TEXT, post_title)
            print(f'Account{self.count}: [+] Пост ЕСТЬ на странице')
            self.flag_check_post = 1
        except NoSuchElementException:
            print(f'Account{self.count}: [-] Элемента нет на странице, перехожу в NEW')

    def get_post_id(self):
        try:
            current_url = self.browser.current_url
            self.post_id = current_url.split('/')[-3]
            print(f'Account{self.count}: [+] Получил post_id')
            return self.post_id
        except NoSuchElementException:
            print(f'Account{self.count}: [-] НЕ получил post_id')

    def tab_new_script(self, sub_name, post_title_like):

        self.tab_new(sub_name)
        self.search_post_with_title_name(post_title_like)
        self.up_vote_random()
        self.save_or_share_or_pass()
        self.random_follow_author()
        self.close_browser()

        print(f'Account{self.count}({self.username}: {datetime.datetime.now()}): [+] КОНЕЦ СКРИПТА, РАБОТА ЧЕРЕЗ NEW')

    def tab_top_script(self, url, post_title_like):

        self.search_post_with_title_name(post_title_like)
        self.get_post_id()
        self.up_vote_random()
        self.save_or_share_or_pass()

        if self.random_number_for_save < 0.5:
            self.browser.back(2)
            self.smart_dis()
            self.close_browser()
            print(f'Account{self.count}({self.username}: {datetime.datetime.now()}): [+] КОНЕЦ СКРИПТА, РАБОТА ЧЕРЕЗ TOP (SAVE)')
        else:
            if random.random() < 0.5:
                self.open_authors_page()
                self.random_follow_author()
                self.open_communities_url(url)
                self.smart_dis()
                self.close_browser()
                print(f'Account{self.count}({self.username}: {datetime.datetime.now()}): [+] КОНЕЦ СКРИПТА, РАБОТА ЧЕРЕЗ TOP (FOLLOW AUTHOR)')
            else:
                self.browser.back()
                self.smart_dis()
                self.close_browser()
                print(f'Account{self.count}({self.username}: {datetime.datetime.now()}): [+] КОНЕЦ СКРИПТА, РАБОТА ЧЕРЕЗ TOP (CLEAR)')

    @staticmethod
    def smart_top(i):
        my_bot = SmartBot(i)

        url = 'https://www.reddit.com/r/DadWouldBeProud/'
        sub_name = 'DadWouldBeProud'
        post_title_like = "daddy, let me tickle your nerves with this gif"

        try:
            my_bot.start_browser()
            my_bot.open_communities_url(url)
            my_bot.random_subscribe()
            my_bot.check_post_in_page(post_title_like)

            if my_bot.flag_check_post == 1:
                my_bot.tab_top_script(url, post_title_like)
            else:
                my_bot.tab_new_script(sub_name, post_title_like)

        except Exception as e:
            my_bot.close_browser()
            print(f'Account{my_bot.count}({my_bot.username}: {datetime.datetime.now()}): [-] ПРОБЛЕМЫ! ВЫЛЕТЕЛ ПО ПРИЧИНЕ: {e}')

    @staticmethod
    def start_mass_smart_dis(i):  # start for script # Старт основого скрипта
        my_like = SmartBot(i)
        url = 'https://www.reddit.com/r/DadWouldBeProud/'
        sub_name = 'DadWouldBeProud'
        post_title_like = "daddy, let me tickle your nerves with this gif"

        try:
            my_like.start_browser()
            my_like.open_communities_url(url)
            my_like.search_post_with_title_name(post_title_like)
            my_like.get_post_id()
            my_like.smart_dis()
            my_like.close_browser()

        except Exception as e:
            my_like.close_browser()
            print(f'Проблемы с масс.лайкингом: {e}')


def main():
    with Pool(1) as p:  # МУЛЬТИПРОЦЕССИНГ
        p.map(SmartBot.start_mass_smart_dis, [1, 1])


if __name__ == '__main__':
    main()
