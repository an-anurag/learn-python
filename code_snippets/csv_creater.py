import csv


def main():
    """Logic for handling csv read and write"""

    source_file = r"I:\Master\Documents\source.csv"
    dest_file = r"I:\Master\Documents\destination.csv"
    # specify row_count for desired rows to be written
    row_count = 5
    # reading csv
    source_csv = open(source_file, 'r')
    csv_reader = csv.reader(source_csv)
    print("Source file loaded successfully")
    header = next(csv_reader)
    first_row = next(csv_reader)
    source_csv.close()
    print("First row of the source file is: ")
    print(first_row)
    column_choice = list(map(int, input("Enter column index saparating with single space to increament (index starts from zero): ").split()))
    # writing csv
    dest_csv = open(dest_file, 'w')
    csv_writer = csv.writer(dest_csv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    csv_writer.writerow(header)
    # result list to store formatted lines
    result_list = list()
    for i in range(row_count):
        line = ""
        for j in range(0, len(first_row)):
            
            if j not in column_choice:
                line += first_row[j]
                line += ","
            else:
                element = first_row[j]
                element = int(element) + i
                line += str(element)
                line += ","
        result_list.append(line.split(',')[:-1])
    # writing each line
    for line in result_list:
        csv_writer.writerow(line)
    print("Destination file written successfully")


main()
