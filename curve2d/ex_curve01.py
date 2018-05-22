#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2018
"""
import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import exchange

from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a B-Spline curve instance
curve = BSpline.Curve()

# Set up curve
curve.ctrlpts = exchange.read_txt("ex_curve01.cpt")
curve.degree = 4

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.01

# Evaluate curve
curve.evaluate()

# Plot the control point polygon and the evaluated curve
vis_comp = VisMPL.VisCurve2D()
curve.vis = vis_comp
curve.render()

# Insert a knot
u = 0.2
curve.insert_knot(u)

# Plot the control point polygon and the evaluated curve after knot insertion
curve.render()

# Good to have something here to put a breakpoint
pass
