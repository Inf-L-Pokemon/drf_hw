# DRF HW

DRF HW - это проект на Django REST Framework (DRF), в котором каждый желающий может
разместить свои полезные материалы или курсы.

## Установка приложения

1. Клонируйте репозиторий на ваш локальный компьютер, введя в консоль команду:    

`git clone https://github.com/Inf-L-Pokemon/drf_hw`     

*Убедитесь, что у вас установлен [***Git***](https://git-scm.com/) на вашем компьютере.   
Это можно проверить введя команду `git --version` в консоли.  
Если [***Git***](https://git-scm.com/) установлен - появится номер установленной версии, в обратном случае - 
перейдите по ссылке и выполните установку.*

2. Заполните файл `.env_example`, находящийся в корневой папке проекта и переименуйте его в `.env`.     


3. Установите [**Docker Desktop**](https://www.docker.com/), перейдя по ссылке. Находясь в корневой папке проекта, 
введите в консоли команду:  

`docker-compose up -d --build`


4. Перейдите в своём браузере по адресу http://127.0.0.1:8000/redoc/ или http://127.0.0.1:8000/swagger/ для ознакомления
с API документацией.


5. Для остановки запущенного контейнера введите в консоли команду:  

`docker-compose stop`