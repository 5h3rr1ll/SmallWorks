#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Hier wird die Klasse Parent erzeugt.
class Parent(object):
# Die Klasse Parent hat eine Methode override, die etwas printet
    def override(self):
        print("PARENT override()")
# s.o
    def implicit(self):
        print("PARENT implicit()")
# s.o.
    def altered(self):
        print("PARENT altered()")

#Hier wird die Klasse Child erzeugt
class Child(Parent):
# Die Child Klasse überschreibt hier die Methode override von der Eltern-Klasse
# um seinen eigenen Print auszugeben
    def override(self):
        print("CHILD override()")

# auch hier überrschreibt die Child klasse vorerst die Methode altered...
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
# Nun greift sie via super(Klasse, self).funktion (Methode) auf die Eltern-Klasse
# zu und führt die Methode wie dort definiert aus...
        super(Child, self).altered()
# und überschreibt dann erneut die Methode.
        print("CHILD,AFTER PARENT altered()")

# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()
#
# dad.override()
# son.override()
#
# dad.altered()
# son.altered()
