import multiprocessing 

def test():
    print("this is the child")

if __name__ == '__main__':
    m = multiprocessing.Process(target=test)
    print("This si the parent")
    m.start()
    m.join()