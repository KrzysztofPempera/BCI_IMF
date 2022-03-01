import numpy as np
import sklearn.cross_decomposition as sk
import sys

np.set_printoptions(threshold=sys.maxsize)

#ref_signal = []

#t = np.arange(0,100/10,1)

#t2 = np.arange(0,200/10,1)

#ref_signal.append(np.sin(np.pi*2*10*t))


#ref_signal.append(np.cos(np.pi*2*10*t))

#ref_signal = np.array(ref_signal)


#ref_signal2 = []

#ref_signal2.append(np.sin(np.pi*2*14*t))
#ref_signal2.append(np.cos(np.pi*2*14*t))

#ref_signal2 = np.array(ref_signal2)

#freq = np.array([ref_signal,ref_signal2])

#temp = []

#temp.append(ref_signal)
#temp.append(ref_signal2)

#temp = np.array([temp])

#print(temp.shape)

#print(freq.shape)

#freqT = freq.T

#cca = sk.CCA(1)

#signal = []



#signal.append(np.sin(np.pi*2*5*t))


#signal = np.array(signal)

#cca.fit(np.squeeze(freq[0,:,:]).T,signal.T)

#x,y = cca.transform(np.squeeze(freq[0,:,:]).T,signal.T)

#corr = np.corrcoef(x[:,0],y[:,0])[0,1]

#print(corr)

#cca.fit(np.squeeze(freqT[2,:,:]),np.squeeze(freqT[3,:,:]))

#x,y = cca.transform(np.squeeze(freqT[2,:,:]),np.squeeze(freqT[3,:,:]))



#corr = np.corrcoef(x[:,0],y[:,0])

#print(corr)

#mat = []

#n = []
#n.append([1,2,3,4,5,6])
#n.append([1,2,3,4,5,1])

#mat.append(np.array(n))
#n = np.array(n)


#k = []
#k.append([5,3,2,1,0,0])
#k.append([5,4,3,2,1,0])

#mat.append(np.array(k))
#k = np.array(k)

#l = []
#l.append([0,0,1,1,2,2])
#l.append([2,2,1,1,0,0])

#mat.append(np.array(l))
#l = np.array(l)

#mat = np.array(mat)

#mat2 = np.array([n,k,l])

#x,y = cca.transform(np.squeeze(mat[0,:,:]).T,np.squeeze(mat[1,:,:]).T)



data2 = []

for i in range(2):
    data = []
    data.append(np.array([i,1,2,3,4,5]))
    data.append(np.array([0,i,2,3,4,5]))

    data2.append( np.array(data))

data2 = np.array(data2)


data3 = [[i,1,2,3,4,5] for i in range(5)]


channel, data3 = data3[0], np.delete(data3,0,0)



buffer = np.array(channel).reshape(tuple([5,6]))

print(np.squeeze(data2[0,:,:]).T,np.squeeze(data2[0,:,:]).T.shape)


print(buffer.T,buffer.T.shape)

#cca = sk.CCA(1)

#cca.fit(buffer.T,np.squeeze(data2[0,:,:]).T)

#x,y = cca.transform(buffer.T,np.squeeze(data2[0,:,:]).T)

#print(x,y)