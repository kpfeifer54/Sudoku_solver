import csv

with open('sample_sudoku_board_inputs.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    board_matrix = {}
    for row in csv_reader:
        for i in range(10):
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')