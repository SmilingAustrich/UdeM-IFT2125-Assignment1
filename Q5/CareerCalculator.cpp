#include "CareerCalculator.h"
#include <vector>
#include <math.h>
#include <iostream>

// ce fichier contient les definitions des methodes de la classe CareerCalculator
// this file contains the definitions of the methods of the CareerCalculator class

using namespace std;

CareerCalculator::CareerCalculator()
{
}

bool CareerCalculator::CalculateMaxCareer(const vector<int>& Steps) {
    int n = Steps.size();
    int maxReachableIdx = 0;
    int i = 0;

    while (i <= maxReachableIdx) { // Our greedy decision making process
      //We always choose the maximum possible reach at each step. Always choosing a local optimum.
        maxReachableIdx = max(maxReachableIdx, i + Steps[i]);
        if (maxReachableIdx >= n - 1) return true; // Reached or exceeded the last index, optimal solution found.
        i++;
    }

    return false; // If we exit, we couldn't reach the last index.
}
