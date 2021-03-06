"""
/*******************************************************************************
 * @author  Joseph Kamel
 * @email   josephekamel@gmail.com
 * @date    28/11/2018
 * @version 2.0
 *
 * SCA (Secure Cooperative Autonomous systems)
 * Copyright (c) 2013, 2018 Institut de Recherche Technologique SystemX
 * All rights reserved.
 *******************************************************************************/
"""

import os
import json
import numpy as np
from numpy import array

class MlDataCollector:
	
	initCollection = False

	ValuesData = []
	TargetData = []

	valuesCollection = np.array([])
	targetCollection = np.array([])

	curDateStr = ''

	savePath = ''

	def setCurDateSrt(self, datastr):
		self.curDateStr = datastr

	def getValuesCollection(self):
		return self.valuesCollection

	def setSavePath(self, datastr):
		self.savePath = datastr

	def getTargetCollection(self):
		return self.targetCollection

	def saveData(self):
		self.initValuesData(self.ValuesData)
		self.initTargetData(self.TargetData)

		self.ValuesData = []
		self.TargetData = []

		np.save(self.savePath+'/valuesSave_'+self.curDateStr, self.valuesCollection)
		np.save(self.savePath+'/targetSave_'+self.curDateStr, self.targetCollection)

	def loadData(self):
		self.valuesCollection = np.load(self.savePath+'/valuesSave_'+self.curDateStr +'.npy' )
		self.targetCollection = np.load(self.savePath+'/targetSave_'+self.curDateStr +'.npy')
		#print(self.valuesCollection[0:2])
		#print(self.targetCollection[0:2])
		self.initCollection = True	

	def collectData(self,bsmArray):
		self.ValuesData.append([array(bsmArray[0])])
		self.TargetData.append([array(bsmArray[1])])

	def initValuesData(self,New_Rows):
		if self.valuesCollection.shape[0] == 0:
			self.valuesCollection = np.concatenate([row for row in New_Rows])
		else:
			addTargetCollection = np.concatenate([row for row in New_Rows])
			self.valuesCollection  = np.concatenate([self.valuesCollection, addTargetCollection])
		

	def initValuesData_old(self,New_Rows):
		if self.valuesCollection.shape[0] == 0:
			self.valuesCollection = np.vstack([row for row in New_Rows])
		else:
			self.valuesCollection = np.vstack([self.valuesCollection, [row for row in New_Rows]])

	def initTargetData_old(self,New_Rows):
		if self.targetCollection.shape[0] == 0:
			self.targetCollection = np.vstack([row for row in New_Rows])
		else:
			self.targetCollection = np.vstack([self.targetCollection, [row for row in New_Rows]])

	def initTargetData(self,New_Rows):
		if self.targetCollection.shape[0] == 0:
			self.targetCollection = np.concatenate([row for row in New_Rows])
		else:
			addTargetCollection = np.concatenate([row for row in New_Rows])
			self.targetCollection  = np.concatenate([self.targetCollection, addTargetCollection])
		
