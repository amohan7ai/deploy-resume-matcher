from langchain.chat_models import init_chat_model
from dotenv import load_dotenv


def get_job_match_model():
    print("Loading model...")
    load_dotenv()
    return init_chat_model(
    model="gpt-5.4-mini", 
)
