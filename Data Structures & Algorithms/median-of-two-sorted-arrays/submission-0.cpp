class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<double> myvector;
        double ret = 0;
        int count1 = 0;
        int count2 = 0;
        while (count1 < nums1.size() || count2 < nums2.size()) {
            if(count1 >= nums1.size()) {
                myvector.push_back(nums2[count2]);
                count2++;
            } 
            else if (count2 >= nums2.size()) {
                myvector.push_back(nums1[count1]);
                count1++;
            }
            else if(nums1[count1] < nums2[count2]) {
                myvector.push_back(nums1[count1]);
                count1++;
            } else {
                myvector.push_back(nums2[count2]);
                count2++;
            }
        }
        if (myvector.size() % 2 == 0) {
            ret = (myvector[myvector.size() / 2 - 1] + myvector[myvector.size() / 2]) / 2;
        } else {
            ret = myvector[myvector.size()  / 2];
        }
        return ret;
    }
};