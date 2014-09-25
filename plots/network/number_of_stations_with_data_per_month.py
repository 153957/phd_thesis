from datetime import datetime
from artist import Plot

from sapphire import api

def main():
    graph = Plot()
    network = api.Network()
    n_stations = [len(network.stations_with_data(year=y, month=m, day=1))
                  for y in range(2004, 2015) for m in range(1, 13)
                  if not (y == 2014 and m > 9)]

    graph.plot(range(len(n_stations)), n_stations)
    graph.set_xlabel('Date')
    graph.set_ylabel('Number of stations')
    graph.save_as_pdf('number_of_stations_with_data_per_month')


if __name__ == "__main__":
    main()
