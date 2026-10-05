import pandas as pd

file_path = r"C:\workspace\Arrays\sleep_score\Sleep_Efficiency.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Number of records:", len(df))
print("\nColumns:")
print(df.columns.tolist())

df.columns = df.columns.str.strip()

print("\nCleaned columns:")
print(df.columns.tolist())


def duration_score(hours):

    if pd.isna(hours):
        return 0

    if 7 <= hours <= 9:
        return 25

    elif 6 <= hours < 7 or 9 < hours <= 10:
        return 20

    elif 5 <= hours < 6 or hours > 10:
        return 10

    else:
        return 0


def efficiency_score(efficiency):

    if pd.isna(efficiency):
        return 0

    score = efficiency * 30

    return min(max(score, 0), 30)


def range_score(value, lower, upper, maximum):

    if pd.isna(value):
        return 0

    if lower <= value <= upper:
        return maximum

    if value < lower:
        difference = lower - value
    else:
        difference = value - upper

    penalty = (difference / 5) * (maximum / 2)

    score = maximum - penalty

    return max(0, min(score, maximum))


def stage_score(light, deep, rem):

    light_score = range_score(
        light,
        lower=45,
        upper=60,
        maximum=10
    )

    deep_score = range_score(
        deep,
        lower=13,
        upper=23,
        maximum=12
    )

    rem_score = range_score(
        rem,
        lower=20,
        upper=30,
        maximum=13
    )

    total = light_score + deep_score + rem_score

    return total, light_score, deep_score, rem_score


def awakening_score(awakenings):

    if pd.isna(awakenings):
        return 0

    if awakenings == 0:
        return 10

    elif awakenings == 1:
        return 9

    elif awakenings == 2:
        return 7

    elif awakenings == 3:
        return 5

    elif awakenings == 4:
        return 3

    else:
        return 0


def classify_sleep(score):

    if score >= 85:
        return "Excellent"

    elif score >= 75:
        return "Good"

    elif score >= 65:
        return "Satisfactory"

    else:
        return "Bad"


def sleep_score_agent(row):

    duration = row["Sleep duration"]

    efficiency = row["Sleep efficiency"]

    light = row["Light sleep percentage"]

    deep = row["Deep sleep percentage"]

    rem = row["REM sleep percentage"]

    awakenings = row["Awakenings"]

    duration_points = duration_score(duration)

    efficiency_points = efficiency_score(efficiency)

    stage_points, light_points, deep_points, rem_points = stage_score(
        light,
        deep,
        rem
    )

    awakening_points = awakening_score(awakenings)

    total_score = (
        duration_points
        + efficiency_points
        + stage_points
        + awakening_points
    )

    total_score = min(max(total_score, 0), 100)

    category = classify_sleep(total_score)

    return pd.Series({

        "Duration Score": round(duration_points, 2),

        "Efficiency Score": round(efficiency_points, 2),

        "Light Sleep Score": round(light_points, 2),

        "Deep Sleep Score": round(deep_points, 2),

        "REM Sleep Score": round(rem_points, 2),

        "Stage Score": round(stage_points, 2),

        "Awakening Score": round(awakening_points, 2),

        "Sleep Score": round(total_score, 2),

        "Sleep Quality": category
    })


results = df.apply(sleep_score_agent, axis=1)

df_result = pd.concat([df, results], axis=1)


print("\n==============================================")
print("          SLEEP SCORE AGENT RESULTS")
print("==============================================")

print(
    df_result[
        [
            "Sleep duration",
            "Light sleep percentage",
            "Deep sleep percentage",
            "REM sleep percentage",
            "Sleep efficiency",
            "Awakenings",
            "Sleep Score",
            "Sleep Quality"
        ]
    ]
)


print("\n==============================================")
print("             10 SAMPLE RECORDS")
print("==============================================")

sample_10 = df_result.head(10)

print(
    sample_10[
        [
            "Sleep duration",
            "Light sleep percentage",
            "Deep sleep percentage",
            "REM sleep percentage",
            "Sleep efficiency",
            "Awakenings",
            "Sleep Score",
            "Sleep Quality"
        ]
    ]
)


print("\n==============================================")
print("          SLEEP QUALITY SUMMARY")
print("==============================================")

category_counts = df_result["Sleep Quality"].value_counts()

print(category_counts)


output_file = "Sleep_Score_Agent_Results.csv"

df_result.to_csv(output_file, index=False)

print("\nResults saved successfully as:")
print(output_file)