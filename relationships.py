# SPDX-License-Identifier: CC0-1.0

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('relationships.csv')

graph = nx.from_pandas_edgelist(df, source='source', target='target',
                                create_using=nx.DiGraph())

plt.figure(figsize=(10, 10))

center_nodes = ["GDAL", "GEOS", "PROJ"]
shells = [center_nodes, list(set(graph.nodes) - set(center_nodes))]

layout = nx.shell_layout(graph, nlist=shells)

nx.draw(graph, layout,
        edge_color='gray',
        node_color='lightblue',
        arrowsize=20,
        with_labels=True)

plt.title('Dependencies between FOSS4G stack')
plt.savefig('relationships.png', format='png', dpi=300)
plt.savefig('relationships.svg', format='svg')
