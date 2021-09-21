from types.lesson import Lesson, to_list_lessons
import settingsManager
import clock


def main():
    settings = settingsManager.get_settings()
    lessons = to_list_lessons(settings)
    clock.run(lessons)


if __name__ == "__main__":
    main()
