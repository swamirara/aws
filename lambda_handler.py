def get_personal_data(event, context):
    return {
        "name": "Swamirara",
        "dob": "1992-01-01",
        "nationality": "Indian",
        "gender": "Male",
    }


def get_gender(event, context):
    print(event)
    person_data = event['AWS_STEP_FUNCTIONS_STARTED_BY_EXECUTION_INPUT']
    return {"gender": person_data["gender"]}

