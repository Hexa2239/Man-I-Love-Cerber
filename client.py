import CerberThread

curInitThread = 0


while True:
    while curInitThread < 300:
        thread = CerberThread.Yippie()
        thread.run()
        thread.begin()

    