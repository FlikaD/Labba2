from spyre import server

import pandas as pd
import numpy as np
import urllib2
import os.path
import json
import csv
import time
import pprint
import matplotlib.pyplot as plt

class StockExample(server.App):
    def get_state_name(id): 
        if (id == 1): 
            state = 'Vinnitsa'
            return state 
        elif (id == 2): 
            state = 'Volyn' 
            return state 
        elif (id == 3): 
            state = 'Dnipropetrovsk'
            return state 
        elif (id == 4): 
            state = 'Donetsk'
            return state 
        elif (id == 5): 
            state = 'Zhytomyr'
            return state 
        elif (id == 6):
            state = 'Zakarpattia'
            return state
        elif ( id == 7): 
            state = 'Zaporozhye' 
            return state 
        elif (id == 8): 
            state = 'Ivano-Frankivsk'
            return state 
        elif (id == 9): 
            state = 'Kyiv' 
            return state 
        elif (id == 10): 
            state = 'Kirovograd' 
            return state
        elif (id == 11): 
            state = 'Lugansk' 
            return state 
        elif (id == 12): 
            state = 'Lviv' 
            return state 
        elif (id == 13): 
            state = 'Nikolaev'
            return state 
        elif (id == 14): 
            state = 'Odessa' 
            return state 
        elif (id == 15): 
            state = 'Poltava' 
            return state
        elif (id == 16): 
            state = 'Rivnnska'
            return state 
        elif (id == 17): 
            state = 'Sumi' 
            return state 
        elif (id == 18): 
            state = 'Ternopil' 
            return state
        elif (id == 19): 
            state = 'Kharkov' 
            return state 
        elif (id == 20): 
            state = 'Kherson' 
            return state 
        elif (id == 21): 
            state = 'Khmelnytsky' 
            return state 
        elif (id == 22): 
            state = 'Cherkas'
            return state 
        elif (id == 23): 
            state = 'Chernivtsi' 
            return state 
        elif (id == 24): 
            state = 'Chernihiv'
            return state 
        elif (id == 25): 
            state = 'Republic of Crimea'
            return state
    
    title = "VHI, TCI, VCI index in Ukraine"
    
    inputs = [{
            "type":'dropdown',
            "label": 'Index',
            "options": [{"label": 'VHI', "value":'VHI'},
                        {"label": 'TCI', "value":'TCI'},
                        {"label": 'VCI', "value":'VCI'}],
            "key": 'index',
            "action_id": "update_data"
              },


              {     "type":'dropdown',
                    "label": 'State', 
                    "options" : [ {"label": get_state_name(1), "value":1},
                                  {"label": get_state_name(2), "value":2},
                                  {"label": get_state_name(3), "value":3},
                                  {"label": get_state_name(4), "value":4},
                                  {"label": get_state_name(5), "value":5},
                                  {"label": get_state_name(6), "value":6},
                                  {"label": get_state_name(7), "value":7},
                                  {"label": get_state_name(8), "value":8},
                                  {"label": get_state_name(9), "value":9},
                                  {"label": get_state_name(10), "value":10},
                                  {"label": get_state_name(11), "value":11},
                                  {"label": get_state_name(12), "value":12},
                                  {"label": get_state_name(13), "value":13},
                                  {"label": get_state_name(14), "value":14},
                                  {"label": get_state_name(15), "value":15},
                                  {"label": get_state_name(16), "value":16},
                                  {"label": get_state_name(17), "value":17},
                                  {"label": get_state_name(18), "value":18},
                                  {"label": get_state_name(19), "value":19},
                                  {"label": get_state_name(20), "value":20},
                                  {"label": get_state_name(21), "value":21},
                                  {"label": get_state_name(22), "value":22},
                                  {"label": get_state_name(23), "value":23},
                                  {"label": get_state_name(24), "value":24},
                                  {"label": get_state_name(25), "value":25}],
                    "key": 'ticker', 
                    "action_id": "update_data"},
              {
                    "type":'slider',
                    "label": 'Year1', 
                    "max":2016, "min":1981,
                    "key": 'year1',
                    "value":1982,
                    "action_id": "update_data"},
              
                      {
                    "type":'slider',
                    "label": 'Year2', 
                    "max":2016, "min":1981,
                    "key": 'year2',
                    "value":1985,
                    "action_id": "update_data"},
              {
                "type":'dropdown',
                "label": 'Background color',
                "options": [{"label": 'Yellow', "value":'lightyellow'},
                            {"label": 'Blue', "value":'honeydew'},
                            {"label": 'Grey', "value":'lightgrey'}
                            ],
                "key": 'bg',
                "action_id": "update_data"
              },
              {
                    "type":'slider',
                    "label": 'Line Width', 
                    "min" : 0.5,
                    "max" : 2.5,
                    "step" : 0.01,
                    "value" : 0.5,
                    "key": 'lw',
                    "action_id": "update_data"}
              ]

    controls = [{   "type" : "hidden",
                    "label" : "Update",
                    "id" : "update_data"}]

    tabs = ["Plot", "Table"]

    outputs = [{ "type" : "plot",
                    "id" : "getPlot",
                    "control_id" : "update_data",
                    "tab" : "Plot"},
                { "type" : "table",
                    "id" : "table_id",
                    "control_id" : "update_data",
                    "tab" : "Table",
                    "on_page_load" : True }]
       

    def getData(self, params):
        ticker = params['ticker']
        year1 = int(params['year1'])
        year2 = int(params['year2'])
        self.state_name = str(ticker) + '.csv'
        print(self.state_name)
        df = pd.read_csv(r"C:/Users/nazarskiy/IPython/lab2/freshdata/%s" % self.state_name)  
        df_year=df[(df['Year']>=year1)&(df['Year']<=year2)]
        return df_year

    def getPlot(self, params):
        ticker = params['ticker']
        index = str(params['index'])
        year1 = int(params['year1'])
        year2 = int(params['year2'])
        lw = float(params['lw'])
        bg = params['bg']
        title = index+' '+str(year1)+'-'+str(year2)
        plt.figure(figsize=(10,5))
        while (year1<=year2):
            df = self.getData(params)   
            df_new=df[(df['Year']==year1)]
            df_new=df_new.loc[:,['Year','Week',index]]            
            plt.subplot(axisbg=bg)            
            plt.plot((df_new['Week']), df_new[index], label=str(year1), linewidth=lw)
            year1=year1+1

        plt.title(title,fontsize=15)
        plt.xlabel('Week')
        plt.ylabel(index)
        plt.xlim(1,52)
        plt.ylim(0,100)
        plt.legend()
        plt.grid(color='black')  
        return plt.gcf()       
        

app = StockExample()
app.launch(port=9093)
