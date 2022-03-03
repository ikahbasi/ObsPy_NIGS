from obspy import read
from obspy.signal.trigger import recursive_sta_lta
import matplotlib.pyplot as plt

st = read("../sample-data/envelop.mseed")

st = st.select(component="Z")

st.merge(method=-1)
st.detrend('constant')
st.merge(fill_value=0)



tr = st[0]


data = tr.data
time = tr.times()

tr_nsta = int(5 * tr.stats.sampling_rate)
tr_nlta = int(10 * tr.stats.sampling_rate)
cft = recursive_sta_lta(a=data,
                        nsta=tr_nsta,
                        nlta=tr_nlta)

mask = cft > 1.5

time_eq = time[mask]
time_trigger = time_eq[0]
time_trigger_2 = tr.stats.starttime + time_trigger

print(tr.id, time_trigger_2)
