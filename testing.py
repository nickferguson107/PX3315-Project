import RandomGraph
import general
import numpy as np
import matplotlib.pyplot as plt


network, _ = RandomGraph.random_network(1000, 0.005)
components = RandomGraph.get_all_components(network)