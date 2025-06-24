import networkx as nx
import matplotlib.pyplot as plt
import random

# ==================================================
# CONFIG
# ==================================================
rooms_per_floor = 18
floors_per_block = 4
rooms_per_block = rooms_per_floor * floors_per_block
total_rooms = rooms_per_block * 2

# ==================================================
# BUILD ADJACENCY FUNCTION
# ==================================================
def build_adjacency_for_block(start_index=0):
    adjacency = []
    for floor in range(floors_per_block):
        offset = floor * rooms_per_floor + start_index
        # Adjacency within floor
        for room in range(rooms_per_floor - 1):
            adjacency.append((offset + room, offset + room + 1))
        # Vertical adjacency across floors
        if floor < floors_per_block - 1:
            for room in range(rooms_per_floor):
                adjacency.append((floor * rooms_per_floor + room + start_index,
                                   (floor + 1) * rooms_per_floor + room + start_index))
    return adjacency

# ==================================================
# GENERATION
# ==================================================
adj_mawar = build_adjacency_for_block(start_index=0)
adj_kenanga = build_adjacency_for_block(start_index=72)

# All adjacency combined
all_edges = adj_mawar + adj_kenanga

# ==================================================
# EXAMPLE CHANNEL ASSIGNMENT (Replace this with actual results!)
# ==================================================
random.seed(42)  # Demo
channels = [random.randint(0, 2) for _ in range(total_rooms)]

# ==================================================
# COLOR MAP
# ==================================================
color_palette = {
    0: "#FFD700",  # Gold
    1: "#1E90FF",  # Blue
    2: "#FF4500",  # Red-Orange
}
node_colors = [color_palette[ch] for ch in channels]

# ==================================================
# UTILITY FUNCTION TO DRAW GRAPH
# ==================================================
def draw_graph(edges, node_range, title, filename):
    """Draw the adjacency graph with channel assignment."""
    G = nx.Graph()
    G.add_edges_from(edges)

    node_subset = range(*node_range)
    pos = nx.spring_layout(G.subgraph(node_subset), seed=42, k=0.15)

    fig, ax = plt.subplots(figsize=(10, 10))
    nx.draw_networkx(
        G.subgraph(node_subset),
        pos,
        node_size=100,
        node_color=[node_colors[i] for i in node_subset],
        with_labels=False,
        edgecolors='black',
        alpha=0.9,
        ax=ax
    )
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.axis("off")
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()


# ==================================================
# DRAW MAWAR
# ==================================================
draw_graph(adj_mawar, (0, 72), "Mawar Block: Channel Assignment Graph", "Results/mawar_block.png")

# ==================================================
# DRAW KENANGA
# ==================================================
draw_graph(adj_kenanga, (72, 144), "Kenanga Block: Channel Assignment Graph", "Results/kenanga_block.png")

# ==================================================
# DRAW COMBINED
# ==================================================
draw_graph(all_edges, (0, 144), "Mawar + Kenanga Blocks: Combined Channel Graph",
           "Results/ktdi_combined.png")
