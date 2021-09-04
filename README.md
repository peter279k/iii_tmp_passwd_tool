# Introduction

This is a III portal website for III employees to get temp password happily.

# Prerequisites

- It should establish III VPN connection firstly.
- Using the `Ubuntu 18.04+` for the current running environment.
- Python3 and pip3 commands are available.
    - Using `pip3 install pipenv --user` to install `pipenv` if the `pipenv` command is not installed.
    - If using the `Ubuntu 18.04+`, the `pipenv` command will be located on `/home/user/.local/bin` folder.
    - Using the `PATH=$PATH:/home/user-name/.local/bin` command to be available for using `pipenv` command.
    - Using the `pipenv install` command to create Python virtual environment and install required Python dependencies.

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

- Using the `pipenv shell` to enter into current Python virtual environment shell.
- Using `./run.sh last-6-lengths-of-your-id-number` command to run `./run.sh` shell script and start getting temp password on III portal!
- After running above `./run.sh` script is successful, using the `exit` command exit this virtual environment shell.

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


# References

- https://shallowsky.com/blog/programming/deleting-pop-email.html
- https://www.dev2qa.com/python-parse-emails-and-attachments-from-pop3-server-example/
- https://pipenv-fork.readthedocs.io/en/latest/basics.html
- https://pipenv.pypa.io/en/latest/install/
- https://www.codingforentrepreneurs.com/comments/16093
- https://github.com/pypa/pipenv/issues/84
- https://stackoverflow.com/questions/49944871/deactivate-a-pipenv-environment
- https://docs.python-requests.org/en/master
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
- https://gist.github.com/strayge/f619cacb972d956ddbe1472d882821fe
