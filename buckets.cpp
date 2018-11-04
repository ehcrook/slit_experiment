#include "buckets.h"
#include <iostream>
#include <list>
#include <stdlib.h>
#include <time.h>
using namespace std;

list<list<float> > bucket(list<float> intensity, list<float> y)
{
	list<list<float> > result;

	// calculating the probabilities for each point in the distribution
	float sum = 0;
	for(list<float>::iterator itr = intensity.begin(); itr != intensity.end(); itr++)
		sum += *itr;
	
	list<float> probabilities;
	for(list<float>::iterator itr = intensity.begin(); itr != intensity.end(); itr++)
		probabilities.push_back((*itr/sum)*100);

	// making the probability buckets
	list<list<float> > buckets;
	list<list<float> > bucket_intensity;
	list<float> current_bucket;
	list<float> current_intensity;
	float current_sum = 0;

	list<float>::iterator itr1 = intensity.begin();
	list<float>::iterator itr2 = probabilities.begin();
	list<float>::iterator itr3 = y.begin();

	for(; itr1 != intensity.end(); itr1++, itr2++, itr3++)
	{
		float prob = *itr2;
		current_bucket.push_back(*itr3);
		current_intensity.push_back(*itr1);
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

	// selecting a particular bucket at random
	// as they should have the same probability
	// of finding the particle there
	srand(time(NULL));
	int num = rand() % buckets.size();
	list<list<float> >::iterator ij = buckets.begin();
	list<list<float> >::iterator ji = bucket_intensity.begin();
	for(int i = 0; i < num; i++)
	{
		ij++;
		ji++;
	}
	result.push_back(*ij);
	result.push_back(*ji);

	return result;
}