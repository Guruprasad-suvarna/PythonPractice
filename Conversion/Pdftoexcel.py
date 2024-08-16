# import  tabula

# # data=tabula.read_pdf("input.pdf",pages="all")
# # print (data)

# tabula.convert_into("CDT-DentalCodes.pdf","CDT-DentalCodes.csv",pages="all",output_format="csv")


#MUltiple sheet

# import tabula
# import pandas as pd

# # Replace 'input.pdf' with the path to your PDF file
# pdf_file = "CDT-DentalCodes.pdf"

# # Specify the output Excel file
# output_excel_file = "output.xlsx"

# # Extract tables from the PDF, skipping headers
# dfs = tabula.read_pdf(pdf_file, pages='all', stream=True, multiple_tables=True, pandas_options={'header': None})

# # Create a Pandas Excel writer using XlsxWriter as the engine
# excel_writer = pd.ExcelWriter(output_excel_file, engine='xlsxwriter')

# # Iterate through the dataframes and save each as a separate sheet in the Excel file
# for i, df in enumerate(dfs):
#     df.to_excel(excel_writer, sheet_name=f"Sheet_{i + 1}", index=False, header=False)  # Exclude headers

# # Save the Excel file
# excel_writer._save()

# print(f"PDF tables converted to Excel sheets in {output_excel_file}")



#Single sheet
# import tabula
# import pandas as pd

# # Replace 'input.pdf' with the path to your PDF file
# pdf_file = "CDT-DentalCodes.pdf"

# # Specify the output Excel file
# output_excel_file = "output.xlsx"

# # Initialize an empty DataFrame to store the combined data
# combined_df = pd.DataFrame()

# # Extract tables from the PDF, skipping headers
# dfs = tabula.read_pdf(pdf_file, pages='all', stream=True, multiple_tables=True, pandas_options={'header': None})

# # Iterate through the dataframes and append them to the combined DataFrame
# for i, df in enumerate(dfs):
#     combined_df = combined_df._append(df, ignore_index=True)

# # Save the combined data to a single sheet in the Excel file
# combined_df.to_excel(output_excel_file, index=False, header=False)

# print(f"PDF tables combined into one sheet in {output_excel_file}")



# import os
# import tabula
# import pandas as pd

# # Directory containing the PDF files
# pdf_directory = "C:\Python\Conversion\pdf_directory"

# # Output directory for Excel files
# output_directory = "output"

# # Create the output directory if it doesn't exist
# os.makedirs(output_directory, exist_ok=True)

# # List all PDF files in the input directory
# pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

# for pdf_file in pdf_files:
#     # Construct the full path to the input PDF
#     pdf_path = os.path.join(pdf_directory, pdf_file)

#     # Specify the output Excel file path with the same name as the input PDF
#     excel_file = os.path.join(output_directory, os.path.splitext(pdf_file)[0] + '.xlsx')

#     # Initialize an empty DataFrame to store the combined data
#     combined_df = pd.DataFrame()

#     # Extract tables from the PDF, skipping headers
#     dfs = tabula.read_pdf(pdf_path, pages='all', stream=True, multiple_tables=True, pandas_options={'header': None})

#     # Iterate through the dataframes and append them to the combined DataFrame
#     for i, df in enumerate(dfs):
#         combined_df = combined_df._append(df, ignore_index=True)

#     # Save the combined data to the Excel file with the same name as the input PDF
#     combined_df.to_excel(excel_file, index=False, header=False)

#     print(f"PDF tables from '{pdf_file}' combined into '{excel_file}'")


import os
import tabula
import pandas as pd

# Directory containing the PDF files
pdf_directory = "C:\Python\Conversion\pdf_directory"

# Output directory for Excel files
output_directory = "output"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List all PDF files in the input directory
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

for pdf_file in pdf_files:
    # Construct the full path to the input PDF
    pdf_path = os.path.join(pdf_directory, pdf_file)

    # Specify the output Excel file path with the same name as the input PDF
    excel_file = os.path.join(output_directory, os.path.splitext(pdf_file)[0] + '.xlsx')

    # Extract tables from the PDF, skipping headers
    dfs = tabula.read_pdf(pdf_path, pages='all', stream=True, multiple_tables=True, pandas_options={'header': None})

    # Create a Pandas Excel writer using XlsxWriter as the engine
    excel_writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

    # Iterate through the dataframes and save each as a separate sheet in the Excel file
    for i, df in enumerate(dfs):
        df.to_excel(excel_writer, sheet_name=f"Sheet_{i + 1}", index=False, header=False)  # Exclude headers

    # Save the Excel file
    excel_writer._save()

    print(f"PDF tables from '{pdf_file}' converted to Excel sheets in '{excel_file}'")


