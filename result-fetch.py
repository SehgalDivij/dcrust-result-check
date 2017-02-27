import ntpath
import os
import smtplib
import sys
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

import requests
from bs4 import BeautifulSoup


# parse and return body of html document, parsing with default html.parser
def get_body(html_doc):
    body = BeautifulSoup(html_doc, 'html.parser').find('body')
    if not body:
        return ''
    else:
        return body.prettify()


def alert_user(email="", pwd="", initial_setup=False, attachment=''):
    if initial_setup:
        SUBJECT = 'IMP: Successfully setup result alert.'
        body = 'Hola ' + email.split('@')[0] + ',\n\nIf you are receiving this email, you have successfully set up ' \
                                               'your university exam result alert.\nThis program will check the ' \
                                               'results at the university website every hour your device is switched ' \
                                               'on(The device you set this up on) and inform you if there are any ' \
                                               'changes to the default results page on the university website. For ' \
                                               'now, the current output of the results page is the result of the ' \
                                               'previous examinations and is attached in this email.\n\n In case of ' \
                                               'any issues, contact me @ divij.sehgaal7@gmail.com. Try to describe ' \
                                               'the problem as well as you can.\n\n Note: Do not delete the file ' \
                                               'created by the program @ C:\\results\\ or it may lead to unexpected ' \
                                               'behaviour '
    else:
        SUBJECT = 'IMP : DCRUST Result Status Changed.'
        body = 'Result out - Login to Check more details: http://www.dcrustedp.in/EDP/ or check out the attached file.'
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(body))
    with open(attachment, "r") as file:
        contents = file.read()
        print(contents)
        part = MIMEApplication(
            contents,
            Name=path_leaf(attachment)
        )
        part['Content-Disposition'] = 'attachment; filename="%s"' % path_leaf(attachment)
        msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, pwd)
    server.sendmail(email, email, msg.as_string())
    server.quit()


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def login():
    first_setup = False
    if len(sys.argv) < 4:
        print('Please enter arguments as follows:')
        print('1. University Roll Number')
        print('2. University Account Password')
        print('3. Gmail ID where the alert will be sent')
        print('4. Password of gmail id')
        print('5. Full path of file where the result would be saved.')
        print('An example execution would be:')
        print('python result-fetch.py <University-id> <University-id\'s password> <Gmail Username> <Gmail Password> '
              '<Full Path of file to create result to>')
        print('Note: 1. If no path is specified, the result will be saved to: C:\\results\\result_<University-id.html')
        print('      2. This program will not work for wrong credentials. Please verify credentials before proceeding.')
        print('      3. To schedule the execution of this script, perform setup as properly stated on GITHUB PAGE.')
        print('      4. The result saved to the results file will almost always be as per the most recent result\n'
              '         of the last main semester.')
        print('      5. Let me know of your suggestions and comments(and any bugs that arise) at \n'
              '         divij.sehgaal7@gmail.com.')
        sys.exit(0)
    page_01 = 'http://www.dcrustedp.in/EDP/'
    page_02 = 'http://www.dcrustedp.in/EDP/myexamlogin.php'
    page_03 = 'http://www.dcrustedp.in/EDP/checkexamlogin.php'
    after_login_01 = 'http://www.dcrustedp.in/EDP/studentpage.php'
    report_card = 'http://www.dcrustedp.in/EDP/reportcard.php'
    payload = {
        "Username": sys.argv[1],
        "Password": sys.argv[2]
    }
    usr_email = sys.argv[3]
    usr_password = sys.argv[4]
    current_session = requests.session()
    current_session.get(page_01)
    current_session.get(page_02)
    current_session.post(page_03, data=payload)
    current_session.get(after_login_01)
    r = current_session.get(report_card)
    fileStr = 'C:\\results\\result_' + sys.argv[1] + '_' + str(sys.argv[3]).split('@')[0] + '.html'
    if not os.path.exists(os.path.dirname(fileStr)):
        os.mkdir(os.path.dirname(fileStr))
    if not os.path.isfile(fileStr):
        print('File not found. Creating ' + path_leaf(fileStr))
        with open(fileStr, 'w+') as file_creator:
            first_setup = True
    old_res = open(fileStr, 'r')
    result_old = old_res.read().replace("\n", "").strip()
    result_new = r.text.replace("\n", "").strip()
    old_res.close()
    new_body = get_body(result_new)
    old_body = get_body(result_old)
    if old_body.strip() == new_body.strip():
        print('No changes in result.')
        pass
    else:
        with open(fileStr, 'w') as old_result:
            old_result.seek(0)
            old_result.truncate()
            old_result.write(result_new)
        # if not first_setup:
        alert_user(email=usr_email, pwd=usr_password, initial_setup=first_setup, attachment=fileStr)


login()
