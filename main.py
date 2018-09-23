import argparse
import time_measurement
from diagram import Diagram


def main():
    parser = argparse.ArgumentParser(
        description="This program check different sortings")
    parser.add_argument('--set', '-s', action='store_const',  const=1,
                        help="Use this options if you want to set parameters")
    arguments = parser.parse_args()
    if arguments.set == 1:
        print('Enter methods of sorting with a space:')
        functions = input().split()
        print('Enter count of element of arrays with a space:')
        counts_string = input().split()
        counts = []
        for string in counts_string:
            counts.append(int(string))
        print("Enter types of data('best', 'worst', 'random') with a space:")
        types = input().split()
        research = time_measurement.Researh(functions, counts, types)
    else:
        research = time_measurement.Researh()
    research.check()
    diagram = Diagram(research.functions_data)
    diagram.draw()


if __name__ == '__main__':
    main()