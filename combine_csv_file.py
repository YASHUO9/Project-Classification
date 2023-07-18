
# <-------------------------------combining the csv files---------------------------------------------------->#
import os
import csv
import glob


def combining_csv(file_location, cwd):
    """ This function is used to combine the multiple csv file in the single csv file 
         This function is taking two input cwd = current directory location and """
    Dir = file_location
    count = 0
    Avg_Dir = fr"{cwd}"

    csv_file_list = glob.glob(os.path.join(
        Dir, '*.csv'))  # returns the file list
    print(csv_file_list)

    with open(os.path.join(Avg_Dir, 'Output.csv'), 'w', newline='') as f:
        wf = csv.writer(f, lineterminator='\n')

        for files in csv_file_list:
            if count > 1200:
                break
            with open(files, 'r') as r:
                next(r)                   # SKIP HEADERS
                rr = csv.reader(r)

                for row in rr:
                    wf.writerow(row)
                    count += 1
    print('Output file has been created')
