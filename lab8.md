
Лабораторная работа №8
Установка WSL и выполнение базовых команд Linux
Цель работы

Изучить процесс установки Windows Subsystem for Linux (WSL), установить дистрибутив Linux и освоить базовые команды работы с файловой системой Linux.

Ход выполнения работы
Установка WSL

Открыт PowerShell с правами администратора.

Выполнена команда включения подсистемы Linux:

dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart


Включена поддержка виртуальной машины:

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart


Выполнена перезагрузка компьютера.

Из Microsoft Store установлен дистрибутив Ubuntu.

При первом запуске создан пользователь и пароль.

Работа с файловой системой Linux

Создание рабочей директории:

mkdir ~/LabWork


Переход в директорию:

cd ~/LabWork


Создание файла и запись текста:

echo "Hello, World!" > example.txt


Копирование файла:

cp example.txt copy_example.txt


Переименование файла:

mv copy_example.txt renamed_example.txt


Удаление файла:

rm renamed_example.txt

Контрольные вопросы

1. Какая команда используется для создания директории?
Команда mkdir.

2. Как создать файл и сразу записать в него текст?
С помощью команды echo "текст" > имя_файла.

3. Какая команда используется для копирования файлов?
Команда cp.

4. Как переименовать файл?
С помощью команды mv.

5. Как удалить файл?
Команда rm.
