import numpy as np
import csv

# ==================================================
# CONFIGURE BASES
# ==================================================
rooms_per_floor = 18
floors_per_block = 4
total_rooms = rooms_per_floor * floors_per_block  # 72

# Initialize adjacency matrix
adj_matrix = np.zeros((total_rooms, total_rooms), dtype=int)

# ==================================================
# BUILD ADJACENCY
# ==================================================

# 1️⃣ Horizontal adjacency within the same floor
for floor in range(floors_per_block):
    offset = floor * rooms_per_floor
    for room in range(rooms_per_floor - 1):  # adjacency within floor
        room_id = offset + room
        next_room_id = offset + room + 1
        adj_matrix[room_id, next_room_id] = 1
        adj_matrix[next_room_id, room_id] = 1

# 2️⃣ Vertical adjacency across floors
for floor in range(floors_per_block - 1):  # adjacency across floors
    for room in range(rooms_per_floor):
        room_id = floor * rooms_per_floor + room
        room_above = (floor + 1) * rooms_per_floor + room
        adj_matrix[room_id, room_above] = 1
        adj_matrix[room_above, room_id] = 1

# ==================================================
# EXPORT TO .csv
# ==================================================
filename = "Results/ktdi_adjacency_matrix.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    for row in adj_matrix:
        writer.writerow(row)

print(f"✅ Exported adjacency matrix for KTDI (72 rooms) to {filename}")
