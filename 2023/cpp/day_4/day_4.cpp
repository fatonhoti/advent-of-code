#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <utility>
#include <unordered_map>
#include <set>
#include <iterator>
#include <algorithm>
#include <cmath>
#include <sstream>

void read_input(std::vector<std::string>& lines) {
    std::ifstream file("day_4.txt");
    if (file.is_open()){
        std::string line;
        while (std::getline(file, line))
            lines.push_back(line);
        return;
    }
}

std::set<int> str_to_arr(std::string numbers) {
    std::set<int> ns;
    std::stringstream ss(numbers);
    while(!ss.eof()) {
        int num;
        ss >> num;
        ns.insert(num);
    }
    return ns;
}

int main() {

    std::vector<std::string> lines;
    read_input(lines);

    std::unordered_map<int, int> matches;
    std::unordered_map<int, int> n_copies;
    for (size_t i = 0; i < lines.size(); i++) {
        auto line = lines[i];
        int card_id = static_cast<int>(i + 1);

        auto ns = line.substr(line.find(":") + 2, line.npos);
        int pos_bar = ns.find("|");

        auto winning = str_to_arr(ns.substr(0, pos_bar));
        auto have = str_to_arr(ns.substr(pos_bar + 2, ns.npos));

        std::vector<int> common;
        std::set_intersection(winning.begin(), winning.end(), have.begin(), have.end(), std::back_inserter(common));

        matches[card_id] = common.size();
        n_copies[card_id] = 1;

    }

    int sum1 = 0;
    int sum2 = 0;
    for (int i = 1; i <= matches.size(); i++) {
        int card_id = i;
        int num_matches = matches[card_id];

        sum2 += n_copies[card_id];

        if (num_matches == 0)
            continue;
        
        int card_pts = pow(2, std::max(0, num_matches - 1));
        sum1 += card_pts;

        for (int j = 0; j < num_matches; j++)
            n_copies[card_id + 1 + j] += n_copies[card_id];
    }

    std::cout << "Part 1: " << sum1 << "\n";
    std::cout << "Part 2: " << sum2 << std::endl;

    return 0;

}