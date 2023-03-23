from selenium.common import NoSuchElementException
from v40_like import UpVote
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        self.block_close_post_class = '_25ONQRwoX20oeRXFl_FZXt'
        self.btn_follow = '#AppRouter-main-content > div > div > div._3ozFtOe6WpJEMUtxDOIvtU > div._31N0dvxfpsO6Ur5AKx4O5d > div._3Kd8DQpBIbsr5E1JcrMFTY._1tvThPWQpORoc2taKebHxs > div > div._27SH1SRzjtOk_2NB2YC-FR > div > div._3lhzE6Cg3SSeQGIHuLjILb.GQV0F7lQiMOV6EofzopdJ > div:nth-child(1) > button'

    def switching_display_post(self):
        try:
            # Убиваем стартововое меню
            self.random_time_sleep_big()
            self.browser.execute_script(f"window.scrollBy(0, {self.random_step});")
            self.random_time_sleep_large()
            self.browser.refresh()

            # Открываем выпадающий список и обновляем элементы в DOM
            self.move_to_and_click_static_css(self.open_menu_switch)
            self.browser.execute_script("document.body.style.zoom = '100%'")
            self.random_time_sleep_large()

            # Жмем на кнопку переключения
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
        # Определяем элемент на странице
        elements = self.browser.find_elements(By.CSS_SELECTOR, "[class^='_1oQyIsiPHYt6nx7VOmd1sz']")
        element = elements[0]

        # Если пост виден, открываем его
        if element.is_displayed():
            self.move_and_click_element_ls(element)

        # Цикл пролистывающий до нужного поста
        else:
            while not element.is_displayed():
                self.browser.execute_script(f"window.scrollBy(0, {self.random_step});")
                self.random_time_for_scroll()
            self.search_random_post()
            return

        self.random_time_sleep_large()

    def open_authors_page(self):
        # Переменные для поиска нужного элемента
        current_url = self.browser.current_url
        post_id = current_url.split('/')[-3]
        author_link = f'//*[@id="UserInfoTooltip--t3_{post_id}--lightbox"]'
        # Переходим в профиль
        try:
            self.move_and_click_xpath(author_link)
            print(f'Account{self.count}: [+] Перешел в профиль автора')
        except NoSuchElementException:
            print(f'Account{self.count}: [-] НЕ смог перейти в профиль автора')

        self.random_time_sleep_large()

    def close_post(self):
        try:
            self.move_to_and_click_static_class(self.block_close_post_class)
            print(f'Account{self.count}: [+] Закрыл пост')
        except NoSuchElementException:
            print(f'Account{self.count}: [-] НЕ смог закрыть пост')

    def random_follow_author(self):
        try:
            # Находим кнопку подписаться
            follow_btn = self.browser.find_element(By.CSS_SELECTOR, self.btn_follow)
            # Если уже подписаны, ничего не делаем
            if follow_btn.text == 'Unfollow':
                print(f'Account{self.count}: [+] Уже подписан на этого автора')
            # Если не подписаны, подписываемся с рандомом
            if follow_btn.text == 'Follow' and random.random() < 0.5:
                self.random_time_sleep_fast()
                self.move_and_click_css(self.btn_follow)
                self.random_time_sleep_large()
                print(f'Account{self.count}: [+] Подписалс на автора')

        except Exception as e:
            print(f'Account{self.count}: [-] Возникли проблемы с подпиской на автора')
            print(f'Account{self.count}: {e}')


    @staticmethod
    def start_test_walker(i):
        bot = Walker(i)
        try:
            bot.start_browser()
            # bot.switching_display_post()
            # bot.scroll_page()
            bot.search_random_post()
            bot.open_authors_page()
            bot.random_follow_author()
            # bot.close_post()
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
