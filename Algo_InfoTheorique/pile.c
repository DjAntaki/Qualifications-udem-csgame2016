#include <stdio.h>
#include <stdlib.h>


typedef struct Pile
{
  int val;
  int refcount;
  struct Pile* next;
} Pile;


Pile* empile (int val, Pile* p)
{
  Pile* nouvelle_pile = (Pile*) malloc(sizeof(Pile));
  nouvelle_pile->val = val;
  nouvelle_pile->next = p;
  nouvelle_pile->refcount = 0;
  if (NULL != p)
    p->refcount++;
  return nouvelle_pile;
};


// Sert à protéger une référence de la collecte par reference counting.
Pile* ref (Pile* p)
{
  p->refcount++;
  return p;
}


// Sert à relacher une référence afin quelle soit libérée par le
// reference counting.
Pile* unref (Pile* p)
{
  p->refcount--;
  return p;
}


// Utiliser pour libérer la mémoire utilisée par la pile.
void free_pile (Pile* p)
{
  if (NULL != p && p->refcount == 0)
    {
      p->next->refcount--;
      free (p);
      free_pile (p->next);
    }
}


Pile* depile (Pile* p)
{ 
  return p->next;  
}


int look (Pile* p)
{
  return p->val;
}


void print_pile(Pile* p)
{
  while (NULL != p)
  {
    printf("%d ", look(p));
    p = depile(p);
  }
  printf("\n");
}


int main (void)
{
  int i;
  Pile* p= NULL;
  Pile* a = NULL;
  for (i = 0; i < 20; i++)
    {
       p = empile(i, p);
    }
  print_pile(p);

  a = ref(p);
  for (i = 0; i < 10; i++)
    {
       p = depile(p);
    }
  
  for (i = 100; i < 110; i++)
    {
       p = empile(i, p);
    }

  print_pile(a);
  print_pile(p);

  // On voit ici que les piles partagent des données. Deux versions
  // coexistent.
  free_pile(a);
  print_pile(p);


}
