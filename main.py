import requests
from datetime import datetime
import os

GENDER = "female"
WEIGHT = 48.5
HEIGHT = 166
AGE = 16

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

TOKEN = os.environ["TOKEN"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_params = {
    "query": input("What exercises did you do? "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=exercise_params, headers=headers)
exercise_data = response.json()["exercises"][0]

exercise = exercise_data["name"].title()
duration = exercise_data["duration_min"]
calories = exercise_data["nf_calories"]

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

ggl_sheet_endpoint = os.environ["SHEET_ENDPOINT"]

workout_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

workout_params = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

add_row_response = requests.post(url=ggl_sheet_endpoint, json=workout_params, headers=workout_headers)
# print(add_row_response.text)
