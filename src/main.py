import clock
import settingsManager
from types.lesson import to_list_lessons


def main():
    settings = settingsManager.get_settings()
    lessons = to_list_lessons(settings)
    clock.run(lessons)


if __name__ == "__main__":
    main()
