{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO/sL4UrtYpkgijPV9AeKr2",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/harshininomula3/Machine-learning/blob/main/Dense%20layer-forwardpass.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "UKnDn0TUda2v"
      },
      "outputs": [],
      "source": [
        "import numoy as np\n",
        "import nnfs\n",
        "from nnfs.datasets import spiral_data\n",
        "nnfs.init()\n",
        "class Layer_Dense:\n",
        "    def __init__(self,n_inputs,n_neurons):\n",
        "        self.weights=0.10*np.random.randn(n_inputs,n_neurons)\n",
        "        self.biases=np.zeros((1,n_neurons))\n",
        "    #forward pass\n",
        "    def forward(self,inputs):\n",
        "        self.output=np.dot(inputs,self.weights)+self.biases\n",
        "    X,y=spiral_data(100,3)\n",
        "layer1=Layer_Dense(2,5)\n",
        "layer2=Layer_Dense(5,2)\n",
        "layer1.forward(X)\n",
        "print(layer1.output)\n"
      ]
    }
  ]
}