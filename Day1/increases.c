#include <stdio.h>
#include <stdbool.h>

int main(int argc, char *argvs[]) {
    int num_inputs = 2000;

    bool is_previous_set = false;
    int previous;
    int current;
    int count;

    FILE* fp = fopen("input.txt", "r");

    while(fscanf(fp, "%d", &current) == 1) {
        if (is_previous_set == true) {
            if (current-previous > 0) {
                count++;
            }
        }
        previous = current;
        if (is_previous_set == false) {
            is_previous_set = true;
        }
    }
        
    printf("%d\n", count);
    fclose(fp);
}