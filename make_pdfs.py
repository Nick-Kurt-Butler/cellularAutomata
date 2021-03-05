from cell_auto_lib import *
from time import time

start = time()

fig,ax = subplots(64,4)
for rule in range(256):
    ax[rule].text(10,15,rule,size=25,color="white",backgroundcolor="black")
    ax[rule].imshow(cell_auto(rule,100),cmap="Greys");
plt.savefig("media/1D_Cell_Auto.pdf")

print(time()-start)

start = time()

fig,ax = subplots(64,4)
for rule in range(256):
    ax[rule].text(10,15,rule,size=25,color="white",backgroundcolor="black")
    ax[rule].imshow(cell_auto(rule,100,ic="random"),cmap="Greys");
plt.savefig("media/1D_Cell_Auto_Random_IC.pdf")

print(time()-start)

#plt.show()
