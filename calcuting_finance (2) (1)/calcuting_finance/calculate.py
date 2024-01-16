import math

def clean_input(input_str):
    # Remove spaces, commas, and unnecessary special characters
    cleaned_input = ''.join(char for char in input_str if char.isdigit() or char == '.')

    # Check for valid decimal point placement
    if cleaned_input.count('.') > 1 or cleaned_input.startswith('.') or cleaned_input.endswith('.'):
        return None
    return cleaned_input

def calculate_investment_s(principal, rate, time):
    future_value_s = principal*(1+(rate/100)*time)
    return future_value_s

def calculate_investment_c(principal, rate, time):
    future_value_c = principal* math.pow((1+(rate/100)),time)
    return future_value_c

def calculate_bond(principal, rate, time):
    rate = rate/1200
    time = time*12
    bond_value = (rate * principal)/(1 - (1+rate)**-time)
    return bond_value

def main():
    while True:
        print("=======================================")
        print("  Thee Deciders Financial Calculator   ")
        print("-----------------Menu------------------")
        print("=======================================")

        while True:
            investment_type = input("\nEnter 'I' for investment or 'B' for bond: \n")
            if investment_type.upper() == 'I':
                while True:
                    principal_input = input("\nHow much do you want to invest: \nR ")
                    cleaned_principal_input = principal_input.replace(" ","").strip()
                    if cleaned_principal_input.replace(".","",1).isdigit() and float(cleaned_principal_input) > 0:
                        principal = float(cleaned_principal_input)
                        break
                    else:
                        print("\nInvalid input. Enter a valid amount (Numeric)")
                        
                while True:
                    rate_input = input("\nEnter the annual interest rate (%): \n")
                    cleaned_rate = rate_input.replace(" ","").strip()
                    if cleaned_rate.replace(".","",1).isdigit() and float(cleaned_rate) > 0:
                        rate = float(cleaned_rate)
                        if rate <= 100:
                            break
                        else:
                            print("\nRate must be equal or less than 100")
                    else:
                        print("\nInvalid rate. Enter a valid rate.")
                while True:
                    time_input = input("\nEnter the time period (in years): \n")
                    cleaned_time = time_input.replace(" ","").strip()
                    if cleaned_time.replace(".","",1).isdigit() and float(cleaned_time) > 0:
                        time = float(cleaned_time)
                        break
                    else:
                        print("\nInvalid input. Enter valid time")
            
                while True:
                    invest = input("\nIs it simple 'S' or Compound 'C' interest?: \n")
                    if invest.upper() == 'S':
                        future_value_s = calculate_investment_s(principal, rate, time)
                        print(f"\nThe future value of your investment will be: R{future_value_s:.2f}")
                        break
                        
                    elif invest.upper() == 'C':
                        future_value_c = calculate_investment_c(principal, rate, time)
                        print(f"\nThe future value of your investment will be: R{future_value_c:.2f}")
                        break
                    
                    else:
                        print("\nInvalid input.")

            elif investment_type.upper() == 'B':
                while True:
                    principal_input = input("\nEnter the amount of your bond: \nR ")
                    cleaned_principal_input = principal_input.replace(" ","").strip()
                    if cleaned_principal_input.replace(".","",1).isdigit() and float(cleaned_principal_input) > 0:
                        principal = float(cleaned_principal_input)
                        break
                    else:
                        print("\nInvalid input. Enter a valid amount (Numeric)")
                        
                while True:
                    rate_input = input("\nEnter the annual interest rate (%):\n")
                    cleaned_rate = rate_input.replace(" ","").strip()
                    if cleaned_rate.replace(".","",1).isdigit() and float(cleaned_rate) > 0:
                        rate = float(cleaned_rate)
                        if rate <= 100:
                            break
                        else:
                            print("\nRate must be equal or less than 100")
                    else:
                        print("\nInvalid rate. Enter a valid rate.")
                while True:
                    time_input = input("\nEnter the time period (in years): \n")
                    cleaned_time = time_input.replace(" ","").strip()
                    if cleaned_time.replace(".","",1).isdigit() and float(cleaned_time) > 0:
                        time = float(cleaned_time)
                        break
                    else:
                        print("\nInvalid input. Enter valid time")

                bond_value = calculate_bond(principal, rate, time)
                print(f"\nThe value of the bond will be: R{bond_value:.2f}")
            
            else:
                print("\nInvalid input. Please enter 'I' for investment or 'B' for bond.")
                continue
            
            another_calculation = input("\nDo you want to perform another calculation? (yes/no): \n")
            while another_calculation.lower() not in ['yes', 'no', 'y', 'n']:
                print("\nInvalid input. Please enter 'yes' or 'no'.")
                another_calculation = input("\nDo you want to perform another calculation? (yes/no): \n")
                
            if another_calculation.lower() in ['no','n']:
                print("\nThank You for using our services. Goodbye!!")
                break

        if another_calculation.lower() in ['no','n']:
            break
if __name__ == "__main__":
    main()
