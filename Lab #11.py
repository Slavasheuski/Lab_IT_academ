import threading, random, time

class ActivePool:
   
    start = time.time()

    def __init__(self):
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            tm = time.time() - self.start
            print(f'Время: {round(tm, 3)} Running: {self.active}')

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            tm = time.time() - self.start
            if self.active:
                print(f'Время: {round(tm, 3)} Running: {self.active}')
                


def worker(sem, pool):
    with sem:
        th_name = threading.current_thread().name
        print(f'{th_name} ожидает присоединения к пулу')
        pool.makeActive(th_name)
        time.sleep(0.5)
        pool.makeInactive(th_name)

   
sem = threading.Semaphore(2)


pool = ActivePool()

for i in range(100):
    t = threading.Thread(
        target=worker,
        args=(sem, pool),
    )
    t.start()
