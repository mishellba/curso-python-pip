import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f"./images/{name}.png")  # Save the bar chart as a PNG file
    plt.close()

def generate_pie_chart(labels, values):  # Generacion de grafico de pie
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.savefig("pie_chart.png")  # Save the pie chart as a PNG file
    plt.close()

if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [20, 10, 70]
    generate_pie_chart(labels, values)
