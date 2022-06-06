import csv


def write_csv(filename, header, data):
	try:
		with open(filename, 'w', newline='') as csv_file:
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow(header)
			csv_writer.writerows(data)
	except (IOError, OSError) as csv_file_errror:
		print(f"Unable to write the contents to csv file. Exception: {csv_file_errror}")


if __name__ == "__main__":
	header = ['name', 'age', 'gender']
	data = [['Richard', 32, 'M'], ['Mumzil', 21, 'F'], ['Melinda', 25, 'F'], ['Arun', 22, 'M']]
	filename = "sample_output.csv"
	write_csv(filename, header, data)
