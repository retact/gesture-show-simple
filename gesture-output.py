import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import multiprocessing as mp
import time
from PIL import Image


# Assign classes to common variables in order
def input_class(gesture_class):
    for i in range(52):
        gesture_class.value = i
        time.sleep(3)


# The process of displaying an image
def show_classimage(gesture_class):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Processing without displaying lines and axes
    ax.spines['right'].set_color('None')
    ax.spines['top'].set_color('None')
    ax.spines['left'].set_color('None')
    ax.spines['bottom'].set_color('None')
    ax.tick_params(axis='x', which='both', top=False, bottom=False, labelbottom=False)
    ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

    def update(i):
        if gesture_class.value >= 0 and gesture_class.value <= 52:
            tmp = Image.open('gestures/gesture '+str(gesture_class.value)+'.png')
            plt.imshow(tmp)
        else:
            print('Correct classification was not possible.')
    ani = FuncAnimation(fig, update, interval=100)
    plt.show()


if __name__ == "__main__":
    gesture_class = mp.Value('i', 0)
    process1 = mp.Process(target=input_class, args=(gesture_class,))
    process2 = mp.Process(target=show_classimage, args=(gesture_class,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
