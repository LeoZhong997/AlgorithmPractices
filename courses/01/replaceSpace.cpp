class Solution {
public:
    string replaceSpace(string s) {
        // Time: O(N)
        // Space: O(1)
        int count = 0, len = s.size();
        // count num of space
        for (char c: s) {
            if (c == ' ') count++;
        }
        if (count == 0) {
            return s;
        }
        // string is length-variable in c++
        s.resize(len + 2 * count);
        // reverse traverse
        for (int i = len - 1, j = s.size() - 1; i < j; i--, j--) {
            if (s[i] != ' ')
                s[j] = s[i];
            else {
                s[j - 2] = '%';
                s[j - 1] = '2';
                s[j] = '0';
                j -= 2;
            }
        }
        return s;
    }
};