import pandas as pd
import numpy as np


def monthly_cash_flow(df, interestRate, monthsOfLoan, insurance, downPaymentDecimal):
    # Define Variables
    interestRate /= 12
    insurance /= 12

    # covert to percentage owed on the house
    downPaymentDecimal = 1 - downPaymentDecimal

    # Calculate Property Tax
    df["propertyTax"] = round((df["Price"] * .0125) / 12, 2)
    # Calculate Monthly Mortgage
    df["MonthlyMortgagePayment"] = round(
        ((downPaymentDecimal * df["Price"]) * (interestRate * (1 + interestRate) ** monthsOfLoan)) / (((1 + interestRate) ** monthsOfLoan) - 1),2)

    # Calculate Monthly Cash Flow
    df["MonthlyCashFlow"] = round(df["RentEstimate"] - (
            df["propertyTax"] + df["MonthlyMortgagePayment"] + insurance), 2)

    # Sort by MonthlyCashFlow in descending order
    df.sort_values(by=['MonthlyCashFlow'], inplace=True, ascending=False)

    # Reset index, drop extra column
    df.reset_index(inplace=True)
    df.drop(['index'], axis=1, inplace=True)

    # Return dataframe
    return df


# Calculates that down payment percentage required for a purchase to be profitable
# Appends the down payment percentage to the dataframe as well as the down payment amount
# Params: DataFrame, interest rate of the loan
def breakEvenCashFlow(df, interest):
    #########Define Variables needed########
    # New dataframe that gets returned from the function
    breakEven_df = pd.DataFrame()

    # Temporary dataframe used to hold the values of the Monthly Cash Flow during calculation
    mcf_df = pd.DataFrame()

    # A List to store the down payment percentages that make the purchase profitable
    downPayPercent = []

    # Loop to iterate through the MonthlyCashFlow column of data frame passed to the function
    for profit in df['MonthlyCashFlow']:

        # if Monthly Cash Flow is positive with 20% down, append it to the existing dataframe
        if profit > 0:
            breakEven_df = pd.concat([breakEven_df, df.loc[df['MonthlyCashFlow'] == profit]], ignore_index=True)
            downPayPercent.append(.2)

        # if profit is negative with 20% down
        elif profit <= 0:
            mcf_df = df.loc[df['MonthlyCashFlow'] == profit]
            # begin the down payment percentage at 20% and increase by 1% until the purchase is profitable
            for downPaymentPercentage in np.arange(.2, 1.0, .01):
                # Calculates monthly cash flow based on downPaymentPercentage
                monthly_cash_flow(mcf_df, interest, 360, 1000, downPaymentPercentage)
                # Check if monthlyCashFlow is positive
                if (mcf_df['MonthlyCashFlow'] > 0).any():
                    # add house to the dataframe
                    breakEven_df = pd.concat([breakEven_df, mcf_df], ignore_index=True)
                    # add downPaymentPercentage to the list
                    downPayPercent.append(downPaymentPercentage)
                    break
                else:
                    continue
    dpp_df = pd.DataFrame([downPayPercent])
    # print(dpp_df)
    breakEven_df = pd.concat([breakEven_df, dpp_df.T], axis=1)
    breakEven_df.rename(columns={breakEven_df.columns[-1]: 'DownPaymentPercentage'}, inplace=True)
    breakEven_df['DownPaymentAmount'] = breakEven_df['DownPaymentPercentage'] * breakEven_df['Price']

    return breakEven_df


def ZillowSetColumns(df):
    df.rename(columns={'hdpData.homeInfo.homeType': 'HomeType', 'hdpData.homeInfo.streetAddress': 'Address',
                                 'hdpData.homeInfo.city': 'City',
                                 'hdpData.homeInfo.state': 'State', 'hdpData.homeInfo.zipcode': 'Zipcode',
                                 'hdpData.homeInfo.bedrooms': 'Beds',
                                 'hdpData.homeInfo.bathrooms': 'Baths', 'hdpData.homeInfo.livingArea': 'Sqft',
                                 'hdpData.homeInfo.lotAreaValue': 'LotSize',
                                 'hdpData.homeInfo.price': 'Price', 'hdpData.homeInfo.zestimate': 'PriceEstimate',
                                 'hdpData.homeInfo.rentZestimate': 'RentEstimate', 'zpid': 'ID'}, inplace=True)

    # Selected columns for the new dataframe
    columns = ['ID', 'Address', 'Zipcode', 'Beds', 'Baths', 'Sqft', 'LotSize', 'Price',
               'PriceEstimate', 'RentEstimate', 'HomeType']
    return df[columns]


def ZillowSetColumnTypes(df):
    df.dropna(inplace=True)
    df['ID'] = df['ID'].astype(str)
    df['Address'] = df['Address'].astype(str)
    df['Zipcode'] = df['Zipcode'].astype(str)
    df['Beds'] = df['Beds'].astype(str)
    df['Baths'] = df['Baths'].astype(str)
    df['LotSize'] = df['LotSize'].astype(str)
    df['Price'] = df['Price'].astype(int)
    df['PriceEstimate'] = df['PriceEstimate'].astype(int)
    df['RentEstimate'] = df['RentEstimate'].astype(int)


def RedfinSetColumns(df):
    df.rename(columns={'listingId': 'ID', 'baths': 'Baths','beds': 'Beds','sqFt.value': 'Sqft',
                       'streetLine.value': 'Address','zip': 'Zipcode','price.value': 'Price',
                       'lotSize.value': 'LotSize'}, inplace=True)
    columns = ['ID', 'Address', 'Zipcode', 'Beds', 'Baths', 'Sqft', 'LotSize', 'Price']
    return df[columns]


def RedfinSetColumnTypes(df):
    df.dropna(inplace=True)
    df['ID'] = df['ID'].astype(str)
    df['Address'] = df['Address'].astype(str)
    df['Zipcode'] = df['Zipcode'].astype(str)
    df['Beds'] = df['Beds'].astype(str)
    df['Baths'] = df['Baths'].astype(str)
    df['LotSize'] = df['LotSize'].astype(str)
    df['Price'] = df['Price'].astype(int)



