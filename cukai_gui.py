import tkinter as tk
from tkinter import ttk
from cukai_bot import Cukai_Bot


def close_app():
    app.destroy()


def run_app():
    user_daerah_code_value = str(daerah_code_value.get())
    user_nohak_min_value = str(nohak_min_value_entry.get())
    user_nohak_max_value = str(nohak_max_value_entry.get())
    user_mukim_code_value = str(mukim_code_value.get())
    user_jshak_code_value = str(jshak_code_value.get())

    print('starting chrome...')
    bot = Cukai_Bot()
    bot.start_cukai_bot(user_daerah_code_value, user_nohak_min_value, user_nohak_max_value,
                        user_mukim_code_value, user_jshak_code_value)


def select_daerah(event):
    option = daerahCombo.get()
    code = option.split("-")[0]
    daerah_code_value.set(code)

    # convert to int for if statement
    code = int(code)

    mukimComboValues = []

    if code == 1:
        mukimComboValues = [
            "40 - Bandar Kuala Klawang",
            "01 - Mukim Glami Lemi",
            "04 - Mukim Kuala Klawang",
            "05 - Mukim Kuala Klawang",
            "06 - Mukim Peradong",
            "07 - Mukim Pertang",
            "08 - Mukim Triang Ilir",
            "02 - Mukim Ulu Klawang",
            "03 - Mukim Ulu Triang",
            "70 - Pekan Kuala Klawang",
            "71 - Pekan Pertang",
            "75 - Pekan Petaling",
            "73 - Pekan Simpang Durian",
            "74 - Pekan Simpang Pertang",
            "76 - Pekan Sungai Mutoh",
            "72 - Pekan Titi"
        ]
    if code == 2:
        mukimComboValues = [
            "40 - Bandar Kuala Pilah",
            "01 - Mukim Ampang Tinggi",
            "04 - Mukim Johol",
            "05 - Mukim Juasseh",
            "06 - Mukim Kepis",
            "07 - Mukim Langkap",
            "08 - Mukim Parit Tinggi",
            "09 - Mukim Pilah",
            "10 - Mukim Sri Menanti",
            "11 - Mukim Terachi",
            "02 - Mukim Ulu Jempol",
            "03 - Mukim Ulu Muar",
            "79 - Pekan Ayer Mawang",
            "77 - Pekan Bukit Gelugor",
            "70 - Pekan Dangi",
            "80 - Pekan Dangi Baru",
            "71 - Pekan Gunung Pasir",
            "72 - Pekan Johol",
            "76 - Pekan Juasseh",
            "78 - Pekan Melang",
            "73 - Pekan Parit Tinggi",
            "74 - Pekan Senaling",
            "75 - Pekan Tanjong Ipoh"
        ]
    if code == 3:
        mukimComboValues = [
            "40 - Bandar Port Dickson",
            "41 - Bandar Telok Kemang",
            "01 - Mukim Jimah",
            "02 - Mukim Linggi",
            "03 - Mukim Pasir Panjang",
            "04 - Mukim Port Dickson",
            "05 - Mukim Si Rusa",
            "78 - Pekan Air Kuning",
            "80 - Pekan Bagan Pinang",
            "76 - Pekan Bukit Pelanduk",
            "73 - Pekan Chuah",
            "83 - Pekan Jemima",
            "77 - Pekan Linggi",
            "70 - Pekan Lukut",
            "71 - Pekan Pasir Panjang",
            "72 - Pekan Pengkalan Kempas",
            "74 - Pekan Port Dickson",
            "79 - Pekan Sungai Menyala",
            "82 - Pekan Tanah Merah Selatan",
            "81 - Pekan Tanah Merah Utara",
            "75 - Pekan Teluk Kemang"
        ]
    if code == 4:
        mukimComboValues = [
            "40 - Bandar Rembau",
            "01 - Mukim Batu Hampar",
            "02 - Mukim Bongek",
            "03 - Mukim Chembong",
            "04 - Mukim Chengkau",
            "05 - Mukim Gadong",
            "06 - Mukim Kundor",
            "07 - Mukim Legong Ilir",
            "08 - Mukim Legong Ulu",
            "09 - Mukim Miku",
            "10 - Mukim Nerasau",
            "11 - Mukim Pedas",
            "12 - Mukim Pilin",
            "13 - Mukim Selemak",
            "14 - Mukim Semerbok",
            "15 - Mukim Sepri",
            "16 - Mukim Tanjung Kling",
            "17 - Mukim Titian Bintangor",
            "74 - Pekan Chembong",
            "76 - Pekan Chengkau",
            "70 - Pekan Kampong Batu",
            "71 - Pekan Kota",
            "72 - Pekan Lubok China",
            "79 - Pekan Merbau Sembilan",
            "73 - Pekan Pedas",
            "75 - Pekan Rembau",
            "78 - Pekan Seri Kendong",
            "77 - Pekan Seri Kota"
        ]
    if code == 5:
        mukimComboValues = [
            "2 - Bandar Baru Enstek",
            "3 - Bandar Baru Sri Kota Mas",
            "4 - Mantin Utama",
            "5 - Bandar Nilai Utama",
            "6 - Bandar Seremban",
            "7 - Bandar Seremban 3",
            "8 - Bandar Seremban Utama",
            "9 - Bandar Sri Sendayan",
            "10 - Mukim Ampangan",
            "11 - Mukim Labu",
            "12 - Mukim Lenggeng",
            "13 - Mukim Pantai",
            "14 - Mukim Rantau",
            "15 - Mukim Rasah",
            "16 - Mukim Seremban",
            "17 - Mukim Setul",
            "18 - Pekan Broga",
            "19 - Pekan Bukit Kepayang",
            "20 - Pekan Bukti",
            "21 - Pekan Dusun Setia",
            "22 - Pekan Labu",
            "23 - Pekan Lenggeng",
            "24 - Pekan Mambau",
            "25 - Pekan Mantin",
            "26 - Pekan Nilai",
            "27 - Pekan Pajam",
            "28 - Pekan Panchor",
            "29 - Pekan Paroi",
            "30 - Pekan Paroi Jaya",
            "31 - Pekan Rahang Baru",
            "32 - Pekan Rantau",
            "33 - Pekan Rasah Jaya",
            "34 - Pekan Senawang",
            "35 - Pekan Seremban Jaya",
            "36 - Pekan Setul",
            "37 - Pekan Shah Bandar",
            "38 - Pekan Sikamat",
            "39 - Pekan Sungai Gadut",
            "40 - Pekan Taman Seremban",
            "41 - Pekan Tiroi",
            "42 - Pekan Ulu Beranang",
            "43 - Pekan Ulu Temiang"
        ]
    if code == 6:
        mukimComboValues = [
            "41 - Bandar Tampin",
            "03 - Mukim Gemencheh",
            "04 - Mukim Keru",
            "05 - Mukim Repah",
            "06 - Mukim Tampin Tengah",
            "07 - Mukim Tebong",
            "71 - Pekan Batang Melaka",
            "72 - Pekan Gemencheh Baru",
            "79 - Pekan Gemencheh Baru Seksyen 1",
            "73 - Pekan Repah",
            "78 - Pekan Repah Jaya",
            "77 - Pekan Repah Permai",
            "74 - Pekan Tampin Tengah"
        ]
    if code == 7:
        mukimComboValues = [
            "41 - Bandar Bahau",
            "42 - Bandar Seri Jempol",
            "40 - Bandar Serting",
            "01 - Mukim Jelai",
            "02 - Mukim Kuala Jempol",
            "03 - Mukim Rompin",
            "04 - Mukim Serting Ilir",
            "05 - Mukim Serting Ulu",
            "70 - Pekan Bahau",
            "77 - Pekan Bahau Seksyen 1",
            "71 - Pekan Batu Kikir",
            "72 - Pekan Kuala Jelai",
            "74 - Pekan Ladang Geddes",
            "75 - Pekan Mahsan",
            "73 - Pekan Rompin",
            "76 - Pekan Serting Tengah"
        ]
    if code == 12:
        mukimComboValues = [
            "40 - Bandar Gemas",
            "01 - Mukim Ayer Kuning",
            "02 - Mukim Gemas",
            "75 - Pekan Ayer Kuning",
            "70 - Pekan Ayer Kuning Selatan",
            "76 - Pekan Pasir Besar",
        ]
    if code == 13:
        mukimComboValues = []

    # internal function to get mukim
    def select_mukim(event):
        option = mukimCombo.get()
        code = option.split("-")[0]
        mukim_code_value.set(code)

    tk.Label(app, text="Select Mukim: ").grid(row=2, column=0, sticky="E")
    mukimCombo = ttk.Combobox(width=40, height=30, values=mukimComboValues, state="readonly")
    mukimCombo.grid(row=2, column=1, padx=10)
    mukimCombo.current(0)  # default selected
    mukimCombo.bind('<<ComboboxSelected>>', select_mukim)


