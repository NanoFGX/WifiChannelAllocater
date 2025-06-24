import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        final int ROOMS_PER_FLOOR = 18;
        final int FLOORS_PER_BLOCK = 4;

        List<List<Integer>> adjacencyMawar = AdjacencyGenerator.buildAdjacency(ROOMS_PER_FLOOR, FLOORS_PER_BLOCK, 0);
        List<List<Integer>> adjacencyKenanga = AdjacencyGenerator.buildAdjacency(ROOMS_PER_FLOOR, FLOORS_PER_BLOCK, 72);

        List<List<Integer>> adjacencyTotal = new ArrayList<>(adjacencyMawar);
        adjacencyTotal.addAll(adjacencyKenanga);

        int totalRooms = ROOMS_PER_FLOOR * FLOORS_PER_BLOCK * 2;

        // Perform Greedy Graph Coloring
        int[] channelAssignments = ChannelAssigner.greedyColoring(totalRooms, adjacencyTotal);

        // Export adjacency
        exportAdjacency("ktdi_adjacency_total.csv", adjacencyTotal);

        // Export channel assignment
        exportChannelAssignments("channel_assignment.csv", channelAssignments);
    }

    public static void exportAdjacency(String filename, List<List<Integer>> adjacency) {
        try (PrintWriter pw = new PrintWriter(new File(filename))) {
            pw.println("Room1,Room2");
            for (List<Integer> edge : adjacency) {
                pw.println(edge.get(0) + "," + edge.get(1));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void exportChannelAssignments(String filename, int[] channelAssignments) {
        try (PrintWriter pw = new PrintWriter(new File(filename))) {
            pw.println("Room,Channel");
            for (int i = 0; i < channelAssignments.length; i++) {
                pw.println(i + "," + channelAssignments[i]);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
