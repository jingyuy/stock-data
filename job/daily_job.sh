#!/bin/bash
cd /Users/jingyu.yan/ws/stock-data/stockapp
/Users/jingyu.yan/.pyenv/shims/pipenv run python3 -m technical_app.fetch_and_save_stock_price_data
/Users/jingyu.yan/.pyenv/shims/pipenv run python3 -m technical_app.create_daily_alerts 
/Users/jingyu.yan/.pyenv/shims/pipenv run python3 -m technical_app.send_alerts
