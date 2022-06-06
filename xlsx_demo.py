import xlsxwriter


def create_workbook(filename):
	workbook = xlsxwriter.Workbook(filename)
	return workbook


def create_worksheet(workbook):
	worksheet = workbook.add_worksheet()
	return worksheet


def write_data(worksheet, data):
	for row in range(len(data)):
		for col in range(len(data[row])):
			worksheet.write(row, col, data[row][col])
	worksheet.write(len(data), 0, 'Avg. Age')
	avg_formula = f"=AVERAGE(B{1}:B{len(data)})"
	worksheet.write(len(data), 1, avg_formula)


def close_workbook(workbook):
	workbook.close()


if __name__ == "__main__":
	data = [['Sheldon Cooper', 12],
			['Missy Cooper', 12],
			['Georgie', 17],
			['Elon Musk', 50],
			['Arun', 22],
			['Harrison Wells', 52],
			['Barry Allen', 27],
			['Iris West', 27],
			['Wally West', 21],
			['Cisco Ramon', 27],
			['Caitlin Snow', 26]]
	workbook = create_workbook('sample_workbook.xlsx')
	worksheet = create_worksheet(workbook)
	write_data(worksheet, data)
	close_workbook(workbook)
