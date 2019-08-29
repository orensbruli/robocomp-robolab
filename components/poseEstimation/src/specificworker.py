#
# Copyright (C) 2019 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

import sys, os, traceback, time

from PySide import QtGui, QtCore
from genericworker import *

import torch
import simpleinference
import numpy as np

# If RoboComp was compiled with Python bindings you can use InnerModel in Python
# sys.path.append('/opt/robocomp/lib')
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel

class SpecificWorker(GenericWorker):
	def __init__(self, proxy_map):
		super(SpecificWorker, self).__init__(proxy_map)
		self.timer.timeout.connect(self.compute)
		self.Period = 2000
		self.timer.start(self.Period)

		if torch.cuda.is_available():
			self.device = 'cuda:0'
			print('using GPU')
		else: 
			self.device = 'cpu'
			print('using CPU')

		self.estimator = simpleinference.PoseEstimator(device=self.device)


	def setParams(self, params):
		return True

	@QtCore.Slot()
	def compute(self):
		return True


	#
	# getSkeleton
	#
	def getSkeleton(self, img, shape):
		# reconstruct a 3d array from the input. (input comes as a string)		
		arr = np.fromstring(img, np.uint8)
		img_restored = np.reshape(arr, (shape[0], shape[1], shape[2]))
		skeleton2d, skeleton3d = self.estimator.estimate(img_restored)
		return skeleton2d, skeleton3d

