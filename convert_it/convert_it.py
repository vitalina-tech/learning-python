def convert(value,from_unit,to_unit):
    conversions={'m':1,'km':1000,'cm':0.01,'mm':0.001}
    if from_unit not in conversions or to_unit not in conversions:
        return None
    result=value*conversions[from_unit]/conversions[to_unit]
    return result
def main():
    print('Unit Converter (Length)')
    print('Available units: m, km, cm, mm')
    try:
        value=float(input('Enter value '))
        from_unit=input('From unit: ').strip().lower()
        to_unit=input('To unit: ').strip().lower()
        result=convert(value,from_unit,to_unit)
        if result is not None:
            print(f'{value} {from_unit} = {result:.4f} {to_unit}')
        else:
            print('Unsupported unit entered.')
    except ValueError:
        print("Please enter a valid number")
if __name__=='__main__':
    main()