from typing import List


def get_temperatures_list(file_path) -> List[int]:
    """
    This method extract temperatures recorded at various dates in a year.
    :param file_path: path of the text file which contains weather data.
    :return: Temperatures recorded in a year in a list of type int.
    """
    temperatures = []

    try:
        f = open(file_path, 'r', encoding='utf-8')
        data_tokens = f.read().split()
        for data in data_tokens:
            temperatures.append(int(data.split(',')[1].split("°")[0]))
    except FileNotFoundError:
        print(f"File Not found. Please verify the path: {file_path}")
        exit(0)
    return temperatures


def calculate_average_temperature(temperatures: List[int]) -> float:
    """
    calculate average of temperatures recorded ina particular year
    :param temperatures: list of temperatures recorded in a year
    :return: Average of temperature.
    """
    return sum(temperatures) / len(temperatures)


temperatures_list_2020 = get_temperatures_list("weather_2020.txt")
temperatures_list_2021 = get_temperatures_list("weather_2021.txt")

avg_temp_2020 = calculate_average_temperature(temperatures_list_2020)
avg_temp_2021 = calculate_average_temperature(temperatures_list_2021)

print(f"The average temperature measured in year 2020 is: {avg_temp_2020}")
print(f"The average temperature measured in year 2021 is: {avg_temp_2021}")

print("The maximum average temperature reported in {} year and it is {}".format(
    "2021" if avg_temp_2021 > avg_temp_2020 else "2020", max(avg_temp_2021, avg_temp_2020)))
