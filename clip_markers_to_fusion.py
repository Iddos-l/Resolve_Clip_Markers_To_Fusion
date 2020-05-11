#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This script imports resolve clip markers
in to fusion page as text+ tool with keyframes.
Iddo Lahman, Bootke color studio, iddolahman@gmail.com
'''
import sys
from python_get_resolve import GetResolve

#=-=-=-=-=-=-=-=-= Utils =-=-=-=-=-=-=-=-=-=-=-=-=-=
def addmarker(tool, startTime, markers):
    """Parse markers dict and apply data to text tool"""
    tool.StyledText = comp.BezierSpline()
    for marker in markers:
        name = markers[marker]['name']
        note = markers[marker]['note']
        content = '** %s **\n%s' % (name, note)
        frameNumber = int(marker) - int(startTime)
        tool.StyledText[frameNumber] = content
#=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
resolve = GetResolve()
if resolve == None:
    sys.exit(-1)

# Get clip markers data
fu = resolve.Fusion()
proj = resolve.GetProjectManager().GetCurrentProject()
clip = proj.GetCurrentTimeline().GetCurrentVideoItem()
markersList = clip.GetMarkers()
if not markersList:
    print('No Markers found!')
    sys.exit(0)

# Open fusion page and add Text+ tool
resolve.OpenPage('Fusion')
comp = fu.GetCurrentComp()
# Get start of comp
if clip.GetName() == 'Adjustment Clip':
    start = 0   # In case of Adjustment Clip no offset
else:
    start = int(comp.GetAttrs()['COMPN_RenderStart'])

comp.TextPlus()
# Make sure to get the new Text+ tool
textList = comp.GetToolList(False, 'TextPlus')
textTool = textList[len(textList)]
textTool.TileColor = { 'R':0.0, 'G':0.0, 'B':0.9}

addmarker(textTool, start, markersList)
sys.exit(0)
