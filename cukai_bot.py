from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from progressbar import ProgressBar
import datetime
import time


class Cukai_Bot:

    def __init__(self):

        print('initiating the bot...')

        option = webdriver.ChromeOptions()
        #option.add_argument('--headless')
        option.add_argument('--no-proxy-server')
        option.add_argument('--hide-scrollbars')
        option.add_argument('--disable-gpu')
        option.add_argument("--log-level=3")  # fatal

        chromedriver_path = 'C:/chromedriver/chromedriver.exe'
        global driver
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=option)  # This will open the Chrome window
        sleep(2)

        # getter method

    def page_scrape(self, url, nohak_val_min, nohak_val_max, muk_code, jshak_code):

        pbar = ProgressBar()

        nama_pemiliks = []
        nama_pembayars = []
        no_kad_pengenalans = []
        alamats = []
        no_hakmiliks = []

        range1 = range(int(nohak_val_min), int(nohak_val_max) + 1)

        for i in pbar(range1):
            driver.get(url)
            driver.find_element_by_xpath(
                '/html/body/form/table/tbody/tr[2]/td[2]/select/option[' + muk_code + ']').click()
            driver.find_element_by_xpath(
                '/html/body/form/table/tbody/tr[2]/td[3]/select/option[' + jshak_code + ']').click()

            nohak = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[4]/input')
            nohak.send_keys(i)
            nohak.send_keys(Keys.ENTER)

            """This function takes care of the scraping part"""
            sleep(5)

            try:
                nama_pemilik = driver.find_element_by_xpath('/html/body/form[2]/p/table[1]/tbody/tr[2]/td[2]/font')
                nama_pembayar = driver.find_element_by_xpath('/html/body/form[2]/p/table[1]/tbody/tr[3]/td[2]/font')
                no_kad_pengenalan = driver.find_element_by_xpath('/html/body/form[2]/p/table[1]/tbody/tr[4]/td[2]/font')
                alamat = driver.find_element_by_xpath('/html/body/form[2]/p/table[1]/tbody/tr[5]/td[2]/font')
                no_hakmilik = driver.find_element_by_xpath('/html/body/form[2]/p/table[1]/tbody/tr[6]/td[2]/font')

                nama_pemiliks.append(nama_pemilik.text.strip())
                nama_pembayars.append(nama_pembayar.text.strip())
                no_kad_pengenalans.append(no_kad_pengenalan.text.strip())
                alamats.append(alamat.text.strip().replace('\n', " "))
                no_hakmiliks.append(no_hakmilik.text.strip())
            except NoSuchElementException:
                nama_pemiliks.append(None)
                nama_pembayars.append(None)
                no_kad_pengenalans.append(None)
                alamats.append(None)
                no_hakmiliks.append(None)

        cols = (['Nama Pemilik', 'Nama Pembayar', 'No Kad Pengenalan', 'Alamat', 'No Hak Milik'])

        cukais_df = pd.DataFrame({'Nama Pemilik': nama_pemiliks,
                                  'Nama Pembayar': nama_pembayars,
                                  'No Kad Pengenalan': no_kad_pengenalans,
                                  'Alamat': alamats,
                                  'No Hak Milik': no_hakmiliks})[cols]

        return cukais_df

    def start_cukai_bot(self, daerah_code, nohak_val_min, nohak_val_max, muk_code, jshak_code):

        start_time = time.time()

        url = ('https://ptgns.ns.gov.my/fpx/fpxv2_qrycukai.php?&daerah=' + daerah_code)
        driver.get(url)

        sleep(randint(18, 25))

        print('starting to scrape.....')

        cukai_details = Cukai_Bot.page_scrape(self, url, nohak_val_min, nohak_val_max, muk_code, jshak_code)

        x = datetime.datetime.now()
        filename = 'export_cukai_' + nohak_val_min + '_' + nohak_val_max + '_' + x.strftime('%Y%m%d_%H%M') + '.csv'
        cukai_details.to_csv(r'' + filename, index=False, header=True)

        print('saved df.....')

        print("--- %s seconds ---" % (time.time() - start_time))
