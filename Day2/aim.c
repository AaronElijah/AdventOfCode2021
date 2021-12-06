#include <stdio.h>
#include <stdlib.h> 

int main(int argc, char* argv[]) {
    int position[] = {0,0}; // {horizontal, vertical}
    int aim = 0;

    char *line = NULL;
    size_t len = 0;
    char read;
    FILE* fp = fopen("input.txt", "r");

    while ((read = getline(&line , &len, fp)) != -1) {
        switch (line[0]) {
            case ('u'): aim = aim - atoi(&line[3]);
            case ('d'): aim = aim + atoi(&line[5]);
            case ('f'):
                position[0] = position[0] + atoi(&line[8]);
                position[1] = position[1] + aim*atoi(&line[8]);
                break;
        }
        line = NULL;
    }

    if (line) {
        free(line);
    } 
    printf("%d %d\n", position[0], position[1]);
    printf("%d\n", position[0]*position[1]);
    fclose(fp);
    return 0 ;
}