#include <assert.h>
#include <stdio.h>
#include <string.h>

/*
Tryin to iterate through all floats,
to make a visualization of float distribution.

Ran for a few minutes and took up 20 gigs!
And my computer definitely can't do it.

Also this code is really shitty, and unsafe of course.
*/

int main() {
    unsigned i;
    float f;
    assert(sizeof(i) == sizeof(f));

    for (i = 0; i < ~0; i++) {
        memcpy(&f, &i, sizeof(i));

        printf("%.40f\n", f);
    }
}
