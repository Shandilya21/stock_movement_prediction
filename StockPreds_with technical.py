# Train ML/DL model to predict stock prices for the next day 
'''
Designed an Stacked GRU and LSTM based model to predict Future price of the stocks
In this implementation I used following TI
Technical Analysis:
Use of Technical Indicators:
1. SMA (OHLC)
2. RSI (Relative Strength Index)
3. Stochastic Oscillator
'''
import os
import math
import numpy as np
import argparse
import pandas as pd
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from config import DATA_PATH

sns.set()
parser = argparse.ArgumentParser()
parser.add_argument('--stock_name',type=str, default="AAPL")
parser.add_argument('--load_all',action='store_true', help='For complete dataset (without TA)')
parser.add_argument('--use_ta',action='store_true', help='with technical indicators')
parser.add_argument('--indicator',type=str, default='RSI', help='technical indicators, (RSI, Stochastic)')
parser.add_argument('--epoch',type=int, default=5, help='number of iterations')
parser.add_argument('--not_train',action='store_true', help='load save model')
arg = parser.parse_args()

test_set_size_percentage = 10

def create_dataset(dataset, step_size):
	data_X, data_Y = [], []
	for i in range(len(dataset)-step_size-1):
		a = dataset[i:(i+step_size), 0]
		data_X.append(a)
		data_Y.append(dataset[i + step_size, 0])
	return np.array(data_X), np.array(data_Y)

'''
DATA_PATH: Path to the Dataset (change in config.py accordingly)
stock_name: Stock Name present in Stock List dataframe (AAPL, DIS, MKT, YHOO, etc) 
'''
df = pd.read_csv(DATA_PATH + '/prices-split-adjusted.csv')
if arg.stock_name not in list(df['symbol']):
	raise ValueError(arg.stock_name +" "+ "is not listed in Stock List")

print('Number of Unique Stocks: ', len(list(set(df.symbol)))) # Total Stocks Name in List (501)
print(list(set(df.symbol))[:10]) # 10 Stock Names

stock_price = df[df['symbol']== arg.stock_name]
sns.relplot(x='date', y='close',kind='line', legend='full' ,data=stock_price[:100]) # plot for 100 samples
sns.relplot(x='date', y='volume',kind='line', legend='full' ,data=stock_price[:100])
df_stocks = stock_price.reindex(index = stock_price.index[::-1])
obs = np.arange(1, len(df_stocks) + 1, 1)
plt.show()

# drop columns from dataframe
df_stocks.drop(['symbol'], 1, inplace=True)
df_stocks.drop(['date'], 1, inplace=True)

# Technical Indicators for Analysis
OHLC_avg = df_stocks[['open', 'high', 'low', 'close']].mean(axis=1) # SMA
HLC_avg = df_stocks[['high', 'low', 'close']].mean(axis=1)
close_val  = df_stocks[['close']]

if arg.use_ta:
	if arg.indicator == 'RSI':
		diff = close_val.diff(1)
		up = diff.where(diff > 0, 0.0)
		dn = -diff.where(diff < 0, 0.0)
		min_periods = 14	
		emaup = up.ewm(alpha=1/14, min_periods=min_periods, adjust=False).mean()
		emadn = dn.ewm(alpha=1/14, min_periods=min_periods, adjust=False).mean()
		rs = emaup / emadn # (https://www.investopedia.com/terms/r/rsi.asp)
		codn = np.where(emadn == 0, 100, 100-(100/(1+rs)))
		codn = codn.flatten()
		rsi = pd.Series(codn, index=close_val.index)
		rsi = rsi.fillna(40, axis=0)
		rsi = pd.Series(rsi, name='RSI')

	if arg.indicator == 'Stoch':
		min_periods = 14
		smin = df_stocks['low'].rolling(14, min_periods=min_periods).min()
		smax = df_stocks['high'].rolling(14, min_periods=min_periods).max()
		stoch_k = 100 * (df_stocks['close'] - smin) / (smax - smin) # (https://www.investopedia.com/terms/s/stochasticoscillator.asp)
		stoch_k = stoch_k.fillna(40, axis=0)
		stoch = pd.Series(stoch_k, name='Stochastic')
		stoch_obs = np.arange(1, len(stoch) + 1, 1)

	if arg.indicator is None:
		raise ValueError("No technical indicator is given, please use correct indicators to proceed")

# Train and Test Split (With and Without Using Technical Indicators)
if arg.load_all:
	ohlc_avg = np.reshape(OHLC_avg.values, (len(OHLC_avg),1))
	scaler = MinMaxScaler(feature_range=(0,1))
	ohlc_avg_norm = scaler.fit_transform(ohlc_avg)
	
	train_ohlc = int(len(ohlc_avg_norm) * 0.9)
	test_ohlc = len(ohlc_avg_norm) - train_ohlc
	train_ohlc, test_ohlc = ohlc_avg_norm[0:train_ohlc,:], ohlc_avg_norm[train_ohlc:len(OHLC_avg),:]
	x_train, y_train = create_dataset(train_ohlc, 1)
	x_test, y_test = create_dataset(test_ohlc, 1)

