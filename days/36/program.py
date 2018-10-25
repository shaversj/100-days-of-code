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


def main():
    """
    Provide list of questions for the user.
    """

    payment_amount = int(input('Enter payment amount (ex. 750): '""))
    month = input(
        'Enter the month the payment should be applied to (ex. March): '"")

    spreadsheet_mapper()
    date_cell_location, payment_cell_location = find_empty_cell(month)
    apply_payment(payment_amount, date_cell_location, payment_cell_location)


def apply_payment(payment_amount: float, date_cell_location, payment_cell_location):
    """
    Applies date and payment amount to google spreadsheet

    """

    try:
        wks.sheet1.update_cell(date_cell_location.row,
                               date_cell_location.col, '=TODAY()') and wks.sheet1.update_cell(
            payment_cell_location.row, payment_cell_location.col, -(payment_amount))
    except gspread.exceptions.GSpreadException as e:
        print(e)
        print('Your update was not successful. Please try again.')
    else:
        print('Your payment was successfully applied to the spreadsheet!')


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
    {'January': [1, 2], 'February': [3, 4], 'March': [5, 6], 'April': [7, 8], 'May': [9, 10], 'June': [11, 12], 'July': [
        13, 14], 'August': [15, 16], 'September': [17, 18], 'October': [19, 20], 'November': [21, 22], 'December': [23, 24]}
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
    """
    Find the first empty cell in the column that is associated with the given month.
    """

    for x in range(1, 6):
        if wks.sheet1.cell(x, month_dict[month][0]).value == '' and wks.sheet1.cell(x, month_dict[month][1]).value == '':
            date_cell_location = wks.sheet1.cell(x, month_dict[month][0])
            payment_cell_location = wks.sheet1.cell(x, month_dict[month][1])

            return date_cell_location, payment_cell_location
        else:
            continue


if __name__ == "__main__":
    main()
