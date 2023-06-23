import random
import string
import time
import tkinter as tk
from PIL import Image, ImageTk
from colorama import init, Fore

init()

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def add_status_to_link(link):
    if random.random() < 0.0001:  # Peluang 0.01% untuk "[working]"
        status = f"{Fore.GREEN}[working]{Fore.RESET}"
    else:
        status = f"{Fore.RED}[not working]{Fore.RESET}"
    return f"{status} {link}"

def generate_nitro_codes():
    num_links = int(entry_num_links.get())  # Jumlah kode yang ingin digenerate
    output_file = "output.txt"
    
    password = entry_password.get()  # Mengambil input password
    
    # Periksa apakah password sesuai dengan yang diharapkan
    if password != "mysecretpassword":
        print("Password salah!")
        return
    
    with open(output_file, "a") as file:
        for _ in range(num_links):
            random_string = generate_random_string(16)
            link = "https://discord.gift/" + random_string
            link_with_status = add_status_to_link(link)
            print(link_with_status)
            if "[working]" in link_with_status:
                file.write(link_with_status + "\n")

            # Delay selama 1 detik
            time.sleep(1)

def change_background_color():
    global entry_color  # Menjadikan entry_color sebagai variabel global
    color = entry_color.get()
    window.configure(background=color)

def open_discord_invite():
    import webbrowser
    webbrowser.open("https://discord.gg/tCmmHMFY")

def open_settings():
    settings_window = tk.Toplevel(window)
    settings_window.title("Settings")
    settings_window.geometry("300x200")

    label_settings = tk.Label(settings_window, text="Pengaturan", font=("Helvetica", 14, "bold"))
    label_settings.pack(pady=10)

    label_color = tk.Label(settings_window, text="Warna Latar Belakang:")
    label_color.pack()
    entry_color = tk.Entry(settings_window)
    entry_color.pack()

    button_change_color = tk.Button(settings_window, text="Ubah Warna", command=change_background_color)
    button_change_color.pack(pady=10)

    button_invite = tk.Button(settings_window, text="Invite Server Discord", command=open_discord_invite)
    button_invite.pack(pady=10)

window = tk.Tk()
window.title("Nitro Generator")
window.geometry("400x400")  # Mengatur ukuran jendela

label_title = tk.Label(window, text="Nitro Generator", font=("Helvetica", 16, "bold"))
label_title.pack(pady=10)

label_by = tk.Label(window, text="By: FaithzZ#0001", font=("Helvetica", 10, "italic"))
label_by.pack()

discord_image = Image.open("dc.jpg")  # Ganti dengan path ke gambar Discord Anda
discord_image = discord_image.resize((100, 100))  # Sesuaikan ukuran gambar
discord_image = ImageTk.PhotoImage(discord_image)

label_discord = tk.Label(window, image=discord_image)
label_discord.pack()

label_num_links = tk.Label(window, text="Jumlah Nitro Codes:")
label_num_links.pack()
entry_num_links = tk.Entry(window)
entry_num_links.pack()

label_password = tk.Label(window, text="Password:")
label_password.pack()
entry_password = tk.Entry(window, show="*")  # Menggunakan show="*" untuk menyembunyikan karakter password
entry_password.pack()

button_generate = tk.Button(window, text="Generate", command=generate_nitro_codes)
button_generate.pack(pady=10)

settings_image = Image.open("st.png")  # Ganti dengan path ke gambar ikon pengaturan Anda
settings_image = settings_image.resize((30, 30))  # Sesuaikan ukuran gambar ikon pengaturan
settings_image = ImageTk.PhotoImage(settings_image)

button_settings = tk.Button(window, image=settings_image, command=open_settings)
button_settings.place(x=370, y=370)

window.mainloop()
