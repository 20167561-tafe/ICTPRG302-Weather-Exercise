import math
import pandas as pd
import statistics
file = "C:/Users/Admin/Desktop/20167561-tafe.github.io/ICTPRG302-Weather-Exercise/weather[1].csv"
# update the file location for your local device

series_titles = ["Maximum temperature (Degree C)", "Minimum temperature (Degree C)", "Rainfall amount (millimetres)"]

def mean(in_series):
    df = pd.read_csv(file)
    mean_values = df[series_titles].mean()
    return mean_values

def variance(in_series):
    data = list(in_series)

    if not data:
        return none

    for value in data:
        if not isinstance(value, ( int , float)):
            raise TypeError(f"non-numeric value found:{v}")

    avg = mean(data)
    squared_diffs = [(value -avg)**2 for value in data]

    variance = sum(squared_diffs) / len(data)

    return variance

def standard_deviation(in_series):
    standard_deviation()== math.sqrt(variance())
    return standard_deviation

def iqr(in_series):
    df = pd.read_csv(file)
    Q1 = df[series_titles].quantile(0.25)
    Q3 = df[series_titles].quantile(0.75)
    IQR = Q3 - Q1
    print(f"IQR: {IQR}")

def filter_series(year_series, month_series, day_series, data_series, max_date=None, min_date=None):
    pass

def read_csv(file,default_value=None):
    data_table = {}
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip().split(',') for line in lines]
    for i in range(len(lines[0])):
        data_table[lines[0][i]] = [default_value if (len(line[i]) == 0) else float(line[i]) for line in lines[1:]]
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

def date_feature(options):
    df = pd.read_csv(file)
    df['datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    print(df['datetime'])
    

def menu(data_table):
    print("Select a data series:")
    choice = get_user_choice(series_titles)
    series = data_table[choice]
    print(f"Mean: {mean(data_table[choice])}")
    iqr(choice)
    date_feature(choice)

if __name__ == "__main__":
    data = read_csv('C:/Users/Admin/Desktop/20167561-tafe.github.io/ICTPRG302-Weather-Exercise/weather[1].csv')
    menu(data)