#include <stdio.h>
#include <stdlib.h> 

int main(int argc, char* argv[]) {
    int position[] = {0,0};

    char *line = NULL;
    size_t len = 0;
    char read;
    FILE* fp = fopen("input.txt", "r");

    while ((read = getline(&line , &len, fp)) != -1) {
        switch (line[0]) {
            case ('u'): position[0] = position[0] - atoi(&line[3]);
            case ('d'): position[0] = position[0] + atoi(&line[5]);
            case ('f'): position[1] = position[1] + atoi(&line[8]);
        }
        line = NULL;
    }

    if (line) {
        free(line);
    } 
    printf("%d\n", position[0]*position[1]);
    fclose(fp);
    return 0 ;
}