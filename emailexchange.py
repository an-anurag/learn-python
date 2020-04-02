from exchangelib import DELEGATE, Account, Credentials, Configuration

# pip install exchangelib

username = ""
password = ""
server = ""
email = ""

# Get Exchange account connection with server
# :param username: Usernames for authentication are of one of these forms:
# * PrimarySMTPAddress
# * WINDOMAIN\\username
# * User Principal Name (UPN)
# :param password: Clear-text password

creds = Credentials(username=username, password=password)

# :param primary_smtp_address: The primary email address associated with the account on the Exchange server
# :param credentials: A Credentials object containing valid credentials for this account.
# :param autodiscover: Whether to look up the EWS endpoint automatically using the autodiscover protocol.
# :param access_type: The access type granted to 'credentials' for this account. Valid options are 'delegate'
account = Account(
    primary_smtp_address=server,
    credentials=creds,
    autodiscover=True,
    access_type=DELEGATE)

# Print first 5 inbox messages in reverse order
for item in account.inbox.all().order_by('-datetime_received')[:5]:
    print(item.subject, item.body)

# creds = Credentials(username=username, password=password)
# config = Configuration(server=server, credentials=creds)
# account = Account(primary_smtp_address=email, autodiscover=False, config=config, access_type=DELEGATE)
#
# for item in account.inbox.all().order_by('-datetime_received')[:10]:
#     print(item.subject, item.body)
