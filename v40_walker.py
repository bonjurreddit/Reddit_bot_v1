from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from v40_like import UpVote
from selenium.webdriver.common.by import By
from multiprocessing import Pool
import time
import random


class Walker(UpVote):

    def __init__(self, count):
        super().__init__(count)
        self.random_step = int(random.randint(81, 158))
        self.random_scroll_time = int(random.randint(60, 80))
        self.start_time = time.time()


        # Элементы гулялки
        self.open_menu_switch = '#view--layout--FUE'
        self.content_menu = 'body > div:nth-child(65) > div'

    def switching_display_post(self):
        try:
            self.random_time_sleep_large()
            self.browser.refresh()
            self.move_to_and_click_static_css(self.open_menu_switch)
            self.browser.execute_script("document.body.style.zoom = '100%'")
            self.random_time_sleep_large()
            self.move_to_and_click_static_css(self.content_menu)
            self.random_time_sleep_fast()
            print(f'Account{self.count}: [+]  Переключил на плитку')
        except NoSuchElementException:
            self.move_to_and_click_static_css(self.open_menu_switch)
            print(f'Account{self.count}: [-] Уже переключено на плитку')

    def scroll_page(self):

        while time.time() - self.start_time < 100:
            self.browser.execute_script(f"window.scrollBy(0, {self.random_step});")
            self.random_time_for_scroll()

    def search_random_post(self):

        elements = self.browser.find_elements(By.CSS_SELECTOR, "[class^='_1oQyIsiPHYt6nx7VOmd1sz']")
        last_27_elements = elements[-27:]
        random_element = random.choice(last_27_elements)


        for element in elements:
            if element.is_displayed():
                self.move_and_click_element_ls(element)
                break
        self.random_time_sleep_large()


    @staticmethod
    def start_test_walker(i):
        bot = Walker(i)
        try:
            bot.start_browser()
            bot.switching_display_post()
            bot.scroll_page()
            bot.search_random_post()
            bot.close_browser()
        except Exception as e:
            bot.close_browser()
            print(f'Xyeta {e}')


def main():
    try:
        with Pool(2) as p:  # МУЛЬТИПРОЦЕССИНГ
            p.map(Walker.start_test_walker, [1, 2])

    except Exception as e:
        print(f'Проблемы с мультипроцессингом: {e}')


if __name__ == '__main__':
    main()
