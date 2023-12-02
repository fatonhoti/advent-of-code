#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <unordered_map>

int main() {

    // Parse input
    std::ifstream file("day_1.txt");
    std::vector<std::string> lines;
    if (file.is_open()){
        std::string line;
        while (std::getline(file, line))
            lines.push_back(line);
    } else {
        std::cerr << "Failed opening file" << std::endl;
        return -1;
    }

    // Part 1
    auto is_digit = [](char& c) {
        return c >= '0' && c <= '9';
    };

    int sum1 = 0;
    for (auto& line : lines) {
        std::string first{""};
        std::string last{""};
        for (auto& c : line) {
            if (is_digit(c)) {
                last = c;
                if (first.empty())
                    first = c;
            }
        }
        sum1 += std::stoi(first + last);
    }
    std::cout << "Part 1: " << sum1 << std::endl;

    // Part 2
    std::unordered_map<std::string, std::string> spelled_out;
    spelled_out = {
        {"zero", "0"},
        {"one", "1"},
        {"two", "2"},
        {"three", "3"},
        {"four", "4"},
        {"five", "5"},
        {"six", "6"},
        {"seven", "7"},
        {"eight", "8"},
        {"nine", "9"},
    };

    int sum2 = 0;
    for (auto& line : lines) {
        std::string first = "";
        std::string last = "";
        for (size_t i = 0; i < line.length(); i++) {
            char& one = line.at(i);
            std::string three = line.substr(i, 3);
            std::string four = line.substr(i, 4);
            std::string five = line.substr(i, 5);

            if (is_digit(one))
                last = one;
            else if (spelled_out.find(three) != spelled_out.end())
                last = spelled_out[three];
            else if (spelled_out.find(four) != spelled_out.end())
                last = spelled_out[four];
            else if (spelled_out.find(five) != spelled_out.end())
                last = spelled_out[five];
            if (first.empty())
                first = last;
        }
        sum2 += std::stoi(first + last);
    }
    std::cout << "Part 2: " << sum2 << std::endl;

    return 0;

}