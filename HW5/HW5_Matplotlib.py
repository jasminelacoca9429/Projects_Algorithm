import numpy as np
import matplotlib.pyplot as plt

y0 = 1972
n0 = 0.0025
year_predicted = np.arange(1972, 2013, 2)
num_predicted = np.log10(n0) + ((year_predicted - y0) / 2) * np.log10(2)

year_observed = [1972, 1974, 1978, 1982, 1985, 1989, 1993, 1997, 1999, 2000, 2003, 2004, 2007, 2008, 2012]
num_observed = [0.0025, 0.005, 0.029, 0.12, 0.275, 1.18, 3.1, 7.5, 24.0, 42.0, 220.0, 592.0, 1720.0, 2046.0, 3100.0]
plt.plot(year_predicted, num_predicted,'c--o', label='Prediction')
plt.plot(year_observed, np.log10(num_observed),'b-s', label='Observation')
plt.title('Moore\'s Law -- Observation VS Prediction', fontsize=20, fontname='Calibri', c='brown')
plt.xlabel('Year', fontsize=20, fontname='Calibri', )
plt.ylabel('Number of transistors (log)', fontsize=20, fontname='Calibri')
plt.grid()
plt.legend()
plt.show()

