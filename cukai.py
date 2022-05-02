# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import datetime
from time import sleep
from progressbar import ProgressBar

pbar = ProgressBar()

nama_pemiliks = []
nama_pembayars = []
no_kad_pengenalans = []
alamats = []
no_hakmiliks = []

nohak_val_min = input("Enter min number: ")
nohak_val_max = input("Enter max number: ")

range1 = range(int(nohak_val_min), int(nohak_val_max) + 1)

url = 'https://ptgns.ns.gov.my/fpx/fpxv2_qrycukai.php?&daerah=05'

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--hide-scrollbars')
option.add_argument('--disable-gpu')
option.add_argument("--log-level=3")  # fatal
driver = webdriver.Chrome('C:/chromedriver/chromedriver85.exe', options=option)

print('--------------------------------')
print('|        INITIALIZING...       |')
print('--------------------------------\n\n')

print('\t2 - Bandar Baru Enstek          12 - Mukim Lenggeng')
print('\t3 - Bandar Baru Sri Kota Mas    13 - Mukim Pantai')
print('\t4 - Mantin Utama                14 - Mukim Rantau')
print('\t5 - Bandar Nilai Utama          15 - Mukim Rasah')
print('\t6 - Bandar Seremban             16 - Mukim Seremban')
print('\t7 - Bandar Seremban 3           17 - Mukim Setul')
print('\t8 - Bandar Seremban Utama       18 - Pekan Broga')
print('\t9 - Bandar Sri Sendayan         19 - Pekan Bukit Kepayang')
print('\t10 - Mukim Ampangan             20 - Pekan Bukti')
print('\t11 - Mukim Labu                 21 - Pekan Dusun Setia\n')

print('\t22 - Pekan Labu                 32 - Pekan Rantau')
print('\t23 - Pekan Lenggeng             33 - Pekan Rasah Jaya')
print('\t24 - Pekan Mambau               34 - Pekan Senawang')
print('\t25 - Pekan Mantin               35 - Pekan Seremban Jaya')
print('\t26 - Pekan Nilai                36 - Pekan Setul')
print('\t27 - Pekan Pajam                37 - Pekan Shah Bandar')
print('\t28 - Pekan Panchor              38 - Pekan Sikamat')
print('\t29 - Pekan Paroi                39 - Pekan Sungai Gadut')
print('\t30 - Pekan Paroi Jaya           40 - Pekan Taman Seremban')
print('\t31 - Pekan Rahang Baru          41 - Pekan Tiroi\n')

print('\t42 - Pekan Ulu Beranang')
print('\t43 - Pekan Ulu Temiang\n')

muk_code = input("Enter Mukim code: ")

print('\n\n\t2 - GERAN MUKIM	(GM)')
print('\t3 - GERAN  (GRN)')
print('\t4 - HAKMILIK SEMENTARA DAFTAR (HSD)')
print('\t5 - HAKMILIK SEMENTARA MUKIM (HSM)')
print('\t6 - PAJAKAN MUKIM (PM)')
print('\t7 - PAJ NEGERI (PN)\n')

jshak_code = input('Enter Jenis Hak Milik code: ')

print('\n\nPlease wait while system retrieves the information your need.\n\n')

for i in pbar(range1):
    driver.get(url)
    driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/select/option[' + muk_code + ']').click()
    driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[3]/select/option[' + jshak_code + ']').click()

    nohak = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[4]/input')
    nohak.send_keys(i)
    nohak.send_keys(Keys.ENTER)

    sleep(10)

    try:
        nama_pemilik = driver.find_element_by_xpath('/html/body/form[2]/p/table[1]/tbody/tr[2]/td[2]/font')
        nama_pembayar = driver.find_element_by_xpath('/html/body/form[2]/p/table[1]/tbody/tr[3]/td[2]/font')
        no_kad_pengenalan = driver.find_element_by_xpath('/html/body/form[2]/p/table[1]/tbody/tr[4]/td[2]/font')
        alamat = driver.find_element_by_xpath('/html/body/form[2]/p/table[1]/tbody/tr[5]/td[2]/font')
        no_hakmilik = driver.find_element_by_xpath('/html/body/form[2]/p/table[1]/tbody/tr[6]/td[2]/font')

        nama_pemiliks.append(nama_pemilik.text.strip())
        nama_pembayars.append(nama_pembayar.text.strip())
        no_kad_pengenalans.append(no_kad_pengenalan.text.strip())
        alamats.append(alamat.text.strip())
        no_hakmiliks.append(no_hakmilik.text.strip())
    except NoSuchElementException:
        nama_pemiliks.append(None)
        nama_pembayars.append(None)
        no_kad_pengenalans.append(None)
        alamats.append(None)
        no_hakmiliks.append(None)


x = datetime.datetime.now()
filename = 'export_cukai_' + nohak_val_min + '_' + nohak_val_max + '_' + x.strftime('%Y%m%d-%H%M') + '.csv'

datas = {'Nama Pemilik': nama_pemiliks, 'Nama Pembayar': nama_pembayars, 'No Kad Pengenalan': no_kad_pengenalans, 'Alamat': alamats, 'No Hak Milik': no_hakmiliks}

df = pd.DataFrame(datas, columns=['Nama Pemilik', 'Nama Pembayar', 'No Kad Pengenalan', 'Alamat', 'No Hak Milik'])
df.to_csv(r''+filename, index=False, header=True)

print('SUCESSFULLY CREATED: ' + filename + '\n\n')
print('PROGRAM END')
