import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970

def speed_calc_decorator(function):
    def time_decorator():
        time_start = time.time()
        function()
        time_end = time.time()
        final_time = time_end - time_start
        print(f"{function.__name__} function run speed: " + str(final_time)) #getting the string with the function name

    return time_decorator


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()