elif arg.indicator == 'RSI':
	RSI_avg = np.reshape(rsi.values, (len(rsi),1))
	scaler = MinMaxScaler(feature_range=(0, 1))
	rsi_avg_norm = scaler.fit_transform(RSI_avg)

	train_rsi = int(len(rsi_avg_norm) * 0.9)
	test_rsi = len(rsi_avg_norm) - train_rsi
	train_rsi, test_rsi = rsi_avg_norm[0:train_rsi,:], rsi_avg_norm[train_rsi:len(rsi),:]
	x_train, y_train = create_dataset(train_rsi, 1)
	x_test, y_test = create_dataset(test_rsi, 1)
else:
	stoch_avg = np.reshape(stoch.values, (len(stoch),1))
	scaler = MinMaxScaler(feature_range=(0,1))
	stoch_avg_norm = scaler.fit_transform(stoch_avg)

	train_stoch = int(len(stoch_avg_norm) * 0.9)
	test_stoch = len(stoch_avg_norm) - train_stoch
	train_stoch, test_stoch = stoch_avg_norm[0:train_stoch,:], stoch_avg_norm[train_stoch:len(stoch),:]
	x_train, y_train = create_dataset(train_stoch, 1)
	x_test, y_test = create_dataset(test_stoch, 1)

# RESHAPING TRAIN AND TEST DATA
x_train = np.reshape(x_train, (x_train.shape[0], 1, x_train.shape[1]))
x_test = np.reshape(x_test, (x_test.shape[0], 1, x_test.shape[1]))
step_size = 1

# Model
input_shape = (x_train.shape[1], x_train.shape[2])
input_layer = tf.keras.Input(shape=input_shape)
x = tf.keras.layers.GRU(256, input_shape=(1, step_size), return_sequences=True)(input_layer)
x = tf.keras.layers.Dropout(0.4)(x)
x = tf.keras.layers.LSTM(256)(x)
x = tf.keras.layers.Dropout(0.4)(x)
x = tf.keras.layers.Dense(64, activation='relu')(x)
x = tf.keras.layers.Dense(1)(x)

model = tf.keras.Model(inputs=input_layer, outputs=x)
model.summary()

# Load saved model or training a new model
if os.path.exists('{}_stock_prices__{}_{}.h5'.format(arg.stock_name, arg.indicator, arg.epoch)):
	history = load_model('{}_stock_prices__{}_{}.h5'.format(arg.stock_name, arg.indicator, arg.epoch))
else:
	model.compile(loss='mse', optimizer='adam', metrics=["mse"])
	history = model.fit(x_train, y_train, epochs=arg.epoch, batch_size=2, verbose=1, validation_data = (x_test,y_test))
	if arg.indicator:
		model.save('{}_stock_prices__{}_{}.h5'.format(arg.stock_name, arg.indicator, arg.epoch)) # save model
	else:
		model.save('{}_stock_prices__{}.h5'.format(arg.stock_name, arg.epoch))

	plt.plot(history.history['mean_squared_error'])
	plt.plot(history.history['val_mean_squared_error'])
	plt.title('model mean squared error')
	plt.ylabel('accuracy')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()

	# summarize history for loss
	plt.plot(history.history['loss'])
	plt.plot(history.history['val_loss'])
	plt.title('model loss')
	plt.ylabel('loss')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()

trainPredict = model.predict(x_train)
testPredict = model.predict(x_test)

if arg.not_train:
	def model_score(model, x_train, y_train, x_test, y_test):
		trainScore = model.evaluate(x_train, y_train, verbose=0)
		print('Train Score: %.5f MSE (%.2f RMSE)' % (trainScore[0], math.sqrt(trainScore[0])))
		testScore = model.evaluate(x_test, y_test, verbose=0)
		print('Test Score: %.5f MSE (%.2f RMSE)' % (testScore[0], math.sqrt(testScore[0])))
		return trainScore[0], testScore[0]
	model_score(model, x_train, y_train, x_test, y_test)

# DE-NORMALIZING FOR PLOTTING
trainPredict = scaler.inverse_transform(trainPredict)
y_train = scaler.inverse_transform([y_train])
testPredict = scaler.inverse_transform(testPredict)
y_test = scaler.inverse_transform([y_test])

# PREDICT FUTURE VALUES
last_val = testPredict[-1]
last_val_scaled = last_val/last_val
next_val = model.predict(np.reshape(last_val_scaled, (1,1,1)))
print("Last Day Value:", np.asscalar(last_val))
print("Next Day Value:", np.asscalar(last_val*next_val))