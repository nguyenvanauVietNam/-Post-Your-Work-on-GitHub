import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dictionary to hold city data files
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    while True:
        city = input("Please choose a city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city. Please choose from chicago, new york city, or washington.")

    # Get user input for month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Please choose a month (january, february, ..., june) or 'all' for no filter: ").lower()
        if month in months:
            break
        else:
            print("Invalid month. Please choose from january to june or 'all'.")

    # Get user input for day
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Please choose a day (monday, tuesday, ..., sunday) or 'all' for no filter: ").lower()
        if day in days:
            break
        else:
            print("Invalid day. Please choose from monday to sunday or 'all'.")

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
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day.lower()]

    return df

def display_raw_data(df):
    """Displays raw data upon user request."""
    row_index = 0
    while True:
        view_data = input("Would you like to see 5 lines of raw data? Enter 'yes' or 'no': ").lower()
        if view_data == 'yes':
            print(df.iloc[row_index: row_index + 5])  # Display 5 rows
            row_index += 5
        elif view_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        if row_index >= len(df):  # Check if there are more rows to display
            print("No more raw data to display.")
            break

def time_stats(df, city):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    print(f"The most common month is: {common_month}")

    # Display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"The most common day of the week is: {common_day}")

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f"The most common start hour is: {common_hour}")

    # Plotting the common hour histogram
    plt.figure(figsize=(10, 6))
    ax = df['hour'].plot(kind='hist', bins=24, alpha=0.7, color='blue')
    plt.title(f'Frequency of Start Hours in {city.title()}')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Frequency')
    plt.grid(True)

    # Add values on top of the bars
    counts, _ = np.histogram(df['hour'], bins=24)
    for i, count in enumerate(counts):
        if count > 0:
            ax.text(i, count + 0.5, str(count), ha='center', va='bottom')

    # Save the plot as a PNG image
    plt.savefig('start_hour_histogram.png')  
    plt.close()  # Close the plot to avoid display issues

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df, selected_city):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {common_start_station}")

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {common_end_station}")

    # Display most frequent combination of start station and end station trip
    df['Start-End Combination'] = df['Start Station'] + " to " + df['End Station']
    common_combination = df['Start-End Combination'].mode()[0]
    print(f"The most frequent combination of start and end stations is: {common_combination}")

    # Plotting the common start stations
    plt.figure(figsize=(10, 6))
    station_counts = df['Start Station'].value_counts().head(10)
    station_counts.plot(kind='bar', alpha=0.7, color='green')
    plt.title('Top 10 Start Stations')
    plt.xlabel('Start Station')
    plt.ylabel('Number of Trips')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('start_station_bar_chart.png')  # Save the plot as a PNG image
    plt.close()  # Close the plot to avoid display issues

    # Plotting the comparison of selected city with others
    compare_city_stats(selected_city)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def compare_city_stats(selected_city):
    """Compares the selected city's start station stats with other cities."""
    all_data = {city: pd.read_csv(file) for city, file in CITY_DATA.items()}
    city_counts = {city: data['Start Station'].value_counts().head(10) for city, data in all_data.items()}

    plt.figure(figsize=(12, 8))
    for city, counts in city_counts.items():
        if city == selected_city:
            counts.plot(kind='bar', alpha=0.7, color='red', label=city)
        else:
            counts.plot(kind='bar', alpha=0.5, color='blue', label=city)

    plt.title(f'Comparison of Top Start Stations: {selected_city.title()} vs Other Cities')
    plt.xlabel('Start Station')
    plt.ylabel('Number of Trips')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('city_comparison_bar_chart.png')  # Save the comparison plot as a PNG image
    plt.close()  # Close the plot to avoid display issues

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n", user_types)

    # Display counts of gender if available
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:\n", gender_counts)
    else:
        print("\nGender data is not available for this city.")

    # Display earliest, most recent, and most common year of birth if available
    if 'Birth Year' in df.columns:
        earliest_birth = int(df['Birth Year'].min())
        most_recent_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode()[0])
        print(f"\nEarliest year of birth: {earliest_birth}")
        print(f"Most recent year of birth: {most_recent_birth}")
        print(f"Most common year of birth: {common_birth}")
    else:
        print("\nBirth Year data is not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)  # Call the new function to display raw data

        time_stats(df, city)
        station_stats(df, city)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
