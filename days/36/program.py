import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config
import calendar

month_dict = {}

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    config.my_google_key_file_name, scope)

gc = gspread.authorize(credentials)

wks = gc.open_by_key(config.spreadsheet_key)

#wks.sheet1.update_acell('A3', str(datetime.date.today()))
wks.sheet1.update_acell('A5', '=TODAY()')
wks.sheet1.update_acell('B5', '-250')
list_of_lists = wks.sheet1.get_all_values()

# Find a cell with exact string value
cell = wks.sheet1.findall("a")
cell2 = wks.sheet1.findall("d")
cell3 = wks.sheet1.findall("January")
cell4 = wks.sheet1.findall("e")
print(cell)
print(wks.sheet1.cell(4, 3).value == '')
print(cell2)
print(cell3)
print(cell4)
#print("Found something at R%sC%s" % (cell.row, cell.col))
#print("Found something at R%sC%s" % (cell2.row, cell2.col))
# print(list_of_lists)


def main():
    """
    Provide list of questions for the user.

    What do you want to do?
    1. Apply Payment
        Input the following:
                            Date when received payment:
                            Amount of payment:         
    2. Retrieve Amount Due
    3. Notify Renter of Amount Due.

    """
    pass


def load_google_sheet():

    # return sheet
    pass


def apply_payment(date_cell_location, payment_cell_location, payment_amount: float):
    """
    Applies payment to google spreadsheet

    Each cell has a value and coordinates properties.
    value = cell.value
    row_number = cell.row
    column_number = cell.col

    #insert on the next available row
    date_today=str(datetime.date.today())
    TODAY() Google Sheets Function returns the current date.
    wks.sheet1.update_acell('A4', '=TODAY()')
    """

    wks.sheet1.update_cell(date_cell_location.row,
                           date_cell_location.col, '=TODAY()')
    wks.sheet1.update_cell(
        payment_cell_location.row, payment_cell_location.col, -(payment_amount))


def retrieve_amount_due():
    pass


def spreadsheet_mapper():
    """
    Builds a dictionary using the Month as key and the column numbers associated with the date and payment values.

    {'January': [1, 2]}

    1 = Column #1 of spreadsheet
    2 = Column #2 of spreadsheet

    Retrieve values by using: month_dict['January'][0]

    >>> print(month_dict)
    {'January': [1, 2], 'February': [3, 4], 'March': [5, 6], 'April': [7, 8], 'May': [9, 10], 'June': [11, 12], 'July': [13, 14], 'August': [15, 16], 'September': [17, 18], 'October': [19, 20], 'November': [21, 22], 'December': [23, 24]}
    >>> month_dict['January'][0]
    1
    >>> month_dict['November'][1]
    22
    """

    date_column = 1
    payment_column = 2

    for month in calendar.month_name[1:]:
        month_dict[month] = [date_column]
        month_dict[month].append(payment_column)
        date_column += 2
        payment_column += 2


def find_empty_cell(month: str):

    for x in range(1, 6):
        if wks.sheet1.cell(x, month_dict[month][0]).value == '' and wks.sheet1.cell(x, month_dict[month][1]).value == '':
            date_cell_location = wks.sheet1.cell(x, month_dict[month][0])
            payment_cell_location = wks.sheet1.cell(x, month_dict[month][1])

            return date_cell_location, payment_cell_location
        else:
            continue

# if __name__ == "__main__":
#    load_google_sheet()
