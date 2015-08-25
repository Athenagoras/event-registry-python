﻿"""
trending information is computed by comparing how frequently are individual concepts/categories
mentioned in the articles. By default trends are computed by comparing the total number of mentions of a concept/category
in the last two days compared to the number of mentions in the two weeks before. The trend for each concept/category
is computed as the Pearson residual. The returned concepts/categories are the ones that have the highest residual.
"""
import os, sys, urllib2, urllib, json, re
from Base import *
from ReturnInfo import *


class TrendsBase(ParamsBase):
    def _getPath(self):
        return "/json/trends"

class GetTrendingConcepts(TrendsBase):
    """
    get currently top trending concepts
    """
    def __init__(self, 
                 source = "news",   # source information from which to compute top trends. Options: "news", "social"
                 count = 20,        # number of top trends to return
                 returnInfo = ReturnInfo()):     # specify the details of the concepts to return
        ParamsBase.__init__(self)
        self._setVal("action", "getTrendingConcepts")
        self._setVal("source", source)
        self._setVal("conceptCount", count)
        self.queryParams.update(returnInfo.getParams())


class GetTrendingCategories(TrendsBase):
    """
    get currently top trending categories
    """
    def __init__(self, 
                 source = "news",   # source information from which to compute top trends. Options: "news", "social"
                 count = 20,        # number of top trends to return
                 returnInfo = ReturnInfo()):     # specify the details of the categories to return
        ParamsBase.__init__(self)
        self._setVal("action", "getTrendingCategories")
        self._setVal("source", source)
        self._setVal("categoryCount", count)
        self.queryParams.update(returnInfo.getParams())


class GetTrendingCustomItems(TrendsBase):
    """
    get currently top trending items for which the users provided the data
    this data can be stock prices, energy prices, etc...
    """
    def __init__(self, 
                 count = 20,        # number of top trends to return
                 returnInfo = ReturnInfo()):     # specify the details of the concepts to return
        ParamsBase.__init__(self)
        self._setVal("action", "getTrendingCustom")
        self._setVal("conceptCount", count)
        self.queryParams.update(returnInfo.getParams())


class GetTrendingConceptGroups(TrendsBase):
    """
    get currently top trending groups of concepts
    a group can be identified by the concept type or by a concept class uri
    """
    def __init__(self, 
                 source = "news",   # source information from which to compute top trends. Options: "news", "social"
                 count = 20,        # number of top trends to return
                 returnInfo = ReturnInfo()):     # specify the details of the concepts to return
        ParamsBase.__init__(self)
        self._setVal("action", "getConceptTrendGroups")
        self._setVal("source", source)
        self._setVal("conceptCount", count)
        self.queryParams.update(returnInfo.getParams())

    def getConceptTypeGroups(types = ["person", "org", "loc", "wiki"]):
        """request trending of concepts of specified types"""
        self._setVal("conceptType", types)

    def getConceptClassUris(conceptClassUris):
        """request trending of concepts assigned to the specified concept classes"""
        self._setVal("conceptClassUri", conceptClassUris)

