import tkinter as tk
import os
from tkinter import messagebox

window = tk.Tk()
window.geometry("900x600")
window.title("Устройства")

mainmenu = tk.Menu(window)
window.config(menu=mainmenu)

image_folder = "images"

def load_image_tk(device_name):
    file_names = {
        "Камера": ["camera.png", "camera.jpg"],
        "Сервопривод": ["servo.png", "servo.jpg"],
        "Датчик движения": ["sensor.png", "sensor.jpg"],
        "Термометр": ["thermometer.png", "thermometer.jpg"]
    }

    for filename in file_names[device_name]:
        path = os.path.join(image_folder, filename)
        if os.path.exists(path):
            try:
                photo = tk.PhotoImage(file=path)
                photo = photo.subsample(5, 5)
                return photo
            except:
                continue
    return None

def show_image_in_window(device):
    image_window = tk.Toplevel(window)
    image_window.title(f"Изображение: {device}")
    image_window.geometry("300x300")

    photo = load_image_tk(device)

    if photo:
        img_label = tk.Label(image_window, image=photo)
        img_label.image = photo
        img_label.pack(pady=20)
    else:
        no_image_label = tk.Label(image_window, text=f"Нет изображения: {device}", font=("Arial", 12))
        no_image_label.pack(pady=50)

    close_btn = tk.Button(image_window, text="Закрыть", command=image_window.destroy)
    close_btn.pack(pady=10)

def show_specs(device):
    specs_window = tk.Toplevel(window)
    specs_window.title(f"Характеристики: {device}")
    specs_window.geometry("400x300")

    text_widget = tk.Text(specs_window, font=("Arial", 12), wrap=tk.WORD, padx=10, pady=10)
    text_widget.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    if device == "Камера":
        specs_text = """ХАРАКТЕРИСТИКИ КАМЕРЫ:

Разрешение: 1920x1080
Тип: USB
Угол обзора: 120°"""
    elif device == "Сервопривод":
        specs_text = """ХАРАКТЕРИСТИКИ СЕРВОПРИВОДА:

Модель: SG90
Напряжение: 5V
Вращение: 0-180°"""
    elif device == "Датчик движения":
        specs_text = """ХАРАКТЕРИСТИКИ ДАТЧИКА:

Тип: PIR
Дальность: 7м
Угол: 110°"""
    else:
        specs_text = """ХАРАКТЕРИСТИКИ ТЕРМОМЕТРА:

Модель: DHT22
Температура: -40°C до 80°C
Влажность: 0-100%"""

    text_widget.insert(1.0, specs_text)
    text_widget.config(state=tk.DISABLED)

    close_btn = tk.Button(specs_window, text="Закрыть", command=specs_window.destroy)
    close_btn.pack(pady=10)


def show_camera_photo():
    messagebox.showinfo("Камера", "Фотография показана")

def process_camera_photo():
    messagebox.showinfo("Камера", "Фотография обработана")

def rotate_servo_0():
    messagebox.showinfo("Сервопривод", "Повернут на 0 градусов")

def rotate_servo_180():
    messagebox.showinfo("Сервопривод", "Повернут на 180 градусов")

def enable_motion_sensor():
    messagebox.showinfo("Датчик движения", "Датчик включен")

def disable_motion_sensor():
    messagebox.showinfo("Датчик движения", "Датчик выключен")

def show_humidity():
    messagebox.showinfo("Термометр", "Влажность: 45%")

def show_temperature():
    messagebox.showinfo("Термометр", "Температура: 22°C")

filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход", command=window.quit)

imgmenu = tk.Menu(mainmenu, tearoff=0)
imgmenu.add_command(label="Камера", command=lambda: show_image_in_window("Камера"))
imgmenu.add_command(label="Сервопривод", command=lambda: show_image_in_window("Сервопривод"))
imgmenu.add_command(label="Датчик движения", command=lambda: show_image_in_window("Датчик движения"))
imgmenu.add_command(label="Термометр", command=lambda: show_image_in_window("Термометр"))

harkamenu = tk.Menu(mainmenu, tearoff=0)
harkamenu.add_command(label="Камера", command=lambda: show_specs("Камера"))
harkamenu.add_command(label="Сервопривод", command=lambda: show_specs("Сервопривод"))
harkamenu.add_command(label="Датчик движения", command=lambda: show_specs("Датчик движения"))
harkamenu.add_command(label="Термометр", command=lambda: show_specs("Термометр"))

funcmenu = tk.Menu(mainmenu, tearoff=0)

cam = tk.Menu(mainmenu, tearoff=0)
cam.add_command(label="Показ фотографии", command=show_camera_photo)
cam.add_command(label="Обработка фото", command=process_camera_photo)

servo = tk.Menu(mainmenu, tearoff=0)
servo.add_command(label="Повернуть на 0 градусов", command=rotate_servo_0)
servo.add_command(label="Повернуть на 180 градусов", command=rotate_servo_180)

dd = tk.Menu(mainmenu, tearoff=0)
dd.add_command(label="Включить датчик", command=enable_motion_sensor)
dd.add_command(label="Выключить датчик", command=disable_motion_sensor)

term = tk.Menu(mainmenu, tearoff=0)
term.add_command(label="Показать влажность", command=show_humidity)
term.add_command(label="Показать температуру", command=show_temperature)

funcmenu.add_cascade(label="Камера", menu=cam)
funcmenu.add_cascade(label="Сервопривод", menu=servo)
funcmenu.add_cascade(label="Датчик движения", menu=dd)
funcmenu.add_cascade(label="Термометр", menu=term)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Изображение", menu=imgmenu)
mainmenu.add_cascade(label="Характеристика", menu=harkamenu)
mainmenu.add_cascade(label="Функции", menu=funcmenu)

info_label = tk.Label(window, text="Выберите пункт меню", font=("Arial", 14))
info_label.pack(pady=50)

window.mainloop()