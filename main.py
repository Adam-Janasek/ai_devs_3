import logging
import os
import sys

import openai
from dotenv import load_dotenv

from console import main

load_dotenv()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

openai.api_key = os.getenv('OPENAI_API_KEY')

if __name__ == '__main__':
    main()
