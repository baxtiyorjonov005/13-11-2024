# -*- coding: utf-8 -*-
"""Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

def mashina_narxi(beligi):
  if belgi=="damas":
    return "7 000$"
  elif belgi== "nexia 3":
    return "8 500$"
  elif belgi=="cobolt":
     return "12 000$"
  elif belgi== "onix":
    return "14 500$"
  elif belgi=="monza":
     return "16 000$"
  elif belgi== "trekr":
    return "19 500$"
  elif belgi=="exinoxe":
     return "24 000$"
  elif belgi== "travers":
    return "27 500$"
  elif belgi=="trelblazer":
     return "40 000$"
  elif belgi=="tahoe":
     return "100 000$"
  else:
     return "GM ga murojaat qiling"
belgi=input("Mashina turini kiriting")
natija=mashina_narxi(belgi)
print(natija)

def kasallik_tashxisi(beligi):
  if belgi=="istima":
    return "parasetamol"
  elif belgi== "tish og'rig'i":
    return "qupen"
  elif belgi=="qorin og'rig'i":
     return "levomitsin"

  else:
    return "vrachga murojaat qiling"
belgi=input("Kasallik belgisini kiriting")
natija=kasallik_tashxisi(belgi)
print(natija)