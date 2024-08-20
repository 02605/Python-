
def my_fb(max_num):
    n, a, b = 0, 1, 1
    while n < max_num:
        yield b
        # 同时赋值
        a, b = b, a + b
        print(f"a={a}, b={b}")
        n = n + 1


def test_my_fb():
    fb = my_fb(5)
    assert 1 == next(fb)
    assert 2 == next(fb)
    assert 2 == next(fb)


if __name__ == '__main__':
    fb = my_fb(5)
    print(next(fb))
    print(next(fb))
    print(next(fb))