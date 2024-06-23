import time

def my_decorators(func):
    def wrapper():
        start_time = time.time()
        print("start_time")
        func()
        end_time = time.time()
        print("end_time")
        print(f"Time: {end_time - start_time}")

    return wrapper

@my_decorators
def my_function():
    time.sleep(5)  # Simulating some time-consuming operation
    print('time taken for function: ')

my_function()
