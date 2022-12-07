#include <stdio.h>
int checkunique(char chars[], int size);
int totalchars(int markersize);
int main() {
  printf("Part 1: %d\nPart 2: %d\n", totalchars(4), totalchars(14));
}

int totalchars(int markersize) {
  FILE *fp = fopen("input.txt", "r");
  if (fp == NULL) {
    printf("Could not open file");
    return 1;
  }
  char buffer[markersize];
  int total = 0;
  char ch;
  while ((ch = fgetc(fp)) != EOF &&
         (total < markersize || !checkunique(buffer, markersize))) {
    buffer[total++ % markersize] = ch;
  }
  fclose(fp);
  return total;
}

int checkunique(char chars[], int size) {
  for (int i = 0; i < size; i++) {
    for (int j = i + 1; j < size; j++) {
      if (chars[i] == chars[j]) {
        return 0;
      }
    }
  }
  return 1;
}
