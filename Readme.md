# dcrust-result-checker

Monitor a DCRUST student's account for result related updates.

This is a simple scraper that checks DCRUST University's results site to see if your previous semester result is out.

For an even semester student, it will fetch the results of the previous odd semester examination taken by the student.0

Simply input the following four values during setup and this
 
    1. University Roll Number
    2. University Account Password
    3. Gmail Account ID(Currently, in test phase, so only build for a gmail id)
    4. Gmail Account Password(Only for sending email, as the script sends you email from your own account in case of an update)
 
This script will check your email account on the university web site every hour during the day(8:00 A.M. - 8:00 P.M.)

#REQUIREMENTS

    A windows PC, Windows 7 & and up, preferably (Linux version coming soon)

    Make sure your system is running python3. If you do not have python3, install it from  this link: https://www.python.org/downloads/release/python-343/
    
    If you are unable to set this up due to some error, try googling the error you receive and should you not find any solution, contact me at divij.sehgaal7@gmail.com

#EXAMPLE

A successful execution of the result-fetch.bat file should result in the following output on the command line:

```
Installing required packages 
Requirement already satisfied: beautifulsoup4 in c:\python34\lib\site-packages
Requirement already satisfied: requests in c:\python34\lib\site-packages
Enter info when asked to properly setup university Result Checker. False inputs may lead to unexpected results.
Make sure you enter the correct information for proper results.
Enter University Roll Number:13007001017
University Account Password: wZO6y0NG
Enter Email Account to send alert from and receive alert to:
This stays within the application only. It is never shared;  View the source code on GitHub for more info.
Enter Gmail Email ID: abc@gmail.com
Enter GMAIL Password: password
Details entered by you are:
University roll number: XXXXXXXXXXX
University Password: <password>
Email id: abc@gmail.com
Gmail id password: password
Proceed?[Enter y/n only]: y
Proceeding with Setup...
WARNING: The task name "DCRUST_RESULT_CHECK" already exists. Do you want to replace it (Y/N)? y
SUCCESS: The scheduled task "DCRUST_RESULT_CHECK" has successfully been created.
Press any key to continue . . .
```
The part:
```
Requirement already satisfied: beautifulsoup4 in c:\python34\lib\site-packages
Requirement already satisfied: requests in c:\python34\lib\site-packages
```
should be visible only if the two required libraries are already downloaded on your machine or they will be downloaded for you.

The result file will be available in the folder ```C:\results\```

# VERIFY

To make sure that the setup is successful, look for an email in the email account that you entered. 

To make sure the alert is setup on the local machine, run 

```schtasks /QUERY /TN DCRUST_RESULT_CHECK```

The above should an output like this:
```
Folder: \
TaskName                                 Next Run Time          Status
======================================== ====================== ===============
DCRUST_RESULT_CHECK                      27-02-2017 20:04:00    Ready
```

Please share your feedback on this with me and let me know your feedback at divij.sehgaal7@gmail.com

If you like this, share it with as many people as you can :)
