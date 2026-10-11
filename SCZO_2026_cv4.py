import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread 
from skimage.color import rgb2gray
from skimage.exposure import equalize_hist,equalize_adapthist

plt.close('all')

# Ukol 1
# =============================================================================
# Nactete obraz "Matterhorn.jpg“, prevedte jej na sedotonovy, vytvorte histogram obrazu
# K obrazu prictete hodnotu 0.3 a zobrazte jej i s odpovidajicim histogramem
# Vytvorte dalsi obraz vynasobenim puvodniho obrazu hodnotou 1.5 a zobrazte jej i s odpovidajicim histogramem
# =============================================================================

# Nactete obraz "Matterhorn.jpg“, prevedte jej na sedotonovy, vytvorte histogram obrazu
img =rgb2gray(imread('data/Matterhorn.jpg'))

plt.figure()
plt.subplot(2,3,1)
plt.imshow(img,cmap='gray', vmin = 0, vmax = np.max(img))
plt.title('Originalni obraz')

plt.subplot(2,3,4)
...
plt.title('Histogram originalniho obrazu')
plt.xlabel('Jasova hodnota')
plt.ylabel('Cetnost')

plt.subplot(2,3,2)
plt.imshow(...,cmap='gray', vmin = 0, vmax = np.max(...))
plt.title('Obr + 0.3')
plt.subplot(2,3,5)
...
plt.title('Histogram obrazu po pricitani')
plt.xlabel('Jasova hodnota')
plt.ylabel('Cetnost')

plt.subplot(2,3,3)
plt.imshow(...,cmap='gray', vmin = 0, vmax = np.max(...))
plt.title('Obra * 1.5')
plt.subplot(2,3,6)
...
plt.title('Histogram obrazu po nasobeni')
plt.xlabel('Jasova hodnota')
plt.ylabel('Cetnost')

plt.show()


# Ukol 2
# =============================================================================
# Nactete obraz „rtg_ruka.jpg“, prevedte jej do rozsahu 0-1 a upravte jej tak, aby byla vyuzita cela skala stupnu sedi
# Porovnejte obrazy a jejich histogramy
# Vytvorte negativ obrazu a zobrazte jej spolu s jeho histogramem
# Upravte kontrast obrazu pomoci gama transformace s hodnotou γ>1 a γ<1
# Provedte vhodnou korekci nelinearniho zkresleni v obraze „gamma.png“ pomoci gama korekce
# =============================================================================
plt.close('all')

# Nactete obraz „rtg_ruka.jpg“, prevedte jej do rozsahu 0-1 a upravte jej tak, aby byla vyuzita cela skala stupnu sedi
img = imread('data/rtg_ruka.jpg')

# Porovnejte obrazy a jejich histogramy
plt.figure()
plt.subplot(2,2,1)
plt.imshow(img,cmap='gray', vmin=0,vmax=1)
plt.title('Originalni obraz')

plt.subplot(2,2,3)
...
plt.title('Histogram originalniho obrazu')
plt.xlabel('Jasova hodnota')
plt.ylabel('Cetnost')

plt.subplot(2,2,2)
plt.imshow(...,cmap='gray',vmin=0,vmax=1)
plt.title('Transformovany obraz')

plt.subplot(2,2,4)
...
plt.title('Histogram transformovaneho obrazu')
plt.xlabel('Jasova hodnota')
plt.ylabel('Cetnost')
plt.show()


plt.figure()
plt.subplot(2,3,1)
plt.imshow(...,cmap='gray',vmin=0,vmax=1)
plt.title('Negativ')

plt.subplot(2,3,4)
...
plt.title('Histogram negativu')
plt.xlabel('Jasova hodnota')
plt.ylabel('Cetnost')

plt.subplot(2,3,2)
plt.imshow(...,cmap='gray',vmin=0,vmax=1)
plt.title('Transformovany obraz gamma < 1')
plt.subplot(2,3,5)
...
plt.title('Histogram transformovaneho obrazu gamma < 1')
plt.xlabel('Jasova hodnota')
plt.ylabel('Cetnost')

plt.subplot(2,3,3)
plt.imshow(...,cmap='gray',vmin=0,vmax=1)
plt.title('Transformovany obraz gamma < 1')

plt.subplot(2,3,6)
...
plt.title('Histogram transformovaneho obrazu gamma > 1')
plt.xlabel('Jasova hodnota')
plt.ylabel('Cetnost')
plt.show()


plt.figure()
plt.subplot(1,2,1)
plt.imshow(...,cmap='gray',vmin=0,vmax=1)
plt.title('Originalni obraz')

plt.subplot(1,2,2)
plt.imshow(...,cmap='gray',vmin=0,vmax=1)
plt.title('Obr po gamma korekci')
plt.show()

# Ukol 3
# =============================================================================
# Nactete obraz "fotbal.png“, prevedte jej na sedotonovy o rozsahu 0-1
# Provedte ekvalizaci histogramu a zobrazte vysledny obraz s jeho histogramem (equalize_hist)
# Provedte kontrastne omezenou adaptivni ekvalizaci histogramu (CLAHE) a zobrazte vysledny obraz s jeho histogramem
# =============================================================================
plt.close('all')

# Nactete obraz "fotbal.png“, prevedte jej na sedotonovy o rozsahu 0-1
img = rgb2gray(imread('data/fotbal.png'))


plt.figure()
plt.subplot(2,3,1)
plt.imshow(img, vmin = 0, vmax = 1, cmap = 'gray')
plt.title('Originalni obraz')

plt.subplot(2,3,4)
...
plt.title('Histogram originalu')
plt.xlabel('Jasova hodnota')
plt.ylabel('Cetnost')

plt.subplot(2,3,2)
plt.imshow(..., vmin = 0, vmax = 1, cmap = 'gray')
plt.title('Ekvalizovany obraz')

plt.subplot(2,3,5)
...
plt.title('Histogram ekvalizovaneho')
plt.xlabel('Jasova hodnota')
plt.ylabel('Cetnost')

plt.subplot(2,3,3)
plt.imshow(..., vmin = 0, vmax = 1, cmap = 'gray')
plt.title('CLAHE')

plt.subplot(2,3,6)
...
plt.title('Histogram CLAHE')
plt.xlabel('Jasova hodnota')
plt.ylabel('Cetnost')
plt.show()
