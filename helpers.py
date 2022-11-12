from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

CR = CurrencyRates()
CC = CurrencyCodes()

def convert_currency(original_cur, converted_cur, amount):
    """Call Forex, To convert currency"""
    conv_rate = CR.get_rate(original_cur, converted_cur)

    return round((conv_rate * int(amount)), 2) # Round amount times curr rate

def get_symbol(cur_code):
    return  CC.get_symbol(cur_code)

def validate_inputs(original_cur, converted_cur):
    """Validate inputs from Form"""
    invalid_inputs = []
    original_symb = get_symbol(original_cur)
    conv_symb = get_symbol(converted_cur)

    if ( original_symb == None):
        invalid_inputs.append('Convert FROM Code is invalid')
    if (conv_symb == None): 
        invalid_inputs.append('Convert TO Code is invalid')
        
    return invalid_inputs