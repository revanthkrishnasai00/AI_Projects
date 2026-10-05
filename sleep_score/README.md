# Sleep Score Agent

## 1. Project Overview

The **Sleep Score Agent** is a rule-based intelligent agent that
evaluates sleep quality from a CSV dataset.

The agent reads sleep-related parameters for each record, calculates
individual component scores, combines them into a final **Sleep Score
out of 100**, and classifies the result into one of four categories:

Sleep Score Sleep Quality

---

85--100 Excellent
75--84.99 Good
65--74.99 Satisfactory
0--64.99 Bad

The project uses **Python and Pandas**.

---

## 2. Objectives

The main objectives of the agent are:

1.  Read sleep data from a CSV file.
2.  Clean the column names.
3.  Calculate a score for sleep duration.
4.  Calculate a score for sleep efficiency.
5.  Evaluate the distribution of Light, Deep, and REM sleep.
6.  Calculate an awakening score.
7.  Combine all component scores into a Sleep Score between 0 and 100.
8.  Classify the sleep quality.
9.  Display the results.
10. Save the calculated results to a new CSV file.

---

## 3. Input Dataset

The input file is:

Sleep_Efficiency.csv

The dataset used in this project contains **452 records** and the
following columns:

ID
Age
Gender
Bedtime
Wakeup time
Sleep duration
Sleep efficiency
REM sleep percentage
Deep sleep percentage
Light sleep percentage
Awakenings
Caffeine consumption
Alcohol consumption
Smoking status
Exercise frequency

The agent uses these columns:

Sleep duration
Sleep efficiency
REM sleep percentage
Deep sleep percentage
Light sleep percentage
Awakenings

The other columns remain in the original dataset but are not currently
used in the scoring calculation.

---

## 4. Requirements

Install Python 3.x and Pandas.

Install Pandas using:

bash
pip install pandas

No NumPy library is required for the current version of the program.

---

## 5. Project Structure

Recommended folder structure:

sleep_score/
│
├── main.py
├── Sleep_Efficiency.csv
└── Sleep_Score_Agent_Results.csv

`main.py` contains the agent code.

`Sleep_Efficiency.csv` is the input dataset.

`Sleep_Score_Agent_Results.csv` is generated automatically after
execution.

---

## 6. How to Run

Open PowerShell or the VS Code terminal.

Move to the project directory:

bash
cd C:\workspace\Arrays\sleep_score

Run the program:

bash
python main.py

The program will:

1.  Load the CSV.
2.  Process all records.
3.  Calculate the sleep scores.
4.  Display the results.
5.  Display the first 10 records.
6.  Display the number of records in each sleep-quality category.
7.  Create `Sleep_Score_Agent_Results.csv`.

---

# 7. Agent Architecture

The agent follows this flow:

Sleep_Efficiency.csv
|
v
Load Dataset
|
v
Clean Column Names
|
v
Read One Sleep Record
|
+-------------------+
| |
v v
Sleep Duration Sleep Efficiency
Score /25 Score /30
| |
+---------+---------+
|
v
Sleep Stages
Score /35
|
v
Awakenings /10
|
v
Combine Component Scores
|
v
Sleep Score /100
|
v
Sleep Quality Category

The `sleep_score_agent()` function is the main decision-making
component.

---

# 8. Scoring Method

The maximum score is 100.

Component Maximum Score

---

Sleep Duration 25
Sleep Efficiency 30
Sleep Stages 35
Awakenings 10
**Total** **100**

Therefore:

25 + 30 + 35 + 10 = 100

---

## 9. Sleep Duration Score

The `duration_score()` function evaluates the number of hours slept.

Sleep Duration Score

---

7--9 hours 25
6 to \<7 hours 20
\>9 to 10 hours 20
5 to \<6 hours 10
\>10 hours 10
\<5 hours 0
Missing value 0

Examples:

8 hours -> 25
6.5 hours -> 20
5.5 hours -> 10
4 hours -> 0

---

## 10. Sleep Efficiency Score

The dataset stores sleep efficiency as a decimal between 0 and 1.

Examples:

0.88 = 88%
0.81 = 81%
0.91 = 91%
0.76 = 76%

The formula used is:

Efficiency Score = Sleep Efficiency × 30

Examples:

0.88 × 30 = 26.4
0.81 × 30 = 24.3
0.91 × 30 = 27.3
0.76 × 30 = 22.8

The score is restricted to the range 0--30.

---

## 11. Sleep Stage Score

Sleep stage scoring contributes a maximum of 35 points.

Sleep Stage Reference Range Maximum

---

Light Sleep 45--60% 10
Deep Sleep 13--23% 12
REM Sleep 20--30% 13
**Total** **35**

The agent does not simply assume that more deep sleep is always better.

Instead, it checks whether each sleep-stage percentage is within the
defined reference range.

### Inside the range

The full score is awarded.

For example:

Deep sleep = 18%
Reference = 13–23%

18 is inside the range
Therefore: 12/12

### Outside the range

A gradual penalty is applied based on the distance from the reference
range.

The formula is:

