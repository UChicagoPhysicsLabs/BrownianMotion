import trackpy as tp
def batch(frames,d,mm):
	a= tp.batch(frames, diameter=d, minmass=mm, invert=True,processes=1)
	return a