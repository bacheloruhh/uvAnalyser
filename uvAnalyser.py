import csv
import os

# ====================
# Default variables:
default_avg_cnt = 10
default_exc_thr = 0.02

default_low_wvl = 300
default_hig_wvl = 1014
default_delimit = '\t'
default_exc_fin = True
# ====================


def welcome():
    # Print a welcome screen and ask for user input. Check if input is valid.
    # If so return input, if not return default values.
    print("Welcome.\nThis script will merge all files in this directory, " +
          "normalize them\nand make suggestions for the location of the " +
          "first exciton.\nPress 'Enter' for default values (i.e. %d, %.2f).\n"
          % (default_avg_cnt, default_exc_thr)
          )

    avg_cnt = raw_input("Number of baseline values for average: ")
    if avg_cnt and valid_input(avg_cnt):
        avg_cnt = int(avg_cnt)
    else:
        avg_cnt = default_avg_cnt

    exc_thr = raw_input("Exciton absorbance threshold: ")
    if exc_thr and valid_input(exc_thr):
        exc_thr = float(exc_thr)
    else:
        exc_thr = default_exc_thr
    print

    return avg_cnt, exc_thr


def valid_input(x):
    # Check if value is castable into int or float.
    try:
        int(x) or float(x)
        return True
    except ValueError:
        return False


def read_data():
    # Returns data from csv-files in current directory in form of a 2d list.
    print "Reading data..."
    data = [["name"]]
    for i in range(default_low_wvl, default_hig_wvl+1):
        data.append([i])

    for filename in os.listdir(os.getcwd()):
        if filename.endswith("C.txt"):
            data[0].append(':'.join([filename[11:13], filename[13:15]]))

            with open(filename) as csvfile:
                csvfile.next()
                reader = csv.reader(csvfile, delimiter='\t')
                for index, row in enumerate(reader):
                    data[index+1].append(row[1])
    return data


def normalize_data(data):
    # Takes a 2d list, normalizes the values and returns it.
    print "oh shit"


def write_data(data, delim):
    # Takes a 2d list  and a delimiter and writes a csv-file.
    print "Writing data..."
    with open("merged_files.txt", 'w') as output_file:
        writer = csv.writer(output_file, delimiter=delim)
        writer.writerows(data)


def exciton_finder(data):
    # Takes a 2d list and writes a file with a guess for the first exciton.
    if default_exc_fin:
        exc_found = 0
        print "%d of %d excitons found." % (exc_found, len(data[0]))
    else:
        print "Exciton finder disabled."


avg_cnt, exc_thr = welcome()
data = read_data()

write_data(data, default_delimit)
exciton_finder(data)
print
raw_input("Press 'Enter' to close window...")
