import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york city', 'washington']
FILTERS = ['month', 'day', 'both', 'all']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
RAW_DATA = ['yes', 'no']
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
        city = input('Would you like to see data for Chicago, New York City, or Washington?').lower()
        if city in CITIES:
            break
        else:
            print('That\'s not a valid input')
    #get user input for filter preferences (month, day, both, or all)
    while True:
        datefilter = input('Would you like to filter the data by month, day, both, or not at all? Type "all" for no time filter.').lower()
        if datefilter in FILTERS:
            break
        else:
            print('That\'s not a valid input')
    # get user input for month (all, january, february, ... , june)
    if datefilter == 'all':
        month = 'all'
        day = 'all'
    if datefilter == "month":
        day = 'all'
        while True:
            month = input('Which month? January, February, March, April, May, or June? (Months after June are not included in dataset)').lower()
            if month in MONTHS:
                break
            else:
                print('That\'s not a valid input')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    if datefilter == "day":
        month ='all'
        while True:
            day = input('Which day? (e.g., "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")').lower()
            if day in DAYS:
                break
            else:
                print('That\'s not a valid input')
    # get user input when filter prefence is both (month and day of the week)
    if datefilter == "both":
        while True:
            month = input('Which month? January, February, March, April, May, or June?').lower()
            if month in MONTHS:
                break
            else:
                print('That\'s not a valid input')
        while True:
            day = input('Which day? (e.g., "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")').lower()
            if day in DAYS:
                break
            else:
                print('That\'s not a valid input')
    print('-'*40)
    print("filters: ", city, month, day)
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour_of_day'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

df = load_data('chicago', 'march', 'friday')

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month= df['month'].mode()[0]
    print('The most common month in this dataset is:', most_common_month)
    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common weekday in this dataset is:', most_common_day_of_week)
    # display the most common start hour
    most_common_start_hour = df['hour_of_day'].mode()[0]
    print('The most common hour in this dataset is:', most_common_start_hour)
    #display query execution time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common starting station is: ', most_common_start_station)
    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common ending station is: ', most_common_end_station)
    # display most frequent combination of start station and end station trip
    most_common_station_combination = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most common start and end station combination is: {}, {}'.format(most_common_station_combination[0], most_common_station_combination[1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print('The total travel time in your query is: ', total_travel_time)
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time in your query is: ', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    for i, user_type_count in enumerate(user_type_counts):
        print('The counts of {} in this query are: '.format(user_type_counts.index[i]), user_type_count)
    # Display counts of gender
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' and 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        for i, gender_count in enumerate(gender_counts):
            print('The counts of {} gender in this query are: '.format(gender_counts.index[i]), gender_count)
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest birth year in this query is: ', int(earliest_birth_year))
        most_recent_birth_year = df['Birth Year'].max()
        print('The most recent birth year in this query is: ', int(most_recent_birth_year))
        most_common_birth_year = df['Birth Year'].mode()
        print('The most common birth year in this query is: ', int(most_common_birth_year))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def raw_data(df):
    """Displays 5 rows of raw data at a time if opted for by user"""
    while True:
        raw_display= input('Would you like to review the first 5 rows of raw data? Select yes or no: ').lower()
        if raw_display != 'yes':
            break
        else:
            n = 0
            print(df[n:n+5])
            n+=5
            break
    while True:
        if raw_display != 'yes':
            break
        else:
            more_raw = input('Would you like to see an additional 5 rows of raw data? Select yes or no:').lower()
            if more_raw != 'yes':
                break
            else:
                print(df[n:n+5])
                n+=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
