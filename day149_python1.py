import threading

def work(name):
    print(name)

t1 = threading.Thread(target=work,args=("A",))
t2 = threading.Thread(target=work,args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()
