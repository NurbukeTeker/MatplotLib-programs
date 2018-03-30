import matplotlib.pyplot as plt
import numpy as np

metrekare = np.random.rand(100)
gercekhayatmetrekare = 80 + 100*metrekare
print(gercekhayatmetrekare)

fiyat = gercekhayatmetrekare*2+35*np.random.rand(100)
metrekare =gercekhayatmetrekare

def hatahesapla(m,b,x,y):
    toplamhata = 0
    for i in range(100):
        toplamhata = toplamhata + (y[i]-(m*x[i]+b))**2
    return toplamhata


def turevhesapla(bsimdi,msimdi,x,y,learningrate):
    bturev = 0
    mturev = 0
    for i in range(100):
        bturev = -(y[i]-(msimdi*x[i]+bsimdi))
        mturev = -x[i]*(y[i]-(msimdi*x[i]+bsimdi))
        yeni_b = bsimdi-(learningrate*bturev)
        yeni_m = msimdi-(learningrate*mturev)
        bturev = 0
        mturev = 0
    return yeni_m,yeni_b

def calistir(x,y,b,m,learningrate,tekrar,hatagoster = True):

    hata = np.array([])
    if hatagoster==True:
        for i in range(tekrar):
            m,b = turevhesapla(b,m,x,y,learningrate)
            hata = np.append(hata,hatahesapla(m,b,x,y))
        return m,b,hata

m,b,hatamiz = calistir(metrekare,fiyat,0.02,0.02,0.00001,500)

print(m)
print(b)

linearreg = m*metrekare+b

plt.scatter(metrekare,fiyat)
plt.plot(0)
plt.show()
plt.scatter(metrekare,fiyat)
plt.plot(metrekare,linearreg)
plt.show()

plt.plot(np.arange(0,len(hatamiz))+1,hatamiz)
plt.show()
