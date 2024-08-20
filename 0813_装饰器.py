import time


def cost_time_func(my_func):
    def wrapper():
        start_time = time.perf_counter()
        func = my_func()
        end_time = time.perf_counter()
        print(f"cost {(end_time-start_time)*1000} ns.")
        return func

    return wrapper


@cost_time_func
def sleep_func():
    print("sleep...")
    time.sleep(1)


sleep_func()