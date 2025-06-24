import numpy as np
import csv
import json

# ==================================================
# CONFIGURE BASES
# ==================================================
rooms_per_floor = 18
floors_per_block = 4
rooms_per_block = rooms_per_floor * floors_per_block  # 72
blocks = ["Mawar", "Kenanga"]

def build_adjacency_for_block():
    """Build adjacency matrix for one block of 72 rooms."""
    adj_matrix = np.zeros((rooms_per_block, rooms_per_block), dtype=int)

    # 1️⃣ Horizontal adjacency
    for floor in range(floors_per_block):
        offset = floor * rooms_per_floor
        for room in range(rooms_per_floor - 1):  # adjacency within floor
            room_id = offset + room
            next_room_id = offset + room + 1
            adj_matrix[room_id, next_room_id] = 1
            adj_matrix[next_room_id, room_id] = 1

    # 2️⃣ Vertical adjacency
    for floor in range(floors_per_block - 1):  # adjacency across floors
        for room in range(rooms_per_floor):
            room_id = floor * rooms_per_floor + room
            room_above = (floor + 1) * rooms_per_floor + room
            adj_matrix[room_id, room_above] = 1
            adj_matrix[room_above, room_id] = 1

    return adj_matrix

# ==================================================
# GENERATION
# ==================================================
adj_mawar = build_adjacency_for_block()
adj_kenanga = build_adjacency_for_block()

adj_total = np.zeros((rooms_per_block * 2, rooms_per_block * 2), dtype=int)

# Put Mawar adjacency
adj_total[:72, :72] = adj_mawar
# Put Kenanga adjacency
adj_total[72:, 72:] = adj_kenanga

# ==================================================
# EXPORT TO CSV
# ==================================================
def export_matrix(matrix, filename):
    """Export adjacency matrix to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for row in matrix:
            writer.writerow(row)

export_matrix(adj_mawar, "ktdi_adjacency_mawar.csv")
export_matrix(adj_kenanga, "ktdi_adjacency_kenanga.csv")
export_matrix(adj_total, "ktdi_adjacency_total.csv")

# ==================================================
# EXPORT TO JSON
# ==================================================
adj_json = {
    "Mawar": adj_mawar.tolist(),
    "Kenanga": adj_kenanga.tolist(),
    "Total": adj_total.tolist()
}
with open("ktdi_adjacency.json", "w") as json_file:
    json.dump(adj_json, json_file, indent=4)

print("\n✅ Export Complete!\n- ktdi_adjacency_mawar.csv\n- ktdi_adjacency_kenanga.csv\n- ktdi_adjacency_total.csv\n- ktdi_adjacency.json\n")
