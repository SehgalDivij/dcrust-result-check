@echo off
echo Make sure your system is running python3.
echo If you are unable to set this up, try googling the error you receive and should you not find any solution, contact me at divij.sehgaal7@gmail.com
echo This will fetch  results of the main semester of all students, i.e, if you are currently an even semester student, it will inform you on the results of the last odd-semester exam and vice-versa
echo If you like this, do share it with as many students of dcrust as possible. To contribute or suggest new features email me @ divij.sehgaal7@gmail.com
echo Installing required packages
for %%x in (beautifulsoup4, requests) do (pip install %%x)
echo Enter info when asked to properly setup university Result Checker. False inputs may lead to unexpected results.
echo Make sure you enter the correct information for proper results.
rem: University Roll Number to check the result for.
SET /P university_roll=Enter University Roll Number:
rem: Password for the university account.
SET /P university_password=University Account Password: 
echo Enter Email Account to send alert from and receive alert to:
echo This stays within the application only. It is never shared;  View the source code on GitHub for more info.
rem: Email id to receive email from and deliver email to.
SET /P email_id=Enter Gmail Email ID: 
rem: Password for the entered GMAIL ID of the user.
SET /P email_password=Enter GMAIL Password: 
echo Details entered by you are:
echo University roll number: %university_roll%
echo University Password: %university_password%
echo Email id: %email_id%
echo Gmail id password: %email_password%
SET yes_str=y
SET no_str=n
:proceed_check
SET /P proceed=Proceed?[Enter y/n only]: 
if %proceed% == %yes_str% (
	echo Proceeding with Setup...
	python %cd%\result-fetch.py %university_roll% %university_password% %email_id% %email_password%
	schtasks /Create /SC HOURLY /TN DCRUST_RESULT_CHECK /ST 08:00 /ET 20:00 /TR "python %cd%\result-check.py %university_roll% %university_password% %email_id% %email_password%"
	goto end
) else (
	if %proceed% == %no_str% (
		echo Setup Cancelled. 
		echo This Program will now exit & echo No alerts have been setup
		goto end
	) else (
		echo Invalid Option. Please try again.
		goto proceed_check
	)
)
:end
PAUSE