Penalty = (Difference / 5) × (Maximum / 2)

Score = Maximum - Penalty

The final score is restricted between 0 and the component maximum.

---

## 12. Awakening Score

The awakening score contributes a maximum of 10 points.

    Number of Awakenings   Score

---

                       0      10
                       1       9
                       2       7
                       3       5
                       4       3
               5 or more       0
           Missing value       0

The general idea is that fewer awakenings indicate better sleep
continuity.

---

# 13. Final Sleep Score

The final score is calculated as:

Sleep Score =
Duration Score

- Efficiency Score
- Stage Score
- Awakening Score

The score is then restricted to:

0 ≤ Sleep Score ≤ 100

---

# 14. Sleep Quality Classification

The `classify_sleep()` function converts the numerical score into a
category.

Score >= 85
-> Excellent

Score >= 75
-> Good

Score >= 65
-> Satisfactory

Score < 65
-> Bad

For example:

92.5 -> Excellent
80.0 -> Good
68.5 -> Satisfactory
55.0 -> Bad

---

# 15. Main Agent Function

The main agent is:

python
def sleep_score_agent(row):

It receives one dataset row and performs the following steps:

1. Read sleep duration
2. Read sleep efficiency
3. Read Light sleep percentage
4. Read Deep sleep percentage
5. Read REM sleep percentage
6. Read Awakenings
7. Calculate individual scores
8. Add the scores
9. Restrict the total to 0–100
10. Classify the sleep quality
11. Return the result

# 16. Output

The program adds the following calculated columns:

Duration Score
Efficiency Score
Light Sleep Score
Deep Sleep Score
REM Sleep Score
Stage Score
Awakening Score
Sleep Score
Sleep Quality

The complete result is saved as:

Sleep_Score_Agent_Results.csv

---

# 17. Test Cases

The following test cases verify the main scoring functions and the complete Sleep Score Agent.

## Test Case 1 — Ideal Sleep Duration

**Input:**

```text
Sleep duration = 8 hours
```

**Expected:**

```text
Duration Score = 25
```

**Reason:**

8 hours is within the target range of 7–9 hours.

---

## Test Case 2 — Sleep Efficiency

**Input:**

```text
Sleep efficiency = 0.88
```

**Expected:**

```text
Efficiency Score = 26.4
```

**Calculation:**

```text
0.88 × 30 = 26.4
```

This verifies that the agent correctly handles efficiency values stored between 0 and 1.

---

## Test Case 3 — Ideal Sleep Stages

**Input:**

```text
Light sleep = 50%
Deep sleep = 18%
REM sleep = 25%
```

**Expected:**

```text
Light Sleep Score = 10
Deep Sleep Score = 12
REM Sleep Score = 13
Stage Score = 35
```

**Reason:**

All three values are within their defined reference ranges.

---

## Test Case 4 — Awakening Score

**Input:**

```text
Awakenings = 3
```

**Expected:**

```text
Awakening Score = 5
```

This verifies that the agent correctly applies the awakening scoring rules.

---

## Test Case 5 — Excellent Sleep

**Input:**

```text
Sleep duration = 8
Sleep efficiency = 1.00
Light sleep = 50
Deep sleep = 18
REM sleep = 25
Awakenings = 0
```

**Expected Component Scores:**

```text
Duration Score = 25
Efficiency Score = 30
Stage Score = 35
Awakening Score = 10
```

**Final Score:**

```text
25 + 30 + 35 + 10 = 100
```

**Expected Result:**

```text
Sleep Score = 100
Sleep Quality = Excellent
```

This verifies the maximum possible score of the agent.

---

## Test Case 6 — Good Sleep

**Input:**

```text
Sleep duration = 6
Sleep efficiency = 0.88
Light sleep = 45
Deep sleep = 23
REM sleep = 20
Awakenings = 4
```

**Expected Component Scores:**

```text
Duration Score = 20
Efficiency Score = 26.4
Stage Score = 35
Awakening Score = 3
```

**Final Score:**

```text
20 + 26.4 + 35 + 3 = 84.4
```

**Expected Result:**

```text
Sleep Score = 84.4
Sleep Quality = Good
```

This verifies the overall score calculation and quality classification.

---

## Test Case 7 — Bad Sleep

**Input:**

```text
Sleep duration = 4
Sleep efficiency = 0.50
Light sleep = 10
Deep sleep = 70
REM sleep = 20
Awakenings = 5
```

**Expected:**

```text
Duration Score = 0
Efficiency Score = 15
Light Sleep Score = 0
Deep Sleep Score = 0
REM Sleep Score = 13
Awakening Score = 0
Sleep Quality = Bad
```

This verifies that the agent can identify a poor sleep record.

# 18. Conclusion

The Sleep Score Agent demonstrates a simple **rule-based
intelligent-agent approach**.

The agent:

Perceives
↓
Sleep-related input values

Processes
↓
Predefined scoring rules

Decides
↓
Sleep Score

Classifies
↓
Excellent / Good / Satisfactory / Bad

The final score provides both an overall sleep-quality classification
and individual component scores, making the agent's decision easier to
understand and verify.
