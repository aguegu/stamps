import logging
import os

from stamps.config import StampsConfiguration
from stamps.services import StampsService

logging.basicConfig()
logging.getLogger("suds.client").setLevel(logging.ERROR)

file_path = os.path.abspath(__file__)
directory_path = os.path.dirname(file_path)
file_name = os.path.join(directory_path, "stamps/tests.cfg")
configuration = StampsConfiguration(wsdl="testing", file_name=file_name)

service = StampsService(configuration=configuration)
account = service.get_account()
print account, type(account)

print account['Address']['FirstName']
