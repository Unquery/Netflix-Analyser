import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import re

def loadFile(url):
    response = requests.get(url)
    with open('NetflixActivity.csv', 'wb') as file:
         file.write(response.content)


def getDf():
    df = pd.read_csv('NetflixActivity.csv')
    return df


def extract_series_name(title):
    return re.sub(r'\:.*|\(.*\)', '', title).strip()


def extract_episode(title):
    return re.sub(r'^.*Season \d+: ', '', title).strip()


def showNumOfEpisodesWatched():
    df = getDf()
    df['Series Name'] = df['Title'].apply(extract_series_name)
    df['Episode'] = df['Title'].apply(extract_episode)
    number_of_episodes = df.groupby('Series Name')['Episode'].count()
    plt.figure(figsize=(12, 8))
    number_of_episodes.plot(kind='bar', color='skyblue')
    plt.ylabel('Number of episodes')
    plt.xlabel('Series Name')
    plt.title('Episodes watched in series')
    plt.xticks(rotation=45, ha='right')
    plt.show()


def showNumOfEpisodesWatchedByDevice():
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


def showTitleToDuration():
    df = getDf()
    df['Duration'] = pd.to_timedelta(df['Duration'])
    df['Series Name'] = df['Title'].apply(extract_series_name)
    total_watched_time = df.groupby('Series Name')['Duration'].sum()
    total_watched_time_hours = total_watched_time.dt.total_seconds() / 3600
    plt.figure(figsize=(12, 8))
    total_watched_time_hours.plot(kind='bar', color='skyblue')
    plt.ylabel('Total Watched Time (hours)')
    plt.xlabel('Series Name')
    plt.title('Total Watched Time by Series Name')
    plt.xticks(rotation=45, ha='right')
    plt.show()

def showTimeWatchedByCountry():
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


def showUsersCountByCountry():
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


