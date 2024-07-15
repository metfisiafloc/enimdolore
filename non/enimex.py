import numpy as np

def CO2_compensation_point_no_resp(Leaf_Temp, KMC, KMO):
    const1 = -3.3801
    const2 = 5220.0
    const3 = 210.0
    R = 8.314  # Universal gas constant in J/(mol·K)
    
    T_kelvin = Leaf_Temp + 273.0
    exponent = const1 + (const2 / T_kelvin)
    compensation_point = 0.5 * np.exp(exponent) * const3 * (KMC / KMO)
    
    return compensation_point

# Example usage
Leaf_Temp = 25.0  # in Celsius
KMC = 1.0  # example value
KMO = 1.0  # example value

result = CO2_compensation_point_no_resp(Leaf_Temp, KMC, KMO)
print(result)
