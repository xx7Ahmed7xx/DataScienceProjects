import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Gets city input
    city = input("Specify city: ").lower()
    while city not in ('Wrong city, choose from chicago, new york city or washington'):
        print('Wrong city, choose from chicago, new york city or washington')
        city = input("Specify city: ").lower()
        if city in ('new york city', 'chicago', 'washington'):
            break

    # Ask for filtering by month and day or not
    filtermd = input("Would you like to filter the data by month, day, both, or not at all? Type none for no time filtering: ").lower()
    while filtermd not in (None, '', 'month', 'day', 'both', 'none'):
        print('Wrong input, try again!')
        filtermd = input("Would you like to filter the data by month, day, both, or not at all? Type none for no time filtering: ").lower()
    
    if (filtermd == 'month'):
        # Gets month input
        month = input("Specify month: ").lower()
        while month not in (None, '', 'january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('Wrong month, try again!')
            month = input("Specify month: ").lower()
        day = None
    elif (filtermd == 'day'):
        # Gets day input
        day = input("Specify day: ").lower()
        while day not in (None, '', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('Wrong day, try again!')
            day = input("Specify day: ").lower()
        month = None
    elif (filtermd == 'both'):
        # Gets month input
        month = input("Specify month: ").lower()
        while month not in (None, '', 'january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('Wrong month, try again!')
            month = input("Specify month: ").lower()
        # Gets day input
        day = input("Specify day: ").lower()
        while day not in (None, '', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('Wrong day, try again!')
            day = input("Specify day: ").lower()
    elif (filtermd == 'none'):
        month = 'all'
        day = 'all'

    

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Choose dataframe
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Prepare new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()


    # Filter by Month if possible
    if month not in ('all', None):
        # Get index of Month
        months = ('january', 'february', 'march', 'april', 'may', 'june')
        month = months.index(month) + 1

        # Filter by Month
        df = df[df['Month'] == month]

    # filter by day if possible
    if day not in ('all', None):
        # filter by Day
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('Calculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # Show the most common Month , useless if month is filtered though
    months = ('january', 'february', 'march', 'april', 'may', 'june')
    print("The most common Month is " + months[df['Month'].mode()[0] - 1])

    # Show the most common Day , useless if day is filtered though
    print("The most common Day  is " + df['Day of Week'].mode()[0])

    # Show the most common Start Hour
    df['Hour'] = df['Start Time'].dt.hour
    print("The most common Start Hour is " + str(df['Hour'].mode()[0]))

    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # Show most common used Start Station
    print("The most commonly used Start Station is " + df['Start Station'].mode()[0])

    # Show most common used End Station
    print("The most commonly used End Station is " + df['End Station'].mode()[0])

    # Show most common combination of Start Station and End Station trip
    df['Combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of Start Station and End Station trip is: " + df['Combination'].mode()[0])

    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('Calculating Trip Duration...')
    start_time = time.time()

    # display total travel time
    print("The total travel time is " + str(df['Trip Duration'].sum()))

    # display mean travel time
    print("The total mean time is " + str(df['Trip Duration'].mean()))

    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('Calculating User Stats...')
    start_time = time.time()

    # Display Number of User Types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types)

    # Display Number of each Gender
    gender = df.groupby(['Gender'])['Gender'].count()
    print(gender)

    # Display earliest, most recent, and most common year of birth
    MostRecent = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
    Earliest = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
    CommonBirth = df['Birth Year'].mode()[0]
    print("The earliest year of birth is " + str(Earliest))
    print("The most recent year of birth is " + str(MostRecent))
    print("The most common year of birth is " + str(CommonBirth))

    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    x = 1
    raw = input('Would you like to see some raw data? Enter yes or no: ')
    if raw.lower() == 'no':
        pass
    while raw.lower() not in (None, ''):
        if raw.lower() == 'no':
            break
        if raw.lower() == 'yes':
            print(df[x : x + 5])
            x = x + 5
            raw = input('Would you like to see some raw data? Enter yes or no: ')
        else:
            print('Wrong input, either enter yes or no!')
            raw = input('Would you like to see some raw data? Enter yes or no: ')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('Would you like to restart? Enter yes or no: ')
        if restart.lower() == 'no':
            break
        if restart.lower() == 'yes':
            pass
        while restart not in ('yes', 'no'):
            print('Wrong answer, only Yes or No allowed!')
            restart = input('Would you like to restart? Enter yes or no: ')
            if restart.lower() == 'no':
                break
            if restart.lower() == 'yes':
                pass
        if restart.lower() == 'no':
            break
            

            


if __name__ == "__main__":
	main()
