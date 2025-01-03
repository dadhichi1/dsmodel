#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import ipywidgets as widgets
from IPython.display import display

# Function to calculate P&L details
def calculate_pnl(fixed_costs, storage_revenue, order_revenue, variable_costs):
    total_revenue = storage_revenue + order_revenue
    total_costs = fixed_costs + variable_costs
    profit = total_revenue - total_costs

    pnl_data = {
        "Category": ["Storage Revenue", "Order Revenue", "Total Revenue", "Fixed Costs", "Variable Costs", "Total Costs", "Profit"],
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

    return pd.DataFrame(pnl_data)

# Interactive display function
def interactive_pnl_model(fixed_costs, storage_rate, storage_capacity, 
                          fill_rate, order_revenue_per_order, throughput, variable_cost_per_order):
    # Calculate revenues and costs
    storage_revenue = fill_rate * storage_capacity * storage_rate
    order_revenue = throughput * order_revenue_per_order
    variable_costs = throughput * variable_cost_per_order

    # Generate P&L
    pnl_df = calculate_pnl(fixed_costs, storage_revenue, order_revenue, variable_costs)
    display(pnl_df)

# Create sliders
fixed_costs_slider = widgets.FloatSlider(value=465000, min=100000, max=1000000, step=5000, description="Fixed Costs (₹):")
storage_rate_slider = widgets.FloatSlider(value=25, min=10, max=50, step=1, description="Storage Rate (₹/cubic ft):")
storage_capacity_slider = widgets.FloatSlider(value=15000, min=5000, max=30000, step=500, description="Storage Capacity (cubic ft):")
fill_rate_slider = widgets.FloatSlider(value=0.7, min=0.1, max=1.0, step=0.05, description="Fill Rate:")
order_revenue_slider = widgets.FloatSlider(value=25, min=10, max=50, step=1, description="Order Revenue (₹):")
throughput_slider = widgets.IntSlider(value=12000, min=1000, max=50000, step=1000, description="Throughput (orders):")
variable_cost_per_order_slider = widgets.FloatSlider(value=8, min=2, max=20, step=0.5, description="Variable Cost (₹/order):")

# Use `interactive_output` for dynamic updates
ui = widgets.VBox([
    fixed_costs_slider, storage_rate_slider, storage_capacity_slider, 
    fill_rate_slider, order_revenue_slider, throughput_slider, variable_cost_per_order_slider
])

output = widgets.interactive_output(
    interactive_pnl_model,
    {
        'fixed_costs': fixed_costs_slider,
        'storage_rate': storage_rate_slider,
        'storage_capacity': storage_capacity_slider,
        'fill_rate': fill_rate_slider,
        'order_revenue_per_order': order_revenue_slider,
        'throughput': throughput_slider,
        'variable_cost_per_order': variable_cost_per_order_slider
    }
)

# Display the widgets and the output
display(ui, output)


# In[14]:


import pandas as pd
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
from ipywidgets import FloatProgress

# Function to calculate P&L details
def calculate_pnl(fixed_costs, storage_revenue, order_revenue, variable_costs, storage_rate, storage_capacity, fill_rate, order_revenue_per_order, throughput, variable_cost_per_order):
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

    return pd.DataFrame(pnl_data)

# Interactive display function
def interactive_pnl_model(fixed_costs, storage_rate, storage_capacity, 
                          fill_rate, order_revenue_per_order, throughput, variable_cost_per_order):
    # Calculate revenues and costs
    storage_revenue = fill_rate * storage_capacity * storage_rate
    order_revenue = throughput * order_revenue_per_order
    variable_costs = throughput * variable_cost_per_order

    # Generate P&L
    pnl_df = calculate_pnl(fixed_costs, storage_revenue, order_revenue, variable_costs, storage_rate, storage_capacity, fill_rate, order_revenue_per_order, throughput, variable_cost_per_order)
    
    display(pnl_df)

    # Progress bar to show the impact on profit with changing throughput
    throughput_values = range(1000, 50001, 1000)
    profit_values = []
    for t in throughput_values:
        order_revenue = t * order_revenue_per_order
        variable_costs = t * variable_cost_per_order
        total_revenue = storage_revenue + order_revenue
        total_costs = fixed_costs + variable_costs
        profit_values.append(total_revenue - total_costs)
    
    fig, ax = plt.subplots()
    ax.plot(throughput_values, profit_values)
    ax.set_xlabel('Throughput (orders)')
    ax.set_ylabel('Profit (₹)')
    ax.set_title('Impact of Throughput on Profit')
    plt.show()

# Create sliders
fixed_costs_slider = widgets.FloatSlider(value=465000, min=100000, max=1000000, step=5000, description="Fixed Costs (₹):")
storage_rate_slider = widgets.FloatSlider(value=25, min=10, max=50, step=1, description="Storage Rate (₹/cubic ft):")
storage_capacity_slider = widgets.FloatSlider(value=15000, min=5000, max=30000, step=500, description="Storage Capacity (cubic ft):")
fill_rate_slider = widgets.FloatSlider(value=0.7, min=0.1, max=1.0, step=0.05, description="Fill Rate:")
order_revenue_slider = widgets.FloatSlider(value=25, min=10, max=50, step=1, description="Order Revenue (₹):")
throughput_slider = widgets.IntSlider(value=12000, min=1000, max=50000, step=1000, description="Throughput (orders):")
variable_cost_per_order_slider = widgets.FloatSlider(value=8, min=2, max=20, step=0.5, description="Variable Cost (₹/order):")

# Use `interactive_output` for dynamic updates
ui = widgets.VBox([
    fixed_costs_slider, storage_rate_slider, storage_capacity_slider, 
    fill_rate_slider, order_revenue_slider, throughput_slider, variable_cost_per_order_slider
])

output = widgets.interactive_output(
    interactive_pnl_model,
    {
        'fixed_costs': fixed_costs_slider,
        'storage_rate': storage_rate_slider,
        'storage_capacity': storage_capacity_slider,
        'fill_rate': fill_rate_slider,
        'order_revenue_per_order': order_revenue_slider,
        'throughput': throughput_slider,
        'variable_cost_per_order': variable_cost_per_order_slider
    }
)

# Display the widgets and the output
display(ui, output)


# In[15]:


import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output

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

# Interactive display function
def interactive_pnl_model(fixed_costs, storage_rate, storage_capacity, fill_rate, order_revenue_per_order, throughput, variable_cost_per_order):
    pnl_df, profit = calculate_pnl(fixed_costs, storage_rate, storage_capacity, fill_rate, order_revenue_per_order, throughput, variable_cost_per_order)
    clear_output(wait=True)
    display(pnl_df)
    display(widgets.Label(f'Profit: ₹{profit}'))

# Create sliders
fixed_costs_slider = widgets.FloatSlider(value=465000, min=100000, max=1000000, step=5000, description="Fixed Costs (₹):")
storage_rate_slider = widgets.FloatSlider(value=25, min=10, max=50, step=1, description="Storage Rate (₹/cubic ft):")
storage_capacity_slider = widgets.FloatSlider(value=15000, min=5000, max=30000, step=500, description="Storage Capacity (cubic ft):")
fill_rate_slider = widgets.FloatSlider(value=0.7, min=0.1, max=1.0, step=0.05, description="Fill Rate:")
order_revenue_slider = widgets.FloatSlider(value=25, min=10, max=50, step=1, description="Order Revenue (₹):")
throughput_slider = widgets.IntSlider(value=12000, min=1000, max=50000, step=1000, description="Throughput (orders):")
variable_cost_per_order_slider = widgets.FloatSlider(value=8, min=2, max=20, step=0.5, description="Variable Cost (₹/order):")

# Use `interactive_output` for dynamic updates
ui = widgets.VBox([
    fixed_costs_slider, storage_rate_slider, storage_capacity_slider, 
    fill_rate_slider, order_revenue_slider, throughput_slider, variable_cost_per_order_slider
])

output = widgets.interactive_output(
    interactive_pnl_model,
    {
        'fixed_costs': fixed_costs_slider,
        'storage_rate': storage_rate_slider,
        'storage_capacity': storage_capacity_slider,
        'fill_rate': fill_rate_slider,
        'order_revenue_per_order': order_revenue_slider,
        'throughput': throughput_slider,
        'variable_cost_per_order': variable_cost_per_order_slider
    }
)

# Function to display optimal P&L
def show_optimal_pnl(b):
    storage_rate_range = range(10, 51, 5)
    storage_capacity_range = range(5000, 30001, 5000)
    throughput_range = range(1000, 50001, 5000)
    
    best_params, best_profit = find_optimal_pnl(fixed_costs_slider.value, storage_rate_range, storage_capacity_range, fill_rate_slider.value, order_revenue_slider.value, throughput_range, variable_cost_per_order_slider.value)
    
    best_storage_rate, best_storage_capacity, best_throughput = best_params
    optimal_pnl_df, _ = calculate_pnl(fixed_costs_slider.value, best_storage_rate, best_storage_capacity, fill_rate_slider.value, order_revenue_slider.value, best_throughput, variable_cost_per_order_slider.value)
    
    clear_output(wait=True)
    display(optimal_pnl_df)
    display(widgets.Label(f'Optimal Profit: ₹{best_profit}'))
    display(widgets.Label(f'Best Storage Rate: ₹{best_storage_rate}/cubic ft'))
    display(widgets.Label(f'Best Storage Capacity: {best_storage_capacity} cubic ft'))
    display(widgets.Label(f'Best Throughput: {best_throughput} orders'))

# Button to find and display optimal P&L
button = widgets.Button(description="Find Optimal P&L")
button.on_click(show_optimal_pnl)

# Display the widgets, button and the output
display(ui, button, output)

