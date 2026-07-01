import os
import random
from datetime import datetime, timedelta

# ==========================
# Modifier la période ici
# ==========================
START_DATE = datetime(2025, 7, 1)
END_DATE   = datetime(2026, 6, 30)

FILE_NAME = "history.txt"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write("GitHub History\n")

current = START_DATE

while current <= END_DATE:

    weekday = current.weekday()  # 0=Lundi ... 6=Dimanche

    # --------------------------
    # Répartition réaliste
    # --------------------------

    if weekday < 5:      # Lundi → Vendredi
        commits = random.choices(
            population=[2,3,4,5,6,7,8,9,10],
            weights=[5,8,12,18,20,16,10,7,4],
            k=1
        )[0]

    elif weekday == 5:   # Samedi
        commits = random.choices(
            population=[1,2,3,4,5],
            weights=[10,25,35,20,10],
            k=1
        )[0]

    else:                # Dimanche
        commits = random.choices(
            population=[0,1,2,3],
            weights=[30,35,25,10],
            k=1
        )[0]

    for i in range(commits):

        hour = random.randint(8, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        commit_date = current.replace(
            hour=hour,
            minute=minute,
            second=second
        )

        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write(
                f"{commit_date.strftime('%Y-%m-%d %H:%M:%S')} - {random.randint(1000,9999)}\n"
            )

        os.system("git add history.txt")

        date = commit_date.strftime("%Y-%m-%dT%H:%M:%S")

        os.system(
            f'git commit --date="{date}" -m "Update {random.randint(1000,9999)}"'
        )

    current += timedelta(days=1)

print("Finished!")