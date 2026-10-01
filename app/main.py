import read_csv
import utils

import charts


def run():
    data = read_csv.read_csv("data.csv")
    data = list(filter(lambda item: item["Continent"] == "South America", data))

    countries = list(map(lambda item: item["Country/Territory"], data))
    percentages = list(
        map(lambda item: float(item["World Population Percentage"]), data)
    )
    charts.generate_pie_chart(countries, percentages)

    country = input("Digite el país => ")

    resultado = utils.population_by_country(data, country)

    if len(resultado) > 0:
        country = resultado[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country["Country/Territory"], labels, values)


if __name__ == "__main__":
    run()  # le dice al archivo main .py que si es ejecutado desde la terminal
# ejecute la funcion run.
