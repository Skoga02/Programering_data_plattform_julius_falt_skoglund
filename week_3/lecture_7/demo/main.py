import pandas as pd 

if __name__ == '__main__':

    product_df = pd.DataFrame(
        {
            "id": ["SKU-1", "SKU-2", "SKU-3", "SKU-4", "SKU-5"],
            "name": ["shoes", "pants", "shirts", "sweaters", "designer jacket"],
            "price": [760, 520, 450, 550, 4500],
            "currency": ["SEK", "SEK", "SEK", "SEK", "SEK"], # TODO - Missing Vlaues for csv files when loaded (Crash)
        }
    )

    print(product_df)

    print(product_df["price"].max())    # Highest Value
    print(product_df["price"].min())    # Minimum Value
    print(product_df["price"].mean())   # Mean of Total
    print(product_df["price"].median()) # Median of Total     

    print(product_df.describe())

    print(product_df.sort_values("price"))  # Sorting algorithm == Quiksort

    # to_* (exporting files)
    product_df.to_csv("Products.csv", index=False) # Path = Project Folder

    #########################################
    ########### DRITY DATAFRAME #############

    dirty_df = pd.DataFrame(
        {
            "id": [" sku-1 ", "SKU- 2", "Sku-3", "sku_4", "SKU5 "],
            "name": [" Shoes", "pants ", "SHIRTS", " SweaTers ", "designer  jacket"],
            "price": [" 760 ", "520", " 450", "550 ", " 4500"],
            "currency": [" sek", "SEK ", "Sek", "sek ", " SEK"],
        }
    )
    ## dirty_df.id = [cleaned strings] <-- FALSE
    # dirty_df["id"].split() # This won´t propperly replace values in Series (columns)
    dirty_df["id"] = dirty_df["id"].str.strip() # Remove whitespaces (start/end of sting)
    dirty_df["id"] = dirty_df["id"].str.upper() # ALL CAPS
    dirty_df["id"] = dirty_df["id"].str.replace(" ", "").str.replace("_", "-") # Replace string content 
    # SKU4 <-- Thecnical danger zone, what if multiple -- exists?
    # SKU5 <-- which EXCLUDES '-', Danger zone, because transformation isn't adding symbols...


    dirty_df["price"] = dirty_df["price"].astype(float) # Casts: Current-Datatype --> Float


    dirty_df["name"] = dirty_df["name"].str.strip()
    dirty_df["name"] = dirty_df["name"].str.title()
    dirty_df["name"] = dirty_df["name"].str.replace(r"\s+", " ", regex = True)   #regex, value, bool

    print(dirty_df.values)


    #################################################
    ############# MISSING DATA DATAFRAME ############

    missing_df = pd.DataFrame(
        {
            "id": [" sku-1 ", "SKU- 2", None, "sku_4", "SKU5 "],
            "name": [" Shoes", None, "SHIRTS", " SweaTers ", "designer  jacket"],
            "price": [" 760 ", "520", None, "550 ", " 4500"],
            "currency": [" sek", "SEK ", "Sek", None, " SEK"],
        }
    )

    print(missing_df.isna())    # Pandas tool for identifiyng TRUE missin values

    # Flag missing values, helps decide strategy later on 
    # Currency is an example of a REPLACED column
    missing_df["id_missing"] = missing_df["id"].isna()  # This creates a separate column
    missing_df["name_missing"] = missing_df["name"].isna()  # This creates a separate column
    missing_df["price_missing"] = missing_df["price"].isna()    # This creates a separate column
    missing_df["currency"] = missing_df["currency"].isna()  # This replaces the column
    print(missing_df)
 
    # DRY version, does the same as before, this method might have worse performance
    mdf_values = ["id", "name", "price", "currency"]
    for mdf in mdf_values:
        missing_df[mdf+"-missing"] = missing_df[mdf].isna()


    print(missing_df)

    