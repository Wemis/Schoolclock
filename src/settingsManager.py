def get_settings():
    return input(
        "Enter lesson titles separated by commas: "
    ).replace(" ", "").split(",")
