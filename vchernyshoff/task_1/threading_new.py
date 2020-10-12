"""1. Threading - это многопоточность
все скрипты в привычном исполняются команда за командой. Тут же попытка реализовать задачи в 2 потока, т.е. выполнять
вторую задачу, не дожидаясь окончания первой
    На самом деле, сам пайтон не может юзать несколько процессоров по причине наличия механизма GIL - global unterpreter
 lock. Но есть multiThreading, который позволяет использовать разные файлы скриптов на разные ядра.
 Под капотом питон просто быстро переключается между задачами, выделяя сколько-то процессорного времени каждому потоку.
 Где такое надо спользовать: в тех случаях, когда задача ждет сигнала на исполнение, но может быть запущена сразу. Это
 позволит ускорить выполнение двух задач.

 threading.active_count() - количество активных
  threading.enumerate() - список всех активных

 threading.current_thread() - текущий поток
 threading.main_thread() - основной (из него все)

 thread.join()

Все расскажу словами и покажу
 """

# картинка 12Мб - http://www.etomesto.ru/map/base/21/yadrinskiy-uezd-1913.jpg


from threading import Thread
import threading
import requests
import time

# image_url = 'http://www.etomesto.ru/map/base/21/yadrinskiy-uezd-1913.jpg' # 12Mb
# image_url = 'https://storge.pic2.me/download/origin/208299.jpeg' # 6 Mb
image_url = 'https://storge.pic2.me/download/origin/5689.jpeg' # 6 Mb


def download_image_with_i_name(index):
    index += 1
    image = requests.get(image_url)
    # os.system(f'touch ~/Python/tech_leaders/education/vchernyshoff/task_1/files_with_no_threading/file{index}.jpg')
    file = open(f'images/file{index}.jpg', 'wb')
    file.write(image.content)
    file.close()
    print(f'скачал картинку {index}')


def get_with_no_threading():
    for i in range(100):
        download_image_with_i_name(i)


def get_with_threading():
    for i in range(100):
        thr = Thread(target=download_image_with_i_name, args=(i, ))
        thr.start()
    while threading.active_count() > 2:
        pass
    print('осталась последняя картинка')


def main():

    # get_with_no_threading()


    get_with_threading()





start_time = time.time()

main()

print('Время в секундах: ' + format(time.time() - start_time))




