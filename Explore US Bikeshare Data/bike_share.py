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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter the city you want \n"city must be one of (chicago, new york city, washington)."\n>>').lower()
        if city in CITY_DATA.keys():
            break
        print(city, 'is invalid')

    # get user input for month (all, january, february, ... , june)
    ALLOWED_MONTHES = ['january', 'february', 'march', 'may', 'june', 'all']
    while True:
        month = input('Enter the month you want \n"month must be one of (all, january, february, ... , june)."\n>>').lower()
        if month in ALLOWED_MONTHES:
            break
        print(month, 'is invalid')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS = ['monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input('Enter the day of week you want \n"day must be one of (all, monday, tuesday, ... sunday)."\n>>').lower()
        if day in DAYS:
            break
        print(month, 'is invalid')

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
    df = pd.read_csv(CITY_DATA[city])
    # Convert Start Time to datetime formate and extract month to new colunm
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract months from Strat Time to new colunm 
    df['month'] = df['Start Time'].dt.month
    
    # Extract day of week from Start Time to new colunm
    df['day'] = df['Start Time'].dt.day_name()
    # Filter to get required month
    if month != 'all':
        # Get month corresponding number
        MONTHS = ['january', 'february', 'march', 'april','may', 'june']
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]
    
    # Filter to get required day
    if day != 'all':
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # Convert Start Time colunm to datetime formate
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    print('The most common momth is:', df['month'].mode()[0])

    # display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    print('The most common day of week is:', df['day'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour in day is:', df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The Most Start Station is:',common_start_station) 

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The Most Common End Station is:',common_end_station)     

    # display most frequent combination of start station and end station trip
    print(f'The Most Frequent Combination Of Start Station and End Station is: ({common_start_station} and {common_end_station}).')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The Total Travel Time is:', df['Trip Duration'].sum())

    # display mean travel time
    print('The Mean Travel Time is:', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count Of User Types is\n{}'.format(df['User Type'].value_counts()))

    # Display counts of gender
    if 'Gender' in df.columns or 'Birth Year' in df.columns:
        print('Count Of User Types is\n{}'.format(df['Gender'].value_counts()))
    else:
        print('There is no any data about gender in this city.')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Count of birth years is\n{}'.format(df['Birth Year'].value_counts()))
    else:
        print('There is no data about birth year in this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def read():
    while True:
        read = input('Do You Want To read some rows in data[yes/no]\n>> ').lower()
        if read == 'yes':
            while True:
                city = input('What is city do you want [chicago, new york city, washington]\n>> ').lower()
                if city in CITY_DATA:
                    break
                else:
                    print('Invalid city ):')
                for chunk in pd.read_csv(CITY_DATA[city], chunksize=5):
                    print(chunk)
                more = input('Do you want to explore more[yes/no]\n>> ').lower()
                if more != 'yes':
                    break

        else:
            break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        read()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
