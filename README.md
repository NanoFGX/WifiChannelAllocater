!!!!ONLINE PORTFOLIO LINK:!!!!
https://nanofgx.github.io/testPORT/



KTDI Wi‑Fi Channel Optimization
🎯 Project Goal
Optimize the placement of routers and the assignment of Wi‑Fi channels across Blok Mawar and Blok Kenanga at KTDI, Universiti Putra Malaysia (UPM), using Greedy Graph Coloring.
This project aims to reduce channel interference, minimize the number of routers required, and improve overall internet reliability for students.

🏁 Scenario
Location: Blok Mawar & Blok Kenanga, KTDI, UPM.

Issue: Frequent connectivity problems due to overlapping Wi‑Fi signals and inefficient channel assignment across adjacent rooms and floors.

Objective:

Minimize signal overlap.

Minimize the number of routers used.

Maintain robust and stable internet connectivity.

⚡️ Methodology
We model the floor layout as a Graph:

Rooms ➔ Nodes

Adjacency between rooms (and across floors) ➔ Edges

Apply Greedy Graph Coloring to assign Wi‑Fi channels:

Adjacent rooms must have different channels.

Minimize total channel usage across the block.

✅ Features
Builds adjacency matrices for multi‑floor layouts (72 rooms per block).

Applies a Greedy Graph Coloring algorithm for channel assignment.

Ensures:

No adjacent rooms share the same channel.

Reduced total number of routers required.

Export adjacency data and channel assignment results in .csv and .json.

Visualize results:

Individual block adjacency graph.

Combined block adjacency graph.

👥 Team Members
Name	Role
SRIRAM A/L SUNDRADAS:	             Developed adjacency matrix generation for multi‑floor room layouts.
ZAKARIA BIN ALI:	                 Integrated Greedy Graph Coloring for channel assignment.
ADIB ZAQUAN ISKANDAR BIN NORZILAM: Created test scenarios and verified adjacency constraints across floor connections.
NITESH A/L PRAKASH:	               Debugged edge cases, exported results, and added project documentation.
