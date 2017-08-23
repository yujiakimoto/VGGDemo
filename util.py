import pygame
import pygame.camera
import numpy as np
import matplotlib.pyplot as plt

def show_image(array, plot=None):
    if plot is None:
        plot = plt.imshow(array, vmin=0, vmax=255)
    else:
        plot.set_data(array)
    plt.pause(0.001)
    plt.draw()
    # print(dataset.shape)
    """for img in dataset:
        print(img)
        if plot is None:
            plot = plt.imshow(img, vmin=0, vmax=255)
        else:
            plot.set_data(img)
        plt.pause(0.0001)
        plt.draw()"""
    # plt.close()

class webcam:

    def __init__(self, output=None):

        self.output = output
        self.size = (640, 480)
        self.events = None
        self.ready = False
        display = pygame.display.set_mode(self.size, 0)
        pygame.camera.init()
        cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], self.size)
        cam.start()
        snapshot = pygame.surface.Surface(self.size, 0, display)

        try:
            while True:
                self.events = pygame.event.get()
                snapshot = cam.get_image(snapshot)
                display.blit(snapshot, (0, 0))
                pygame.display.flip()
                for event in self.events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            img = cam.get_image()
                            raw = img.get_buffer().raw
                            arr = np.flip(np.frombuffer(raw, dtype=np.ubyte).reshape(self.size[1], self.size[0], 3), 2)
                            print('Picture taken!')
                            self.output = arr
                            self.ready = True
        except KeyboardInterrupt:
            pass
        cam.stop()

    def is_ready(self):
        return self.ready

def main():
    cam = webcam()

if __name__ == '__main__':
    main()