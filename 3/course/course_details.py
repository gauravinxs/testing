import multiprocessing
import multiprocessing.process

def test():
    print("this is the multiprocessing program")

if __name__ == '__main__':
    m = multiprocessing.Process(target = test)
    print("this is the main program")
    m.start()
    m.join()

import multiprocessing
def sq(n):
    return n**2

if __name__ == '__main__':
    with multiprocessing.Pool(processes=3) as pool:
        out = pool.map(sq, [3,2,4,4,3,2,4])
        print(out)

    
import multiprocessing

def square(n):
    return n**2

if __name__=='__main__':
    with multiprocessing.Pool(processes=5) as pool:
        out = pool.map(square, [2, 4, 5, 6, 7, 7, 4])
        print(out)
