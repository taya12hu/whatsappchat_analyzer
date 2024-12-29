<<<<<<< HEAD
import re
import pandas as pd

def preprocess(data):
    pattern = r'(\d{2}/\d{2}/\d{2}), (\d{2}:\d{2}) - (.*?): (.*)'

    # Split the data into lines
    lines = data.split('\n')

    # Parse lines into lists
    parsed_data = []
    for line in lines:
        match = re.match(pattern, line)
        if match:
            parsed_data.append(match.groups())

    # Convert to DataFrame
    df = pd.DataFrame(parsed_data, columns=['Date', 'Time', 'Sender', 'Message'])

    # Display the DataFrame
    return df

=======
import re
import pandas as pd

def preprocess(data):
    pattern = r'(\d{2}/\d{2}/\d{2}), (\d{2}:\d{2}) - (.*?): (.*)'

    # Split the data into lines
    lines = data.split('\n')

    # Parse lines into lists
    parsed_data = []
    for line in lines:
        match = re.match(pattern, line)
        if match:
            parsed_data.append(match.groups())

    # Convert to DataFrame
    df = pd.DataFrame(parsed_data, columns=['Date', 'Time', 'Sender', 'Message'])

    # Display the DataFrame
    return df

>>>>>>> 7b42a8b7034339b285df1333cc77fd312f0ffce3
