import click
import pandas as pd
import datetime


@click.group()
def commands():
  pass


@commands.command()
@click.option('--name',help='input your name')
def run(name):
  #put your logic here
  print("hello "+ name)


@commands.command()
@click.option('--input', help='location to csv input file')
@click.option('--output', help='location to csv output file')
def run(input, output):
  data = pd.read_csv(input)
  
  # data['day'] = pd.to_datetime(data['timestamp'])
  data['transactions'] = 1
  s1 = data.groupby('user')['transactions'].sum()
  s1 = s1.sort_values(axis=0, ascending=False)
  s1 = s1[:10]
  

  s2 = data[['user', 'timestamp', 'product']].copy()
  s2 = s2.set_index('user')
  

  s1 = pd.DataFrame(s1)
  
  df = s1.join(s2)
  df = df.sort_values(by='timestamp', ascending=True)
  df_grouped = df.groupby('user').first()
  df_grouped = df_grouped.set_index('product')
  df_grouped = df_grouped.drop(['transactions', 'timestamp'], axis=1)
  # print(df_grouped)

  df_grouped.to_csv(output, header=False)
  

if __name__ == '__main__':
  commands()
