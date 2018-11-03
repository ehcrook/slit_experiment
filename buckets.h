#ifndef buckets_h_
#define buckets_h_
#include <vector>
using namespace std;

class Buckets {
    public:
        vector<vector<float> > bucket(vector<float> intensity, vector<float> y);
};

#endif