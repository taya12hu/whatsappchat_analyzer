<<<<<<< HEAD

from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji


def fetch_stats(selected_user,df):

    if selected_user!="Overall":
        df = df[df['Sender'] == selected_user]

    #for getting total messages
    num_messages = df.shape[0]

    #for getting media number
    num_media=df[df["Message"]=='<Media omitted>'].shape[0]

    #for getting total words
    words = []
    for message in df["Message"]:
        words.extend(message.split())

    return num_messages, words, num_media


# for getting most active person
def active_users(df):
                x= df['Sender'].value_counts().head()
                df=round((df['Sender'].value_counts()/df.shape[0]*100),2).reset_index()
                return x,df

#timeline
def monthly_timeline(selected_user,df):
    if selected_user!="Overall":
        df = df[df['Sender'] == selected_user]

    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')
    # Create 'Month_Year' column for grouping by month and year
    df['Month_Year'] = df['Date'].dt.to_period('M')
    # Count the occurrences of each 'Month_Year'
    monthly_count = df.groupby('Month_Year').size().reset_index(name='Message_Count')
    # Convert 'Month_Year' to string or datetime to make it plot-friendly
    monthly_count['Month_Year'] = monthly_count['Month_Year'].astype(str)


    df['Day_of_Week'] = df['Date'].dt.day_name()
    # Group by the day of the week and count the number of messages
    daywise_count = df['Day_of_Week'].value_counts().reindex(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ).reset_index()
    daywise_count.columns = ['Day_of_Week', 'Message_Count']


    df['Month'] = df['Date'].dt.month_name()  # Extract month name
    monthwise_count = df.groupby('Month').size().reset_index(name='Message_Count')
    # Sort months in calendar order
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    monthwise_count['Month'] = pd.Categorical(monthwise_count['Month'], categories=month_order, ordered=True)
    monthwise_count = monthwise_count.sort_values(by='Month')


    heatmap_data = df.groupby(['Day_of_Week', 'Month']).size().unstack(fill_value=0)
    heatmap_data = heatmap_data.reindex(columns=[m for m in month_order if m in heatmap_data.columns])


    return monthly_count,daywise_count,monthwise_count,heatmap_data



#wordcloud
def create_wordcloud(selected_user,df):
    if selected_user != "Overall":
        df = df[df['Sender'] == selected_user]
    temp = df[df['Message'] != '<Media omitted>']

        # Combine all the messages into one large string
    all_messages = temp['Message'].str.cat(sep=' ')  # Concatenate all messages into one string

    # Generate word cloud
    wc = WordCloud(width=800, height=400, background_color='white').generate(all_messages)

    return wc

#most_common20words
def most_common_words(selected_user,df):
    f=open('stop_hinglish.txt','r')
    stop_words = f.read()

    if selected_user != "Overall":
        df = df[df['Sender'] == selected_user]
    temp=df[df['Message']!='<Media omitted>']

    words = []
    for message in temp["Message"]:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    mostcommon_df=pd.DataFrame(Counter(words).most_common(5),columns=['Word','Frequency'])
    return mostcommon_df

#emoji analysis
def emoji_analysis(selected_user, df):
    if selected_user != "Overall":
        df = df[df['Sender'] == selected_user]

    emojis = []
    for message in df["Message"]:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_counts = Counter(emojis).most_common(5)  # Get the emoji counts
    emojis_df = pd.DataFrame(emoji_counts, columns=['Emoji', 'Frequency'])  # Convert to DataFrame
    return emojis_df

=======

from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji


def fetch_stats(selected_user,df):

    if selected_user!="Overall":
        df = df[df['Sender'] == selected_user]

    #for getting total messages
    num_messages = df.shape[0]

    #for getting media number
    num_media=df[df["Message"]=='<Media omitted>'].shape[0]

    #for getting total words
    words = []
    for message in df["Message"]:
        words.extend(message.split())

    return num_messages, words, num_media


# for getting most active person
def active_users(df):
                x= df['Sender'].value_counts().head()
                df=round((df['Sender'].value_counts()/df.shape[0]*100),2).reset_index()
                return x,df

#timeline
def monthly_timeline(selected_user,df):
    if selected_user!="Overall":
        df = df[df['Sender'] == selected_user]

    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')
    # Create 'Month_Year' column for grouping by month and year
    df['Month_Year'] = df['Date'].dt.to_period('M')
    # Count the occurrences of each 'Month_Year'
    monthly_count = df.groupby('Month_Year').size().reset_index(name='Message_Count')
    # Convert 'Month_Year' to string or datetime to make it plot-friendly
    monthly_count['Month_Year'] = monthly_count['Month_Year'].astype(str)


    df['Day_of_Week'] = df['Date'].dt.day_name()
    # Group by the day of the week and count the number of messages
    daywise_count = df['Day_of_Week'].value_counts().reindex(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ).reset_index()
    daywise_count.columns = ['Day_of_Week', 'Message_Count']


    df['Month'] = df['Date'].dt.month_name()  # Extract month name
    monthwise_count = df.groupby('Month').size().reset_index(name='Message_Count')
    # Sort months in calendar order
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    monthwise_count['Month'] = pd.Categorical(monthwise_count['Month'], categories=month_order, ordered=True)
    monthwise_count = monthwise_count.sort_values(by='Month')


    heatmap_data = df.groupby(['Day_of_Week', 'Month']).size().unstack(fill_value=0)
    heatmap_data = heatmap_data.reindex(columns=[m for m in month_order if m in heatmap_data.columns])


    return monthly_count,daywise_count,monthwise_count,heatmap_data



#wordcloud
def create_wordcloud(selected_user,df):
    if selected_user != "Overall":
        df = df[df['Sender'] == selected_user]
    temp = df[df['Message'] != '<Media omitted>']

        # Combine all the messages into one large string
    all_messages = temp['Message'].str.cat(sep=' ')  # Concatenate all messages into one string

    # Generate word cloud
    wc = WordCloud(width=800, height=400, background_color='white').generate(all_messages)

    return wc

#most_common20words
def most_common_words(selected_user,df):
    f=open('stop_hinglish.txt','r')
    stop_words = f.read()

    if selected_user != "Overall":
        df = df[df['Sender'] == selected_user]
    temp=df[df['Message']!='<Media omitted>']

    words = []
    for message in temp["Message"]:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    mostcommon_df=pd.DataFrame(Counter(words).most_common(5),columns=['Word','Frequency'])
    return mostcommon_df

#emoji analysis
def emoji_analysis(selected_user, df):
    if selected_user != "Overall":
        df = df[df['Sender'] == selected_user]

    emojis = []
    for message in df["Message"]:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_counts = Counter(emojis).most_common(5)  # Get the emoji counts
    emojis_df = pd.DataFrame(emoji_counts, columns=['Emoji', 'Frequency'])  # Convert to DataFrame
    return emojis_df

>>>>>>> 7b42a8b7034339b285df1333cc77fd312f0ffce3
