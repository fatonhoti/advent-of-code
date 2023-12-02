#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <sstream>

std::vector<std::string> split(const std::string &s, std::string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    std::string token;
    std::vector<std::string> res;

    while ((pos_end = s.find(delimiter, pos_start)) != std::string::npos) {
        token = s.substr(pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back(token);
    }

    res.push_back(s.substr (pos_start));
    return res;
}

std::string trim(std::string& str) {
    int start = 0;
    while (std::isspace(str[start]))
        start++;
    int end = str.length();
    while (std::isspace(str[end]))
        end--;
    return str.substr(start, (end - start) + 1);
}

int main() {

    // Parse input
    std::ifstream file("day_2.txt");
    std::vector<std::string> lines;
    if (file.is_open()){
        std::string line;
        while (std::getline(file, line))
            lines.push_back(line);
    } else {
        std::cerr << "Failed opening file" << std::endl;
        return -1;
    }

    // Parse input
    std::unordered_map<int, std::vector<int>> games;
    for (auto& line : lines) {
        auto gid_rest = split(line, ":");

        int gid = std::stoi(split(gid_rest[0], " ")[1]);
        std::vector<std::string> sets = split(gid_rest[1], ";");
        
        std::unordered_map<std::string, int> max;
        for (auto& set : sets) {
            auto cubes = split(set, ", ");
            for (auto& cube : cubes) {
                std::vector<std::string> amount_color = split(trim(cube), " ");
                std::string color = amount_color[1];
                max[color] = std::max(max[color], std::stoi(amount_color[0]));
            }
        }
        games[gid] = { max["red"], max["green"], max["blue"] };
    }

    // Part 1 & 2
    int sum1 = 0;
    int sum2 = 0;
    for (auto& game : games) {
        int gid = game.first;
        auto& max_colors = game.second;
        if (max_colors[0] <= 12 && max_colors[1] <= 13 && max_colors[2] <= 14)
            sum1 += gid;
        sum2 += max_colors[0] * max_colors[1] * max_colors[2];
    }
    std::cout << "Part 1: " << sum1 << "\n";
    std::cout << "Part 2: " << sum2 << std::endl;

    return 0;

}