import os

# Judge criteria (from competition.yaml judge brief, most important first):
# 1. About office life and lands as a joke
# 2. Observation true to the office (meetings, email, bosses, coffee, deadlines, printer)
# 3. Turn is surprising (fresh angle / unexpected last word, not a pun or stock line)
# 4. Tight: one line, no wasted setup, reads cleanly aloud in one breath
# 5. Original: not a familiar line with the nouns swapped
#
# Draft candidates (my own, scored 1-5 per criterion above):
#
# Candidate A: "My boss called a meeting to ask why our meetings take so long, then scheduled a follow-up to discuss it."
#   Scores: 1=5, 2=5, 3=3, 4=4, 5=2  Total=19  (true, but the meeting-about-meetings loop is a stock angle)
#
# Candidate B: "The printer only jams when the deadline is in ten minutes, as if it also needs the pressure to perform."
#   Scores: 1=5, 2=5, 3=3, 4=4, 5=3  Total=20  (printer/deadline nod is strong, turn is gentle rather than surprising)
#
# Candidate C: "The fastest way to get an answer at work is to email the wrong person — suddenly three departments care."
#   Scores: 1=5, 2=5, 3=5, 4=4, 5=4  Total=23  (email truth, the wrong-recipient turn flips the expectation)
#
# Candidate D: "I don't need a gym membership; I get my cardio chasing the boss who says 'quick question' and walks away."
#   Scores: 1=4, 2=4, 3=3, 4=3, 5=3  Total=17  (boss observation lands, but setup is wordy for one breath)
#
# Winner: Candidate C — highest total, strongest on the top-weighted criteria
# (office subject, true observation, surprising turn).

LINE = "The fastest way to get an answer at work is to email the wrong person — suddenly three departments care."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
