#!/usr/bin/env python3
# -*- coding: utf-8 -*
Spyder Editor

This is a temporary script file.

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)

plt.plot(x,x,label='linear')
plt.legend()
plt.show()