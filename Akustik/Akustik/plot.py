import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from numpy import *
from sys import argv
import Akustik_class



def ex1():
    '''Basic default example'''
    X = np.linspace(-pi, pi, 256, endpoint=True)
    C, S = cos(X), sin(X)
    plt.plot(X, C)
    plt.plot(X, S)

    plt.show()

def ex_subplot():

    def plot():
        X = np.linspace(-pi, pi, 256, endpoint=True)
        C, S = cos(X), sin(X)
        plt.plot(X, C)
        plt.plot(X, S)

    plt.figure(figsize=(6,12), dpi=80)
    #subplot(abc), a: rows, b: columns, c: plot slot number
    plt.subplot(411)
    plot()
    plt.subplot(412)
    plot()
    plt.subplot(413)
    plot()
    plt.subplot(414)
    plot()
    plt.show()

def ex2():
    # Create a new figure of size 8x6 points, using 100 dots per inch
    plt.figure(figsize=(10,6), dpi=80)

    # Create a new subplot from a grid of 1x1
    plt.subplot(111)

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    # Set x limits
    plt.xlim(-4.0,4.0)
    # Set x ticks, not the latex syntax to format the ticks.
    #plt.xticks(np.linspace(-4,4,9,endpoint=True))
    plt.xticks([-pi, -pi/2, 0, pi/2, pi],
    [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$+\pi$'])
    # Set y limits
    plt.ylim(-1.0,1.0)
    # Set y ticks
    plt.yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])
    #Render the tick labels larger and with background
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='black', edgecolor='none', alpha=0.25 ))

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C,S = np.cos(X), np.sin(X)

    t = 2 * pi / 3
    plt.plot([t,t],[0, cos(t)], color='blue', linewidth=1.5, linestyle='--')
    plt.scatter([t,], [cos(t),], 50, color='blue')

    plt.plot([t,t],[0, sin(t)], color ='red', linewidth=1.5, linestyle="--")
    plt.scatter([t,],[sin(t),], 50, color ='red')

    plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->",
             connectionstyle="arc3,rad=.2"))

    plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
            xy=(t, sin(t)), xycoords='data',
            xytext=(+10, +30), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3, rad=.2"))
    # Plot cosine using blue color with a continuous line of width 1 (pixels)
    plt.plot(X, C, color="blue", linewidth=2.0, linestyle="-",
            label='cosine')

    # Plot sine using green color with a continuous line of width 1 (pixels)
    plt.plot(X, S, color="red", linewidth=2.0, linestyle="-",
                label='sine')

    # Save figure using 72 dots per inch
    # savefig("../figures/exercice_2.png",dpi=72)
    plt.legend(loc='upper left', frameon=False)
    # Show result on screen
    plt.show()

def ex3():
    fig = plt.figure()
    ax = Axes3D(fig)
    #arange: return array of evenly spaced values
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    #meshgrid: return a set of matched arrays(vectors)
    X, Y, = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    #3D plot
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='spring')
    #2D plot
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
    ax.set_zlim(-2, 2)

    plt.show()

def plot3D(X, Y, Z):
        fig = plt.figure()
        ax = Axes3D(fig)
        X, Y, = np.meshgrid(X, Y)

        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='spring')
        #ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
        ax.set_zlim(min(Z), max(Z))

        plt.show()

def plot_freq_response_vented_box(Loudspeaker,
                                    Enclousure, Freq_range):
    '''Plot the frequency response of a speaker system with a
        vented box, Freq_range: a touple'''
    dBmagData = [x for x in range(len(Freq_range))]
    x = 0
    Vb = Loudspeaker.transducer.Vb
    Vas = Loudspeaker.transducer.Vas
    Fs = Loudspeaker.transducer.Fs
    Qts = Loudspeaker.transducer.Qts
    Fb = Loudspeaker.transducer.Fb
    Ql = Loud
    for f in Freq_range:
        dBmadData[x] = freq_response_vented_box(Vb, Vas, Fs, Qts, Fb, Ql, F)
    plt.plot(dBmagData, Freq_range)
    plt.show()
