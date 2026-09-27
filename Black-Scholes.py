import numpy as np #loads NumPy for advanced maths
from scipy.stats import norm #enters the stats section of SciPy and takes the normal distribution tool

def calculate_black_scholes( #defines the tool
    S: float, K: float, T: float, r: float, sigma: float #type hinting to show they are all decimals
) -> float: #answer back will be a decimal
    """
    Calculates the price of a European Call Option using Black-Scholes (European meaning you can only exercise your right to buy on the day of expiration).
    
    Parameters:
    S (float): Stock Price Now
    K (float): Strike Price (contract target price)
    T (float): Time until contract maturity (years)
    r (float): Risk-free Interest Rate (decimal) (found as the adjustment of past value with a risk-free investment 
               (e.g. government bonds))
    sigma (float): Volatility (decimal) (measures speed and magnitude of price swings 
                   (higher volatility = higher option price due to likelihood of a large swing, possibly past strike price))
    """
    # 1. Avoiding division by zero errors
    if T <= 0 or sigma <= 0:  #Neither time or volatility can be less than zero
        raise ValueError("Time until contract maturity and Volatility must both be greater than zero.")
        """ 
        raise ValueError instantly and stop the program if one or both of the conditions are met and produces an error message
        """
        
    try:
        # 2. The Formula
        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T)) #Finds the d1 variable in the Black-Scholes formula using mathematical operations and parameters from earlier
        d2 = d1 - sigma * np.sqrt(T) #finds d2, which is the other part of the final formula
        
        call_price = (S * norm.cdf(d1)) - (K * np.exp(-r * T) * norm.cdf(d2)) # This is the actual final formula; cdf finds the total probability that the stock will finish in the profitable zone, 
        #and the second part applies the  Risk-Free Interest Rate to account for the interest the money could've been making instead 
        return float(call_price) #this returns the call price as a decimal, as long as the try block worked
        
    except Exception as e: # If the try block doesn't work, print this error message describing what broke {e} and return 0 value
        print(f"An unexpected mathematical error occurred: {e}")
        return 0.0
# Example Use
if __name__ == "__main__": #only runs this code if specific section is run
    # Price a call option for a stock at $100, strike at $105, 1 year to expiry
    price = calculate_black_scholes(S=42.0, K=40.0, T=0.5, r=0.1, sigma=0.20) #Calls equation from earlier with example numbers from Options, Futures, and Other Derivatives by John C. Hull
    print(f"Theoretical Call Price: ${price:.2f}") #pastes it already in currency and to 2 decimal places
