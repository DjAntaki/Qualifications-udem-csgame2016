/* Code grandement inspiré de l'article de wikipédia sur le tri bitonique */
#include <stdio.h>

typedef enum { false, true } bool;


void swap(int* a, int*b)
{
  int tmp = *a; *a = *b; *b = tmp;
}


void print_array(int* x)
{
  while (*x >= 0)
    {
      printf("%d, ", *x);
      x++;
    }
}


void compare(bool up, int* x, int start, int end)
{
  int dist = (end - start) / 2;
  int i = 0, tmp = 0;

  for(i = start; i < dist + start; i++)
    if ((x[i] > x[i + dist]) == up)
      swap(&x[i], &x[i + dist]);
}


void merge(bool up, int* x, int start, int end)
{
  if (end - start > 1)
    {
      compare(up, x, start, end);
      merge(up, x, start, (end - start) / 2 + start);
      merge(up, x, (end - start) / 2 + start, end);
    }
}


void bitonic_sort(bool up, int* x, int start, int end)
{
  if (end - start > 1)
    {
      bitonic_sort(true, x, start, (end - start) / 2 + start);
      bitonic_sort(false, x, (end - start) / 2 + start, end);
      merge(up, x, start, end);
    }
}


int main (void)
{
  int t[17] = {67, 8,  9,  11, 35, 22, 7,  63, 68, 0,
               20, 41, 62, 32, 48, 2, -1};
  printf("tableau initial\n");
  print_array(t);
  printf("\n\ntableau ordonne\n");
  bitonic_sort(true, t, 0, 16);
  print_array(t);
  printf("\n");
}
