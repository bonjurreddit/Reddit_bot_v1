import random
import datetime
from v40_walker import Walker
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class SmartBot(Walker):

    def __init__(self, count):
        super().__init__(count)
        self.post_id = None
        self.flag_check_post = 0
        self.current_url = None
        self.post_url_old = None

        # Элементы реддит
        self.count_like = 'body > div.side > div:nth-child(2) > div > div.score > span.number'

    def smart_dis(self):
        try:
            elements = self.browser.find_elements(By.CSS_SELECTOR, self.random_post)
            index = - 1
            for element in elements:
                index += 1
                class_name = element.get_attribute("class")
                if self.post_id in class_name:
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

    def get_post_url(self):
        try:
            current_url = self.browser.current_url
            self.post_url_old = current_url.replace("www", "old")
            print(f'Account{self.count}: [+] Получил post_url')
            return self.post_id
        except NoSuchElementException:
            print(f'Account{self.count}: [-] НЕ получил post_url')

    def start_sub_scroll(self):
        for i in range(random.randint(30, 35)):
            self.browser.execute_script(f"window.scrollBy(0, {self.random_step});")

    def like_count(self):
        if self.count in [15, 30, 45, 60, 75, 90, 102]:
            self.browser.get(self.post_url_old)
            element = self.browser.find_element(By.CSS_SELECTOR, self.count_like)
            print(f'Account{self.count}: ==============================  КОЛИЧЕСТВО ЛАЙКОВ: {element.text}  ==============================')

    def check_like(self):
        self.browser.execute_script(f"window.open('{self.post_url_old}');")
        self.browser.switch_to.window(self.browser.window_handles[-1])

        element = self.browser.find_element(By.CSS_SELECTOR, self.count_like)
        likes_before_like = int(element.text)
        self.random_time_sleep_fast()

        self.browser.switch_to.window(self.browser.window_handles[0])
        self.up_vote_random()

        self.browser.switch_to.window(self.browser.window_handles[-1])
        self.browser.refresh()
        element = self.browser.find_element(By.CSS_SELECTOR, self.count_like)
        likes_after_like = int(element.text)

        if likes_after_like <= likes_before_like:
            print(f'Account{self.count}: [-] НЕ ЛАЙКАЕТ')
        else:
            print(f'Account{self.count}: [+] ЛАЙКАЕТ')







    def tab_new_script(self, sub_name, post_title_like):

        self.tab_new(sub_name)
        self.search_post_with_title_name(post_title_like)
        self.get_post_url()
        self.up_vote_random()
        self.save_or_share_or_pass()
        self.open_authors_page()
        self.random_follow_author()
        self.like_count()
        self.close_browser()

        print(f'Account{self.count}({self.username}: {datetime.datetime.now()}): [+] КОНЕЦ СКРИПТА, РАБОТА ЧЕРЕЗ NEW')

    def tab_top_script(self, url, post_title_like):

        self.random_time_sleep_big()
        self.search_post_with_title_name(post_title_like)
        self.get_post_id()
        self.get_post_url()
        self.up_vote_random()
        self.save_or_share_or_pass()

        if self.random_number_for_save < 0.5:
            self.open_communities_url(url)
            self.search_post_with_title_name_not_open(post_title_like)
            self.smart_dis()
            self.like_count()
            self.close_browser()
            print(f'Account{self.count}({self.username}: {datetime.datetime.now()}): [+] КОНЕЦ СКРИПТА, РАБОТА ЧЕРЕЗ TOP (SAVE)')
        else:
            if random.random() < 0.5:
                self.open_authors_page()
                self.random_follow_author()
                self.open_communities_url(url)
                self.search_post_with_title_name_not_open(post_title_like)
                self.smart_dis()
                self.like_count()
                self.close_browser()
                print(f'Account{self.count}({self.username}: {datetime.datetime.now()}): [+] КОНЕЦ СКРИПТА, РАБОТА ЧЕРЕЗ TOP (FOLLOW AUTHOR)')
            else:
                self.close_post()
                self.smart_dis()
                self.like_count()
                self.close_browser()
                print(f'Account{self.count}({self.username}: {datetime.datetime.now()}): [+] КОНЕЦ СКРИПТА, РАБОТА ЧЕРЕЗ TOP (CLEAR)')
