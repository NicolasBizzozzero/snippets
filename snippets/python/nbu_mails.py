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
