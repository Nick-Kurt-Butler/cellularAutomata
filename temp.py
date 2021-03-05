from cell_auto_lib import *

plt.axis('off')

fix,ax = subplots(2,2)
ax[0].imshow(cell_auto(1599,300,base=3,random=True,totalistic=True),cmap="Greys");
#ax[0].text(30,45,1599,size=25,color="black",backgroundcolor="white")
ax[1].imshow(cell_auto(1599,100,base=3,random=True,totalistic=True),cmap="Greys");
#ax[1].text(10,15,1599,size=25,color="black",backgroundcolor="white")

ax[2].imshow(cell_auto(357,300,base=3,random=True,totalistic=True),cmap="Greys");
#ax[2].text(30,45,357,size=25,color="black",backgroundcolor="white")
ax[3].imshow(cell_auto(357,100,base=3,random=True,totalistic=True),cmap="Greys");
#ax[3].text(10,15,357,size=25,color="black",backgroundcolor="white");

plt.show()
