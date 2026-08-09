# SIP Calculator with Step-up option

def calculate_sip(monthly_investment, annual_return, years, step_up_percent=0):
    monthly_rate = annual_return / 12 / 100
    total_invested = 0
    future_value = 0
    current_sip = monthly_investment

    for year in range(years):
        months_remaining = (years - year) * 12
        # Future value of this year's 12 SIP installments
        for month in range(12):
            total_invested += current_sip
            future_value = future_value * (1 + monthly_rate) + current_sip
        current_sip += current_sip * (step_up_percent / 100)

    return total_invested, future_value


monthly_investment = float(input("Enter monthly SIP amount (₹): "))
annual_return = float(input("Enter expected annual return (%): "))
years = int(input("Enter investment duration (years): "))
step_up = float(input("Enter yearly step-up (%) [0 if none]: "))

total_invested, future_value = calculate_sip(monthly_investment, annual_return, years, step_up)
gains = future_value - total_invested

print(f"\nTotal Invested: ₹{total_invested:,.2f}")
print(f"Estimated Future Value: ₹{future_value:,.2f}")
print(f"Wealth Gained: ₹{gains:,.2f}")
