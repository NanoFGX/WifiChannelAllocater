import java.util.*;

public class ChannelAssigner {
    public static int[] greedyColoring(int totalRooms, List<List<Integer>> adjacencyList) {
        List<Set<Integer>> adjacencyMap = new ArrayList<>();
        for (int i = 0; i < totalRooms; i++) adjacencyMap.add(new HashSet<>());
        for (List<Integer> edge : adjacencyList) {
            adjacencyMap.get(edge.get(0)).add(edge.get(1));
            adjacencyMap.get(edge.get(1)).add(edge.get(0));
        }

        int[] colors = new int[totalRooms];
        Arrays.fill(colors, -1);

        for (int room = 0; room < totalRooms; room++) {
            boolean[] used = new boolean[totalRooms];
            for (int neighbor : adjacencyMap.get(room))
                if (colors[neighbor] != -1) used[colors[neighbor]] = true;

            for (int color = 0; color < totalRooms; color++) {
                if (!used[color]) {
                    colors[room] = color;
                    break;
                }
            }
        }
        return colors;
    }
}
