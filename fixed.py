from random import choice
from datacenter.models import Schoolkid, Mark, Chastisement
from datacenter.models import Lesson, Commendation, Subject
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


TEXT_COMMENDATIONS = [
    'Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!'
    'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!',
    'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!',
    'Очень хороший ответ!', 'Талантливо!', 'Ты сегодня прыгнул выше головы!',
    'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!',
    'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!'
    'Это как раз то, что нужно!', 'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!',
    'Ты растешь над собой!', 'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!',
]


def fetch_entered_name(name):
    try:
        child = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.MultipleObjectsReturned:
        print(f'"{name}": Совпадение имен, уточните ученика!')
        return None
    except Schoolkid.ObjectDoesNotExist:
        print(f'"{name}": Такого ученика нет в базе!')
        return None
    else:
        return child


def fix_marks(name):
    child = fetch_entered_name(name)
    if child:
        fixed_marks = Mark.objects.filter(
            schoolkid=child, points__in=[2, 3]
        ).update(points = 5)
        print(f'Исправлено плохих оценок: {fixed_marks}')


def remove_chastisements(name):
    child = fetch_entered_name(name)
    if child:
        deleted_objs,_ = Chastisement.objects.filter(
            schoolkid=child
        ).delete()
        print(f'Удалено {deleted_objs} замечаний.')


def create_commendation(subject, name):
    child = fetch_entered_name(name)
    if child:
        lesson = Lesson.objects.filter(
            year_of_study=child.year_of_study,
            group_letter=child.group_letter,
            subject__title=subject
        ).order_by('-date').first()
        if lesson:
            commendation, created = Commendation.objects.update_or_create(
                created=lesson.date,
                schoolkid=child,
                subject=lesson.subject,
                teacher=lesson.teacher
            )
            if created:
                commendation.text = choice(TEXT_COMMENDATIONS)
                commendation.save()
        else:
            print(f'Урок {subject} не найден. Уточните название предмета!')

