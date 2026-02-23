import fastf1
import fastf1.plotting
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

fastf1.plotting.setup_mpl()

"""year = 2020
race = "Belgian Grand Prix"
"""
session = fastf1.get_session(year, race, 'R')
session.load()

laps = session.laps
laps = laps.sort_values(['Driver', 'LapNumber'])
laps['LapTimeSeconds'] = laps['LapTime'].dt.total_seconds()
print(laps.head())

laps.to_csv("laps_preview.csv", index=False)

# COMPOUND COLOR MAP
COMPOUND_COLORS = {
    'SOFT': '#FF3333',
    'MEDIUM':'#FFD700',
    'HARD':'#C6BFBF',
    'INTERMEDIATE':'#39B54A',
    'WET' : '#0077FF'
}

#Race Strategy

finishing_order = session.results.sort_values('Position')['Abbreviation'].tolist()
drivers = finishing_order[::-1] #P1 at bottom

results = session.results
dnf_drivers = session.results[
    (session.results['Position'].isna()) |
    (session.results['Status'].str.contains('Accident|Engine|Retired|Gearbox', na=False))
    ]['Abbreviation'].tolist()

y_positions = {driver: i for i, driver in enumerate(drivers)}

fig,ax = plt.subplots(figsize=(14,10))

for driver in drivers:
    driver_laps = laps[laps['Driver'] == driver]

    driver_laps = driver_laps.copy()
    driver_laps['PitStop'] = driver_laps['PitInTime'].notna()
    driver_laps['RebuiltStint'] = driver_laps['PitStop'].cumsum()

    stints = driver_laps.groupby('RebuiltStint')

    # stints = driver_laps.groupby('Stint')

    alpha = 0.35 if driver in dnf_drivers else 1.0
    y = y_positions[driver]

    for stint, data in stints:
        compound = data['Compound'].mode()[0]
        width = data['LapNumber'].max() - data['LapNumber'].min() + 1

        ax.barh(
            y,
            width,
            left = data['LapNumber'].min(),
            color = COMPOUND_COLORS.get(compound, '#AAAAAA'),
            alpha = alpha
        )

    #Pit stop markers
    pit_laps = driver_laps.loc[
        driver_laps['Stint'].diff() == 1, 'LapNumber'
    ]

    for lap in pit_laps:
        ax.plot(lap, y, marker='o', color='black', markersize = 3, zorder = 6)
        ax.vlines(
            lap,
            y - 0.4,
            y + 0.4,
            colors = 'black',
            linestyles= 'dashed',
            linewidth = 1.5,
            alpha = 0.8,
            zorder = 5
        )

#Fix y-axis label
ax.set_yticks(range(len(drivers)))
ax.set_yticklabels(drivers)

ax.set_xlabel("Lap Number")
ax.set_ylabel("Driver")
ax.set_title("Race Strategy Visualization")
plt.grid(axis='x', linestyle='--', alpha=0.4)
plt.show()
