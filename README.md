# Ochre [![Build Status](https://travis-ci.org/pgdr/ochre.svg?branch=master)](https://travis-ci.org/pgdr/ochre)

OCR ABC 123

## Optical Character Recognition Tutorial

This package is the course material for the OCR workshop.

In two days, we go from scratch, to a fully working OCR application for single
page documents.


## Functionality

Using `freetype-py` we generate an image:

![freetype-py generated image](https://raw.githubusercontent.com/pgdr/ochre/master/assets/input-img.png)

Using a neural network to train on the letters in the text, we predict back the
original sentence:

![neural network output](https://raw.githubusercontent.com/pgdr/ochre/master/assets/console-output.png)
