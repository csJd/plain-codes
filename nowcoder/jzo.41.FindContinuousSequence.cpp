/*
https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe

题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,
他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很
快的找出所有和为S的连续正数序列?Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<vector<int>> FindContinuousSequence(int sum) {
        vector<vector<int>> res;
        int left = 1, right = 2;
        int cursum = 3;
        while (left < right) {
            while (cursum < sum) {
                ++right;
                cursum += right;
            }
            if (cursum == sum) {
                vector<int> seq;
                for (int i = left; i <= right; ++i) {
                    seq.push_back(i);
                }
                res.push_back(seq);
            }
            cursum -= left;
            ++left;
        }
        return res;
    }
};

// int main() {
//     vector<vector<int>> res = Solution().FindContinuousSequence(100);
//     for (auto seq : res) {
//         for (int x : seq) {
//             cout << x << ' ';
//         }
//         cout << endl;
//     }
//     return 0;
// }