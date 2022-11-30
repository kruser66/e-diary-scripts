from random import choice
from datacenter.models import Schoolkid, Mark, Chastisement
from datacenter.models import Lesson, Commendation
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


text_commendations = [
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


def select_entered_name(name):
    try:
        child = Schoolkid.objects.get(full_name__contains=name)
    except MultipleObjectsReturned:
        print(f'"{name}": Совпадение имен, уточните ученика!')
        return None
    except ObjectDoesNotExist:
        print(f'"{name}": Такого ученика нет в базе!')
        return None
    else:
        return child


def fix_marks(name):
    child = select_entered_name(name)
    if child:
        child_marks = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
        print(f'Плохих оценок: {child_marks.count()}')
        for mark in child_marks:
            mark.points = 5
            mark.save()
        child_marks = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
        print(f'Плохих оценок: {child_marks.count()}')


def remove_chastisements(name):
    child = select_entered_name(name)
    if child:
        child_chastisements = Chastisement.objects.filter(schoolkid=child)
        for chastiment in child_chastisements:
            chastiment.delete()


def remove_commendation(name):
    child = select_entered_name(name)
    if child:
        child_commedation = Commendation.objects.filter(schoolkid=child)
        for chastiment in child_commedation:
            chastiment.delete()


def create_commendation(subj, name):
    child = select_entered_name(name)
    if child:
        lesson = Lesson.objects.filter(
            year_of_study=child.year_of_study,
            group_letter=child.group_letter,
            subject__title=subj
        ).order_by('-date')[0]
        commendation, created = Commendation.objects.update_or_create(
            created=lesson.date,
            schoolkid=child,
            subject=lesson.subject,
            teacher=lesson.teacher
        )
        if created:
            commendation.text = choice(text_commendations)
            commendation.save()


if __name__ == '__main__':
    pass
