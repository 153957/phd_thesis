import itertools

import numpy as np
from artist import Plot, PolarPlot

from sapphire.clusters import SingleStation
from sapphire.analysis.direction_reconstruction import DirectAlgorithmCartesian2D


TIME_RESOLUTION = 2.5  # nanoseconds
C = .3  # lightspeed m/ns


def generate_discrete_times(station, detector_ids=[0, 2, 3]):
    """Generates possible arrival times for detectors

    The times are relative to the first detector, which is assumed to be
    at t = 0.

    """
    r = station_size(station, detector_ids)
    max_dt = ceil_in_base(r / C, TIME_RESOLUTION)
    times = np.arange(-max_dt, max_dt, TIME_RESOLUTION)
    time_combinations = itertools.product(times, repeat=len(detector_ids) - 1)
    return time_combinations


def station_size(station, detector_ids=[0, 2, 3]):
    """Get the largest distance between any two detectors in a station

    :param detectors: list of :class:`sapphire.clusters.Detector` objects

    """
    r = [station.calc_r_and_phi_for_detectors(d0, d1)[0]
         for d0, d1 in itertools.combinations(detector_ids, 2)]
    return max(r)


def ceil_in_base(value, base):
    return base * np.ceil(value / base)


if __name__ == '__main__':

    dirrec = DirectAlgorithmCartesian2D()

    station = SingleStation().stations[0]

    graph = PolarPlot(use_radians=True)

    ids = [0, 2, 3]
    times = generate_discrete_times(station, detector_ids=ids)
    detectors = [station.detectors[id].get_coordinates() for id in ids]
    x, y, z = zip(*detectors)

    theta, phi = itertools.izip(*(dirrec.reconstruct_common((0,) + t, x, y, z)
                                  for t in times))

    thetaa = [t for t in theta if not np.isnan(t)]
    phia = [p for p in phi if not np.isnan(p)]
    graph.scatter(phia, thetaa, markstyle='mark size=.5pt')

    graph.set_ylimits(0, np.pi / 2)
    graph.set_yticks([0, np.pi / 6, np.pi / 3, np.pi / 2])
    graph.set_ytick_labels([r'$0$', r'$\frac{1}{6}\pi$',
                           r'$\frac{2}{6}\pi$', r'$\frac{1}{2}\pi$',])
    graph.set_ylabel('Zenith [rad]')
    graph.set_xlabel('Azimuth [rad]')
#     graph.save_as_pdf('discrete_directions')
    graph.save('discrete_directions')
