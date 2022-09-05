#include <iostream>
#include <vector>
#include <set>

int main()
{

    // Input
    int a;
    std::set<int> nums;
    std::vector<int> numsv;
    while (std::cin >> a)
    {
        nums.insert(a);
        numsv.push_back(a);
    }

    // Part 1
    for (auto &n : nums)
    {
        if (nums.find(2020 - n) != nums.end())
        {
            std::cout << "Part 1: " << n * (2020 - n) << std::endl;
            break;
        }
    }

    // Part 2
    int found = 0;
    for (int i = 0; i < numsv.size() - 2; i++)
    {
        int a = numsv[i];
        for (int j = i + 1; j < numsv.size(); j++)
        {
            int b = numsv[j];
            if (nums.find(2020 - a - b) != nums.end())
            {
                std::cout << "Part 2: " << a * b * (2020 - a - b) << std::endl;
                found = 1;
                break;
            }
        }
        if (found)
        {
            break;
        }
    }

    return 0;
}