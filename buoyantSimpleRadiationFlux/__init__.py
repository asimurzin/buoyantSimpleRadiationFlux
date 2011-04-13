#!/usr/bin/env python

#--------------------------------------------------------------------------------------
## VulaSHAKA (Simultaneous Neutronic, Fuel Performance, Heat And Kinetics Analysis)
## Copyright (C) 2009-2010 Pebble Bed Modular Reactor (Pty) Limited (PBMR)
## 
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
## 
## See https://vulashaka.svn.sourceforge.net/svnroot/vulashaka
##
## Author : Alexey PETROV
##


#--------------------------------------------------------------------------------------------
argv = None
import sys, os

# Check is the pythonFlu installed
try:
   import Foam
   pass
except ImportError:
   print 
   print "You must install pythonFlu first( http://sourceforge.net/projects/pythonflu/files/)" 
   print
   os._exit( os.EX_UNAVAILABLE )
   pass


#--------------------------------------------------------------------------------------
from Foam import FOAM_VERSION, FOAM_BRANCH_VERSION,FOAM_REF_VERSION
if FOAM_VERSION( "<=", "010401" ):
    from Foam.OpenFOAM import ext_Info
    ext_Info() << "\n\n To use this solver, it is necessary to SWIG OpenFOAM-1.5 or higher\n"    
    pass


#----------------------------------------------------------------------------------------------
if FOAM_REF_VERSION( "==", "010500" ):
    from buoyantSimpleRadiationFlux.r1_5 import *
    pass


#----------------------------------------------------------------------------------------------
if FOAM_BRANCH_VERSION( "dev", "==", "010500" ):
    from buoyantSimpleRadiationFlux.r1_5 import *
    pass

#---------------------------------------------------------------------------------------------
if FOAM_REF_VERSION( "==", "010600" ):
    from buoyantSimpleRadiationFlux.r1_6 import *
    pass


#--------------------------------------------------------------------------------------
if FOAM_BRANCH_VERSION( "dev",">=", "010600" ):
    from buoyantSimpleRadiationFlux.r1_6_dev import *
    pass


#--------------------------------------------------------------------------------------
if FOAM_REF_VERSION( ">=", "010700" ):
    from buoyantSimpleRadiationFlux.r1_7_0 import *
    pass


#--------------------------------------------------------------------------------------
def entry_point():
    import sys; argv = sys.argv
    return main_standalone( len( argv ), argv )


#--------------------------------------------------------------------------------------
if __name__ == "__main__" :
    entry_point()
    pass
    
    
#--------------------------------------------------------------------------------------
