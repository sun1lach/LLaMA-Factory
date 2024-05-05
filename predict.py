from llmtuner.api.app import run_api

def predict(data):
    return f"In predict function - {data}"

run_api()