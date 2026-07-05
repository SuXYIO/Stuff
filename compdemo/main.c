/*
Demonstration of the compiling process of c
*/

#include "bar.h"

#define FOO 42

#if FOO > 0
#define BAR 1
#else
#define BAR 0
#endif

int sub(int, int);

int main() {
    add(FOO, BAR);
    sub(FOO, BAR);
}

int sub(int a, int b) { return a - b; }
