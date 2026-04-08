// Last updated: 4/8/2026, 5:08:39 PM
class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int closest = -1;
        int min_distance = 10000000;
        vector<int> current_location = {x, y};
        for (int i = 0; i < points.size(); i++) {
            if (points[i][0] != x && points[i][1] != y) {
                continue;
            } else if (points[i][0] == x && points[i][1] != y) {
                int distance = abs(points[i][1] - y);
                if (distance < min_distance || closest == -1) {
                    closest = i;
                    min_distance = distance;
                }
                continue;
            } else if (points[i][1] == y && points[i][0] != x) {
                int distance = abs(points[i][0] - x);
                if (distance < min_distance || closest == -1) {
                    closest = i;
                    min_distance = distance;
                }
                continue;
            }
            return i;
        }
        return closest;
    }
};