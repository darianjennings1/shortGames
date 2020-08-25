import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim


def bubble(arr):
    if len(arr) == 1:
        return
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                A[i],A[j]=A[j],A[i]
            yield arr

            
 def update_plot(array, rec, epochs):
    for rec, val in zip(rec, array):
        rec.set_height(val)
    epochs[0]+= 1
    text.set_text("No.of operations :{}".format(epochs[0]))

    
def main():
    while input("Would you like to visualize again Y/N?  ").strip().upper() == "Y":
        n = int(input("Enter the number of elements:"))
        array = [i + 1 for i in range(n)]
        random.shuffle(array)

        title = "Bubble Sort Visualizer"
        alg = bubble(array)

        # Initialize fig
        fig, ax = plt.subplots()
        ax.set_title(title)

        bar_rec = ax.bar(range(len(array)), array, align='edge')

        ax.set_xlim(0, n)
        ax.set_ylim(0, int(n * 1.1))

        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

        epochs = [0]
        anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=alg, interval=1, repeat=False)
        plt.show()

    
if __name__ == "__main__":
    main()

