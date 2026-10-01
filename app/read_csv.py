import csv


def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)  # obtengo los nombres de la columnas de mi archivo
        data = []
        for row in reader:
            iterable = zip(
                header, row
            )  # esta union me a devolver tuplas con el encabezado de la columna y su valor.
            country_dict = {key: value for key, value in iterable}  # comprehension dict
            data.append(country_dict)
        return data


# Este bloque es para que este archivo corra como un script
if __name__ == "__main__":
    resultado = read_csv("./app/data.csv")
    print(resultado)
