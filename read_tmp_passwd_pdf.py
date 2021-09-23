import os
import sys
import pdftotext


file_name = 'pdf_auth.txt'
if os.path.isfile(file_name)  is False:
    print(file_name + ' is not found')
    print('Please create ' + file_name + '!')
    sys.exit(1)

file_handler = open(file_name, 'r')
pdf_auth_settings = ''.join(file_handler.readlines()).split('\n')[0:-1]
file_handler.close()

if len(pdf_auth_settings) != 2:
    print(file_name + ' contents are not correct')
    sys.exit(1)

pdf_file_name = pdf_auth_settings[0]
pdf_passwd = pdf_auth_settings[1]

if os.path.isfile(pdf_file_name) is False:
    print(pdf_file_name + 'is not found')
    sys.exit(1)

# If it's password-protected
with open(pdf_file_name, 'rb') as f:
    pdf = pdftotext.PDF(f, pdf_passwd)

# Read all the text into one string
pdf_contents = list(pdf)[0].split('\n')[0:-1]

if len(pdf_contents) != 4:
    print('The PDF contents seem to be wrong.')
    sys.exit(1)

print('Delete ' + pdf_file_name + ' PDF file...')
os.remove(pdf_file_name)

tmp_password = pdf_contents[2]

tmp_password_file = './iii_tmp_password.txt'
file_handler = open(tmp_password_file, 'w')
file_handler.write(tmp_password + '\n')
file_handler.close()

print('Fetching tmp password from specific ' + pdf_file_name + ' has been done!')
