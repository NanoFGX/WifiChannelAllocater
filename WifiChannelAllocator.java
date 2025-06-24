import java.util.Arrays;

public class WifiChannelAllocator {

    // Greedy coloring method
    public static int[] assignChannels(int[][] adjacencyMatrix, int numRooms) {
        int[] roomChannel = new int[numRooms];
        Arrays.fill(roomChannel, -1);

        boolean[] available = new boolean[numRooms];
        for (int i = 0; i < numRooms; i++) {
            Arrays.fill(available, true);
            // Mark used channels by adjacent rooms
            for (int j = 0; j < numRooms; j++) {
                if (adjacencyMatrix[i][j] == 1 && roomChannel[j] != -1) {
                    available[roomChannel[j]] = false;
                }
            }
            // Assign the first available channel
            for (int channel = 0; channel < numRooms; channel++) {
                if (available[channel]) {
                    roomChannel[i] = channel;
                    break;
                }
            }
        }
        return roomChannel;
    }

    public static void main(String[] args) {
        // Example adjacency matrix (5 rooms) for testing.
        // adjacencyMatrix[i][j] == 1 means room i is adjacent to room j.
        int[][] adjacencyMatrix = {
                {0, 1, 1, 0, 0},
                {1, 0, 1, 1, 0},
                {1, 1, 0, 1, 1},
                {0, 1, 1, 0, 1},
                {0, 0, 1, 1, 0}
        };
        int numRooms = adjacencyMatrix.length;

        int[] roomChannel = assignChannels(adjacencyMatrix, numRooms);

        System.out.println("Channel assignment for rooms:");
        for (int i = 0; i < roomChannel.length; i++) {
            System.out.println("Room " + i + " -> Channel " + roomChannel[i]);
        }

        long uniqueChannels = Arrays.stream(roomChannel).distinct().count();
        System.out.println("\nTotal Channels Used: " + uniqueChannels);
    }
}
