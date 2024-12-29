import sys

from matplotlib import pyplot as plt
import seaborn as sns

sys.path.append('D:\\whattsapp chat analysis')

import streamlit as st
import preprocessor
import helper

st.sidebar.title("Whatsapp Chat Analyser")

# File uploader allows multiple files
uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files=True)

if uploaded_files is not None:
    # Handle multiple file uploads
    for uploaded_file in uploaded_files:
        # Process each file
        bytes_data = uploaded_file.getvalue()  # Get the content of the file
        data = bytes_data.decode("utf-8")  # Decode the content to a string

        # Process the data using the preprocessor
        df = preprocessor.preprocess(data)

        # Display the dataframe in Streamlit
        #st.dataframe(df)

        #fetch unique users
        user_list=df['Sender'].unique().tolist()
        user_list.sort()
        user_list.insert(0,"Overall")
        selected_user=st.sidebar.selectbox("Select Sender", user_list)

        if st.sidebar.button("Analyze"):
            num_messages,words,num_media=helper.fetch_stats(selected_user,df)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.header("Total Messages")
                st.title(num_messages)
            with col2:
                st.header("Total words")
                st.title(len(words))
            with col3:
                st.header("Total media in message")
                st.title(num_media)

        # for getting most active person
        if selected_user=="Overall":

            st.title("Most active users")
            x,new_df=helper.active_users(df)
            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)

            with col1:

                ax.bar(x.index, x.values)
                plt.xticks(rotation=90)
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)



#worldcloud
        st.title("Wordcloud")
        wc = helper.create_wordcloud(selected_user,df)
        fig, ax = plt.subplots()
        ax.imshow(wc)
        st.pyplot(fig)

#most common 10 words
        st.title("Most common words")
        mostcommon=helper.most_common_words(selected_user,df)
        col1, col2 = st.columns(2)
        with col1:
         fig,ax=plt.subplots()
         ax.bar(mostcommon['Word'],mostcommon['Frequency'],color='darkblue')
         st.pyplot(fig)
        with col2:
            st.dataframe(mostcommon)

#emojo analysis
        st.title("Emoji analysis")
        emojis_df=helper.emoji_analysis(selected_user,df)
        col1, col2 = st.columns(2)
        with col1:
         fig, ax = plt.subplots()
         ax.bar(emojis_df['Emoji'], emojis_df['Frequency'],color='green')
         st.pyplot(fig)
        with col2:
         st.dataframe(emojis_df)




# timeline analysis
st.title("Timeline analysis")

# Unpack the returned tuple into two variables
monthly_count, daywise_count,monthwise_count,heatmap_data= helper.monthly_timeline(selected_user, df)
# Plot the monthly count timeline
fig, ax = plt.subplots()
plt.plot(monthly_count['Month_Year'], monthly_count['Message_Count'])
st.pyplot(fig)



# Date-wise analysis

# Plot the day count analysis (Date-wise)
fig, ax = plt.subplots()
col1, col2 = st.columns(2)

with col1:
   st.title("Most Busy Dayssss")
   plt.bar(daywise_count['Day_of_Week'].astype(str), daywise_count['Message_Count'],color='purple')
   plt.xticks(rotation=90, ha='right',fontsize=10)
   st.pyplot(fig)

with col2:
    st.title("Most Busy month")
    plt.bar(monthwise_count['Month'], monthwise_count['Message_Count'], color='orange')
    plt.xticks(rotation=90, ha='right', fontsize=10)
    st.pyplot(fig)

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=False, fmt='d', linewidths=0.5)
plt.show()

st.title("Week-Monthly Analysis")
fig, ax = plt.subplots()
ax = sns.heatmap(heatmap_data)
st.pyplot(fig)

