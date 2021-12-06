#include <stdio.h>
#include <stdbool.h>

bool value_in_array(int array[], int value) {
    for (int i = 0; i < 3; i++) {
        if (array[i] == value) {
            return true;
        }
    }
    return false;
}

int sum(int array[]) {
    int val = 0;
    for (int i = 0; i < 3; i++) {
        val = val + array[i];
    }
    return val;
}

int main(int argc, char *argvs[]) {
    int num_inputs = 2000;

    int previous_window[] = {-1, -1, -1};
    int current_window[] = {-1, -1, -1};
    int head;
    int count;

    FILE* fp = fopen("input.txt", "r");

    while(fscanf(fp, "%d", &head) == 1) {
        current_window[2] = current_window[1];
        current_window[1] = current_window[0];
        current_window[0] = head;

        

        if (value_in_array(previous_window, -1)) {
            printf("Previous window not full set\n");
        } else {
            printf("%d %d %d\n", current_window[0], current_window[1], current_window[2]);
            printf("%d %d %d\n", previous_window[0], previous_window[1], previous_window[2]);
            printf("%d\n", sum(current_window) > sum(previous_window));
            if (sum(current_window) > sum(previous_window)) {
                count++;
            }
        }

        previous_window[0] = current_window[0];
        previous_window[1] = current_window[1];
        previous_window[2] = current_window[2];
    }
        
    printf("%d\n", count);
    fclose(fp);
}