def select_jshak(event):
    option = jshakCombo.get()
    code = option.split("-")[0]
    jshak_code_value.set(code)


app = tk.Tk()
app.title("Cukai - v1.2")
app.geometry("500x200")

daerah_code_value = tk.StringVar()
mukim_code_value = tk.StringVar()
jshak_code_value = tk.StringVar()
nohak_min_value = tk.StringVar()
nohak_max_value = tk.StringVar()

daerahComboValues = [
    "01 - Jelebu",
    "02 - Kuala Pilah",
    "03 - Port Dickson",
    "04 - Rembau",
    "05 - Seremban",
    "06 - Tampin",
    "07 - Jempol",
    "12 - Gemas",
    "13 - Pusat Transformasi Bandar"
]

tk.Label(app, text="Select Daerah: ").grid(row=1, column=0, sticky="E")
daerahCombo = ttk.Combobox(width=40, state="readonly", values=daerahComboValues)
daerahCombo.grid(row=1, column=1, padx=10)
daerahCombo.current(0)  # default selected
daerahCombo.bind('<<ComboboxSelected>>', select_daerah)



jshakComboValues = ["2 - GERAN MUKIM (GM)",
                    "3 - GERAN (GRN)",
                    "4 - HAKMILIK SEMENTARA DAFTAR (HSD)",
                    "5 - HAKMILIK SEMENTARA MUKIM (HSM)",
                    "6 - PAJAKAN MUKIM (PM)",
                    "7 - PAJ NEGERI (PN)"]

tk.Label(app, text="Select Jenis Hak: ").grid(row=3, column=0, sticky="E")
jshakCombo = ttk.Combobox(app, width=40, values=jshakComboValues, state="readonly")
jshakCombo.grid(row=3, column=1, sticky="W", padx=10)
jshakCombo.current(0)  # default selected
jshakCombo.bind("<<ComboboxSelected>>", select_jshak)

tk.Label(app, text="Enter No Hak Min value: ").grid(row=4, column=0, sticky="E")
nohak_min_value_entry = tk.Entry(app, textvariable=nohak_min_value)
nohak_min_value_entry.grid(row=4, column=1, sticky="W", padx=10)

tk.Label(app, text="Enter No Hak Max value: ").grid(row=5, column=0, sticky="E")
nohak_max_value_entry = tk.Entry(app, textvariable=nohak_max_value)
nohak_max_value_entry.grid(row=5, column=1, sticky="W", padx=10)

run_btn = tk.Button(app, text="Start", command=run_app, bg="dark green", fg="white", relief="raised")
run_btn.grid(column=2, row=7)

close_btn = tk.Button(app, text="Exit", command=close_app)
close_btn.grid(column=3, row=7)

app.mainloop()
