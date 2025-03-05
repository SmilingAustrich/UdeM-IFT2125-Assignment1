#include "MaxToysCalculator.h"
#include <vector>
#include <math.h>
#include <iostream>

// ce fichier contient les definitions des methodes de la classe MaxToysCalculator
// this file contains the definitions of the methods of the MaxToysCalculator class


using namespace std;

MaxToysCalculator::MaxToysCalculator() {}

int MaxToysCalculator::CalculateMaxToys(const vector<int>& Toys, int S) {
    int left = 0, right = 0;
    int n = Toys.size();
    int current_sum = 0; // To keep track of the sum of the prices within the window
    int max_length = 0;

    while (right < n) { // Greedy part, as long as our right pointer is smaller than the number of toys
        // Add the current toy price to the sum
        current_sum += Toys[right];

        // If the sum exceeds the budget, move left pointer to reduce it
        while (current_sum > S && left <= right) {
            current_sum -= Toys[left]; // the left pointer goes moves right. It removes elements from our current_sum
            left++;						// until the sum is within the budget S.
        }

        // Update maximum segment length
        max_length = max(max_length, right - left + 1); // Updating the maximum ammount of toys that fit in the budget

        // Move right pointer to expand the window
        right++;
    }

    return max_length;
}
