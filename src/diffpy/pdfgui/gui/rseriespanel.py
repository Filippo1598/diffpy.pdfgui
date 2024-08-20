#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
##############################################################################
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
##############################################################################

# generated by wxGlade 0.9.3 on Fri Jul 19 16:05:55 2019

import wx

from diffpy.pdfgui.control.pdfguimacros import makeRSeries
from diffpy.pdfgui.gui.pdfpanel import PDFPanel
from diffpy.pdfgui.gui.wxextensions.validators import FLOAT_ONLY, TextValidator


class RSeriesPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: RSeriesPanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.instructionsLabel = wx.StaticText(
            self,
            wx.ID_ANY,
            "Select a fit from the tree on the left and set the first value, last value, \nand the step size of the maximum and/or minimum of the fit range\nbelow. If you have not set up a fit to be the template for the series, hit\ncancel and rerun this macro once a fit has been created.",  # noqa: E501
        )
        self.maxFirstLabel = wx.StaticText(self, wx.ID_ANY, "first")
        self.maxFirstTextCtrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.maxLastLabel = wx.StaticText(self, wx.ID_ANY, "last")
        self.maxLastTextCtrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.maxStepLabel = wx.StaticText(self, wx.ID_ANY, "step")
        self.maxStepTextCtrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.minFirstLabel = wx.StaticText(self, wx.ID_ANY, "first")
        self.minFirstTextCtrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.minLastLabel = wx.StaticText(self, wx.ID_ANY, "last")
        self.minLastTextCtrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.minStepLabel = wx.StaticText(self, wx.ID_ANY, "step")
        self.minStepTextCtrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.goButton = wx.Button(self, wx.ID_OK, "OK")
        self.cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onOK, self.goButton)
        self.Bind(wx.EVT_BUTTON, self.onCancel, self.cancelButton)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: RSeriesPanel.__set_properties
        self.instructionsLabel.SetFont(
            wx.Font(
                10,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "Sans",
            )
        )
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: RSeriesPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "fit minimum"), wx.HORIZONTAL)
        sizer_4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "fit maximum"), wx.HORIZONTAL)
        sizer_1.Add(self.instructionsLabel, 0, wx.ALL | wx.EXPAND, 5)
        sizer_4.Add(self.maxFirstLabel, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_4.Add(self.maxFirstTextCtrl, 0, wx.ALL, 5)
        sizer_4.Add(self.maxLastLabel, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_4.Add(self.maxLastTextCtrl, 0, wx.ALL, 5)
        sizer_4.Add(self.maxStepLabel, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_4.Add(self.maxStepTextCtrl, 0, wx.ALL, 5)
        sizer_1.Add(sizer_4, 0, wx.ALL | wx.EXPAND, 5)
        sizer_4_copy.Add(self.minFirstLabel, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_4_copy.Add(self.minFirstTextCtrl, 0, wx.ALL, 5)
        sizer_4_copy.Add(self.minLastLabel, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_4_copy.Add(self.minLastTextCtrl, 0, wx.ALL, 5)
        sizer_4_copy.Add(self.minStepLabel, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_4_copy.Add(self.minStepTextCtrl, 0, wx.ALL, 5)
        sizer_1.Add(sizer_4_copy, 0, wx.ALL | wx.EXPAND, 5)
        sizer_3.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_3.Add(self.goButton, 0, wx.ALL, 5)
        sizer_3.Add(self.cancelButton, 0, wx.ALL, 5)
        sizer_1.Add(sizer_3, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    # ################################################
    def __customProperties(self):
        """Set the custom properties of this panel."""
        self.fit = None
        self.ctrlMap = {
            "maxfirst": "maxFirstTextCtrl",
            "maxlast": "maxLastTextCtrl",
            "maxstep": "maxStepTextCtrl",
            "minfirst": "minFirstTextCtrl",
            "minlast": "minLastTextCtrl",
            "minstep": "minStepTextCtrl",
        }

        for var in self.ctrlMap:
            setattr(self, var, None)

        for ctrlname in self.ctrlMap.values():
            textCtrl = getattr(self, ctrlname)
            textCtrl.SetValidator(TextValidator(FLOAT_ONLY))
        return

    def onOK(self, event):  # wxGlade: RSeriesPanel.<event_handler>
        """Add make a temperature series and add it to the project."""
        for varname, ctrlname in self.ctrlMap.items():
            textCtrl = getattr(self, ctrlname)
            value = textCtrl.GetValue()
            if value == "":
                value = None
            else:
                value = float(value)
            setattr(self, varname, value)

        org = makeRSeries(
            self.mainFrame.control,
            self.fit,
            self.maxfirst,
            self.maxlast,
            self.maxstep,
            self.minfirst,
            self.minlast,
            self.minstep,
        )
        self.treeCtrlMain.ExtendProjectTree(org, clear=False)
        self.mainFrame.needsSave()
        self.onCancel(event)
        return

    def onCancel(self, event):  # wxGlade: RSeriesPanel.<event_handler>
        """Return to the main panel."""
        self.mainFrame.setMode("fitting")
        self.treeCtrlMain.UnselectAll()
        self.mainFrame.switchRightPanel("blank")
        return

    def treeSelectionUpdate(self, node):
        """Set the current fit when the tree selection changes."""
        nodetype = self.treeCtrlMain.GetNodeType(node)
        if nodetype == "fit":
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

        if node and nodetype == "fit" and self.fit and self.fit.hasDataSets() and self.fit.hasStructures():
            self.goButton.Enable()
        else:
            self.goButton.Enable(False)
        return


# end of class RSeriesPanel
