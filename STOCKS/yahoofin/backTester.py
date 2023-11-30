from Classes.SMABacktester import SMABacktester as SMA

symbol = ("GENIUS21.MX", "BIMBOA.MX", "HERDEZ.MX", "BOLSAA.MX", "IVVPESOISHRS.MX", "WALMEX.MX")
smas = (20, 200)
tester = SMA(symbol, smas)

tmp_df = tester.getSymbol('IVVPESOISHRS.MX')
tester.setSymbol('IVVPESOISHRS.MX')
print(tester.tmp_df.tail())
print(tester.run_strategy(smas))
tester.plot_positions(smas, "IVVPESOISHRS.MX")
tester.plot_results(smas, "IVVPESOISHRS.MX")

optimal = tester.optimize_parameters((slice(10, 50, 1), slice(100, 252, 1)))
print(optimal)
tester.setParameters(optimal)
tester.run_strategy(())
tester.plot_positions(optimal, "IVVPESOISHRS.MX")