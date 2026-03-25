import os

series_titles = ["Maximum temperature (Degree C)", "Minimum temperature (Degree C)", "Rainfall amount (millimetres)"]

def range_calculation(in_series):
    clean_series = [x for x in in_series if x is not None]
    if not clean_series: return 0
    return max(clean_series) - min(clean_series)

def read_csv(file, default_value=None):
    data_table = {}
    try:
        with open(file) as f:
            lines = [line.strip().split(',') for line in f.readlines()]
        headers = lines[0]
        for i in range(len(headers)):
            data_table[headers[i]] = [None if (len(line[i]) == 0) else float(line[i]) for line in lines[1:]]
        return data_table
    except FileNotFoundError:
        print(f"\nSTILL NOT FOUND: {file}")
        return None

def get_user_choice(options):
    print("\n--- Weather Analysis Menu ---")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    choice = input("Enter choice (or 'exit'): ").strip().lower()
    if choice == 'exit': return None
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        return get_user_choice(options)
    return options[int(choice) - 1]

def menu(data_table):
    while True:
        choice = get_user_choice(series_titles)
        if choice is None: break
        series = data_table[choice]
        print(f"\n{'-'*20}\nRESULT: {choice}\nRange: {range_calculation(series)}\n{'-'*20}")
        input("Press Enter to continue...")

if __name__ == "__main__":
    # This part finds the file relative to the script location
    base_path = os.path.dirname(__file__)
    target_file = os.path.join(base_path, 'weather[1].csv')
    
    data = read_csv(target_file)
    if data:
        menu(data)