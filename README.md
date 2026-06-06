# 🏴‍☠️ Winlocker Simulation with Math Unlock

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Tkinter-GUI-green?style=flat&logo=tkinter&logoColor=white" alt="Tkinter">
  <img src="https://img.shields.io/badge/License-Educational-yellow?style=flat" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows-orange?style=flat&logo=windows&logoColor=white" alt="Platform">
</p>

<img src="https://github.com/ZzZ202ke/Winlocker/blob/main/image.png" width="1500">

🎓 Программа разработана в рамках выполнения индивидуального проекта на 1 курсе. Создана исключительно для того чтобы не отчислили.

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
│  Python 3.14                                             │
│     ├── Tkinter      (GUI)                              │
│     ├── ctypes       (Win32 API)                        │
│     ├── winreg       (Registry)                         │
│     ├── keyboard     (Input hook)                       │
│     ├── psutil       (System monitor)                   │
│     └── playsound    (Audio)                            │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Архитектура

| Функция | Назначение |
|---------|------------|
| `generate_math_problem()` | Генерация случайных примеров и ответов |
| `set_registry_settings()` | Управление `DisableTaskMgr` и автозагрузкой |
| `block_keys()` | Перехват клавиатуры (только цифры + Backspace) |
| `window()` | Главный цикл Tkinter + UI блокировка |
