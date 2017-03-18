"""

Sending mails behind a proxy with the smtp protocol can be tricky.
A few links to help you achieve this:
Python smtplib proxy support - Stack Overflow
http://stackoverflow.com/questions/5239797/python-smtplib-proxy-support
Python send email behind a proxy server - Stack Overflow
http://stackoverflow.com/questions/29830104/python-send-email-behind-a-proxy-server
Sending mail through python script using IITB proxy - Google Groupes
https://groups.google.com/forum/#!topic/wncc_iitb/-fORoSmFhXo
Sending mail through python script using IITB proxy - Google Groupes
https://groups.google.com/forum/#!topic/wncc_iitb/-fORoSmFhXo
"""
from nbu_decorators import todo_implement


@todo_implement
def delete_all_emails(email_adress: str) -> None:
    """ Delete all emails in the mailbox of 'email_adress'. """
    pass


@todo_implement
def delete_all_emails_from(email_adress: str, sender: str) -> None:
    """ Delete all emails in the mailbox of 'email_adress' sended
        by 'sender '.
    """
    pass


@todo_implement
def send_email(source_adress: str, destination_adress: str,
               content: str) -> None:
    """ Send an email containting 'content' from 'source_adress'
        to 'destination_adress'.
    """
    pass


if __name__ == '__main__':
    pass
