import os

from dotenv import load_dotenv
from script import connect

load_dotenv()

PASSWORD = os.getenv("PASS")

result = connect (PASSWORD)

print(result)
