# Introduction

This is a III portal website for III employees to get temp password happily.

# Prerequisites

- It should establish III VPN connection firstly.
- Python3 and pip3 commands are available.
    - pip3 install beautifulsoup4
    - pip3 install pdftotext
    - pip3 install requests

# Usage

- Using `git clone https://github.com/peter279k/iii_tmp_password_tool` to clone this repository.
- Creating the `iii_settings.txt` file and it contents are as follows:

```
your employee number
last 6 lengths of your id number(e.g. 123456)
your birthday year(e.g. 1993)
your birthday month(including zero, e.g. 01)
your birthday day(including zero, e.g. 01)
```

- Creating the `pop3_setting.txt` file and its contents are as follows:

```
your outlook mail account
your outlook mail password
```

- Using `./run.sh last-6-lengths-of-your-id-number` to start getting temp password on III portal!

- The output message is as follows:

```Bash
peter@lee:~/iii_tmp_passwd_tool$ ./run.sh last-6-lengths-of-your-id-number
Please ensure III VPN connection has been established!
Get III tmp password is started...

Loading iii_settings.txt file...
Sending getting tmp password request is successful.
Sleeping 60 seconds to wait for the tmp password e-mail is received...
Total no. of Email :  1


Start Reading Messages


Attached file: pwd90486.pdf has been saved!
Initializing pdf_auth.txt file...
Appending PDF password to pdf_auth.txt file...
Delete pwd90486.pdf PDF file...
Fetching tmp password from specific pwd90486.pdfhas been done!
Now you're getting the III portal tmp password on ./iii_tmp_password.txt file!!
```

- As above sample messages, the temporary password is stored in `./iii_tmp_password.txt` file.
- Congrats! Now it can use this temporary password to login III portal happily :)!
