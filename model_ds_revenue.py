import pandas as pd
import streamlit as st

# Function to calculate P&L details
def calculate_pnl(fixed_costs, storage_rate, storage_capacity, fill_rate, order_revenue_per_order, throughput, variable_cost_per_order):
    storage_revenue = fill_rate * storage_capacity * storage_rate
    order_revenue = throughput * order_revenue_per_order
    variable_costs = throughput * variable_cost_per_order
    total_revenue = storage_revenue + order_revenue
    total_costs = fixed_costs + variable_costs
    profit = total_revenue - total_costs
    
    pnl_data = {
        "Category": ["Storage Revenue", "Order Revenue", "Total Revenue", "Fixed Costs", "Variable Costs", "Total Costs", "Profit"],
        "Rate": [
            storage_rate, 
            order_revenue_per_order, 
            "", 
            "", 
            variable_cost_per_order, 
            "", 
            ""
        ],
        "Quantity": [
            fill_rate * storage_capacity, 
            throughput, 
            "", 
            "", 
            throughput, 
            "", 
            ""
        ],
        "Amount (₹)": [
            storage_revenue, 
            order_revenue, 
            total_revenue, 
            fixed_costs, 
            variable_costs, 
            total_costs, 
            profit
        ]
    }

    return pd.DataFrame(pnl_data), profit

# Function to find the optimal P&L
def find_optimal_pnl(fixed_costs, storage_rate_range, storage_capacity_range, fill_rate, order_revenue_per_order, throughput_range, variable_cost_per_order):
    best_profit = float('-inf')
    best_params = None
    for storage_rate in storage_rate_range:
        for storage_capacity in storage_capacity_range:
            for throughput in throughput_range:
                pnl_df, profit = calculate_pnl(fixed_costs, storage_rate, storage_capacity, fill_rate, order_revenue_per_order, throughput, variable_cost_per_order)
                if profit > best_profit:
                    best_profit = profit
                    best_params = (storage_rate, storage_capacity, throughput)
                    
    return best_params, best_profit

# Streamlit interface
st.title('Interactive P&L Model')

fixed_costs = st.slider('Fixed Costs (₹)', 100000, 1000000, 465000, 5000)
storage_rate = st.slider('Storage Rate (₹/cubic ft)', 10, 50, 25, 1)
storage_capacity = st.slider('Storage Capacity (cubic ft)', 5000, 30000, 15000, 500)
fill_rate = st.slider('Fill Rate', 0.1, 1.0, 0.7, 0.05)
order_revenue_per_order = st.slider('Order Revenue (₹)', 10, 50, 25, 1)
throughput = st.slider('Throughput (orders)', 1000, 50000, 12000, 1000)
variable_cost_per_order = st.slider('Variable Cost (₹/order)', 2, 20, 8, 1)  # Changed step to 1 to match integer types

# Display the P&L Model
pnl_df, profit = calculate_pnl(fixed_costs, storage_rate, storage_capacity, fill_rate, order_revenue_per_order, throughput, variable_cost_per_order)
st.write(pnl_df)
st.write(f'Profit: ₹{profit}')

# Optimize P&L
if st.button('Find Optimal P&L'):
    storage_rate_range = range(10, 51, 5)
    storage_capacity_range = range(5000, 30001, 5000)
    throughput_range = range(1000, 50001, 5000)

    best_params, best_profit = find_optimal_pnl(fixed_costs, storage_rate_range, storage_capacity_range, fill_rate, order_revenue_per_order, throughput_range, variable_cost_per_order)
    
    best_storage_rate, best_storage_capacity, best_throughput = best_params
    optimal_pnl_df, _ = calculate_pnl(fixed_costs, best_storage_rate, best_storage_capacity, fill_rate, order_revenue_per_order, best_throughput, variable_cost_per_order)
    
    st.write('Optimal P&L')
    st.write(optimal_pnl_df)
    st.write(f'Optimal Profit: ₹{best_profit}')
    st.write(f'Best Storage Rate: ₹{best_storage_rate}/cubic ft')
    st.write(f'Best Storage Capacity: {best_storage_capacity} cubic ft')
    st.write(f'Best Throughput: {best_throughput} orders')
