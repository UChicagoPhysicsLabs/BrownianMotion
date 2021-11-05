import trackpy as tp
def batch(frames,d,mm,sepa):
	a= tp.batch(frames, diameter=d, minmass=mm, invert=True,processes=1,separation=sepa)
	return a