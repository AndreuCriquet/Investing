# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:46:50 2021

@author: Andreu Criquet
"""

def intrinsic_value_calc(cash_flow, first_growth, second_growth, discout_rate, terminal_multiple):
    
    for year in range(5):
        if year == 0:
            next_cash_flow = cash_flow
            next_year = 0
            start_year = 0
            intrinsic_value = 0
        last_market_cap = next_cash_flow #I save last market cap for terminal multiple calculation
        next_cash_flow = next_cash_flow+next_cash_flow*(first_growth/100)
        next_intrinsic_value = next_cash_flow * (1+(discout_rate/100))**(start_year-next_year-1)
        next_year += 1  
        intrinsic_value = intrinsic_value + next_intrinsic_value   
        
    for year in range(5,10):
        last_market_cap = next_cash_flow #I save last market cap for terminal multiple calculation
        next_cash_flow = next_cash_flow+next_cash_flow*(second_growth/100)
        next_intrinsic_value = next_cash_flow * (1+(discout_rate/100))**(start_year-next_year-1)
        next_year += 1  
        intrinsic_value = intrinsic_value + next_intrinsic_value 

    last_intrinsic_value = last_market_cap*terminal_multiple
    last_intrinsic_value = last_intrinsic_value * (1+(discout_rate/100))**(0-next_year)
    intrinsic_value = intrinsic_value+last_intrinsic_value
    return(intrinsic_value)


def price_per_share(intrinsic_value, number_shares):
    return(intrinsic_value*1000/number_shares)


def input_decimal(input_text):
    while True:
        try:
            output_float = float(input(input_text))
            return output_float
        except ValueError:
            print("No valid decimal number, please, try again")
    
        
if __name__ == "__main__":

    print("\nThis program calculates company intrisic value and recommended share price" +
          "\nThis model is based on Discounted Cash Flow formula"+
          "\nRemember to always insert and read with the same currency")
    
    repeat = 'yes'
    while repeat != 'quit':
        
        cash_flow = input_decimal("Enter current free cash flow in billions: ")
        first_growth = input_decimal("Enter expected next 5 years yearly average growth in %: ")
        second_growth = input_decimal("Enter expected later 5 years (5 to 10) yearly average growth in %: ")
        investment_return = input_decimal("Enter expected investment return in %: ")
        price_x_cash_flow = input_decimal("Enter expected terminal multiple (e.g. Cash flow per share ratio): ")
        shares_amount = input_decimal("Enter the amount of shares in millions: ")
        intrinsic_value = intrinsic_value_calc(cash_flow,first_growth,second_growth,investment_return,price_x_cash_flow)
        share_price = price_per_share(intrinsic_value, shares_amount)
        print("\n-----------------------------------------------------")
        print("Company's intrinsic value is {} billions".format(intrinsic_value))
        print("Company's recommended share price is {}".format(share_price))
        print("-----------------------------------------------------")       
        repeat = input("Type quit to quit or anything else in order to value another stock: ")
        