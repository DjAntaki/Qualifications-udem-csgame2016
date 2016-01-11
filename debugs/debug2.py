#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Une petite implentation d'une pile.
# Pour créer une pile, il d'appeler push avec seulement une
# valeur.


# Mais bon il y a un bug! Modifier les fonctions
# pour le corriger.

def push(val, stack=[]):
  stack.append(val)
  return stack

def top(stack):
  return stack[-1] if len(stack) > 0 else None

def pop(stack):
  stack.pop()
  return stack


a = push(1)
a = push(2, a)
a = push(3, a)

print a

b = push(top(a))
a = pop(a)
b = push(top(a), b)
a = pop(a)
b = push(top(a), b)
a = pop(a)

print a
print b

