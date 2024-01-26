from matplotlib import pyplot as plt


def RentByZipcode(df):
    plt.scatter(df['Zipcode'], df['RentEstimate'])
    plt.title('Rent By Zipcode')
    plt.xlabel('Zipcode')
    plt.ylabel('Rent')


def RentPerSqft(df):
    plt.scatter(df['Sqft'], df['RentEstimate'])
    plt.title('Rent Per Sqft')
    plt.xlabel('Sqft')
    plt.ylabel('Rent')
