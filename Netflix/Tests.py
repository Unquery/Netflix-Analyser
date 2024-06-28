import PlotMethods as pm
import matplotlib.pyplot as plt


def showExecionTime():
    """"Shows execution time of all plot maker methods"""
    functions = [
            ("Sessions in a Day", lambda: pm.showSessionsDuringADay('2013-03-01')),
            ("Sessions in a Week", lambda: pm.showSessionsDuringAWeek('2013-03-01')),
            ("Sessions in a Month", lambda: pm.showSessionsDuringAMonth('2013-03-01')),
            ("Duration watched by Title", pm.showTitleToDuration),
            ("Number of episodes watched by Serial", pm.showNumOfEpisodesWatched),
            ("Number of episodes watched on Device", pm.showNumOfEpisodesWatchedByDevice),
            ("Duration watched by Country", pm.showTimeWatchedByCountry),
            ("Users count by Country", pm.showUsersCountByCountry)
    ]

    times = {
        'Name': [],
        'Time': []
    }

    for (title, func) in functions:
        times.get('Name').append(title)
        times.get('Time').append(func())

    plt.figure(figsize=(10, 6))
    plt.bar(times['Name'], times['Time'], color='blue')
    plt.xlabel('Function name')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time of Functions')
    plt.xticks(rotation=15, ha='right',fontsize=6)
    plt.show()

