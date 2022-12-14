# "Взламываем" электронный дневник

Скрипт предназначен для исправления записей в базе данных электронного дневника:
* Исправление оценок; 
* Удаление замечаний;
* Создание похвалы;


## Как установить
1. Необходимо скопировать скрипт `fixed.py` в папку с `Django` рядом с `manage.py`.
2. В командной строке перейти в каталог с программой.
3. Запустить интерактивный режим `Django` командой:
```python
python manage.py shell
``` 
4. В интерактивном режиме произвести импорт модуля командой:
```python
from fixed import *
``` 

Далее в интерактивном режиме запускать функции с нужными параметрами.

## Список функций для работы с модулем


### Исправление оценок fix_marks(name)
Входящий параметр:  
	`name` - Фамилия и Имя ученика

Результат выполнения:  
	Все оценки `2` и `3` ученика `name` будут заменены на `5`

Примеры запуска:
```python
fix_marks('Фролов Иван')
fix_marks(name='Фролов Иван')
``` 
или
```python
name = 'Фролов Иван'
fix_marks(name)
``` 

### Удаление всех замечаний remove_chastisements(name)
Входящий параметр:  
	`name` - Фамилия и Имя ученика

Результат выполнения:  
	Все замечания ученика `name` будут удалены

Примеры запуска:
```python
remove_chastisements('Фролов Иван')
remove_chastisements(name='Фролов Иван')
```
или
```python
name = 'Фролов Иван'
remove_chastisements(name)
``` 

### Создание похвалы create_commendation(subject, name)

Входящий параметр:  
	`name` - Фамилия и Имя ученика.  
	`subj` - название предмета ('Музыка', 'Математика')

Результат выполнения:  
	Похвала будет создана за последний урок предмета `subj` для ученика `name`. Если за этот уже есть похвала - изменений не произойдет.

Примеры запуска:
```python
create_commendation('Музыка', 'Фролов Иван')
create_commendation(subject='Музыка', name='Фролов Иван')
```
или 
```python
subject = 'Музыка'
name = 'Фролов Иван'
create_commendation(name)
``` 

# Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](dvmn.org).