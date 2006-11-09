########################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow, Dmitriy Bryndin
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
########################################################################

# version
__id__ = "$Id$"

def _abstract():
    """Raise a specific exception that referrs to the failing method."""
    import inspect
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    raise NotImplementedError(caller + ' must be implemented in subclass')


class PDFPanel(object):
    """Mix-in class for all PDF gui panels.
    
    This method is meant to be a secondary parent class for classed derived from
    wx.Panel. It defines methods and member variables necessary to all panels in
    the PDFGui.
    """
    def __init__(self, *args, **kwds):
        self.mainPanel = None
        self.treeCtrlMain = None
        # The configuration parser for reading and writing to the 
        # configuration file
        self.cP = None      
        # Wrap all events so that the exceptions get handled.
        self.__wrapEvents()
        return

    def __wrapEvents(self):
        """This method wraps all of the event to handle exceptions."""
        import traceback
        from errorreportdialog import ErrorReportDialog
        import pdfguiglobals

        # get access to controlerrors.py
        import sys,os
        
        from pdfgui.control.controlerrors import ControlError

        def _funcBuilder(funcName):
            func = getattr(self, funcName)
            def _f(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except ControlError, e:
                    message = str(e)
                    if not self.mainPanel.quitting:
                        self.mainPanel.showMessage(message, 'Oops!')
                    else:
                        raise
                except:
                    # do not catch when disabled in dbopts
                    if pdfguiglobals.dbopts.noerrordialog:
                        raise
                    msglines = traceback.format_exception(*sys.exc_info())
                    message = "".join(msglines)
                    dlg = ErrorReportDialog(self)
                    dlg.text_ctrl_log.SetValue(message)
                    if not self.mainPanel.quitting:
                        dlg.ShowModal()
                        dlg.Destroy()
                    else:
                        raise
        
                    return

            return _f

        funcNames = [item for item in dir(self) if item[:1] != '_']
        # filter out non-functions
        for name in funcNames:
            if hasattr( getattr(self, name), '__call__'):
                setattr(self, name, _funcBuilder(name))

        return
    
    def refresh(self):
        """Refreshes wigets of the panel.
        
        This method must be overloaded in the derived class or else a
        NotImplementedError will be raised when this method is called.
        """ 
        _abstract()
