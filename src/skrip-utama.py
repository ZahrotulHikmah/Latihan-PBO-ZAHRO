from luas.segitiga import luas_segitiga
from luas import lingkaran, persegi
from volume.kubik import volume_kubik
import volume.bola
from volume.prisma import *

#Luas Segitiga
print("Luas Segitiga = " ,luas_segitiga(21,4))

#Luas Lingkaran dan Persegi
print("Luas Lingkaran = " ,lingkaran.luas_lingkaran(14))
print("Luas Persegi = " ,persegi.luas_persegi(23))

#Volume Kubik
print("Volume Kubik = " ,volume_kubik(20))

#Volume Bola
print("Volume Bola = " ,volume.bola.volume_bola(43))

#Volume Prisma
print("Volume Prisma = ",volume_prisma(6,9,7))