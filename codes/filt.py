from obspy import read
from obspy.signal.filter import bandpass
import matplotlib.pyplot as plt
from obspy import Trace
st = read()

tr = st[0]

data_filt = bandpass(data=tr.data, freqmin=1.0, freqmax=12, df=tr.stats.sampling_rate, corners=4, zerophase=False)

tr_new = Trace(data_filt)

tr_new.plot()