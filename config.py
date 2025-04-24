import os 

from dotenv import load_dotenv # type: ignore

# .env file load karo
load_dotenv()

# Environment variables uthao
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")