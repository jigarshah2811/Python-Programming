
#include <stdio.h>
#include <string.h>

int
collatz(int x)
{
    if (x & 1)
        return 3 * x + 1;
    return x >> 1;
}

int
count_vowels(char *s)
{
    int i, n, count=0;
    char c;

    n = strlen(s);
    for (i=0 ; i<n ; i++) {
        c = s[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            count++;
    }
    return count;
}

int
sumpoly(int n)
{
    int x, s=0;

    for (x = 0 ; x < n ; x++) {
        s += (3 * x * x + 2) * x - 5;
    }
    return s;
}
