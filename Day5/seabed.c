#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>

const char* filename = "input.txt";

int* calculate_points(int x1, int y1, int x2, int y2) {
    if (x1 == x2) {
        // vertical line
        int points = malloc(2 * abs(y2 - y1) * sizeof(int));
        int upper_bound, lower_bound;
        if (y1 > y2) {
            upper_bound = y1;
            lower_bound = y2;
        } else {
            upper_bound = y2;
            lower_bound = y1;
        }
        for (int index = 0; index < upper_bound - lower_bound + 1; index++) {
            int position = 2*index + 1;
            points[&position] = index + lower_bound;
        }
        return points;
    } else {
        int test[] = {1,2};
        return test;
    }
}

int main(int argc, char* argv[]) {
    FILE* fp = fopen(filename, "r");

    struct stat sb;
    stat(filename, &sb);

    int x1;
    int x2;
    int y1;
    int y2;

    while (fscanf(fp, "%d,%d -> %d,%d\n", &x1, &y1, &x2, &y2) != EOF) {
        printf("%d,%d -> %d,%d\n", x1, y1, x2, y2);
        int arr[] = calculate_points(x1, y1, x2, y2);
    }

    fclose(fp);
    exit(EXIT_SUCCESS);

    return 0;
}