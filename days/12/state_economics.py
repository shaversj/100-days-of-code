import csv
import time
import pylab


def main():
    open_file()


def open_file():
    """
    Your program should prompt the user to enter a valid file name. If the file is not found print an error message and keep prompting until a valid file name is entered. This should be done using try and except. You likely already have this function from a previous project.
    """
    while True:
        file_name = input('Enter the name of a file to open: '"")
        try:
            print('Attempting to read file...')
            time.sleep(3)
            data_file = open(file_name, mode='r')
        except IOError:
            # Raised when an I/O operation (such as a print statement, the built-in open() function or a method of a file object) fails for an I/O-related reason, e.g., “file not found” or “disk full”.
            print('Bad file name. Please try again.')
        else:
            print('Found file!')
            time.sleep(1)
            print('Now processing...')
            csv_reader = csv.reader(data_file)
            parse_file(csv_reader)
            break  # exit loop but the finally block will still complete
        finally:
            try:
                data_file.close()
            except NameError:
                print('Trying again')


def parse_file(csv_reader):
    pass


def display_by_region():
    pass


def plot_by_region():
    pass


def plot_gression():
    # provided for me
    pass


if __name__ == "__main__":
    main()
