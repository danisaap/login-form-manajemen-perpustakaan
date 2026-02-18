from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import Entry, Label, Toplevel, messagebox
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import csv

class LoginForm:

    def __init__(self, master):
        self.master = master
        # super().__init__(master)
        self.master.title("Manajemen Perpustakaan - Maha Asik")
        self.master.geometry('1366x768')
        self.master.state('zoomed')
        self.master.config(bg='#1A1A1D')
        self.master.resizable(False, False)
        # window icon
        icon = PhotoImage(file='C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\giradmin.png')
        self.master.iconphoto(True, icon)

        self.bg_frameLogin = '#F6E6A4'
        self.fg_frameLogin = '#2F4454'
        self.font_frameLogin = ('Tw Cen MT', 15, 'bold')

        bg_img = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\bgLogin.jpg').resize((1920,1080)))
        self.bg_label = Label(window, image=bg_img)
        self.bg_label.image = bg_img
        self.bg_label.place(x=0, y=0)
        self.bg_label.pack(expand=YES, fill=BOTH)

        self.frameLogin = Frame(self.master, bg=self.bg_frameLogin, width='950', height='600')
        self.frameLogin.place(x=200, y=70)

        page_img = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\logoLogin.png').resize((450,400)))
        self.page_label = Label(self.frameLogin, image=page_img, bg=self.bg_frameLogin)
        self.page_label.image = page_img
        self.page_label.place(x=5, y=100)

        self.heading = Label(self.frameLogin, text='SELAMAT DATANG DI PERPUSTAKAAN', bg=self.bg_frameLogin, fg=self.fg_frameLogin, font=('Tw Cen MT', 30, 'bold'))
        self.heading.place(x=80, y=30, width=800, height=100)

        self.username_entry = Entry(self.frameLogin, highlightthickness=0, relief='flat', bg=self.bg_frameLogin, fg=self.fg_frameLogin, font=self.font_frameLogin)
        self.username_entry.place(x=550, y=230, width=1000)
        self.set_placeholder(self.username_entry, 'Masukkan Nama Lengkap')

        self.username_line = Canvas(self.frameLogin, width=300, height=2.0, bg='black', highlightthickness=0)
        self.username_line.place(x=550, y=255)

        self.password_entry = Entry(self.frameLogin, highlightthickness=0, relief='flat', bg=self.bg_frameLogin, fg='white', font=self.font_frameLogin)
        self.password_entry.place(x=550, y=310, width=270)
        self.set_placeholder(self.password_entry, 'Masukkan No. Telepon')

        self.password_line = Canvas(self.frameLogin, width=300, height=2.0, bg='black', highlightthickness=0)
        self.password_line.place(x=550, y=335)

        self.login_button = Button(self.frameLogin, text='Masuk', width=25, bd=0, bg='white', fg=self.fg_frameLogin, font=('Tw Cen MT', 15, 'bold'), cursor='hand2', activebackground='white', command=self.verif1)
        self.login_button.place(x=550, y=360)

    def verif1(self):
        self.verif1User = self.username_entry.get()
        self.verif1Pass = self.password_entry.get()

        if self.verif1User == "Masukkan Nama Lengkap" and self.verif1Pass == "Masukkan No. Telepon":
            winDisInfoVerif1 = Toplevel(self.master)
            winDisInfoVerif1.title("Gagal Menjalankan Program")
            winDisInfoVerif1.geometry("350x45")
            winDisInfoVerif1.resizable(False,False)
            
            labelDisInfoVerif1 = Label(winDisInfoVerif1, text='Isi form terlebih dahulu! ')
            labelDisInfoVerif1.pack(padx=5, pady=5)

        elif not self.verif1User or not self.verif1Pass:
            winDisInfoVerif1 = Toplevel(self.master)
            winDisInfoVerif1.title("Gagal Menjalankan Program")
            winDisInfoVerif1.geometry("350x45")
            winDisInfoVerif1.resizable(False,False)
            
            labelDisInfoVerif1 = Label(winDisInfoVerif1, text='Isi form terlebih dahulu! ')
            labelDisInfoVerif1.pack(padx=5, pady=5)

        else:
            self.verif2()

    def verif2(self):
        self.verif1User = self.username_entry.get()
        self.verif1Pass = self.password_entry.get()

        if not self.verif1User.replace(" ","").isalpha() or not self.verif1Pass.isdigit():
            winDisInfoVerif2 = Toplevel(self.master)
            winDisInfoVerif2.title("Gagal Menjalankan Program")
            winDisInfoVerif2.geometry("350x45")
            winDisInfoVerif2.resizable(False,False)
            
            labelDisInfoVerif2 = Label(winDisInfoVerif2, text='Isi form dengan format yang benar! ')
            labelDisInfoVerif2.pack(padx=5, pady=5)

        elif self.verif1User.replace(" ","").isalpha() and self.verif1Pass.isdigit():
            self.verif3()

    def verif3(self):
        self.verif1User = self.username_entry.get()
        self.verif1Pass = self.password_entry.get()

        with open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Peminjam.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if not row['ID'] == self.verif1Pass and not row['Nama Peminjam'] == self.verif1User:
                    self.check_admin()

                elif row['ID'] == self.verif1Pass and row['Nama Peminjam'] == self.verif1User:
                    self.check_admin()

                elif row['ID'] == self.verif1Pass and not row['Nama Peminjam'] == self.verif1User:
                    winDisInfoVerif3 = Toplevel(self.master)
                    winDisInfoVerif3.title("Akun ada! ")
                    winDisInfoVerif3.geometry("350x45")
                    winDisInfoVerif3.resizable(False,False)
                    
                    labelDisInfoVerif3 = Label(winDisInfoVerif3, text='Nama peminjam salah! ')
                    labelDisInfoVerif3.pack(padx=5, pady=5)

                elif not row['ID'] == self.verif1Pass and row['Nama Peminjam'] == self.verif1User:
                    winDisInfoVerif3 = Toplevel(self.master)
                    winDisInfoVerif3.title("Akun ada! ")
                    winDisInfoVerif3.geometry("350x45")
                    winDisInfoVerif3.resizable(False,False)
                    
                    labelDisInfoVerif3 = Label(winDisInfoVerif3, text='No. telepon salah! ')
                    labelDisInfoVerif3.pack(padx=5, pady=5)

    def set_placeholder(self, entry, placeholder_text):
        entry.insert(0, placeholder_text)
        entry.config(fg='grey')  # Ubah warna teks placeholder (misalnya, abu-abu)

        def on_entry_click(event):
            if entry.get() == placeholder_text:
                entry.delete(0, END)
                entry.config(fg=self.fg_frameLogin)  # Ganti warna teks saat dihapus

        def on_focus_out(event):
            if entry.get() == '':
                entry.insert(0, placeholder_text)
                entry.config(fg='grey')  # Kembalikan ke warna teks placeholder

        entry.bind('<FocusIn>', on_entry_click)
        entry.bind('<FocusOut>', on_focus_out)

    def check_admin(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == 'admin' and password == '021':
            self.show_admin()
        else:
            self.show_public()

    def show_public(self):
        public_window = Toplevel(self.master)
        public = Library(public_window, username=self.username_entry.get(), password=self.password_entry.get())

    def show_admin(self):
        admin_window = Toplevel(self.master)
        admin = Admin(admin_window)

class Admin(LoginForm):

    def __init__(self, master):

        super().__init__(master)
        self.frameLogin.destroy()
        self.master.title("user@Admin Center - Maha Asik")
        self.master.config(bg='#F8E8E3')
        
        self.bg_tabel = '#2F4454'
        self.fieldbg_tabel = '#116466'
        self.fg_tabel = '#66FCF1'
        self.bg_tabel_heading = '#376E6F'
        self.fieldbg_tabel_heading = '#45A29E'
        self.fg_tabel_heading = '#950740'
        self.bgPutih = '#F8E8E3'

        #======================================================
        #================= DATA BUKU ==========================
        #======================================================
        self.data_buku = self.load_csv_data_buku('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Buku_Fix.csv')
        max_id_buku = max(int(book['ID']) for book in self.data_buku) if self.data_buku else 0
        self.id_counter_buku = max_id_buku + 1

        #======================================================
        #================= DATA PEMINJAM ======================
        #======================================================
        self.data_peminjam = self.load_csv_data_peminjam('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Peminjam.csv')
        max_id_peminjam = max(int(peminjam['ID']) for peminjam in self.data_peminjam) if self.data_peminjam else 0
        self.id_counter_peminjam = max_id_peminjam + 1

        #======================================================
        #===================== HEADER =========================
        #======================================================
        self.bg_header = '#1FCEC3'
        self.fg_header = '#2F4454'

        self.header = Frame(master, bg=self.bg_header)
        self.header.place(x=300, y=0, width=1070, height=60)

        logoClose = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\closeon.png').resize((30,30)))
        self.LogoCT = Label(self.header, image=logoClose, bg=self.bg_header)
        self.LogoCT.image = logoClose
        self.LogoCT.place(x=918, y=8)

        self.textCloseTab = Button(self.header, text='Close Tab', bg=self.bg_header, font=('Helvetica', 12, 'bold'), bd=0, fg='#45A29E', cursor='hand2', activebackground=self.bg_header, command=self.default_body)
        self.textCloseTab.place(x=950, y=10)

        self.textAdminCenter = Label(self.header, text='Admin Center', fg=self.fg_header, bg=self.bg_header, bd=0, font=('Javanese Text', 23, 'bold'))
        self.textAdminCenter.place(x=10, y=5)

        #======================================================
        #===================== SIDEBAR ========================
        #======================================================
        self.bg_sidebar = '#F6E6A4'
        self.fg_sidebar = '#45A29E'
        self.fg_button_sidebar = '#45A29E'

        self.sidebar = Frame(master, bg=self.bg_sidebar)
        self.sidebar.place(x=0, y=0, width=300, height=768)

        # DATE AND TIME
        logoDateTime = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\datetime.png').resize((50,50)))
        self.LogoDT = Label(self.sidebar, image=logoDateTime, bg=self.bg_sidebar)
        self.LogoDT.image = logoDateTime
        self.LogoDT.place(x=15, y=680)

        self.textDateTime = Label(self.sidebar)
        self.textDateTime.place(x=65, y=690)
        self.show_time()

        # ICON
        logoimage = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\profiladmin.png').resize((150,150)))
        self.Logo = Label(self.sidebar, image=logoimage, bg=self.bg_sidebar)
        self.Logo.image = logoimage
        self.Logo.place(x=65, y=80)

        # ICON BUTTON
        logoDaftarBuku = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\daftarbuku_off.png').resize((50,50)))
        self.LogoDB = Label(self.sidebar, image=logoDaftarBuku, bg=self.bg_sidebar)
        self.LogoDB.image = logoDaftarBuku
        self.LogoDB.place(x=15, y=275)

        self.textDaftarBuku = Button(self.sidebar, text='Daftar Buku', bg=self.bg_sidebar, fg=self.fg_button_sidebar, font=('Helvetica', 12, 'bold'), bd=0, activebackground=self.bg_sidebar, cursor='hand2', command=self.tabel_daftar_buku)
        self.textDaftarBuku.place(x=76, y=287)

        logoDaftarPeminjam = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\daftarpeminjam_off.png').resize((50,50)))
        self.LogoDP = Label(self.sidebar, image=logoDaftarPeminjam, bg=self.bg_sidebar)
        self.LogoDP.image = logoDaftarPeminjam
        self.LogoDP.place(x=15, y=330)

        self.textDaftarPeminjam = Button(self.sidebar, text='Daftar Peminjam', bg=self.bg_sidebar, fg=self.fg_button_sidebar, font=('Helvetica', 12, 'bold'), bd=0, activebackground=self.bg_sidebar, cursor='hand2', command=self.tabel_daftar_peminjam)
        self.textDaftarPeminjam.place(x=76, y=342)

        logoCariPeminjam = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\caripeminjam.png').resize((50,50)))
        self.LogoCP = Label(self.sidebar, image=logoCariPeminjam, bg=self.bg_sidebar)
        self.LogoCP.image = logoCariPeminjam
        self.LogoCP.place(x=19, y=385)

        self.textCariPeminjam = Button(self.sidebar, text='Cari Peminjam', bg=self.bg_sidebar, fg=self.fg_button_sidebar, font=('Helvetica', 12, 'bold'), bd=0, activebackground=self.bg_sidebar, cursor='hand2', command=self.cari_peminjam)
        self.textCariPeminjam.place(x=76, y=397)

        logoExitAdmin = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\exit_icon.png').resize((50,50)))
        self.LogoEA = Label(self.sidebar, image=logoExitAdmin, bg=self.bg_sidebar)
        self.LogoEA.image = logoExitAdmin
        self.LogoEA.place(x=15, y=605)

        self.textExitAdmin = Button(self.sidebar, text='Exit', bg=self.bg_sidebar, fg='gray', font=('Helvetica', 12, 'bold'), bd=0, activebackground=self.bg_sidebar, cursor='hand2', command=self.master.destroy)
        self.textExitAdmin.place(x=76, y=617)
        
        # NAME
        self.name_admin = Label(self.sidebar, text='admin@mahaasik.sada.23f', bg=self.bg_sidebar, font=("Helvetica", 13, "bold"), fg=self.fg_sidebar, bd=0)
        self.name_admin.place(x=40, y=235)

        #======================================================
        #===================== BODY ===========================
        #======================================================
        self.bg_framebody = '#F8E8E3'
        self.fg_body = '#45A29E'

        self.frameButtonTabel = Frame(master, bg=self.bg_framebody)
        self.frameButtonTabel.place(x=312, y=63, width=1040, height=45)

        self.heading = Label(self.frameButtonTabel, text='Selamat datang di menu administrasi', font=('', 13, 'bold'), fg=self.fg_body, bg=self.bg_framebody)
        self.heading.place(x=0, y=10)

        # BODY FULL
        self.bodyframe = Frame(master, bg=self.bg_framebody)
        self.bodyframe.place(x=312, y=110, width=1040, height=625)

    def default_body(self):
        self.text_body = Label(self.bodyframe, bg='#F8E8E3', width=148, height=42)
        self.text_body.place(relheight=1, relwidth=1)
        self.change_button_color(self.textCloseTab)
        self.LogoUB.place_forget()
        self.textUbahBuku.place_forget()
        self.LogoTB.place_forget()
        self.textTambahBuku.place_forget()
        self.LogoHB.place_forget()
        self.textHapusBuku.place_forget()

    def default_bod1(self):
        self.text_body = Label(self.bodyframe, text='WELCOME', bg='#F8E8E3', width=148, height=42)
        self.text_body.place(x=0, y=0)
        self.change_button_color(self.textCariPeminjam)

    def load_csv_data_buku(self, file_path):
        try:
            with open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Buku_Fix.csv', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
            return data
        except FileNotFoundError:
            return []

    def load_csv_data_peminjam(self, file_path):
        try:
            with open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Peminjam.csv', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
            return data
        except FileNotFoundError:
            return []

    def show_time(self):
        now = datetime.now()
        self.time = now.strftime("%H:%M:%S")
        self.date = now.strftime('%d / %m / %Y')
        set_text = f" {self.time} \n {self.date}"
        self.textDateTime.config(text=set_text, font=('Helvetica', 12, 'bold'), bd=0, bg=self.bg_sidebar, fg=self.fg_sidebar)
        self.textDateTime.after(100, self.show_time)

    def change_button_color(self, active_labels):
        labels = [self.textCloseTab, self.textDaftarBuku, self.textDaftarPeminjam, self.textCariPeminjam]
        
        for label in labels:
            if label == active_labels:
                label.configure(fg='#1E1310')
            else:
                label.configure(fg='#45A29E')

        # CONFIGURE Close Tab on/off
        self.LogoCT_on = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\closeoff.png').resize((30,30)))
        self.LogoCT_off = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\closeon.png').resize((30,30)))

        # CONFIGURE Daftar Buku on/off
        self.LogoDB_on = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\bukabuku.png').resize((50,50)))
        self.LogoDB_off = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\daftarbuku_off.png').resize((50,50)))

        # CONFIGURE Daftar Peminjam on/off
        self.LogoDP_on = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\revisiDaftarPeminjam.png').resize((50,50)))
        self.LogoDP_off = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\daftarpeminjam_off.png').resize((50,50)))

        self.LogoCP_on = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\revisiCariPeminjam.png').resize((50,50)))
        self.LogoCP_off = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\caripeminjam.png').resize((50,50)))

        if active_labels == self.textCloseTab:
            self.LogoCT.configure(image=self.LogoCT_on)
        else:
            self.LogoCT.configure(image=self.LogoCT_off)
        
        if active_labels == self.textDaftarBuku:
            self.LogoDB.configure(image=self.LogoDB_on)
        else:
            self.LogoDB.configure(image=self.LogoDB_off)

        if active_labels == self.textDaftarPeminjam:
            self.LogoDP.configure(image=self.LogoDP_on)
        else:
            self.LogoDP.configure(image=self.LogoDP_off)

        if active_labels == self.textCariPeminjam:
            self.LogoCP.configure(image=self.LogoCP_on)
        else:
            self.LogoCP.configure(image=self.LogoCP_off)

    def tabel_daftar_buku(self):
        self.change_button_color(self.textDaftarBuku)

        self.tabel_frame = Frame(self.bodyframe, bg='#ffce86')
        self.tabel_frame.place(x=0, y=0, width=1040, height=625)
        self.tabel_frame.configure(bg='#a09db2')

        style = ttk.Style()
        style.configure("Treeview", background=self.bg_tabel, fieldbackground=self.fieldbg_tabel, foreground=self.fg_tabel)
        style.configure("Treeview.Heading", background=self.bg_tabel, fieldbackground=self.fieldbg_tabel, foreground=self.fg_tabel_heading)

        columns = ["ID", "Judul", "Nama Pengarang", "Tahun Terbit", "Genre"]
        self.tabel = ttk.Treeview(self.tabel_frame, columns=columns, show='headings')
        self.tabel.configure(height=1000)

        for col in columns:
            self.tabel.heading(col, text=col)
            self.tabel.column(col, anchor='w')

        for book in self.data_buku:
            self.tabel.insert('', END, values=[book[col] for col in columns])

        self.tabel.place(relheight=1, relwidth=1)
        self.button_tabel()

    def button_tabel(self):
        logoUbahBuku = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\ubahbuku.png').resize((50,50)))
        self.LogoUB = Label(self.header, image=logoUbahBuku, bg=self.bg_header)
        self.LogoUB.image = logoUbahBuku
        self.LogoUB.place(x=255, y=3)

        self.textUbahBuku = Button(self.header, text='Ubah Data Buku', bg=self.bg_header, fg='gray', font=('Helvetica', 12, 'bold'), bd=0, activebackground=self.bg_header, cursor='hand2', command=self.ubah_data_buku)
        self.textUbahBuku.place(x=305, y=17)

        logoTambahBuku = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\tambahbuku.png').resize((50,50)))
        self.LogoTB = Label(self.header, image=logoTambahBuku, bg=self.bg_header)
        self.LogoTB.image = logoTambahBuku
        self.LogoTB.place(x=450, y=3)

        self.textTambahBuku = Button(self.header, text='Tambah Buku', bg=self.bg_header, fg='gray', font=('Helvetica', 12, 'bold'), bd=0, activebackground=self.bg_header, cursor='hand2', command=self.tambah_data_buku)
        self.textTambahBuku.place(x=500, y=17)

        logoHapusBuku = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\hapusbuku.png').resize((50,50)))
        self.LogoHB = Label(self.header, image=logoHapusBuku, bg=self.bg_header)
        self.LogoHB.image = logoHapusBuku
        self.LogoHB.place(x=645, y=3)

        self.textHapusBuku = Button(self.header, text='Hapus Buku', bg=self.bg_header, fg='gray', font=('Helvetica', 12, 'bold'), bd=0, activebackground=self.bg_header, cursor='hand2', command=self.hapus_data_buku)
        self.textHapusBuku.place(x=695, y=17)

    def ubah_data_buku(self):
        # self.change_button_color_tabel(self.textUbahBuku)

        selected_item = self.tabel.focus()

        if selected_item:

            self.change_button_color_tabel(self.textUbahBuku)

            selected_data = self.tabel.item(selected_item, 'values')

            popup = Toplevel(self.master)
            popup.title("Ubah Data Buku")
            popup.config(bg=self.bgPutih)
            popup.resizable(False,False)

            label_judul = Label(popup, text="Judul\t\t: ", bg=self.bgPutih)
            label_judul.grid(row=0, column=0, padx=10, pady=5, sticky='w')
            entry_judul = Entry(popup)
            entry_judul.grid(row=0, column=1, padx=10, pady=5)
            entry_judul.insert(0, selected_data[1])  # Mengisi entry dengan data buku yang sudah ada

            label_pengarang = Label(popup, text="Nama Pengarang\t: ", bg=self.bgPutih)
            label_pengarang.grid(row=1, column=0, padx=10, pady=5, sticky='w')
            entry_pengarang = Entry(popup)
            entry_pengarang.grid(row=1, column=1, padx=10, pady=5)
            entry_pengarang.insert(0, selected_data[2])

            label_tahun = Label(popup, text="Tahun Terbit\t: ", bg=self.bgPutih)
            label_tahun.grid(row=2, column=0, padx=10, pady=5, sticky='w')
            entry_tahun = Entry(popup)
            entry_tahun.grid(row=2, column=1, padx=10, pady=5)
            entry_tahun.insert(0, selected_data[3])

            label_genre = Label(popup, text="Genre\t\t: ", bg=self.bgPutih)
            label_genre.grid(row=3, column=0, padx=10, pady=5, sticky='w')
            entry_genre = Entry(popup)
            entry_genre.grid(row=3, column=1, padx=10, pady=5)
            entry_genre.insert(0, selected_data[4])

            def simpan_perubahan():

                new_judul = entry_judul.get()
                new_pengarang = entry_pengarang.get()
                new_tahun = entry_tahun.get()
                new_genre = entry_genre.get()

                try:
                    new_tahun = int(new_tahun)
                except ValueError:
                    winDisInfoUBError = Toplevel(self.master)
                    winDisInfoUBError.title("Format Error")
                    winDisInfoUBError.geometry("350x45")
                    winDisInfoUBError.resizable(False,False)
                    
                    labelDisUBError = Label(winDisInfoUBError, text='Silahkan masukkan format tahun terbit dengan Angka')
                    labelDisUBError.pack(padx=5, pady=5)

                    return

                for book in self.data_buku:
                    if book['ID'] == selected_data[0]:
                        book['Judul'] = new_judul
                        book['Nama Pengarang'] = new_pengarang
                        book['Tahun Terbit'] = new_tahun
                        book['Genre'] = new_genre
                        break

                self.tabel.item(selected_item, values=[selected_data[0], new_judul, new_pengarang, new_tahun, new_genre])
                
                winDisInfoUB = Toplevel(self.master)
                winDisInfoUB.title("Sukses")
                winDisInfoUB.geometry("350x45")
                winDisInfoUB.resizable(False,False)
                
                labelDisUB = Label(winDisInfoUB, text='Data Buku berhasil diubah!')
                labelDisUB.pack(padx=5, pady=5)

                self.simpan_ke_csv()

                popup.destroy()
            
            tombol_simpan = Button(popup, text="Simpan", command=simpan_perubahan)
            tombol_simpan.grid(row=4, column=0, columnspan=2, pady=10)

        else:
            winDisInfoUBGagal = Toplevel(self.master)
            winDisInfoUBGagal.title("Gagal menjalankan program")
            winDisInfoUBGagal.geometry("350x45")
            winDisInfoUBGagal.resizable(False,False)

            labelDisUBGagal = Label(winDisInfoUBGagal, text='Pilihlah data pada tabel terlebih dahulu! ')
            labelDisUBGagal.pack(padx=5, pady=5)
        #     messagebox.showwarning("Peringatan", "Pilih data buku terlebih dahulu.")

    def tambah_data_buku(self):
        self.change_button_color_tabel(self.textTambahBuku)
        self.bg_tambahbuku = '#F6E6A4'

        popup = Toplevel(self.master)
        popup.config(bg=self.bgPutih)
        popup.title("Tambah Data Buku Baru")
        popup.resizable(False,False)

        label_judul = Label(popup, text="Judul\t\t:", bg=self.bgPutih)
        label_judul.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        entry_judul = Entry(popup)
        entry_judul.grid(row=0, column=1, padx=10, pady=5)

        label_pengarang = Label(popup, text="Nama Pengarang\t:", bg=self.bgPutih)
        label_pengarang.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        entry_pengarang = Entry(popup)
        entry_pengarang.grid(row=1, column=1, padx=10, pady=5)

        label_tahun = Label(popup, text="Tahun Terbit\t:", bg=self.bgPutih)
        label_tahun.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        entry_tahun = Entry(popup)
        entry_tahun.grid(row=2, column=1, padx=10, pady=5)

        label_genre = Label(popup, text="Genre\t\t:", bg=self.bgPutih)
        label_genre.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        genre_options = ["Ilmiah (Sains dan Fiksi Ilmiah)", "Horror", "Self-Development", "Roman", "Komedi", "Fiksi", "Non-Fiksi", "Petualangan", "Seni"]
        genre_combobox = ttk.Combobox(popup, values=genre_options)
        genre_combobox.grid(row=3, column=1, padx=10, pady=5)
        genre_combobox.set(genre_options[0])

        def simpan_data_baru():
            judul = entry_judul.get()
            pengarang = entry_pengarang.get()
            tahun_terbit = entry_tahun.get()
            genre = genre_combobox.get()

            try:
                tahun_terbit = int(tahun_terbit)
            except ValueError:
                winDisInfoTBError = Toplevel(self.master)
                winDisInfoTBError.title("Format Error")
                winDisInfoTBError.geometry("350x45")
                winDisInfoTBError.resizable(False,False)
                
                labelDisTBError = Label(winDisInfoTBError, text='Silahkan masukkan format tahun terbit dengan Angka')
                labelDisTBError.pack(padx=5, pady=5)
                return

            new_id = len(self.data_buku) + 1
            new_book = {
                'ID': new_id,
                'Judul': judul,
                'Nama Pengarang': pengarang,
                'Tahun Terbit': tahun_terbit,
                'Genre': genre
            }
            self.data_buku.append(new_book)

            self.tabel.insert('', END, values=[new_book['ID'], new_book['Judul'], new_book['Nama Pengarang'], new_book['Tahun Terbit'], new_book['Genre']])

            self.simpan_ke_csv()

            winDisInfoTB = Toplevel(self.master)
            winDisInfoTB.title("Sukses")
            winDisInfoTB.geometry("350x45")
            winDisInfoTB.resizable(False,False)
            
            labelDisTB = Label(winDisInfoTB, text='Data buku berhasil ditambahkan! ')
            labelDisTB.pack(padx=5, pady=5)
            
            popup.destroy()

        tombol_simpan = Button(popup, text="Simpan", command=simpan_data_baru)
        tombol_simpan.grid(row=4, column=0, columnspan=2, pady=10)

    def hapus_data_buku(self):
        # self.change_button_color_tabel(self.textHapusBuku)

        selected_item = self.tabel.focus()

        if selected_item:
            self.change_button_color_tabel(self.textHapusBuku)
            selected_data = self.tabel.item(selected_item, 'values')

            winHapusData = Toplevel(self.master)
            winHapusData.title("Hapus Data Buku!")
            winHapusData.geometry("350x100")
            winHapusData.resizable(False,False)

            def verifHapusBuku():

                with open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\auditlog.csv', 'a', newline='', encoding='utf-8') as auditlog_file:
                    writer = csv.writer(auditlog_file)
                    writer.writerow(selected_data)
                
                new_data_buku = [book for book in self.data_buku if book['ID'] != selected_data[0]]
                self.data_buku = new_data_buku

                for index, book in enumerate(self.data_buku):
                    book['ID'] = index + 1

                self.tabel.delete(*self.tabel.get_children())
                for book in self.data_buku:
                    self.tabel.insert('', END, values=[book['ID'], book['Judul'], book['Nama Pengarang'], book['Tahun Terbit'], book['Genre']])

                self.simpan_ke_csv()

                winDisInfoHapus = Toplevel(self.master)
                winDisInfoHapus.title("Sukses")
                winDisInfoHapus.geometry("350x45")
                
                labelDisHapusSukses = Label(winDisInfoHapus, text='Data Buku berhasil dihapus')
                labelDisHapusSukses.pack(padx=5, pady=5)

                winHapusData.destroy()

            self.frameHapusBuku = Frame(winHapusData)
            self.frameHapusBuku.pack(padx=5, pady=5)

            self.labelHapusBuku = Label(self.frameHapusBuku, text="Apakah anda yakin ingin menghpus buku ini? ")
            self.labelHapusBuku.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

            self.btnHapusYA = Button(self.frameHapusBuku, text="YA", width=15, command=verifHapusBuku)
            self.btnHapusYA.grid(row=1, column=0, padx=5, pady=5)

            self.btnHapusTIDAK = Button(self.frameHapusBuku, text='TIDAK', width=15, command=winHapusData.destroy)
            self.btnHapusTIDAK.grid(row=1, column=1, padx=5, pady=5)

        else:
            winDisInfoHapusElse = Toplevel(self.master)
            winDisInfoHapusElse.title("Gagal Menjalankan Program")
            winDisInfoHapusElse.geometry("350x45")
            winDisInfoHapusElse.resizable(False,False)
            
            labelDisHapusBatal = Label(winDisInfoHapusElse, text='Pilihlah data pada tabel terlebih dahulu! ')
            labelDisHapusBatal.pack(padx=5, pady=5)

    def simpan_ke_csv(self):
        with open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Buku_Fix.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Judul", "Nama Pengarang", "Tahun Terbit", "Genre"])
            writer.writeheader()
            writer.writerows(self.data_buku)

    def tabel_daftar_peminjam(self):
        self.change_button_color(self.textDaftarPeminjam)

        self.tabel_frame = Frame(self.bodyframe, bg='#ffce86')
        self.tabel_frame.place(x=0, y=0, width=1040, height=625)
        self.tabel_frame.configure(bg='#a09db2')

        self.tabel_header = Label(self.tabel_frame, text='Daftar Buku', font=('', 13, 'bold'), fg='#0064d3', bg='#a09db2')
        self.tabel_header.place(x=20, y=20)

        style = ttk.Style()
        style.configure("Treeview", background="#a09db2", fieldbackground="#eff5f6", foreground='black')

        columns = ["ID", "Nama Peminjam", "Judul Buku", "Tanggal Peminjaman", "Tanggal Pengembalian", "Status", "Denda"]
        self.tabel = ttk.Treeview(self.tabel_frame, columns=columns, show='headings')

        for col in columns:
            self.tabel.heading(col, text=col)
            self.tabel.column(col, anchor=CENTER)

        for book in self.data_peminjam:
            self.tabel.insert('', END, values=[book[col] for col in columns])

        self.tabel.place(relheight=1, relwidth=1)

        self.LogoUB.place_forget()
        self.textUbahBuku.place_forget()
        self.LogoTB.place_forget()
        self.textTambahBuku.place_forget()
        self.LogoHB.place_forget()
        self.textHapusBuku.place_forget()

    def cari_peminjam(self):
        
        self.change_button_color(self.textCariPeminjam)

        popup = Toplevel(self.master)
        popup.title("Cari Data Peminjam")
        popup.resizable(False,False)

        label_id = Label(popup, text="Masukkan ID Peminjam (12 digit):")
        label_id.grid(row=0, column=0, padx=10, pady=5)
        entry_id = Entry(popup)
        entry_id.grid(row=0, column=1, padx=10, pady=5)

        def tampilkan_peminjam():
            id_peminjam = entry_id.get()
            if not id_peminjam.isdigit() or len(id_peminjam) != 12:
                messagebox.showerror("Error", "ID Peminjam harus berupa angka dan memiliki panjang 12 digit.")
                return

            found = False
            for peminjam in self.data_peminjam:
                if peminjam['ID'] == id_peminjam:
                    found = True
                    self.save_peminjam = peminjam
                    self.tampilkan_detail_peminjam(peminjam)
                    break

            if not found:
                messagebox.showinfo("Info", "Data Peminjam tidak ditemukan.")

        tombol_cari = Button(popup, text="Cari", command=tampilkan_peminjam)
        tombol_cari.grid(row=1, column=0, columnspan=2, pady=10)

    def tampilkan_detail_peminjam(self, peminjam):
        popup_detail = Toplevel(self.master)
        popup_detail.title("Detail Peminjam")
        popup_detail.resizable(False,False)

        label_id = Label(popup_detail, text="ID Peminjam\t\t: ")
        label_id.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        label_id_value = Label(popup_detail, text=peminjam['ID'])
        label_id_value.grid(row=0, column=1, padx=10, pady=5)

        label_nama = Label(popup_detail, text="Nama Peminjam\t\t: ")
        label_nama.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        label_nama_value = Label(popup_detail, text=peminjam['Nama Peminjam'])
        label_nama_value.grid(row=1, column=1, padx=10, pady=5)

        label_judul = Label(popup_detail, text="Judul Buku\t\t: ")
        label_judul.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        label_judul_value = Label(popup_detail, text=peminjam['Judul Buku'])
        label_judul_value.grid(row=2, column=1, padx=10, pady=5)

        label_tanggal_peminjam = Label(popup_detail, text="Tanggal Peminjaman\t:")
        label_tanggal_peminjam.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        label_tanggal_peminjam_value = Label(popup_detail, text=peminjam['Tanggal Peminjaman'])
        label_tanggal_peminjam_value.grid(row=3, column=1, padx=10, pady=5)

        label_tanggal_pengembalian = Label(popup_detail, text="Tanggal Pengembalian\t:")
        label_tanggal_pengembalian.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        label_tanggal_pengembalian_value = Label(popup_detail, text=peminjam['Tanggal Pengembalian'])
        label_tanggal_pengembalian_value.grid(row=4, column=1, padx=10, pady=5)

        label_status = Label(popup_detail, text="Status\t\t\t:")
        label_status.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        label_status_value = Label(popup_detail, text=peminjam['Status'])
        label_status_value.grid(row=5, column=1, padx=10, pady=5)

        # tanggal_ditetapkan = datetime.strptime(peminjam['Tanggal Pengembalian'], '%d / %m / %Y')
        # tanggal_pengembalian = datetime.strptime(peminjam['Status'], '%d / %m / %Y')

        # if tanggal_pengembalian > tanggal_ditetapkan:
        #     keterlambatan = (tanggal_pengembalian - tanggal_ditetapkan).days
        #     denda = keterlambatan * 5000
        #     peminjam['Denda'] = denda
        # else:
        #     denda = 0

        label_denda = Label(popup_detail, text="Denda\t\t\t:")
        label_denda.grid(row=6, column=0, padx=10, pady=5, sticky='w')
        label_denda_value = Label(popup_detail, text=peminjam['Denda'])
        label_denda_value.grid(row=6, column=1, padx=10, pady=5)

        button_pengembalian = Button(popup_detail, text="Set Tanggal Pengembalian", command=lambda: self.set_tanggal_pengembalian(peminjam, label_status_value, label_denda_value))
        button_pengembalian.grid(row=7, column=0, columnspan=2, pady=10)

    def set_tanggal_pengembalian(self, peminjam, label_status_value, label_denda_value):
        popup_calendar = Toplevel(self.master)
        popup_calendar.title("Pilih Tanggal Pengembalian")
        popup_calendar.resizable(False,False)

        cal = Calendar(popup_calendar, selectmode="day", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)  # You can set the default date
        cal.pack()

        def set_tanggal():
            selected_date = cal.selection_get().strftime("%d / %m / %Y")
            peminjam['Status'] = selected_date
            label_status_value.config(text=selected_date)
            tanggal_ditetapkan = datetime.strptime(peminjam['Tanggal Pengembalian'], '%d / %m / %Y')
            tanggal_pengembalian = datetime.strptime(peminjam['Status'], '%d / %m / %Y')

            if tanggal_pengembalian > tanggal_ditetapkan:
                keterlambatan = (tanggal_pengembalian - tanggal_ditetapkan).days
                denda = keterlambatan * 5000
                peminjam['Denda'] = denda
            else:
                denda = 0
            label_denda_value.config(text=denda)
            # self.tampilkan_detail_peminjam(peminjam)
            self.simpan_ke_csv_peminjam()
            popup_calendar.destroy()

        button_simpan = Button(popup_calendar, text="Simpan Tanggal", command=set_tanggal)
        button_simpan.pack()

    def simpan_ke_csv_peminjam(self):
        with open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Peminjam.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Nama Peminjam", "Judul Buku", "Tanggal Peminjaman", "Tanggal Pengembalian", "Status", "Denda"])
            writer.writeheader()
            writer.writerows(self.data_peminjam)

    def change_button_color_tabel(self, active_labels):
        labels_tabel = [self.textUbahBuku, self.textTambahBuku, self.textHapusBuku]

        for label in labels_tabel:
            if label == active_labels:
                label.configure(fg='#950740')
            else:
                label.configure(fg='grey')

        self.LogoTB_on = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\revisiTambahBuku.png').resize((50,50)))
        self.LogoTB_off = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\tambahbuku.png').resize((50,50)))

        self.LogoUB_on = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\revisiUbahBuku.png').resize((50,50)))
        self.LogoUB_off = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\ubahbuku.png').resize((50,50)))

        self.LogoHB_on = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\revisiHapusBuku.png').resize((50,50)))
        self.LogoHB_off = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\hapusbuku.png').resize((50,50)))

        if active_labels == self.textTambahBuku:
            self.LogoTB.configure(image=self.LogoTB_on)
        else:
            self.LogoTB.configure(image=self.LogoTB_off)

        if active_labels == self.textUbahBuku:
            self.LogoUB.configure(image=self.LogoUB_on)
        else:
            self.LogoUB.configure(image=self.LogoUB_off)

        if active_labels == self.textHapusBuku:
            self.LogoHB.configure(image=self.LogoHB_on)
        else:
            self.LogoHB.configure(image=self.LogoHB_off)

class Library(LoginForm):

    def __init__(self, master, username, password):
        super().__init__(master)
        self.frameLogin.destroy()
        self.master.title("Public Space - Maha Asik")
        self.master.config(bg='#F8E8E3')
        
        # Penyimpan Variable
        self.save_username = username
        self.save_password = password

        self.bg_tabel = '#2F4454'
        self.fieldbg_tabel = '#116466'
        self.fg_tabel = '#66FCF1'
        self.bg_tabel_heading = '#376E6F'
        self.fieldbg_tabel_heading = '#45A29E'
        self.fg_tabel_heading = '#950740'

        #======================================================
        #================= DATA BUKU ==========================
        #======================================================
        self.data_buku = self.load_csv_data_buku('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Buku_Fix.csv')
        max_id_buku = max(int(book['ID']) for book in self.data_buku) if self.data_buku else 0
        self.id_counter_buku = max_id_buku + 1

        #======================================================
        #================= DATA PEMINJAM ======================
        #======================================================
        self.data_peminjam = self.load_csv_data_peminjam('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Peminjam.csv')
        max_id_peminjam = max(int(peminjam['ID']) for peminjam in self.data_peminjam) if self.data_peminjam else 0
        self.id_counter_peminjam = max_id_peminjam + 1

        #======================================================
        #===================== HEADER =========================
        #======================================================
        self.bg_header = '#1FCEC3'
        self.fg_header = '#2F4454'

        self.header = Frame(master, bg=self.bg_header)
        self.header.place(x=300, y=0, width=1070, height=60)

        logoClose = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\closeon.png').resize((30,30)))
        self.LogoCT = Label(self.header, image=logoClose, bg=self.bg_header)
        self.LogoCT.image = logoClose
        self.LogoCT.place(x=918, y=8)

        self.textCloseTab = Button(self.header, text='Close Tab', bg=self.bg_header, font=('Helvetica', 12, 'bold'), bd=0, fg='#45A29E', cursor='hand2', activebackground=self.bg_header, command=self.default_body)
        self.textCloseTab.place(x=950, y=10)

        self.textAdminCenter = Label(self.header, text='PUBLIC SPACE', fg=self.fg_header, bg=self.bg_header, bd=0, font=('Javanese Text', 23, 'bold'))
        self.textAdminCenter.place(x=10, y=5)

        #======================================================
        #===================== SIDEBAR ========================
        #======================================================
        self.bg_sidebar = '#F6E6A4'
        self.fg_sidebar = '#45A29E'
        self.fg_button_sidebar = '#45A29E'

        self.sidebar = Frame(master, bg=self.bg_sidebar)
        self.sidebar.place(x=0, y=0, width=300, height=768)

        # DATE AND TIME
        logoDateTime = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\datetime.png').resize((50,50)))
        self.LogoDT = Label(self.sidebar, image=logoDateTime, bg=self.bg_sidebar)
        self.LogoDT.image = logoDateTime
        self.LogoDT.place(x=15, y=680)

        self.textDateTime = Label(self.sidebar)
        self.textDateTime.place(x=65, y=690)
        self.show_time()

        # ICON
        logoimage = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\iconpublic.png').resize((150,150)))
        self.Logo = Label(self.sidebar, image=logoimage, bg=self.bg_sidebar)
        self.Logo.image = logoimage
        self.Logo.place(x=65, y=80)

        # ICON BUTTON
        logoDaftarBuku = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\daftarbuku_off.png').resize((50,50)))
        self.LogoDB = Label(self.sidebar, image=logoDaftarBuku, bg=self.bg_sidebar)
        self.LogoDB.image = logoDaftarBuku
        self.LogoDB.place(x=15, y=275)

        self.textDaftarBuku = Button(self.sidebar, text='Daftar Buku', bg=self.bg_sidebar, fg=self.fg_button_sidebar, font=('Helvetica', 12, 'bold'), bd=0, activebackground=self.bg_sidebar, cursor='hand2', command=self.tabel_daftar_buku)
        self.textDaftarBuku.place(x=76, y=287)

        logoStatusPeminjam = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\daftarpeminjam_off.png').resize((50,50)))
        self.LogoSP = Label(self.sidebar, image=logoStatusPeminjam, bg=self.bg_sidebar)
        self.LogoSP.image = logoStatusPeminjam
        self.LogoSP.place(x=15, y=330)

        self.textStatusPeminjam = Button(self.sidebar, text='Status Peminjam', bg=self.bg_sidebar, fg=self.fg_button_sidebar, font=('Helvetica', 12, 'bold'), bd=0, activebackground=self.bg_sidebar, cursor='hand2', command=self.tampilkan_status)
        self.textStatusPeminjam.place(x=76, y=342)

        logoExitAdmin = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\exit_icon.png').resize((50,50)))
        self.LogoEA = Label(self.sidebar, image=logoExitAdmin, bg=self.bg_sidebar)
        self.LogoEA.image = logoExitAdmin
        self.LogoEA.place(x=15, y=605)

        self.textExitAdmin = Button(self.sidebar, text='Exit', bg=self.bg_sidebar, fg='gray', font=('Helvetica', 12, 'bold'), bd=0, activebackground=self.bg_sidebar, cursor='hand2', command=self.master.destroy)
        self.textExitAdmin.place(x=76, y=617)
        
        # NAME
        self.name_admin = Label(self.sidebar, text=f'{self.save_username} ({self.save_password})', bg=self.bg_sidebar, font=("Helvetica", 13, "bold"), fg=self.fg_sidebar, bd=0)
        self.name_admin.place(x=30, y=235)

        #======================================================
        #===================== BODY ===========================
        #======================================================
        self.bg_framebody = '#F8E8E3'
        self.fg_body = '#45A29E'

        self.frameButtonTabel = Frame(master, bg=self.bg_framebody)
        self.frameButtonTabel.place(x=312, y=63, width=1040, height=45)

        self.heading = Label(self.frameButtonTabel, text=f'Selamat datang, {username}', font=('', 13, 'bold'), fg=self.fg_body, bg=self.bg_framebody)
        self.heading.place(x=0, y=10)

        # BODY FULL
        self.bodyframe = Frame(master, bg=self.bg_framebody)
        self.bodyframe.place(x=312, y=110, width=1040, height=625)

    def default_body(self):
        self.text_body = Label(self.bodyframe, bg=self.bg_framebody, width=148, height=42)
        self.text_body.place(relheight=1, relwidth=1)
        self.change_button_color(self.textCloseTab)
        self.LogoPB.place_forget()
        self.textPinjamBuku.place_forget()
        self.textCariBuku.place_forget()
        self.LogoCB.place_forget()

    def default_bod1(self):
        self.text_body = Label(self.bodyframe, text='WELCOME', bg=self.bg_framebody, width=148, height=42)
        self.text_body.place(x=0, y=0)
        self.change_button_color(self.textPengembalianBuku)

    def load_csv_data_buku(self, file_path):
        try:
            with open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Buku_Fix.csv', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
            return data
        except FileNotFoundError:
            return []

    def load_csv_data_peminjam(self, file_path):
        try:
            with open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Peminjam.csv', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
            return data
        except FileNotFoundError:
            return []

    def show_time(self):
        now = datetime.now()
        self.time = now.strftime("%H:%M:%S")
        self.date = now.strftime('%d / %m / %Y')
        set_text = f" {self.time} \n {self.date}"
        self.textDateTime.config(text=set_text, font=('Helvetica', 12, 'bold'), bd=0, bg=self.bg_sidebar, fg=self.fg_sidebar)
        self.textDateTime.after(100, self.show_time)

    def change_button_color(self, active_labels):
        labels = [self.textCloseTab, self.textDaftarBuku]
        
        for label in labels:
            if label == active_labels:
                label.configure(fg='#1E1310')
            else:
                label.configure(fg='#45A29E')

        # CONFIGURE Close Tab on/off
        self.LogoCT_on = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\closeoff.png').resize((30,30)))
        self.LogoCT_off = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\closeon.png').resize((30,30)))

        # CONFIGURE Daftar Buku on/off
        self.LogoDB_on = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\bukabuku.png').resize((50,50)))
        self.LogoDB_off = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\daftarbuku_off.png').resize((50,50)))

        if active_labels == self.textCloseTab:
            self.LogoCT.configure(image=self.LogoCT_on)
        else:
            self.LogoCT.configure(image=self.LogoCT_off)
        
        if active_labels == self.textDaftarBuku:
            self.LogoDB.configure(image=self.LogoDB_on)
        else:
            self.LogoDB.configure(image=self.LogoDB_off)

    def tabel_daftar_buku(self):
        self.change_button_color(self.textDaftarBuku)

        self.tabel_frame = Frame(self.bodyframe, bg='#ffce86')
        self.tabel_frame.place(x=0, y=0, width=1040, height=625)
        self.tabel_frame.configure(bg='#a09db2')

        style = ttk.Style()
        style.configure("Treeview", background=self.bg_tabel, fieldbackground=self.fieldbg_tabel, foreground=self.fg_tabel)
        style.configure("Treeview.Heading", background=self.bg_tabel, fieldbackground=self.fieldbg_tabel, foreground=self.fg_tabel_heading)

        columns = ["ID", "Judul", "Nama Pengarang", "Tahun Terbit", "Genre"]
        self.tabel = ttk.Treeview(self.tabel_frame, columns=columns, show='headings')
        self.tabel.configure(height=1000)

        for col in columns:
            self.tabel.heading(col, text=col)
            self.tabel.column(col, anchor='w')

        for book in self.data_buku:
            self.tabel.insert('', END, values=[book[col] for col in columns])

        self.tabel.place(relheight=1, relwidth=1)
        self.button_tabel()

    def Cari_buku(self, keyword):

        for item in self.tabel.get_children():
            self.tabel.delete(item)

        matching_books = []
        for book in self.data_buku:
            if keyword.lower() in book['Judul'].lower():
                matching_books.append(book)
            elif keyword.lower() in book['Nama Pengarang'].lower():
                matching_books.append(book)
            elif keyword.lower() in book['Tahun Terbit'].lower():
                matching_books.append(book)
            elif keyword.lower() in book['Genre'].lower():
                matching_books.append(book)

        columns = ["ID", "Judul", "Nama Pengarang", "Tahun Terbit", "Genre"]
        for book in matching_books:
            self.tabel.insert('', END, values=[book[col] for col in columns])

            self.tabel.place(relheight=1, relwidth=1)

    def search_book(self):
        wincaribuku = Toplevel(self.master)
        wincaribuku.title("Cari Buku")

        self.search_var = StringVar()
        search_label = ttk.Label(wincaribuku, text="Cari Buku:")
        search_label.grid(row=0, column=0, padx=10, pady=10)
        self.search_entry = ttk.Entry(wincaribuku, textvariable=self.search_var)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)

        search_button = ttk.Button(wincaribuku, text="Cari", command=lambda: self.Cari_buku(self.search_entry.get()))
        search_button.grid(row=0, column=2, padx=10, pady=10)

    def update_treeview(self, dataframe):
        # Menambahkan data ke Treeview
        for row in self.tabel.get_children():
            self.tabel.delete(row)

        # Add data to the Treeview
        for index, row_data in dataframe.iterrows():
            self.tabel.insert("", "end", values=list(row_data))

    def button_tabel(self):
        
        logoPinjamBuku = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\pinjambuku.png').resize((50,50)))
        self.LogoPB = Label(self.header, image=logoPinjamBuku, bg=self.bg_header)
        self.LogoPB.image = logoPinjamBuku
        self.LogoPB.place(x=450, y=3)

        self.textPinjamBuku = Button(self.header, text='Pinjam Buku', bg=self.bg_header, fg='gray', font=('Helvetica', 12, 'bold'), bd=0, activebackground=self.bg_header, cursor='hand2', command=self.pinjam_buku)
        self.textPinjamBuku.place(x=500, y=17)

        logoCariBuku = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\hapusbuku.png').resize((50,50)))
        self.LogoCB = Label(self.header, image=logoCariBuku, bg=self.bg_header)
        self.LogoCB.image = logoCariBuku
        self.LogoCB.place(x=645, y=3)

        self.textCariBuku = Button(self.header, text='Cari Buku', bg=self.bg_header, fg='gray', font=('Helvetica', 12, 'bold'), bd=0, activebackground=self.bg_header, cursor='hand2', command=self.search_book)
        self.textCariBuku.place(x=695, y=17)

    def hitung_tanggal_pengembalian(self, tanggal_peminjaman):
        try:
            # Konversi string tanggal peminjaman ke objek datetime
            tanggal_peminjaman_obj = datetime.strftime(tanggal_peminjaman)
            
            # Hitung tanggal pengembalian (14 hari setelah tanggal peminjaman)
            tanggal_pengembalian_obj = tanggal_peminjaman_obj + timedelta(days=14)
            
            # Konversi objek datetime ke string format yang diinginkan
            tanggal_pengembalian_str = tanggal_pengembalian_obj.strftime("%d / %m / %Y")
            
            return tanggal_pengembalian_str
        except ValueError:
            return None

    def pinjam_buku(self):
        self.infoNama = self.save_username
        self.infoNoTelp = self.save_password
        self.change_button_color_tabel(self.textPinjamBuku)

        selected_item = self.tabel.focus()

        if selected_item:

            selected_data = self.tabel.item(selected_item, 'values')

            windowPinjamBuku = Toplevel(self.master)
            windowPinjamBuku.resizable(False, False)

            self.winPinjamBuku = windowPinjamBuku

            self.framePinjamBuku = Frame(windowPinjamBuku)
            self.framePinjamBuku.pack()

            pinjam = Button(self.framePinjamBuku, text='Pinjam', font=('Helvetica', 12), command=lambda: self.tampilkan_kalender() and windowPinjamBuku.destroy, bg='white')
            pinjam.grid(row=6, column=1, padx=10, pady=10)

            labelNama = Label(self.framePinjamBuku, text="Nama Peminjam\t\t:", font=('Helvetica', 12), fg='black')
            labelNama.grid(row=0, column=0, padx=10, pady=5, sticky='w')
            info_Nama = Label(self.framePinjamBuku, text=f'{self.infoNama}', font=('Helvetica', 12))
            info_Nama.grid(row=0, column=1, padx=10, pady=5)

            labelNoTelp = Label(self.framePinjamBuku, text="No. Telepon\t\t:", font=('Helvetica', 12), fg='black')
            labelNoTelp.grid(row=1, column=0, padx=10, pady=5, sticky='w')
            info_NoTelp = Label(self.framePinjamBuku, text=f'{self.infoNoTelp}', font=('Helvetica', 12))
            info_NoTelp.grid(row=1, column=1, padx=10, pady=5)

            labelJudul = Label(self.framePinjamBuku, text="Judul\t\t\t:", font=('Helvetica', 12), fg='black')
            labelJudul.grid(row=2, column=0, padx=10, pady=5, sticky='w')
            self.judul_var = StringVar()
            entry_judul = Entry(self.framePinjamBuku, textvariable=self.judul_var, font=('Helvetica', 12))
            entry_judul.grid(row=2, column=1, padx=10, pady=5)
            entry_judul.insert(0, selected_data[1])

            labelPengarang = Label(self.framePinjamBuku, text="Nama Pengarang\t\t:", font=('Helvetica', 12), fg='black')
            labelPengarang.grid(row=3, column=0, padx=10, pady=5, sticky='w')
            self.nama_var = StringVar()
            entry_pengarang = Entry(self.framePinjamBuku, textvariable=self.nama_var, font=('Helvetica', 12))
            entry_pengarang.grid(row=3, column=1, padx=10, pady=5)
            entry_pengarang.insert(0, selected_data[2])

            labelTahunTerbit = Label(self.framePinjamBuku, text="Tahun Terbit\t\t:", font=('Helvetica', 12), fg='black')
            labelTahunTerbit.grid(row=4, column=0, padx=10, pady=5, sticky='w')
            self.tahun_var = StringVar()
            entry_tahun = Entry(self.framePinjamBuku, textvariable=self.tahun_var, font=('Helvetica', 12))
            entry_tahun.grid(row=4, column=1, padx=10, pady=5)
            entry_tahun.insert(0, selected_data[3])

            labelGenre = Label(self.framePinjamBuku, text="Genre\t\t\t:", font=('Helvetica', 12), fg='black')
            labelGenre.grid(row=5, column=0, padx=10, pady=5, sticky='w')
            self.genre_var = StringVar()
            entry_genre = Entry(self.framePinjamBuku, textvariable=self.genre_var, font=('Helvetica', 12))
            entry_genre.grid(row=5, column=1, padx=10, pady=5)
            entry_genre.insert(0, selected_data[4])
        else:
            winDisInfoPBGagal = Toplevel(self.master)
            winDisInfoPBGagal.title("Gagal menjalankan program")
            winDisInfoPBGagal.geometry("350x45")
            winDisInfoPBGagal.resizable(False,False)
            labelDisPBGagal = Label(winDisInfoPBGagal, text='Pilihlah data pada tabel terlebih dahulu! ')
            labelDisPBGagal.pack(padx=5,pady=5)
                                 
        # def destroyWinPinjam():
        #     windowPinjamBuku.destroy()

            # windowPinjamBuku.destroy()

    def tampilkan_kalender(self):
        
        jendela_kalender = Toplevel(self.master)
        jendela_kalender.title("Pilih Tanggal")
        jendela_kalender.geometry("300x300+100+100")
        jendela_kalender.config(bg='#1A1A1D')
        kalender = Calendar(jendela_kalender, selectmode="day", date_pattern="yy/mm/dd", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        kalender.pack(padx=10, pady=10)

        def dapatkan_tanggal():
            nama = self.save_username
            noTelp = self.save_password
            judul = self.judul_var.get()
            pengarang = self.nama_var.get()  
            tahun_terbit = self.tahun_var.get()
            genre = self.genre_var.get()

            tanggal_terpilih = kalender.get_date()
            disTanggal = datetime.strptime(tanggal_terpilih, "%y/%m/%d") 
            TanggalInfo = disTanggal.strftime("%d / %m / %Y")

            tanggal_obj = datetime.strptime(tanggal_terpilih, "%y/%m/%d")
            tanggal_baru = tanggal_obj + timedelta(days=14)
            tanggal_baru_str = tanggal_baru.strftime("%d / %m / %Y")

            status = 0
            denda = 0
            
            self.winPinjamBuku.destroy()
            
            windowPeminjam = Toplevel(self.master)
            windowPeminjam.title("Informasi Peminjam")

            self.saveWinPeminjam = windowPeminjam

            headerNama = Label(windowPeminjam, text="Nama Peminjam\t\t:", font=('Helvetica', 12), fg='black')
            headerNama.grid(row=0, column=0, padx=10, pady=5, sticky='w')
            info_Nama = Label(windowPeminjam, text=f'{nama}', font=('Helvetica', 12))
            info_Nama.grid(row=0, column=1, padx=10, pady=5)

            headerNoTelp = Label(windowPeminjam, text="No. Telepon\t\t:", font=('Helvetica', 12), fg='black')
            headerNoTelp.grid(row=1, column=0, padx=10, pady=5, sticky='w')
            infoNoTelp = Label(windowPeminjam, text=f'{noTelp}', font=('Helvetica', 12))
            infoNoTelp.grid(row=1, column=1, padx=10, pady=5)

            headerJudul = Label(windowPeminjam, text="Judul\t\t\t:", font=('Helvetica', 12), fg='black')
            headerJudul.grid(row=2, column=0, padx=10, pady=5, sticky='w')
            infoJudul = Label(windowPeminjam, text=f'{judul}', font=('Helvetica', 12))
            infoJudul.grid(row=2, column=1, padx=10, pady=5)

            headerPengarang = Label(windowPeminjam, text="Nama Pengarang\t\t:", font=('Helvetica', 12), fg='black')
            headerPengarang.grid(row=3, column=0, padx=10, pady=5, sticky='w')
            infoPengarang = Label(windowPeminjam, text=f'{pengarang}', font=('Helvetica', 12))
            infoPengarang.grid(row=3, column=1, padx=10, pady=5)
            
            headerTahunTerbit = Label(windowPeminjam, text="Tahun Terbit\t\t:", font=('Helvetica', 12), fg='black')
            headerTahunTerbit.grid(row=4, column=0, padx=10, pady=5, sticky='w')
            infoTahun = Label(windowPeminjam, text=f'{tahun_terbit}', font=('Helvetica', 12))
            infoTahun.grid(row=4, column=1, padx=10, pady=5)
            
            headerGenre = Label(windowPeminjam, text="Genre\t\t\t:", font=('Helvetica', 12), fg='black')
            headerGenre.grid(row=5, column=0, padx=10, pady=5, sticky='w')
            infoGenre = Label(windowPeminjam, text=f'{genre}', font=('Helvetica', 12))
            infoGenre.grid(row=5, column=1, padx=10, pady=5)

            headerTanggalPeminjaman = Label(windowPeminjam, text="Tanggal Peminjaman\t:", font=('Helvetica', 12), fg='black')
            headerTanggalPeminjaman.grid(row=6, column=0, padx=10, pady=5, sticky='w')
            infoTanggalPeminjaman = Label(windowPeminjam, text=f'{TanggalInfo}', font=('Helvetica', 12))
            infoTanggalPeminjaman.grid(row=6, column=1, padx=10, pady=5)

            headerTanggalTetap = Label(windowPeminjam, text="Harus dikembalikan sebelum\t:", font=('Helvetica', 12), fg='black')
            headerTanggalTetap.grid(row=7, column=0, padx=10, pady=5, sticky='w')
            infoTanggalTetap = Label(windowPeminjam, text=f'{tanggal_baru_str}', font=('Helvetica', 12))
            infoTanggalTetap.grid(row=7, column=1, padx=10, pady=10)

            buttonVerif = Button(windowPeminjam, text='Pinjam', command=self.verif_peminjam)
            buttonVerif.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

            self.save_csv_peminjam(noTelp, nama, judul, TanggalInfo, tanggal_baru_str, status, denda)
            
            jendela_kalender.destroy()
            
            return tanggal_terpilih

        tombol_pilih = Button(jendela_kalender, text="Pilih Tanggal", command=dapatkan_tanggal, bg='#66FCF1')
        tombol_pilih.pack(pady=10)

        jendela_kalender.mainloop()

    def verif_peminjam(self):
        winVerifPeminjam = Toplevel(self.master)
        winVerifPeminjam.title("Verifikasi Peminjaman")

        self.saveWinVerifPeminjam = winVerifPeminjam

        labelVerifPeminjam = Label(winVerifPeminjam, text="Apakah anda yakin ingin meminjam buku ini? ", font=('Helvetica', 12))
        labelVerifPeminjam.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        buttonYaVerifPeminjam = Button(winVerifPeminjam, text="Ya", width=20, command=self.hapus_data_buku_peminjam)
        buttonYaVerifPeminjam.grid(row=1, column=0, padx=10, pady=10)

        buttonNoVerifPeminjam = Button(winVerifPeminjam, text="Tidak", width=20)
        buttonNoVerifPeminjam.grid(row=1, column=1, padx=10, pady=10)

    def show_succes(self):
        winShowSucces = Toplevel(self.master)
        winShowSucces.title("Sukses!")
        winShowSucces.resizable(False,False)
        winShowSucces.geometry('350x300')

        labelShowSuccess = Label(winShowSucces, text='Buku anda telah berhasil dipinjam! ')
        labelShowSuccess.grid(row=1, column=0, padx=10, pady=10)

        self.saveWinVerifPeminjam.destroy()
        if hasattr(self, 'saveWinPeminjam') and self.saveWinPeminjam:
            self.saveWinPeminjam.destroy()

    def save_csv_peminjam(self, noTelp, nama, judul, TanggalInfo, tanggal_baru_str, status, denda):
        file_path = 'C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Peminjam.csv'
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([noTelp, nama, judul, TanggalInfo, tanggal_baru_str, status, denda])

    def hapus_data_buku_peminjam(self):
        selected_item = self.tabel.focus()
        selected_data = self.tabel.item(selected_item, 'values')

        with open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\auditlog.csv', 'a', newline='', encoding='utf-8') as auditlog_file:
                    writer = csv.writer(auditlog_file)
                    writer.writerow(selected_data)

        new_data_buku = [book for book in self.data_buku if book['ID'] != selected_data[0]]
        self.data_buku = new_data_buku

        for index, book in enumerate(self.data_buku):
            book['ID'] = index + 1

        self.tabel.delete(*self.tabel.get_children())
        for book in self.data_buku:
            self.tabel.insert('', END, values=[book['ID'], book['Judul'], book['Nama Pengarang'], book['Tahun Terbit'], book['Genre']])

        self.show_succes()
        self.simpan_ke_csv()

    def simpan_ke_csv(self):
        with open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\Data Buku_Fix.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Judul", "Nama Pengarang", "Tahun Terbit", "Genre"])
            writer.writeheader()
            writer.writerows(self.data_buku)

    def tabel_daftar_peminjam(self):
        self.change_button_color(self.textDaftarPeminjam)

        self.tabel_frame = Frame(self.bodyframe, bg='#ffce86')
        self.tabel_frame.place(x=0, y=0, width=1040, height=625)
        self.tabel_frame.configure(bg='#a09db2')

        self.tabel_header = Label(self.tabel_frame, text='Daftar Buku', font=('', 13, 'bold'), fg='#0064d3', bg='#a09db2')
        self.tabel_header.place(x=20, y=20)

        style = ttk.Style()
        style.configure("Treeview", background="#a09db2", fieldbackground="#eff5f6", foreground='black')

        columns = ["ID", "Nama Peminjam", "Judul Buku", "Tanggal Peminjaman", "Tanggal Pengembalian", "Status", "Denda"]
        self.tabel = ttk.Treeview(self.tabel_frame, columns=columns, show='headings')

        for col in columns:
            self.tabel.heading(col, text=col)
            self.tabel.column(col, anchor=CENTER)

        for book in self.data_peminjam:
            self.tabel.insert('', END, values=[book[col] for col in columns])

        self.tabel.place(relheight=1, relwidth=1)

        self.LogoPB.place_forget()
        self.textPinjamBuku.place_forget()

    def tampilkan_status(self):
        idDicari = self.save_password
        found = False

        for peminjam in self.data_peminjam:
            if peminjam['ID'] == idDicari:
                found = True
                self.tampilkan_status_peminjam(peminjam)
                self.tabel_frame.destroy()
                self.LogoPB.place_forget()
                self.textPinjamBuku.place_forget()
                self.LogoCB.place_forget()
                self.textCariBuku.place_forget()
                break

        if not found:
            winDisInfoStatus = Toplevel(self.master)
            winDisInfoStatus.title("Gagal menjalankan program! ")
            winDisInfoStatus.geometry("350x45")
            winDisInfoStatus.resizable(False,False)
            
            labelDisInfoStatus = Label(winDisInfoStatus, text='Akun ini belum meminjam buku! ')
            labelDisInfoStatus.pack(padx=5, pady=5)

    def tampilkan_status_peminjam(self, peminjam):
        self.frameStatus = Frame(self.bodyframe)
        self.frameStatus.place(relheight=1, relwidth=1)

        label_id = Label(self.frameStatus, text="ID Peminjam\t\t\t\t: ")
        label_id.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        label_id_value = Label(self.frameStatus, text=peminjam['ID'])
        label_id_value.grid(row=0, column=1, padx=10, pady=5)

        label_nama = Label(self.frameStatus, text="Nama Peminjam\t\t\t\t: ")
        label_nama.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        label_nama_value = Label(self.frameStatus, text=peminjam['Nama Peminjam'])
        label_nama_value.grid(row=1, column=1, padx=10, pady=5)

        label_judul = Label(self.frameStatus, text="Judul Buku\t\t\t\t: ")
        label_judul.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        label_judul_value = Label(self.frameStatus, text=peminjam['Judul Buku'])
        label_judul_value.grid(row=2, column=1, padx=10, pady=5)

        label_tanggal_peminjam = Label(self.frameStatus, text="Tanggal Peminjaman\t\t\t:")
        label_tanggal_peminjam.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        label_tanggal_peminjam_value = Label(self.frameStatus, text=peminjam['Tanggal Peminjaman'])
        label_tanggal_peminjam_value.grid(row=3, column=1, padx=10, pady=5)

        label_tanggal_pengembalian = Label(self.frameStatus, text="Harus dikembalikan pada tanggal\t\t:")
        label_tanggal_pengembalian.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        label_tanggal_pengembalian_value = Label(self.frameStatus, text=peminjam['Tanggal Pengembalian'])
        label_tanggal_pengembalian_value.grid(row=4, column=1, padx=10, pady=5)

        label_status = Label(self.frameStatus, text="Tanggal Pengembalian\t\t\t:")
        label_status.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        label_status_value = Label(self.frameStatus, text=peminjam['Status'])
        label_status_value.grid(row=5, column=1, padx=10, pady=5)

        label_denda = Label(self.frameStatus, text="Denda\t\t\t\t\t:")
        label_denda.grid(row=6, column=0, padx=10, pady=5, sticky='w')
        label_denda_value = Label(self.frameStatus, text=peminjam['Denda'])
        label_denda_value.grid(row=6, column=1, padx=10, pady=5)

    def change_button_color_tabel(self, active_labels):
        labels_tabel = [self.textPinjamBuku]

        for label in labels_tabel:
            if label == active_labels:
                label.configure(fg='#950740')
            else:
                label.configure(fg='grey')

        self.LogoPB_on = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\pinjambuku_on.png').resize((50,50)))
        self.LogoPB_off = ImageTk.PhotoImage(Image.open('C:\\Users\\danisa\\OneDrive\\ドキュメント\\learning\\projek\\pinjambuku.png').resize((50,50)))

        if active_labels == self.textPinjamBuku:
            self.LogoPB.configure(image=self.LogoPB_on)
        else:
            self.LogoPB.configure(image=self.LogoPB_off)

window = Tk()
Login = LoginForm(window)
window.mainloop()