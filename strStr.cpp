class Solution
{
public:
    int strStr(string haystack, string needle) {
        int m = needle.length(), n = haystack.length();
        if (!m) return 0;
        vector <int> next(m, 0);
        next[0] = -1;
        int j = -1;
        for (int i = 0; i < m - 1; i++) {
            while (j >= 0 && needle[j] != needle[i]) j = next[j];
            j++;
            next[i + 1] = j;
        }

        j = 0;
        for (int i = 0; i < n; i++)
        {
            while (j >= 0 && haystack[i] != needle[j]) j = next[j];
            j++;
            if (j == m) return i - m + 1;
        }

        return -1;
    }
};
