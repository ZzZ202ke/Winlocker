# 🏴‍☠️ Winlocker Simulation with Math Unlock

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Tkinter-GUI-green?style=flat&logo=tkinter&logoColor=white" alt="Tkinter">
  <img src="https://img.shields.io/badge/License-Educational-yellow?style=flat" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows-orange?style=flat&logo=windows&logoColor=white" alt="Platform">
</p>

<img src="https://github.com/ZzZ202ke/Winlocker/blob/main/Screenshot%202026-05-19%20195301.png" width="1500">

> ⚠️ **ВНИМАНИЕ**: Проект создан строго в образовательных целях и для легитимного тестирования систем безопасности. Автор не несет ответственности за вред, причиненный использованием данного кода.

---

## 🔑 Особенности

| Фича | Описание |
|------|----------|
| **Math Unlock** | Динамическая генерация математических примеров (сложение/вычитание двузначных чисел) |
| **Полноэкранный UI** | Перекрытие всех окон с кастомным курсором (пиратский флаг) |
| **Anti-Close** | Блокировка системных комбинаций + отключение Диспетчера задач |
| **UAC Admin** | Автоматический запрос повышенных привилегий |
| **System Monitor** | Real-time отображение CPU/RAM через `psutil` |
| **Audio Background** | Фоновое воспроизведение аудио в отдельном процессе |

---

## 🛠️ Технологический стек

```
┌─────────────────────────────────────────────────────────┐
│  Python 3.x                                             │
│     ├── Tkinter      (GUI)                              │
│     ├── ctypes       (Win32 API)                        │
│     ├── winreg       (Registry)                         │
│     ├── keyboard     (Input hook)                       │
│     ├── psutil       (System monitor)                   │
│     └── playsound    (Audio)                            │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Быстрый старт

```bash
# Клонирование
git clone https://github.com/ваш-репозиторий/winlocker.git
cd winlocker

# Установка зависимостей
pip install keyboard psutil playsound

# Запуск (требует права администратора)
python main.py
```

> 💡 **Рекомендация**: Запускайте в виртуальной машине или Sandbox!

---

## ⚙️ Сборка в .exe

```bash
# Установка pyinstaller
pip install pyinstaller

# Компиляция
pyinstaller --onefile --noconsole --uac-admin main.py
```

| Параметр | Назначение |
|----------|------------|
| `--onefile` | Один .exe файл |
| `--noconsole` | Без консольного окна |
| `--uac-admin` | Требовать права админа |

📂 Результат: `dist/main.exe`

> ⚠️ **Важно**: Антивирусы могут реагировать на .exe из-за keyboard hook и работы с реестром.

---

## 📁 Архитектура

| Функция | Назначение |
|---------|------------|
| `generate_math_problem()` | Генерация случайных примеров и ответов |
| `set_registry_settings()` | Управление `DisableTaskMgr` и автозагрузкой |
| `block_keys()` | Перехват клавиатуры (только цифры + Backspace) |
| `window()` | Главный цикл Tkinter + UI блокировка |

---
