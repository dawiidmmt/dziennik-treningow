# Workout Logger

A command-line workout logger written in **Python**. I use it at the gym to record every set I do. All data goes into a single CSV file, so it can later be analysed with pandas and used for machine learning.

## Features

- Start a training session with a name (e.g. `Lower1`); today's date is added automatically
- Choose exercises from a numbered list, so names are always spelled the same way
- Enter weight, reps and RIR (reps in reserve) for each set
- Shows your **last result** for the chosen exercise before you enter a new set
- Input validation: wrong values never crash the program, it simply asks again
  - weight accepts both `132.5` and `132,5`
  - reps must be between 1 and 50, RIR between 0 and 10
- Summary at the end: number of sets and total volume (weight × reps)
- Saves everything to `dziennik.csv`; the header is written only once

## Data format

One row = one set. Every row describes itself, so the file is ready for pandas:

| date       | trening | exercise | weight | reps | rir |
|------------|---------|----------|--------|------|-----|
| 2026-11-03 | Lower1  | Squat    | 130.0  | 5    | 1   |
| 2026-11-03 | Lower1  | Squat    | 130.0  | 5    | 1   |

## Project structure

```
dziennik_treningow.py   # main program: classes, helper functions, main()
exercises.py            # list of exercises (EXERCISES)
dziennik.csv            # workout data (created on first save)
```

## How to run

No external libraries are needed, only Python 3.

```bash
git clone https://github.com/dawiidmmt/workout-logger.git
cd workout-logger
python3 gym_tracker.py
```

To test without touching your real data, change `DIARY_PATH` at the top of the file to `"test.csv"`.

## What I learned

- Designing classes (`Trening` and `Seria`) and deciding which data belongs where
- Separating data from display: methods return values, printing happens in `main()`
- Reading and writing CSV files (`csv.writer`, `csv.DictReader`, append mode)
- Writing reusable helper functions with `try`/`except` that ask until the input is valid
- Structuring a program: imports, classes, functions, `main()` and `if __name__ == "__main__"`

## Roadmap

- [x] Stage 1: logger in pure Python (classes, menu, CSV)
- [ ] Main menu: new training / show history / quit
- [ ] Save after every set, so nothing is lost if the program is closed
- [ ] Stage 2: progress analysis and charts with pandas and matplotlib
- [ ] Stage 3: predicting the next working weight or a training plateau with scikit-learn
