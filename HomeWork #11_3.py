# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Интроспекция"

import inspect

def introspection_info(obj):
    info_date = {'type': type(obj).__name__,
            'attributes': [],
            'methods': []}
    for name in dir(obj):
        if callable(getattr(obj, name)):
            info_date['methods'].append(name)
        else:
            info_date['attributes'].append(name)
    obj_module = inspect.getmodule(obj)
    if obj_module is None:
        info_date['module'] = __name__
    else:
        info_date['module'] = obj_module.__name__

    return info_date

if __name__ == '__main__':

    print('*'*50, 'Интроспекция числа 42', '*'*50)
    print()
    print(introspection_info(42))
    print()

    print('*'*50, 'Интроспекция метода introspection_info', '*'*50)
    print()
    print(introspection_info(introspection_info))
    print()

    print('*' * 50, 'Интроспекция метода inspect', '*' * 50)
    print()
    print(introspection_info(inspect))
    print()
