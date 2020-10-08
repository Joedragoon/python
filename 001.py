{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled",
      "provenance": [],
      "authorship_tag": "ABX9TyPlWKCjJiVZ6C/R7XjvwzT8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/Joedragoon/python/blob/main/001.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vf57S9eE4gCc",
        "outputId": "ec5bfc6d-ad3d-4404-9e77-f6e4e4cf6ca4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 121
        }
      },
      "source": [
        "# 001\n",
        "\"\"\" primer python  con 3 comillas puedes\n",
        "poner textos en varias lineas\n",
        "\"\"\"\n",
        "'''\n",
        "tambien valen comillas simples\n",
        "es lo mismo\n",
        "'''\n",
        "\n",
        "texto1 = str (\"Hola mundo\") #dato tipo texto\n",
        "print (type (texto1))  # type recibe como argumento una variable y te dice que tipo es\n",
        "num1 = int (2)  #tipo de dato entero\n",
        "num2 = float (2.1)  #tipo de dato decimal\n",
        "print (type(num2))   # type recibe como argumento una variable y te dice que tipo es\n",
        "condicion= bool() #tipo de dato booleano\n",
        "print (texto1)\n",
        "print (num1+num2)\n",
        "\n",
        "# conversión de tipo de datos \n",
        "edad = \"25\"  # según esta no podremos sumar un numero de años\n",
        "print (type(edad))\n",
        "print (int (edad)+10, \"el  tipo de dato sigue siendo \", type(edad))\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'str'>\n",
            "<class 'float'>\n",
            "Hola mundo\n",
            "4.1\n",
            "<class 'str'>\n",
            "35 cambio tipo de datos  <class 'str'>\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}