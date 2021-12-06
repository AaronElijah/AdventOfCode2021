#include <stdio.h>
#include <stdlib.h> 

int main(int argc, char* argv[]) {
    int binary_number_size = 12;
    int binary_count[] = {0,0,0,0,0,0,0,0,0,0,0,0};
    int gamma = 0;
    int epsilon = 0;

    char *line = NULL;
    size_t len = 0;
    char read;
    FILE* fp = fopen("input.txt", "r");

    while ((read = getline(&line , &len, fp)) != -1) {
        for (int i = 0; i < binary_number_size; i++) {
            if (line[i] == '0') {
                binary_count[i] = binary_count[i] - 1;
            } else {
                binary_count[i] = binary_count[i] + 1;
            }
        }
        line = NULL;
    }

    if (line) {
        free(line);
    } 
    fclose(fp);

    for (int i = binary_number_size-1; i >= 0; i--) {
        // create gamma and epsilon using bitwise operators
        if (binary_count[binary_number_size-1-i] > 0) {
            gamma = gamma + (1 << i);
        } else {
            epsilon = epsilon + (1 << i);
        }
    }

    printf("%d %d\n", gamma, epsilon);
    printf("%d\n", gamma*epsilon);
    
    return 0 ;
}