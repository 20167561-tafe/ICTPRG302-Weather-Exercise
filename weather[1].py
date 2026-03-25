import math
import pandas as pd
import statistics
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

file = "C:/Users/Admin/Desktop/20167561-tafe.github.io/ICTPRG302-Weather-Exercise/weather[1].csv"
# update the file location for your local device

series_titles = ["Maximum temperature (Degree C)", "Minimum temperature (Degree C)", "Rainfall amount (millimetres)"]

MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}


def mean(in_series):
    df = pd.read_csv(file)
    mean_values = df[series_titles].mean()
    return mean_values


def variance(in_series):
    data = list(in_series)

    if not data:
        return None

    for value in data:
        if not isinstance(value, (int, float)):
            raise TypeError(f"non-numeric value found: {value}")
        if not isinstance(value, ( int , float)):
            raise TypeError(f"non-numeric value found:{value}")

    avg = mean(data)
    squared_diffs = [(value -avg)**2 for value in data]

    avg = sum(data) / len(data)
    squared_diffs = [(value - avg) ** 2 for value in data]
    variance_val = sum(squared_diffs) / len(data)
    return variance_val


def standard_deviation(in_series):
    return math.sqrt(variance(in_series))


def iqr(in_series):
    df = pd.read_csv(file)
    Q1 = df[series_titles].quantile(0.25)
    Q3 = df[series_titles].quantile(0.75)
    IQR = Q3 - Q1
    print(f"IQR: {IQR}")


def filter_series(year_series, month_series, day_series, data_series, max_date=None, min_date=None):
    pass


def read_csv(file, default_value=None):
    data_table = {}
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip().split(',') for line in lines]
    for i in range(len(lines[0])):
        data_table[lines[0][i]] = [
            default_value if (len(line[i]) == 0) else float(line[i])
            for line in lines[1:]
        ]
    return data_table


def get_user_choice(options):
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    choice = input("Enter the number of your choice: ")
    if choice.lower() == 'exit':
        return None
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        print("Invalid choice. Please try again.")
        return get_user_choice(options)
    choice = int(choice) - 1
    return options[choice]


def show_menu():
    """Displays the statistical calculation menu."""
    print("\n--- Statistical Calculator ---")
    print("mean")
    print("variance")
    print("standard_deviation")
    print("Exit")


def get_data():
    """Collects user input data for calculation."""
    data = input("Enter numbers separated by spaces: ")
    return [float(x) for x in data.split()]


def main():
    while True:
        show_menu()
        choice = get_user_choice(series_titles)
        
        if choice == "Exit":
            print("Exiting...")
            break
        
        if choice in ["mean", "variance", "standard_deviation"]:
            data = get_data()

            if not data:
                print("No data entered")
                continue
            
            if choice == 'mean':
                print(f"mean: {statistics.mean(data)}")
            elif choice == 'variance':
                print(f"variance: {statistics.variance(data)}")
            elif choice == 'standard_deviation':
                if len(data) < 2:
                    print("standard_deviation requires at least two data points.")
                else:
                    print(f"standard_deviation: {statistics.stdev(data)}")
        else:
            print("Invalid choice, please try again.")
   
    
def date_feature(options):
    df = pd.read_csv(file)
    df['datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    print(df['datetime'])


def temperature_range(options):
    df = pd.read_csv(file)
    temp_range = df["Maximum temperature (Degree C)"] - df["Minimum temperature (Degree C)"]
    temp_range.name = "Temperature Range (Degree C)"
    print(temp_range)
    return temp_range


def plot_monthly_min_max_histogram():
    """
    Prompts the user to select a year and month, then displays a grouped
    bar chart (histogram) of daily min and max temperatures for that month.
    Dates are shown in DD-MMM-YYYY format on the x-axis.
    """
    df = pd.read_csv(file)
    df['datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

    # --- Year selection ---
    available_years = sorted(df['Year'].dropna().astype(int).unique().tolist())
    print("\nAvailable years:")
    year_str = get_user_choice([str(y) for y in available_years])
    if year_str is None:
        return
    selected_year = int(year_str)

    # --- Month selection ---
    available_months = sorted(
        df[df['Year'] == selected_year]['Month'].dropna().astype(int).unique().tolist()
    )
    if not available_months:
        print(f"No data found for {selected_year}.")
        return

    month_options = [f"{MONTH_NAMES[m]} ({m})" for m in available_months]
    print(f"\nAvailable months for {selected_year}:")
    month_choice = get_user_choice(month_options)
    if month_choice is None:
        return
    selected_month = available_months[month_options.index(month_choice)]

    # --- Filter data ---
    mask = (df['Year'] == selected_year) & (df['Month'] == selected_month)
    monthly_df = df[mask].copy().sort_values('datetime')

    if monthly_df.empty:
        print(f"No data found for {MONTH_NAMES[selected_month]} {selected_year}.")
        return

    # Drop rows where both temp columns are missing
    monthly_df = monthly_df.dropna(
        subset=["Maximum temperature (Degree C)", "Minimum temperature (Degree C)"],
        how='all'
    )

    # --- Format dates as DD-MMM-YYYY for x-axis labels ---
    date_labels = monthly_df['datetime'].dt.strftime('%d-%b-%Y').tolist()
    x = range(len(date_labels))
    bar_width = 0.35

    max_temps = monthly_df["Maximum temperature (Degree C)"].tolist()
    min_temps = monthly_df["Minimum temperature (Degree C)"].tolist()

    # --- Plot ---
    fig, ax = plt.subplots(figsize=(max(10, len(date_labels) * 0.6), 6))

    bars_max = ax.bar(
        [i - bar_width / 2 for i in x],
        max_temps,
        width=bar_width,
        label='Max Temperature (°C)',
        color='tomato',
        edgecolor='darkred'
    )
    bars_min = ax.bar(
        [i + bar_width / 2 for i in x],
        min_temps,
        width=bar_width,
        label='Min Temperature (°C)',
        color='steelblue',
        edgecolor='navy'
    )

    ax.set_xticks(list(x))
    ax.set_xticklabels(date_labels, rotation=45, ha='right', fontsize=8)
    ax.set_xlabel('Date', fontsize=11)
    ax.set_ylabel('Temperature (°C)', fontsize=11)
    ax.set_title(
        f'Daily Min/Max Temperature — {MONTH_NAMES[selected_month]} {selected_year}',
        fontsize=13, fontweight='bold'
    )
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def menu(data_table):
    print("\nSelect a data series:")
    choice = get_user_choice(series_titles)
    if choice is None:
        return
    print(f"Mean: {mean(data_table[choice])}")
    iqr(choice)
    date_feature(choice)
    temperature_range(choice)

    print("\nWould you like to view the monthly Min/Max temperature histogram?")
    view_hist = input("Enter 'yes' to continue or any other key to skip: ").strip().lower()
    if view_hist == 'yes':
        plot_monthly_min_max_histogram()


if __name__ == "__main__":
    data = read_csv(file)
    menu(data)
    data = read_csv('C:/Users/Admin/Desktop/20167561-tafe.github.io/ICTPRG302-Weather-Exercise/weather[1].csv')
    main(data)
