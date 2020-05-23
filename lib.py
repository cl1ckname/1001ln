from bottle import template as tp

SAMPLE = 'static/html/base.html'

def template(name,title = 'title',**args):
    print(args)
    return tp(SAMPLE,
    including_page = name, title = title, args=args )

d = {
    1: ('Диплодок', 
    'https://img3.goodfon.com/original/2560x1440/5/4c/kinder-syurpriz-igrushka-trava.jpg',
    'Очевидно, что диплодоки самые классные диозавры с длинющей шеей (обычо баскетболисты). Длинна тела около 35 метров, высота - 10 метров, вес - 30 тон. Сильно. Мощно.'),
    2: ('Тиранозавр',
    'https://im0-tub-ru.yandex.net/i?id=48782499d25bb29dbd75adc029f31d78&n=13',
    '(Tyrannosaurus rex) – настоящий король динозавров. Тирекс неспроста стал иконой палеонтологии. Огромный семитонный хищник вобрал в себя огромное множество прогрессивных черт.'),
    3: ('Антоха Карцев',
    'https://sun9-18.userapi.com/c849020/v849020892/39b41/BIc2v6uq9eo.jpg',
    'Тончик))')}