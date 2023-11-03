import functools
import time
from collections.abc import Generator, Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def timeit(function: Callable[P, T]) -> Callable[P, T]:
    @functools.wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()
        print(f"\n{function.__name__}() finished in {end - start:.10f}s")
        return result

    return wrapper


def apply_func(func: Callable[[str], tuple[str, str]], value: str) -> tuple[str, str]:
    return func(value)


EmailComponents = tuple[str, str] # a type alias
@timeit
def parse_email() -> Generator[EmailComponents, str, str]:
    """the first parameter is what the generator yields, in this case, it's a tuple containing two strings - one for the
    username and the other for the domain, both parsed from the email address,
    the second parameter describes input sent to the generator,
    the third parameter represents the final value generator returns when it's done producing - in this case it's done"""
    sent = yield "", ""
    while sent != "":
        if "@" in sent:
            username, domain = sent.split("@")
            sent = yield username, domain
        else:
            sent = yield "invalid email"
    return "Done"
