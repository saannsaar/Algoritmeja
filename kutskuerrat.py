# Toteuta seuraava funktio niin,
# että pystyt laskemaan, montako kertaa 
# funktiota kutsutaan yhteensä rekursion aikana.


def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__

    return helper

@call_counter
def f(n):
    if n <= 2:
        return n
    return f(n-1)+f(n-2)+f(n-3)


print(f(30))
print(f"Funktio kutsuttiin {f.calls} kertaa")

