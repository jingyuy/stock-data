#!/bin/bash
cd /Users/jingyu/ws/stock-data/stockapp
/Users/jingyu/opt/anaconda3/bin/python -m technical_app.fetch_and_save_stock_price_data
/Users/jingyu/opt/anaconda3/bin/python -m technical_app.create_daily_alerts
/Users/jingyu/opt/anaconda3/bin/python -m technical_app.send_alerts
