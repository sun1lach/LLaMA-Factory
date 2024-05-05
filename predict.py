import os

for e in os.environ:
    print(e, " -> ", os.environ[e])

# import subprocess

# try:
#     subprocess.check_call(["pip", "install", "."])
#     subprocess.check_call(["pip", "freeze"])

# except subprocess.CalledProcessError as e:
#     print(f"Error running - {e}")


# from llmtuner.api.app import run_api


def predict(data):
    return f"In predict function - {data}"


# run_api()
