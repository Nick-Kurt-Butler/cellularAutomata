from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import gridspec
import numpy as np
import random as rand
from IPython.display import HTML

def base_rep(x,b=2,l=8):
	"""
	Finds the backwards base representation in a list format

	Parameters
	----------
		x: A decimal number
		b: The base to represent, default b=2 means binary
		l: the size of list to put representation in; default l=8

	Returns
	-------
		A list of length l of the digits in base b of
		number x

		Exp:
			: base_rep(9,2,8)
			> [1,0,0,1,0,0,0,0]

			: baes_rep(23,3,5)
			> [2,1,2,0,0]
	"""
	if l == 0:
		return []
	return [int(x%b)] + base_rep((x-x%b)/b,b,l-1)



def cell_auto(rule=0,rows=10,base=2,radius=1,totalistic=False,random=False,func=None):
	"""
	Produces a 2D array of numbers from a 1D cellular automaton rule

	Parameters
	----------
	rule: this is any integer
	rows: this is a positive interger that gives the number of iterations
		in the program
	base: the default is 2 for binaray, 3 would be ternary and so on
	radius: Standard cellular automaton has a radius of one where the 3
		cells above determine the one below.  A radius of two would
		have the 5 cells above to determine the cell below.  The
		numbers of cells is then 2*radius+1 and the default in this
		program is 1.
	totalistic: Sums the total number of blacks cells above, default False
	random: default is false, true for random initial conditions
	"""
	X = np.zeros([2*rows,4*rows+radius])
	bits = base_rep(rule,base,base**(2*radius+1))

	# sets initial conditions
	if random:
		X[0] = np.random.randint(base,size=4*rows+radius)
	else:
		X[0,2*rows] = 1

	# alters bits if type is specified to be "totalistic"
	if totalistic or func:
		bits = base_rep(rule,base,(2*radius+1)*(base-1)+1)
		base = 1

	# main loop to alter 2D array
	for i in range(1,2*rows):
		for j in range(radius,4*rows):
			cells_above = [base**x*X[i-1,j+radius-x] for x in range(2*radius+1)]
			if func == None:
				X[i,j] = bits[int(sum(cells_above))]
			else:
				X[i,j] = func(cells_above[::-1]) # for continuous cell auto

	# Zooms in on graph to get rid of edge bounding results
	return X[0:rows,rows:3*rows]

def cell_auto_frames(rule=0,rows=10,base=2,radius=1,totalistic=False,random=False,func=None):
	"""
	This function turns an n row 2D array into a 3D array where each
	frame is one more row added from the previous frame

	Parameters
        ----------
        rule: this is any integer
        rows: this is a positive interger that gives the number of iterations
                in the program
        base: the default is 2 for binaray, 3 would be ternary and so on
        radius: Standard cellular automaton has a radius of one where the 3
                cells above determine the one below.  A radius of two would
                have the 5 cells above to determine the cell below.  The
                numbers of cells is then 2*radius+1 and the default in this
                program is 1.
	totalistic: Sums the total number of blacks cells above, default False
	random: default is false, true for random initial conditions
	"""

	X = cell_auto(rule=rule,rows=rows,base=base,radius=radius,totalistic=totalistic,random=random,func=func)
	frames = np.zeros([rows,rows,2*rows])
	for i in range(rows):
		frames[i][:i+1,:] = X[:i+1,:]
	return frames

def animate(canvas,seconds=10,color="Greys",save=False):
	"""
	Displays frame per frame progression of a cellular automaton

	Parameters
	----------
	canvas: A 3D array where canvas[0] is the first frame in the animation
	color: See matplotlib color map for more colors, default is "Greys"
	seconds: the time it take in seconds for the animation to end.
			Default is 10 seconds.
	"""

	fig = plt.figure(figsize = (8,4))
	plt.axis("off")

	im = plt.imshow(canvas[0],cmap=color)
	frames = len(canvas)
	def animate_func(i):
		im.set_array(canvas[i])
		return [im]
	anim = animation.FuncAnimation(fig,animate_func,frames=frames,interval=1000*seconds/frames,repeat=True)
	html = HTML(anim.to_jshtml())
	display(html)
	plt.close()
	if save:
		anim.save(save,writer=animation.writers['ffmpeg']())


def conway_update(X):
	"""
	Updates a single frame based on Conway's game of life

	Parameters
	----------
		X: A 2D array that has only ones and zeros
	"""
	def live_or_die(i,j):
		"""
		Returns 1 if cells lives and 0 otherwise
		"""
		num =  X[i-1,j-1]+X[i-1,j]+X[i-1,j+1]+X[i,j-1]
		num += X[i+1,j-1]+X[i+1,j]+X[i+1,j+1]+X[i,j+1]
		if (X[i,j]==1 and num in [2,3]) or (X[i,j]==0 and num==3):
			return 1
		return 0
	new = np.zeros_like(X).copy()
	for i,row in enumerate(X):
		for j,col in enumerate(row):
			try:
				new[i,j] = live_or_die(i,j)
			except:
				new[i,j] = 0 #edge case
	return new;

def conway(X,n,seconds=10,color="Greys",save=False):
	"""
	An animation of conway's game of life

	Parameters
	----------
		X: A 2D array of ones and zeros
		n: number of update frames
		seconds: the time in second to run the animation once
		color: default "Greys" see matplotlib cmap for more
	"""
	frames = [X]
	for i in range(0,n):
		frames.append(conway_update(frames[i]))
	animate(frames,seconds=seconds,color=color,save=save)

def subplots(x,y):
	"""
	Helps to order the cell plots if there is a large amount of subplots needed.

	Parameters
	----------
		x: the number of rows
		y: the number of columns

	Returns
	-------
		A tuple holding the figure and axes
		Note that ax is a 1D array with size x*y
		this makes it easy to index the array
		return (fig,ax)
	"""
	fig,ax = plt.subplots(x,y,figsize = (8*y,4*x))
	ax = ax.reshape(x*y)
	gs1 = gridspec.GridSpec(x,y)
	gs1.update(wspace=0,hspace=0.05)
	for i in range(x*y):
		ax[i] = plt.subplot(gs1[i])
	plt.setp(ax,xticks=[],yticks=[]) # gets rid of ticks
	return (fig,ax)
