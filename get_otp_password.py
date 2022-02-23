import os
import sys
import poplib
import email
import datetime


server = poplib.POP3_SSL('outlook.office365.com', port=995, timeout=10)

pop3_setting_file = './pop3_setting.txt'
if os.path.isfile(pop3_setting_file) is False:
    print('The ./pop3_setting.txt file not found')
    sys.exit(1)

file_handler = open(pop3_setting_file)
pop3_settings = ''.join(file_handler.readlines()).split('\n')[0:-1]
if len(pop3_settings) != 2:
    print('The POP3 setting contents are wrong.')
    sys.exit(1)

pop3_user = pop3_settings[0]
pop3_passwd = pop3_settings[1]
file_handler.close()
server.user(pop3_user)
server.pass_(pop3_passwd)

pop3_info = server.stat() #access mailbox status
mail_count = pop3_info[0] #total mail count

print("Total no. of Email : " , mail_count)
print ("\n\nStart Reading Messages\n\n")

def decode_header(header):
    decoded_bytes, charset = email.header.decode_header(header)[0]
    if charset is None:
        return str(decoded_bytes)
    else:
        return decoded_bytes.decode(charset)

now_month = datetime.datetime.now().strftime('%b %Y')
for i in range(mail_count):
    raw_email = b'\n'.join(server.retr(i+1)[1])
    parsed_email = email.message_from_bytes(raw_email)
    try:
        decoded_subject = decode_header(parsed_email['Subject'])
    except:
        continue

    if now_month not in parsed_email['Date']:
        server.dele(i+1)
        continue
    if '[資策會入口網站]一次性密碼通知' not in decoded_subject:
        continue

    for part in parsed_email.walk():
        if part.is_multipart():
            # maybe need also parse all subparts
            continue
        elif part.get_content_maintype() == 'text':
            texts = part.get_payload(decode=True).decode(part.get_content_charset())
            text_arr = texts.split('\n')
            if '一次性密碼(OTP)為：' in text_arr[2]:
                otp_password = text_arr[2].split('：')[1]
                print('OTP Password Find! It is: %s' % otp_password)
        else:
            print('Unknown part:', part.get_content_type())
    server.dele(i+1)

with open('./iii_otp_password.txt', 'a') as file_handler:
    file_handler.write(otp_password)

print('Storing OTP in iii_otp_password.txt!')

server.quit()
