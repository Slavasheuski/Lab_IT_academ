import time
import multiprocessing

start = time.perf_counter()

def fib(n):
    start = time.time()
    a1 = a2 = 1
    for i in range(3, n+1):
        a1, a2 = a2, a1 + a2
        print(a2)
    end = time.time()
    print(f'Выполнено за: {end - start} секунд(ы)')

if __name__ == '__main__':
    p = multiprocessing.Process(target = fib, args = [1000])
    p.start()
    p.join()

finish = time.perf_counter()

print(' Finished in {} seconds '.format(finish - start))

fib(1000)
