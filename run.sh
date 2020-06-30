#!/bin/sh
echo "Experiments using Technical Indicator - Stochastic"
python StockPreds_withtechnical.py --stock_name GOOG --use_ta --indicator Stoch --epoch 5
python StockPreds_withtechnical.py --stock_name AAPL --use_ta --indicator Stoch --epoch 10
python StockPreds_withtechnical.py --stock_name YHOO --use_ta --indicator Stoch --epoch 15
python StockPreds_withtechnical.py --stock_name GPS --use_ta --indicator Stoch --epoch 20
python StockPreds_withtechnical.py --stock_name SJM --use_ta --indicator Stoch --epoch 25
python StockPreds_withtechnical.py --stock_name UTX --use_ta --indicator Stoch --epoch 30

echo "Experiments using Technical Indicator - RSI (Relative Strength Index)"
python StockPreds_withtechnical.py --stock_name GOOG --use_ta --indicator RSI --epoch 5
python StockPreds_withtechnical.py --stock_name AAPL --use_ta --indicator RSI --epoch 10
python StockPreds_withtechnical.py --stock_name YHOO --use_ta --indicator RSI --epoch 15
python StockPreds_withtechnical.py --stock_name GPS --use_ta --indicator RSI --epoch 20
python StockPreds_withtechnical.py --stock_name SJM --use_ta --indicator RSI --epoch 25
python StockPreds_withtechnical.py --stock_name UTX --use_ta --indicator RSI --epoch 30

echo "General Experiments"
python StockPreds_withtechnical.py --stock_name AAPL --load_all --epoch 5
python StockPreds_withtechnical.py --stock_name AAPL --load_all --epoch 10
python StockPreds_withtechnical.py --stock_name AAPL --load_all --epoch 15
python StockPreds_withtechnical.py --stock_name AAPL --load_all --epoch 20
python StockPreds_withtechnical.py --stock_name AAPL --load_all --epoch 25
python StockPreds_withtechnical.py --stock_name AAPL --load_all --epoch 30

echo "Done with Experiments"