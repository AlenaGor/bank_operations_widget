"""
Модуль с декораторами для логирования
"""
import os
from datetime import datetime
from functools import wraps
from typing import Optional, Callable, Any


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования работы функций.

    Args:
        filename: Имя файла для записи логов. Если не указан, логи выводятся в консоль.

    Returns:
        Декорированная функция
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"

                if filename:
                    # Запись в файл
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(log_message + '\n')
                else:
                    # Вывод в консоль
                    print(log_message)

                return result

            except Exception as e:
                # Формируем сообщение об ошибке
                args_str = ', '.join(repr(a) for a in args)
                kwargs_str = ', '.join(f"{k}={repr(v)}" for k, v in kwargs.items())
                inputs = f"({args_str}, {kwargs_str})" if kwargs_str else f"({args_str})" if args_str else "()"

                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {inputs}"

                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)

                raise e

        return wrapper

    return decorator