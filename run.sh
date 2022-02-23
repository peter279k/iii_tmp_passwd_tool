#!/bin/bash

echo "Please ensure III VPN connection has been established!"
echo "Or internal III netwwork hsa been connected!"
echo "Get III tmp password is started..."
echo ""

pdf_password=$1

if [[ $pdf_password == '' ]]; then
    echo "Please set pdf_password argument"
    exit 1
fi;

python3 get_iii_tmp_password.py

if [[ $? != 0 ]]; then
    echo "Running get_iii_tmp_password.py is failed!!"
    exit 1
fi;

echo "Sleeping 60 seconds to wait for the tmp password e-mail is received..."
sleep 60

python3 outlook_pop3_fetcher.py

if [[ $? != 0 ]]; then
    echo "Running outlook_pop3_fetcher.py is failed!!"
    exit 1
fi;

echo "Appending PDF password to pdf_auth.txt file..."
echo "$pdf_password" >> pdf_auth.txt

python3 read_tmp_passwd_pdf.py
if [[ $? != 0 ]]; then
    echo "Running get_iii_tmp_password.py is failed!!"
    exit 1
fi;

echo "Now you're getting the III portal tmp password on ./iii_tmp_password.txt file!!"
echo "Don't forget to run the get_otp_password.py program!"
