import threading

# 4.8.5 锁
seen = set()  # 存储已经处理过的项目
seen_lock = threading.Lock()


def already_seen(item):
    # with 语句确保在执行其套件之前获取 seen_lock，并且在由于任何原因退出套件时释放它。
    with seen_lock:
        if item not in seen:
            seen.add(item)
            return False
        return True


# 4.8.6 屏障
counters = [0, 0]
barrier = threading.Barrier(2)  # 指定了两个线程需要在屏障处等待


def count(thread_num: int, steps: int):
    for _ in range(steps):
        other = counters[1 - thread_num]
        barrier.wait()  # wait for reads to complete
        # 写入发生在同一阶段，但它们是不相交的; 这种不相交对于避免在同一阶段并发写入相同数据是必要的。
        counters[thread_num] = other + 1 # 
        barrier.wait()  # wait for writes to complete


def threaded_count(steps):
    other = threading.Thread(target=count, args=(1, steps))
    other.start()
    count(0, steps)
    print("counters:", counters)


threaded_count(10)
