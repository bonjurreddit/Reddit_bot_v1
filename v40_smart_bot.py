from v40_comment import Walker
from Data.comment import comments
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import random
import datetime


class SmartBot(Walker):

    def __init__(self, count):
        super().__init__(count)

        self.random_comment = random.choice(list(comments.values()))
        self.post_id = None
        self.flag_check_post = 0
        self.current_url = None
        self.post_url_old = None

        # Элементы реддит
        self.count_like = 'body > div.side > div:nth-child(2) > div > div.score > span.number'
        self.comment_container = '#overlayScrollContainer > div._1npCwF50X2J7Wt82SZi6J0 > div.u35lf2ynn4jHsVUwPmNU.Dx3UxiK86VcfkFQVHNXNi > div.uI_hDmU5GSiudtABRz_37 > div._1r4smTyOEZFO91uFIdWW6T.aUM8DQ_Nz5wL0EJc_wte6 > div:nth-child(2) > div > div > div._2baJGEALPiEMZpWB2iWQs7 > div > div:nth-child(1) > div > div > div'
        self.comment_container_in_open_post = '#AppRouter-main-content > div > div > div._3ozFtOe6WpJEMUtxDOIvtU > div._31N0dvxfpsO6Ur5AKx4O5d > div._1OVBBWLtHoSPfGCRaPzpTf._3nSp9cdBpqL13CqjdMr2L_._2udhMC-jldHp_EpAuBeSR1.PaJBYLqPf_Gie2aZntVQ7._2OVNlZuUd8L9v0yVECZ2iA > div.uI_hDmU5GSiudtABRz_37 > div._1r4smTyOEZFO91uFIdWW6T.aUM8DQ_Nz5wL0EJc_wte6 > div:nth-child(2) > div > div > div._2baJGEALPiEMZpWB2iWQs7 > div > div:nth-child(1) > div > div > div'
        self.comment_send = '#overlayScrollContainer > div._1npCwF50X2J7Wt82SZi6J0 > div.u35lf2ynn4jHsVUwPmNU.Dx3UxiK86VcfkFQVHNXNi > div.uI_hDmU5GSiudtABRz_37 > div._1r4smTyOEZFO91uFIdWW6T.aUM8DQ_Nz5wL0EJc_wte6 > div:nth-child(2) > div > div > div._17TqawK-44tH0psnHPIhzS.RQTXfVRnnTF5ont3w58rx > div._3SNMf5ZJL_5F1qxcZkD0Cp'
        self.comment_send_in_post = '#AppRouter-main-content > div > div > div._3ozFtOe6WpJEMUtxDOIvtU > div._31N0dvxfpsO6Ur5AKx4O5d > div._1OVBBWLtHoSPfGCRaPzpTf._3nSp9cdBpqL13CqjdMr2L_._2udhMC-jldHp_EpAuBeSR1.PaJBYLqPf_Gie2aZntVQ7._2OVNlZuUd8L9v0yVECZ2iA > div.uI_hDmU5GSiudtABRz_37 > div._1r4smTyOEZFO91uFIdWW6T.aUM8DQ_Nz5wL0EJc_wte6 > div:nth-child(2) > div > div > div._17TqawK-44tH0psnHPIhzS.RQTXfVRnnTF5ont3w58rx > div._3SNMf5ZJL_5F1qxcZkD0Cp'

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
        self.random_time_sleep_fast()

        element2 = self.browser.find_element(By.CSS_SELECTOR, self.count_like)
        likes_after_like = int(element2.text)
        self.browser.switch_to.window(self.browser.window_handles[0])

        if likes_after_like <= likes_before_like:
            print(f'Account{self.count}: [-] НЕ ЛАЙКАЕТ')
        else:
            print(f'Account{self.count}: [+] ЛАЙКАЕТ')

    def write_comment(self):

        if random.random() < 0.07:

            try:
                try:

                    scroll = self.browser.find_element(By.CSS_SELECTOR, self.comment_send)
                    self.enter_word(self.comment_container, self.random_comment)
                    self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
                    self.move_to_and_click_static_css(self.comment_send)
                    self.move_to_and_click_static_css(self.comment_send)
                    print(f'Account{self.count}: [+] Написал комментарий не открывая пост!')

                except NoSuchElementException:

                    scroll = self.browser.find_element(By.CSS_SELECTOR, self.comment_send_in_post)
                    self.enter_word(self.comment_container_in_open_post, self.random_comment)
                    self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
                    self.move_to_and_click_static_css(self.comment_send_in_post)
                    self.move_to_and_click_static_css(self.comment_send_in_post)
                    print(f'Account{self.count}: [+] Написал комментарий открыв пост!')

            except Exception as e:
                print(f'Account{self.count}: [-] Проблемы с комментом {e}')


    def tab_new_script(self, sub_name, post_title_like):

        self.tab_new(sub_name)
        self.search_post_with_title_name(post_title_like)
        self.get_post_url()
        self.check_like()
        self.save_or_share_or_pass()
        self.open_authors_page()
        self.random_follow_author()
        self.like_count()
        self.close_browser()

        print(f'Account{self.count}({self.username}: {datetime.datetime.now()}): [+] КОНЕЦ СКРИПТА, РАБОТА ЧЕРЕЗ NEW')

    def tab_top_script(self, url, post_title_like):
        self.search_post_with_title_name_for_top_script(post_title_like)
        self.get_post_id()
        self.get_post_url()
        self.check_like()
        self.write_comment()
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


    def tab_top_script_not_checker(self, url, post_title_like):
        self.search_post_with_title_name_for_top_script(post_title_like)
        self.get_post_id()
        self.get_post_url()
        self.check_like()
        self.write_comment()
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
