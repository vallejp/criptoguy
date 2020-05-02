import imageio

images = []

for i in range(588):
    images.append(imageio.imread('figures/fig' + str(i) + '.png'))

imageio.mimsave('CA.gif', images)