import time


def Counter():
    count = 0
    while True:
        print(f"The current count is: {count}")
        count += 1
        time.sleep(1)


Counter()
