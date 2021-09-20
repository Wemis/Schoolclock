def get_settings():
    lessons = input(
        "Enter lesson titles separated by commas: "
    ).replace(" ", "").split(",")

    return lessons