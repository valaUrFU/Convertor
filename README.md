# Конвертер чисел

Этот проект представляет собой конвертер чисел, который может преобразовывать числа из десятичной системы счисления в другую систему счисления и обратно.

## Файлы

- `Convertor.py`: Этот файл содержит две основные функции - `convert_from_decimal` и `convert_to_decimal`. Функция `convert_from_decimal` преобразует число из десятичной системы счисления в другую, а функция `convert_to_decimal` преобразует число из любой системы счисления в десятичную.

- `TestConvert.py`: Этот файл содержит тесты для функций в `Convertor.py`. Он использует модуль `unittest` для написания и выполнения тестов.

# Использование

## Ubuntu
Для использования этого проекта вам потребуется Python 3.9. Вы можете установить его на ubuntu, используя следующую команду:

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9
```

Убедитесь, что установка прошла успешно:

```bash
python3.9 --version
```

## Запуск тестов на Ubuntu
После установки `python 3.9` вы можете запустить тесты из директории с проектом, используя следующую команду:

```bash
python -m unittest discover
```
## Windows
Для использования этого проекта вам потребуется Python 3.9. Вы можете установить его на Windows, 
используя следующую инструкцию:

1. Перейдите на [официальный сайт Python](https://www.python.org/)
2. Нажмите на "Downloads" в верхнем меню
3. Нажмите на кнопку "Download Python 3.9" для загрузки Python 3.9. Ваш браузер автоматически загрузит установщик Python для Windows
4. Запустите загруженный файл. Это запустит установщик Python
5. В установщике выберите опцию "Add Python 3.9 to PATH", а затем нажмите "Install Now"
6. Установщик Python установит Python 3.9 и его библиотеки. После завершения установки нажмите на кнопку "Close"
7. Теперь вы можете проверить установку Python, открыв командную строку (нажмите Win+R, введите `cmd` и нажмите Enter) и введя команду `python --version`.
Это должно показать установленную версию Python 3.9
 
## Запуск тестов на Windows
1. Откройте командную строку (нажмите Win+R, введите `cmd` и нажмите Enter)
2. Перейдите в каталог вашего проекта с помощью команды `cd` например: <br /> `cd C:\Users\YourUsername\Path\To\Your\Project`
3. Запустите тесты, используя команду `python -m unittest discover`

## Копирование кода в проект
Также можно копировать функции из Convertor.py или импортировать файл в ваш проект: <br />
***Важно: для импорта функций необходимо сохранить файл в ваш проект!***

```python
from Convertor import convert_from_decimal, convert_to_decimal
```
# GitHub Actions
В этом проекте используется GitHub Actions для автоматического тестирования кода по файлу `TestConvert.py` при каждом push.
Он также проверяет код на соответствие стандартам PEP8 с помощью flake8.
Вы можете посмотреть файл конфигурации `.github/workflows/python-tests.yml` для получения дополнительной информации.

[![Python application test with unittest](https://github.com/valaUrFU/Convertor/actions/workflows/python-tests.yml/badge.svg)](https://github.com/valaUrFU/Convertor/actions/workflows/python-tests.yml)
