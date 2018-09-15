import time_measurement


def main():
    research = time_measurement.Researh()
    research.check()
    for e in research.data:
        print(e.function, e.time)


if __name__ == '__main__':
    main()