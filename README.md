# Black-Scholes-Pricing
Black-Scholes European option pricing engine built in python


# Code Features
Explicit Type Hinting e.g. float to ensure structural layout.
Protects against zero/negative time boundaries (`T <= 0`) and zero volatility to systematically eliminate division-by-zero runtime exceptions.
localized `try-except` protocol so system remains online

# Verification
The script's accuracy was validated using a reference problem from John C. Hull’s 'Options, Futures, and Other Derivatives':

Asset Price (S): $42.00

Strike Price (K): $40.00

Time to Maturity (T): 0.5 Years (6 Months)

Risk-Free Rate (r): 10.0% (0.10)

Volatility (sigma): 20.0% (0.20)

Output Result: $4.76 (Matches textbook value ).

# Limitations
While mathematically precise, this model operates under constraints that diverge from modern live trading desks:
1. Constant Volatility: Assumes market volatility remains flat through expiration, failing to account for the real-world volatility changes
2. Zero Dividends: Does not support underlying equity asset yield payouts prior to expiration.
3. Continuous Trading Style: Assumes frictionless buying/selling without transaction fees or overnight exchange liquidity gaps where price doesnt change smoothly.
