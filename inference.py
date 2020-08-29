#! /usr/bin/env python
import os
import torch
from frontend import *


if __name__ == '__main__':
	camfeed_inference("weights/weights.pth", 'cpu')
