def calculateRetirement(start_age, initial, working, retired):
    def computeBalance(balance, rate_of_return, contribution):
        interest_earned = balance * rate_of_return
        balance += interest_earned + contribution
        return balance

    working_months, working_contribution, working_rate_of_return = working
    retired_months, retired_spending, retired_rate_of_return = retired

    age_years = start_age // 12
    age_months = start_age % 12

    print(f"Age {age_years:3d} month {age_months:2d} you have ${initial:.2f}")

    total_months = start_age + working_months + retired_months

    # Working
    for _ in range(working_months):
        initial = computeBalance(initial, working_rate_of_return, working_contribution)
        age_months += 1
        if age_months == 12:
            age_years += 1
            age_months = 0
        if age_years * 12 + age_months >= total_months:
            break  # Stop calculations at desired age
        print(f"Age {age_years:3d} month {age_months:2d} you have ${initial:.2f}")

    # Retired
    for _ in range(retired_months):
        initial = computeBalance(initial, retired_rate_of_return, retired_spending)
        age_months += 1
        if age_months == 12:
            age_years += 1
            age_months = 0
        if age_years * 12 + age_months >= total_months:
            break  # Stop calculations at desired age
        print(f"Age {age_years:3d} month {age_months:2d} you have ${initial:.2f}")
def main():
    working = (489, 1000, 0.045 / 12)
    retired = (384, -4000, 0.01 / 12)
    calculateRetirement(327, 21345, working, retired)

if __name__ == "__main__":
    main()
    
