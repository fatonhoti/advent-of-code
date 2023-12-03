#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <stdint.h>
#include <functional>
#include <utility>

struct hash_pair final {
    template<class TFirst, class TSecond>
    size_t operator()(const std::pair<TFirst, TSecond>& p) const noexcept {
        uintmax_t hash = std::hash<TFirst>{}(p.first);
        hash <<= sizeof(uintmax_t) * 4;
        hash ^= std::hash<TSecond>{}(p.second);
        return std::hash<uintmax_t>{}(hash);
    }
};

bool is_digit(char& c) {
    return c >= '0' && c <= '9';
}

std::pair<int, int> next_entry(int row, int col, int width) {
    int old_col = col;
    col = (col + 1) % width;
    if (col < old_col)
        row += 1;
    return { row, col };
}

std::pair<bool, std::pair<int, int>> is_adjacent_to_symbol(std::vector<std::string> grid, int width, int height, std::pair<int, int> pos) {
    int row = pos.first;
    int col = pos.second;

    int min_c = std::max(0, col - 1);
    int max_c = std::min(width - 1, col + 1);
    int min_r = std::max(0, row - 1);
    int max_r = std::min(height - 1, row + 1);

    for (size_t r = min_r; r <= max_r; r++) {
        for (size_t c = min_c; c <= max_c; c++) {
            char entry = grid[r][c];
            if (!is_digit(entry) && entry != '.') {
                if (entry == '*')
                    return { true, {r, c} };
                return { true, {-1, -1} };
            }
        }
    }

    return { false, {-1, -1} };

}

int main() {

    // Parse input
    std::ifstream file("day_3.txt");
    std::vector<std::string> grid;
    if (file.is_open()){
        std::string line;
        while (std::getline(file, line))
            grid.push_back(line + ".");
    } else {
        std::cerr << "Failed opening file" << std::endl;
        return -1;
    }

    int width = grid[0].length();
    int height = grid.size();

    int sum1 = 0;
    int sum2 = 0;

    std::unordered_map<std::pair<int, int>, std::vector<int>, hash_pair> gear_to_nums;

    int row = 0;
    int col = 0;

    while (row != height && col != width) {
        if (!is_digit(grid[row][col])) {
            auto p = next_entry(row, col, width);
            row = p.first;
            col = p.second;
            continue;
        }

        bool is_adj_to_symbol = false;
        bool is_adj_to_gear = false;
        std::pair<int, int> gear_pos;

        std::string num{""};
        while (is_digit(grid[row][col])) {
            num += grid[row][col];
            auto[is_adj, pos] = is_adjacent_to_symbol(grid, width, height, { row, col });
            if (is_adj) {
                is_adj_to_symbol = true;
                if (pos.first != -1 && pos.second != -1) {
                    is_adj_to_gear = true;
                    gear_pos = pos;
                    if (gear_to_nums.find(pos) == gear_to_nums.end())
                        gear_to_nums.insert({pos, {}});
                }
            }
            auto[nrow, ncol] = next_entry(row, col, width);
            row = nrow;
            col = ncol;
        }

        int n = std::stoi(num);

        // Part 1
        if (is_adj_to_symbol)
            sum1 += n;

        // Part 2
        if (is_adj_to_gear) {
            gear_to_nums[gear_pos].push_back(n);
            if (gear_to_nums[gear_pos].size() == 2) {
                auto ns = gear_to_nums[gear_pos];
                sum2 += ns[0] * ns[1];
            }
        }

    }

    std::cout << "Part 1: " << sum1 << "\n";
    std::cout << "Part 2: " << sum2 << std::endl;

    return 0;

}