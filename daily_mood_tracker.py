# Daily Mood Tracker - Final Project for Stanford Code in Place 2025
# Author: Badal Pal

import datetime  # Module to work with dates

def get_today_date():
    """Returns today's date as a string in YYYY-MM-DD format."""
    return datetime.date.today().strftime("%Y-%m-%d")

def main():
    mood_log = {}  # Dictionary to store mood by date

    while True:
        today = get_today_date()
        mood = input("How are you feeling today? (Happy/Sad/Excited/Angry/etc.): ").strip().capitalize()

        if today in mood_log:
            print("You've already recorded your mood today.")
        else:
            mood_log[today] = mood
            print(f"✅ Mood for {today} recorded as: {mood}")

        more = input("Do you want to add another day? (yes/no): ").strip().lower()
        if more != "yes":
            break

    # Count how many times each mood appears
    mood_count = {}
    for mood in mood_log.values():
        mood_count[mood] = mood_count.get(mood, 0) + 1

    # Display summary of moods
    print("\n📊 Mood Summary:")
    for mood, count in mood_count.items():
        print(f"{mood}: {count} day(s)")

    # Find the most frequent mood
    most_common = max(mood_count, key=mood_count.get)
    print(f"\n😊 Your most common mood is: {most_common}")

    # Save the mood report to a file
    with open("mood_report.txt", "w") as file:
        for date, mood in mood_log.items():
            file.write(f"{date}: {mood}\n")
        file.write("\nSummary:\n")
        for mood, count in mood_count.items():
            file.write(f"{mood}: {count} day(s)\n")
        file.write(f"\nMost common mood: {most_common}\n")

    print("\n📁 Mood report saved in 'mood_report.txt'")

if __name__ == '__main__':
    main()
