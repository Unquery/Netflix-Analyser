import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import Extractors as ex
import datetime as dt
import Decorators as de


def loadFile(url):
    """Loads a csv file from url"""
    response = requests.get(url)
    with open('NetflixActivity.csv', 'wb') as file:
         file.write(response.content)


def getDf():
    """Return a dataframe from csv"""
    df = pd.read_csv('NetflixActivity.csv')
    return df

@de.measure_time
def showSessionsDuringAMonth(date):
    """Shows sessions during the month since the given date"""
    try:
        df = getDf()
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        start_date = pd.to_datetime(date).date()
        end_date = start_date + dt.timedelta(weeks=4)
        df = df[(df['Start Time'].dt.date >= start_date) & (df['Start Time'].dt.date < end_date)]
        df['Hour'] = df['Start Time'].dt.hour
        df['Date'] = df['Start Time'].dt.date
        heatmap_data = df.groupby(['Date', 'Hour']).size().unstack(fill_value=0)
        heatmap_data = heatmap_data.reindex(columns=range(24), fill_value=0)
        plt.figure(figsize=(12, 8))
        sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt='d', cbar_kws={'label': 'Number of Sessions'})
        plt.ylabel('Date')
        plt.xlabel('Hour of Day')
        plt.title('Number of Sessions per Hour During the Week')
        plt.tight_layout()
        plt.show()
    except:
        print('There is no information with this date')

@de.measure_time
def showSessionsDuringAWeek(date):
    """Shows sessions during the week since the given date"""
    try:
        df = getDf()
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        start_date = pd.to_datetime(date).date()
        end_date = start_date + dt.timedelta(weeks=1)
        df = df[(df['Start Time'].dt.date >= start_date) & (df['Start Time'].dt.date < end_date)]
        df['Hour'] = df['Start Time'].dt.hour
        df['Date'] = df['Start Time'].dt.date
        heatmap_data = df.groupby(['Date', 'Hour']).size().unstack(fill_value=0)
        heatmap_data = heatmap_data.reindex(columns=range(24), fill_value=0)
        plt.figure(figsize=(12, 8))
        sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt='d', cbar_kws={'label': 'Number of Sessions'})
        plt.ylabel('Date')
        plt.xlabel('Hour of Day')
        plt.title('Number of Sessions per Hour During the Week')
        plt.tight_layout()
        plt.show()
    except:
        print('There is no information with this date')

@de.measure_time
def showSessionsDuringADay(date):
    """Shows sessions during the day"""
    try:
        df = getDf()
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df = df[df['Start Time'].dt.date == pd.to_datetime(date).date()]
        df['Hour'] = df['Start Time'].dt.hour
        sessions_per_hour = df.groupby('Hour').size()
        plt.figure(figsize=(12, 8))
        sessions_per_hour.plot(kind='bar', color='skyblue')
        plt.ylabel('Number of sessions')
        plt.xlabel('Hour of the day')
        plt.title(f'Number of Sessions Per Hour for {date}')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()
    except:
        print('There is no information with this date')

@de.measure_time
def showNumOfEpisodesWatched():
    """Shows the number of episodes watched by title"""
    df = getDf()
    df['Series Name'] = df['Title'].apply(ex.extract_series_name)
    df['Episode'] = df['Title'].apply(ex.extract_episode)
    number_of_episodes = df.groupby('Series Name')['Episode'].count()
    plt.figure(figsize=(12, 8))
    number_of_episodes.plot(kind='bar', color='skyblue')
    plt.ylabel('Number of episodes')
    plt.xlabel('Series Name')
    plt.title('Episodes watched in series')
    plt.xticks(rotation=45, ha='right')
    plt.show()

@de.measure_time
def showNumOfEpisodesWatchedByDevice():
    """Shows the number of episodes watched by device"""
    df = getDf()
    device_episodes_count = df.groupby('Device Type')['Title'].count()
    plt.figure(figsize=(12, 8))
    device_episodes_count.plot(kind='bar', color='skyblue')
    plt.ylabel('Number of episodes')
    plt.xlabel('Device Type')
    plt.title('Episodes watched on device')
    plt.xticks(rotation=45, ha='right')
    plt.yticks(range(0, max(device_episodes_count) + 10, 10))
    plt.show()

@de.measure_time
def showTitleToDuration():
    """Shows the duration watched of title"""
    df = getDf()
    df['Duration'] = pd.to_timedelta(df['Duration'])
    df['Series Name'] = df['Title'].apply(ex.extract_series_name)
    total_watched_time = df.groupby('Series Name')['Duration'].sum()
    total_watched_time_hours = total_watched_time.dt.total_seconds() / 3600
    plt.figure(figsize=(12, 8))
    total_watched_time_hours.plot(kind='bar', color='skyblue')
    plt.ylabel('Total Watched Time (hours)')
    plt.xlabel('Series Name')
    plt.title('Total Watched Time by Series Name')
    plt.xticks(rotation=45, ha='right')
    plt.show()

@de.measure_time
def showTimeWatchedByCountry():
    """Shows the time watched by country"""
    df = getDf()
    df['Country'] = df['Country']
    df['Duration'] = pd.to_timedelta(df['Duration'])
    total_watched_time = df.groupby('Country')['Duration'].sum()
    total_watched_time_hours = total_watched_time.dt.total_seconds() / 3600
    plt.figure(figsize=(12, 8))
    total_watched_time_hours.plot(kind='bar', color='skyblue')
    plt.ylabel('Total Watched Time (hours)')
    plt.xlabel('Country')
    plt.title('Total Watched Time by Country')
    plt.xticks(rotation=45, ha='right')
    plt.show()


@de.measure_time
def showUsersCountByCountry():
    """Shows the number of users by country"""
    df = getDf()
    number_of_users = df.groupby('Country')['Profile Name'].nunique()
    plt.figure(figsize=(12, 8))
    number_of_users.plot(kind='bar', color='skyblue')
    plt.ylabel('Number of Users')
    plt.xlabel('Country')
    plt.title('Users in Country')
    plt.xticks(rotation=45, ha='right')
    plt.yticks(range(0, max(number_of_users) + 10, 100))
    plt.show()


