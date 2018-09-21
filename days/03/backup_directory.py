import os
import time
import zipfile
import send2trash

print('-----Download Directory Cleaner-------')

os.chdir('/Users/shaverj/Downloads')
downloads_dir = '/Users/shaverj/Downloads'
timestr = time.strftime("%Y%m%d")


def delete_files_over_50mb():
    for dirpath, dirnames, filenames in os.walk(downloads_dir):
        for f in filenames:
            file_path = os.path.join(dirpath, f)
            file_size = os.path.getsize(file_path)
            if int(file_size) >= int(50000000):
                print(f'Sending files over 50MB to the trash {file_path}')
                send2trash.send2trash(file_path)
                # import send2trash module so that you can write code that deletes files


def backup_files():
    zipFileName = timestr + '_backup.zip'
    backup_zip = zipfile.ZipFile(zipFileName, mode='w')
    for dirpath, dirnames, filenames in os.walk(downloads_dir):
        #print(f'Adding files in {dirpath}')
        backup_zip.write(dirpath)
        for filename in filenames:
            #print(os.path.join(dirpath, filename))
            if filename.endswith('.zip') or filename.endswith('.app'):
                print(f'Excluding {filename} from zipfile')
                continue
            backup_zip.write(os.path.join(dirpath, filename))
            #print(f'Excluding {filename} from zipfile')
            #backup_zip.write(os.path.join(dirpath, filename))
            #    print(new)
    backup_zip.close()


def send_to_trash():
    for dirpath, dirnames, filenames in os.walk(downloads_dir):
        for filename in filenames:
            print(f'Sending {filename} to trash!')
            file_path = os.path.join(dirpath, filename)
            if filename.startswith('2018') and filename.endswith('.zip'):
                print(f'---------Excluding {filename} from trash!--------')
                continue
            send2trash.send2trash(file_path)
            # does not delete folders...only deletes files and files inside folders.

# print('Done.')


# delete_files_over_50mb()
# backup_files()
send_to_trash()
