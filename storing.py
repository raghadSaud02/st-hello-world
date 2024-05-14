import streamlit as st




st.image("image.png", width=200)

st.title('Discover your perfect job!')


st.write("Let's embark on a collaborative journey to identify high-demand roles in today's dynamic labor market, pinpoint companies offering extensive job prospects, and explore the abundant opportunities awaiting graduates as they enter the workforce.")




import streamlit as st
import pandas as pd
import plotly.graph_objs as go

def main():
    # Load your data (Replace this with your data loading code)
    df = pd.read_csv("Jadarat_data.csv")

    if isinstance(df.index, pd.DatetimeIndex) or isinstance(df.index, pd.MultiIndex):
        df = df.reset_index()

    # Remove any pre-existing indices for ease of use in the code
    df = df.reset_index(drop=True)
    df.columns = [str(c) for c in df.columns]  # Update columns to strings if they are numbers

    # Select only non-null job titles
    s = df[df['job_title'].notnull()]['job_title']

    # Calculate value counts and percentage
    chart = pd.value_counts(s).to_frame(name='data')
    chart['percent'] = (chart['data'] / chart['data'].sum()) * 100
    chart.index.name = 'labels'

    # Sort values and select top 100
    chart = chart.reset_index().sort_values(['data', 'labels'], ascending=[False, True])[:100]

    # Create Plotly chart with dark green colors
    fig = go.Figure(data=[go.Bar(x=chart['labels'], y=chart['data'], name='Frequency', marker_color='darkgreen')],
                    layout=go.Layout({
                        'barmode': 'group',
                        'legend': {'orientation': 'h'},
                        #'title': {'text': 'job_title Value Counts'},
                        'xaxis': {'title': {'text': 'Job Title'}},
                        'yaxis': {'title': {'text': 'Job ad frequency'}}
                    }))

    # Display the chart
    st.plotly_chart(fig)

    
    st.write("The data speaks volumes: in the Kingdom of Saudi Arabia, the role most coveted by the labor market reigns as that of a salesperson. If your skill set aligns with the demands of this pivotal position, seize the opportunity to apply and cultivate your expertise within it. With the potential for dynamic growth and impact, pursuing a career in sales opens pathways for personal and professional development, propelling you toward success in the vibrant Saudi market.")
    
    
    



    
    st.write("Now that we've uncovered the top in-demand job in the Kingdom of Saudi Arabia, let's embark on a journey to explore the companies offering exceptional job opportunities. By delving into the expansive landscape of Saudi businesses, we'll uncover organizations primed to provide not just employment, but platforms for growth, development, and success. Join me in this exploration  ")


   # Select only non-null company names
    s = df[df['comp_name'].notnull()]['comp_name']

    # Calculate value counts and percentage
    chart = pd.value_counts(s).to_frame(name='data')
    chart['percent'] = (chart['data'] / chart['data'].sum()) * 100
    chart.index.name = 'labels'

    # Sort values and select top 100
    chart = chart.reset_index().sort_values(['data', 'labels'], ascending=[False, True])[:100]

    # Create Plotly chart with dark green color
    fig = go.Figure(data=[go.Bar(x=chart['labels'].values, y=chart['data'].values, name='Frequency', marker_color='darkgreen')],
                    layout=go.Layout({
                        'barmode': 'group',
                        'legend': {'orientation': 'h'},
                        #'title': {'text': 'comp_name Value Counts'},
                        'xaxis': {'title': {'text': 'Comp Name'}},
                        'yaxis': {'title': {'text': 'Number of jobs available'}}
                    }))

    # Display the chart
    st.plotly_chart(fig)
    st.write("As depicted in the visual data, Company (العرض المتقن)stands out as the leading provider of job opportunities. Now, let's delve deeper into their vision to ascertain its compatibility with your skill set, enabling you to make an informed decision regarding application and leveraging these abundant opportunities. By aligning your skills with the company's vision, you can maximize your potential for success and fulfillment within their dynamic environment.")

    





    st.write("Let's investigate whether the widespread belief in Saudi Arabia—that graduates struggle to find job opportunities")
     # Remove any pre-existing indices for ease of use
    df = df.reset_index().drop('index', axis=1, errors='ignore')
    df.columns = [str(c) for c in df.columns]  # Update columns to strings if they are numbers

    # Select only non-null values of 'exper'
    s = df[df['exper'].notnull()]['exper']

    # Calculate value counts and percentage
    chart = pd.value_counts(s).to_frame(name='data')
    chart['percent'] = (chart['data'] / chart['data'].sum()) * 100
    chart.index.name = 'labels'

    # Sort values and select top 100
    chart = chart.reset_index().sort_values(['data', 'labels'], ascending=[False, True])[:100]

    # Create Plotly chart with dark green bars
    fig = go.Figure(data=[go.Bar(x=chart['labels'].values, y=chart['data'].values, name='Frequency', marker_color='darkgreen')],
                    layout=go.Layout({
                        'barmode': 'group',
                        'legend': {'orientation': 'h'},
                        #'title': {'text': 'exper Value Counts'},
                        'xaxis': {'title': {'text': 'Exper'}},
                        'yaxis': {'title': {'text': 'Number of jobs available'}}
                    }))

    # Display the chart
    st.plotly_chart(fig)


    
    st.write("Surprisingly, the snapshot above reveals a striking trend: a substantial portion of job openings in the labor market are specifically designed for fresh graduates, challenging the prevailing notion that they encounter scarcity in opportunities.")


    st.title('conclusion')

    st.write("our exploration has illuminated the landscape of job opportunities in the Kingdom of Saudi Arabia, showcasing the demand for sales roles and the abundance of opportunities tailored for fresh graduates. We've identified Company A as a prominent player in providing job prospects, urging individuals to align their skills with the company's vision for optimal success. Contrary to common belief, recent graduates are met with a wealth of job openings, promising a bright future in the Saudi labor market. With this knowledge in hand, individuals are empowered to embark on their journey towards finding their perfect job and realizing their full potential.")





if __name__ == "__main__":
    main()