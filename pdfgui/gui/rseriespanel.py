#!/usr/bin/env python
########################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
########################################################################

# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4 on Fri May 12 11:44:04 2006

import wx
from diffpy.pdfgui.control.pdfguimacros import makeRSeries
from pdfpanel import PDFPanel
from wxExtensions.validators import TextValidator, FLOAT_ONLY

class RSeriesPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: RSeriesPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.sizer_4_copy_staticbox = wx.StaticBox(self, -1, "fit minimum")
        self.sizer_4_staticbox = wx.StaticBox(self, -1, "fit maximum")
        self.instructionsLabel = wx.StaticText(self, -1, "Select a fit from the tree on the left and set the first value, last value, \nand the step size of the maximum and/or minimum of the fit range\nbelow. If you have not set up a fit to be the template for the series, hit\ncancel and rerun this macro once a fit has been created.")
        self.maxFirstLabel = wx.StaticText(self, -1, "first")
        self.maxFirstTextCtrl = wx.TextCtrl(self, -1, "")
        self.maxLastLabel = wx.StaticText(self, -1, "last")
        self.maxLastTextCtrl = wx.TextCtrl(self, -1, "")
        self.maxStepLabel = wx.StaticText(self, -1, "step")
        self.maxStepTextCtrl = wx.TextCtrl(self, -1, "")
        self.minFirstLabel = wx.StaticText(self, -1, "first")
        self.minFirstTextCtrl = wx.TextCtrl(self, -1, "")
        self.minLastLabel = wx.StaticText(self, -1, "last")
        self.minLastTextCtrl = wx.TextCtrl(self, -1, "")
        self.minStepLabel = wx.StaticText(self, -1, "step")
        self.minStepTextCtrl = wx.TextCtrl(self, -1, "")
        self.goButton = wx.Button(self, wx.ID_OK, "OK")
        self.cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onOK, id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: RSeriesPanel.__set_properties
        self.instructionsLabel.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: RSeriesPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy = wx.StaticBoxSizer(self.sizer_4_copy_staticbox, wx.HORIZONTAL)
        sizer_4 = wx.StaticBoxSizer(self.sizer_4_staticbox, wx.HORIZONTAL)
        sizer_1.Add(self.instructionsLabel, 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        sizer_4.Add(self.maxFirstLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_4.Add(self.maxFirstTextCtrl, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_4.Add(self.maxLastLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_4.Add(self.maxLastTextCtrl, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_4.Add(self.maxStepLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_4.Add(self.maxStepTextCtrl, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add(sizer_4, 0, wx.ALL|wx.EXPAND, 5)
        sizer_4_copy.Add(self.minFirstLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_4_copy.Add(self.minFirstTextCtrl, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_4_copy.Add(self.minLastLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_4_copy.Add(self.minLastTextCtrl, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_4_copy.Add(self.minStepLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_4_copy.Add(self.minStepTextCtrl, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add(sizer_4_copy, 0, wx.ALL|wx.EXPAND, 5)
        sizer_3.Add((20, 20), 1, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_3.Add(self.goButton, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add(self.cancelButton, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add(sizer_3, 0, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        # end wxGlade

    ##################################################
    def __customProperties(self):
        """Set the custom properties of this panel."""
        self.fit = None
        self.ctrlMap = {'maxfirst'  :   'maxFirstTextCtrl',
                        'maxlast'   :   'maxLastTextCtrl',
                        'maxstep'   :   'maxStepTextCtrl',
                        'minfirst'  :   'minFirstTextCtrl',
                        'minlast'   :   'minLastTextCtrl',
                        'minstep'   :   'minStepTextCtrl',
                        }

        for var in self.ctrlMap:
            setattr(self, var, None)

        for ctrlname in self.ctrlMap.values():
            textCtrl = getattr(self, ctrlname)
            textCtrl.SetValidator(TextValidator(FLOAT_ONLY))
        return

    def onOK(self, event): # wxGlade: RSeriesPanel.<event_handler>
        """Add make a temperature series and add it to the project."""
        for (varname, ctrlname) in self.ctrlMap.items():
            textCtrl = getattr(self, ctrlname)
            value = textCtrl.GetValue()
            if value == '':
                value = None
            else:
                value = float(value)
            setattr(self, varname, value)

        org = makeRSeries(self.mainFrame.control, self.fit, 
                self.maxfirst, self.maxlast, self.maxstep, 
                self.minfirst, self.minlast, self.minstep)
        self.treeCtrlMain.ExtendProjectTree(org, clear=False)
        self.mainFrame.needsSave()
        self.onCancel(event)
        return

    def onCancel(self, event): # wxGlade: RSeriesPanel.<event_handler>
        """Return to the main panel."""
        self.mainFrame.setMode("fitting")
        self.treeCtrlMain.UnselectAll()
        self.mainFrame.switchRightPanel("blank")
        return 

    def treeSelectionUpdate(self, node):
        """Set the current fit when the tree selection changes."""
        nodetype = self.treeCtrlMain.GetNodeType(node)
        if nodetype == 'fit':
            self.fit = self.treeCtrlMain.GetControlData(node)
        self.refresh()
        return

    def refresh(self):
        """Block out OK button if there is no fit.

        This also blocks OK if the fit has no datasets or phases.
        """
        # We can't rely on Veto to block unwanted tree selections on windows.
        # So, we have to check for errors here.
        node = None
        nodetype = None
        selections = self.treeCtrlMain.GetSelections()
        if selections: 
            node = selections[0]
            nodetype = self.treeCtrlMain.GetNodeType(node)

        if node and nodetype == "fit" \
                and self.fit and self.fit.hasDataSets() \
                and self.fit.hasStructures():
            self.goButton.Enable()
        else:
            self.goButton.Enable(False)
        return

# end of class RSeriesPanel
__id__ = "$Id$"
