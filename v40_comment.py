from Data.comment import comments
from v40_walker import Walker
from selenium.common import NoSuchElementException
import random


class Comment(Walker):
    def __int__(self, count):
        super().__init__(count)

        self.random_comment = random.choice(list(comments.values()))
        self.comment_container = '#overlayScrollContainer > div._1npCwF50X2J7Wt82SZi6J0 > div.u35lf2ynn4jHsVUwPmNU.Dx3UxiK86VcfkFQVHNXNi > div.uI_hDmU5GSiudtABRz_37 > div._1r4smTyOEZFO91uFIdWW6T.aUM8DQ_Nz5wL0EJc_wte6 > div:nth-child(2) > div > div > div._2baJGEALPiEMZpWB2iWQs7 > div > div:nth-child(1) > div > div > div'
        self.comment_container_in_open_post = '#AppRouter-main-content > div > div > div._3ozFtOe6WpJEMUtxDOIvtU > div._31N0dvxfpsO6Ur5AKx4O5d > div._1OVBBWLtHoSPfGCRaPzpTf._3nSp9cdBpqL13CqjdMr2L_._2udhMC-jldHp_EpAuBeSR1.PaJBYLqPf_Gie2aZntVQ7._2OVNlZuUd8L9v0yVECZ2iA > div.uI_hDmU5GSiudtABRz_37 > div._1r4smTyOEZFO91uFIdWW6T.aUM8DQ_Nz5wL0EJc_wte6 > div:nth-child(2) > div > div > div._2baJGEALPiEMZpWB2iWQs7 > div > div:nth-child(1) > div > div > div'

    def write_comment(self):
        try:
            self.enter_word(self.comment_container, self.random_comment)
            print(f'Account{self.count}: [+] Написал комментарий не открывая пост!')

        except NoSuchElementException:
            self.enter_word(self.comment_container, self.random_comment)
            print(f'Account{self.count}: [-] Написал комментарий открыв пост!')
