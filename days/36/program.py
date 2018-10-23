import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config


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


def apply_payment(month: str, amount: float):
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

    # if month == 'January':
    #    date_cell = cell.

    pass


def retrieve_amount_due():
    pass


# if __name__ == "__main__":
#    load_google_sheet()
