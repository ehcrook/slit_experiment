#include "buckets.h"
#include <iostream>
#include <vector>
#include <stdlib.h>
#include <time.h>
using namespace std;

vector<vector<float> > Buckets::bucket(vector<float> intensity, vector<float> y)
{
	vector<vector<float> > result;

	// calculating the probabilities for each point in the distribution
	float sum = 0;
	for(unsigned int i = 0; i < intensity.size(); i++)
		sum += intensity[i];
	
	vector<float> probabilities;
	for(unsigned int i = 0; i < intensity.size(); i++)
		probabilities.push_back((intensity[i]/sum)*100);

	// making the probability buckets
	vector<vector<float> > buckets;
	vector<vector<float> > bucket_intensity;
	vector<float> current_bucket;
	vector<float> current_intensity;
	float current_sum = 0;

	for(unsigned int i = 0; i < probabilities.size(); i++)
	{
		float prob = probabilities[i];
		current_bucket.push_back(y[i]);
		current_intensity.push_back(intensity[i]);
		current_sum += prob;
		if(1-current_sum < 0.01)
		{
			buckets.push_back(current_bucket);
			bucket_intensity.push_back(current_intensity);
			current_sum = 0;
			current_bucket.clear();
			current_intensity.clear();
		}
	}

	// selecting a particular bucket
	srand(time(NULL));
	int num = rand() % buckets.size();
	result.push_back(buckets[num]);
	result.push_back(bucket_intensity[num]);

	return result;
}