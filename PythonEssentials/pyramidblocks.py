'''
Source: https://edube.org/learn/pe-1/lab-essentials-of-the-while-loop-3

Objectives
Familiarize the student with:
- using the while loop;
- finding the proper implementation of verbally defined rules;
- reflecting real-life situations in computer code.

Scenario
Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks.
They are building a pyramid.
Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat.
The pyramid is stacked according to one simple principle: each lower layer contains one block more
than the layer above. Your task is to write a program which reads the number of blocks the builders have,
and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers -
if the builders don't have a sufficient number of blocks and cannot complete the next layer,
they finish their work immediately.
'''

# Passos:
# 1) dizer o número de blocos
# 2) enquanto o número de blocos usados for menor ou igual ao número de blocos disponíveis,
# construir camadas, tal que e altura += 1
# 3) imprimir altura na tela

# 1) dizer o número de blocos:

blocks = int(input("Enter the number of blocks: "))

# 2) enquanto o número de blocos usados for menor ou igual ao número de blocos disponíveis,
# construir camadas, tal que e altura += 1

'''height = 0
usedblocks = 1

while usedblocks <= blocks:
    height += 1
    usedblocks += height
    blocks -= usedblocks
'''

# solução
height = 0
in_layer = 1

while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1

# 3) imprimir altura na tela:

print("The height of the pyramid:", height)
