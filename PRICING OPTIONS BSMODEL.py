from QuantLib import *
import matplotlib.pyplot as plot
import numpy as np

#valutazione premio MCD option put
today = Date(18, June, 2021)
Settings.instance().evaluationDate = today
option = EuropeanOption(PlainVanillaPayoff(Option.Put, 233.88), EuropeanExercise(Date(18, September, 2021)))

u = SimpleQuote(231.33)
r = SimpleQuote(0.015)
sigma = SimpleQuote(0.074)

riskFreeCurve = FlatForward(0, TARGET(), QuoteHandle(r), Actual360())
volatility = BlackConstantVol(0, TARGET(), QuoteHandle(sigma), Actual360())

process = BlackScholesProcess(QuoteHandle(u), YieldTermStructureHandle(riskFreeCurve),
                              BlackVolTermStructureHandle(volatility))

engine = AnalyticEuropeanEngine(process)

option.setPricingEngine(engine)

print(option.NPV())
#print(option.delta())
#print(option.gamma())
#print(option.vega())

#u.setValue(230.00)
#print(option.NPV())

f, ax = plot.subplots()
xs = np.linspace(0.80, 500, 400)
ys = []

Settings.instance().evaluationDate = Date(18, July, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(30, July, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(14, August, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(28, August, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(17, September, 2021)
print(option.NPV())

for x in xs:
    u.setValue(x)
    ys.append(option.NPV())

ax.set_title("Option Value")
_ = ax.plot(xs, ys)
plot.show()

#valutazione premio MCD option call
from QuantLib import *
import matplotlib.pyplot as plot
import numpy as np

today = Date(18, June, 2021)
Settings.instance().evaluationDate = today
option = EuropeanOption(PlainVanillaPayoff(Option.Call, 233.88), EuropeanExercise(Date(18, September, 2021)))

u = SimpleQuote(235.18)
r = SimpleQuote(0.015)
sigma = SimpleQuote(0.074)

riskFreeCurve = FlatForward(0, TARGET(), QuoteHandle(r), Actual360())
volatility = BlackConstantVol(0, TARGET(), QuoteHandle(sigma), Actual360())

process = BlackScholesProcess(QuoteHandle(u), YieldTermStructureHandle(riskFreeCurve),
                              BlackVolTermStructureHandle(volatility))

engine = AnalyticEuropeanEngine(process)

option.setPricingEngine(engine)

print(option.NPV())
#print(option.delta())
#print(option.gamma())
#print(option.vega())

#u.setValue(241.00)
#print(option.NPV())

f, ax = plot.subplots()
xs = np.linspace(0.80, 500, 400)
ys = []

Settings.instance().evaluationDate = Date(18, July, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(30, July, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(14, August, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(28, August, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(17, September, 2021)
print(option.NPV())

for x in xs:
    u.setValue(x)
    ys.append(option.NPV())

ax.set_title("Option Value")
_ = ax.plot(xs, ys)
plot.show()

#valutazione premio DPZ opzione put
today = Date(18, June, 2021)
Settings.instance().evaluationDate = today
option = EuropeanOption(PlainVanillaPayoff(Option.Put, 457.20), EuropeanExercise(Date(18, September, 2021)))

u = SimpleQuote(446.62)
r = SimpleQuote(0.015)
sigma = SimpleQuote(0.0215)

riskFreeCurve = FlatForward(0, TARGET(), QuoteHandle(r), Actual360())
volatility = BlackConstantVol(0, TARGET(), QuoteHandle(sigma), Actual360())

process = BlackScholesProcess(QuoteHandle(u), YieldTermStructureHandle(riskFreeCurve),
                              BlackVolTermStructureHandle(volatility))

engine = AnalyticEuropeanEngine(process)

option.setPricingEngine(engine)

print(option.NPV())
#print(option.delta())
#print(option.gamma())
#print(option.vega())

#u.setValue(230.00)
#print(option.NPV())

f, ax = plot.subplots()
xs = np.linspace(0.80, 700, 400)
ys = []

Settings.instance().evaluationDate = Date(18, July, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(30, July, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(14, August, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(28, August, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(17, September, 2021)
print(option.NPV())

for x in xs:
    u.setValue(x)
    ys.append(option.NPV())

ax.set_title("Option Value")
_ = ax.plot(xs, ys)
plot.show()

#valutazione DPZ opzione Call
from QuantLib import *
import matplotlib.pyplot as plot
import numpy as np

today = Date(18, June, 2021)
Settings.instance().evaluationDate = today
option = EuropeanOption(PlainVanillaPayoff(Option.Call, 457.20), EuropeanExercise(Date(18, September, 2021)))

u = SimpleQuote(454.2)
r = SimpleQuote(0.015)
sigma = SimpleQuote(0.0215)

riskFreeCurve = FlatForward(0, TARGET(), QuoteHandle(r), Actual360())
volatility = BlackConstantVol(0, TARGET(), QuoteHandle(sigma), Actual360())

process = BlackScholesProcess(QuoteHandle(u), YieldTermStructureHandle(riskFreeCurve),
                              BlackVolTermStructureHandle(volatility))

engine = AnalyticEuropeanEngine(process)

option.setPricingEngine(engine)

print(option.NPV())
#print(option.delta())
#print(option.gamma())
#print(option.vega())

#u.setValue(241.00)
#print(option.NPV())

f, ax = plot.subplots()
xs = np.linspace(0.80, 700, 400)
ys = []

Settings.instance().evaluationDate = Date(18, July, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(30, July, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(14, August, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(28, August, 2021)
print(option.NPV())
Settings.instance().evaluationDate = Date(17, September, 2021)
print(option.NPV())

for x in xs:
    u.setValue(x)
    ys.append(option.NPV())

ax.set_title("Option Value")
_ = ax.plot(xs, ys)
plot.show()