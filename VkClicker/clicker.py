from __future__ import print_function
import collections
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore, Style
from colorama import init


history = collections.deque(maxlen=4)


class VkClicker:
    """ VkClicker class """

    def __init__(self, username, password):
        print(f'\n*** {Fore.YELLOW}{Style.BRIGHT}SETTING UP{Style.RESET_ALL} ***', end='')
        self.username = username
        self.password = password
        self.driver = webdriver.Opera()  # ИЗМЕНИТЬ НА ОПЕРУ
        self.driver.get("https://vk.com/gim170347829?peers=94582428_263781082&tab=unread")
        sleep(2)

        # Logging in
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(2)

        try:
            # Entering authentication code
            self.driver.find_element_by_xpath('//*[@id="authcheck_code"]').send_keys(input('\r*** Введите код '
                                                                                           'аутентификации: '))
            self.driver.find_element_by_xpath('//*[@id="login_authcheck_submit_btn"]').click()
            sleep(2)

        except NoSuchElementException:
            pass

        # Just for removing "setting up"
        print(f"\r*** {Fore.GREEN}{Style.BRIGHT}WORKING{Style.RESET_ALL} ***")
        sleep(0.5)

        while True:
            try:
                for i in range(1, 6):

                    try:
                        if self.driver.find_element_by_xpath(f'//*[@id="im_dialogs"]/li[{i}]/div[2]/div/div[3]/span['
                                                             f'1]/span[2]'):

                            continue

                    except NoSuchElementException:
                        pass

                    for word in words:

                        # Looking for word in the container
                        if word.lower() in (self.driver.find_element_by_xpath(f'//*[@id="im_dialogs"]/li[{i}]/div[2]/div/div['
                                                                      f'3]/span[1]').text).lower():

                            self.driver.find_element_by_xpath(f'//*[@id="im_dialogs"]/li[{i}]').click()
                            sleep(5)
                            self.driver.back()
                            sleep(2)

                sleep(2)

            except NoSuchElementException:
                self.driver.quit()
                print(Fore.RED + 'Error: No Such Element')
                print('*Возможно появилась капча, которая помешала работе кликера')
                reload()
                main()

            except TimeoutError:
                self.driver.quit()

            except Exception as ex:
                print(Fore.RED + f'Fatal Error:{ex}')
                print(Style.RESET_ALL)
                input('\nPress Enter to exit...')


def reload():
    """ Animation of reloading """
    history.append(reload)
    symbols = ['|', '/', '-', '\\']

    # Just to avoid recursion
    if len(history) == 3:
        raise TimeoutError('Too many retries')

    for i in range(100):
        print(Fore.YELLOW + f'Reloading {i}% {symbols[i % 4]}', end='')
        print('\r', end='')
        sleep(0.1)
    print(Fore.GREEN + "Successfully      ")
    print(Style.RESET_ALL)


def main():
    """ Main function """

    def count_lines(filename, chunk_size=1 << 13):
        """ Counting number of lines in the file """
        with open(filename) as file:
            return sum(chunk.count('\n')
                       for chunk in iter(lambda: file.read(chunk_size), ''))

    with open("info.txt", 'r') as f:
        username = f.readline()[:-1]
        password = f.readline()


    if not words:
        with open("words.txt", 'r') as w:
            for j in range(count_lines("words.txt")):
                phrase = w.readline()
                words.append(phrase[:-1])
            phrase = w.readline()
            words.append(phrase)
    else:
        pass

    VkClicker(username, password)

    return tries


if __name__ == "__main__":
    tries = 0
    words = []
    init()
    print(Style.BRIGHT +
          '* * * * * * * * * * * * * * * * *\n'
          '*                               *\n'
          '*           VkClicker           *\n'
          '*                               *\n'
          f'*    Telegram - {Fore.CYAN}@chaddydaddy {Style.RESET_ALL}   *\n'
          '*                               *\n'
          '* * * * * * * * * * * * * * * * *')
    sleep(1)
    main()
