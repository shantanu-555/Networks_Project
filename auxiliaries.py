import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import math


def read_in_network(city, mode):
    """
    Reads in the network data from the csv files and returns the dataframes
    :param city: city name
    :param mode: mode of transport
    :return: network data and nodes data
    """
    df = pd.read_csv(f"network_data/{city}/network_{mode}.csv", sep=";")
    df.index += 1
    df_nodes = pd.read_csv(f"network_data/{city}/network_nodes.csv", sep=";")
    return df, df_nodes


def convert_lon_lat_to_xy(lon, lat):
    """
    Converts longitude and latitude to x and y coordinates
    :param lon: longitude
    :param lat: latitude
    :return: x and y coordinates
    """
    x = lon * 20037508.34 / 180
    y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
    y = y * 20037508.34 / 180
    return y, x


def convert_to_graph(network):
    """
    Converts the network data to a graph
    :param network: network data as pandas dataframe
    :return: graph
    """
    G = nx.from_pandas_edgelist(
        network, source="from_stop_I", target="to_stop_I", edge_attr="duration_avg"
    )
    return G


def add_positions(G, nodes):
    """
    Adds the positions to the nodes in the graph
    :param G: graph
    :param nodes: nodes data as pandas dataframe
    :return: position dictionary
    """

    # add positions to nodes from df_nodes to position dictionary
    pos = {}
    for i in range(len(nodes)):
        pos[nodes["stop_I"][i]] = convert_lon_lat_to_xy(
            nodes["lon"][i], nodes["lat"][i]
        )

    # add positions to nodes in G
    for node in G.nodes():
        G.nodes[node]["pos"] = pos[node]

    return pos


def visualize(city, graph, pos):
    """
    Visualizes the graph
    :param city: city name
    :param graph: graph
    :param pos: position dictionary
    :return: None
    """
    plt.figure(figsize=(12, 6))
    nx.draw_networkx(
        graph,
        pos,
        with_labels=False,
        arrows=True,
        node_size=10,
        node_color="red",
        edge_color="grey",
        label=f"Subway stations in {city}",
        width=1,
    )
    plt.legend()


def draw_nodes_on_map(city_nodes):
    """
    Draws the nodes on an open street map
    :param city_nodes: nodes data as pandas dataframe
    :return: None
    """
    fig = px.scatter_mapbox(
        city_nodes,
        lat="lat",
        lon="lon",
        hover_name="name",
        zoom=8,
        height=800,
        width=800,
    )

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()


# order in which to call
# berlin, berlin_nodes = read_in_network('berlin')
# G = convert_to_graph(berlin)
# pos = add_positions(G, berlin_nodes)
# visualize("Berlin", G, pos)
# draw_nodes_on_map(berlin_nodes)
