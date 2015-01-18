import random

import numpy as np
from artist import Plot

from sapphire.simulations.detector import HiSPARCSimulation


def transport_time():
    sim = HiSPARCSimulation
    dt = sim.simulate_signal_transport_time(10000)
    counts, bins = np.histogram(dt, bins=np.arange(1, 8.1, 0.1))

    mc_bins = np.arange(1, 8.1, 0.1)
    mc_data = [0, 0, 1, 3, 2, 4, 3, 2, 5, 19, 22, 26, 34, 58, 78, 123,
               201, 296, 414, 445, 435, 460, 552, 579, 304, 196, 198,
               185, 191, 193, 165, 203, 177, 218, 239, 199, 205, 192,
               218, 165, 230, 183, 216, 177, 226, 208, 191, 188, 153,
               178, 165, 197, 149, 130, 117, 89, 75, 55, 35, 20, 5, 2,
               1, 0, 0, 0, 0, 0, 0, 0]

    sim_x = [2.5507, 2.5507, 3.4953,3.4953, 6.463, 6.463]
    sim_y = [0, 380.96, 380.96, 186.68, 186.68, 0]

    graph = Plot()
    graph.histogram(mc_data, mc_bins, linestyle='gray')
    graph.plot(sim_x, sim_y, mark=None, linestyle='dashed, lightgray')
    graph.histogram(counts, bins)
    graph.set_xlabel(r'Transport time [\si{\nano\second}]')
    graph.set_ylabel('Counts')
    graph.set_ylimits(min=0.)
    graph.save('transport_time')


def signal_efficiency():
    sim = HiSPARCSimulation
    particle = np.array([(0, 0, 1.)],
                        dtype=[('p_x','f8'),('p_y','f8'),('p_z','f8')])
    mips = [sim.simulate_detector_mip(particle) for _ in xrange(10000)]
    counts, bins = np.histogram(mips, bins=np.arange(0, 2.5, 0.05))

    graph = Plot()
    graph.histogram(counts, bins)
    graph.set_xlabel(r'Signal strength [\si{\mip}]')
    graph.set_ylabel('Counts')
    graph.set_ylimits(min=0.)
    graph.save('signal_efficiency')


def set_seeds():
    random.seed(153)
    np.random.seed(153)

if __name__ == '__main__':
    set_seeds()
    transport_time()

    set_seeds()
    signal_efficiency()
