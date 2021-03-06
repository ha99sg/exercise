import click
import pandas as pd

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

  data['transactions'] = 1
  s1 = data.groupby('user')['transactions'].sum()
  s1 = s1.sort_values(axis=0, ascending=False)
  s1 = s1[:10]
  d1 = pd.DataFrame(s1)

  d2 = data[['user', 'product', 'timestamp']].copy()
  d2 = d2.set_index('user')

  # d2 = d2.drop_duplicates(subset=['product'])

  # d2 = d2.drop(['timestamp'], axis=1)
  # d1 = d1.drop(['transactions'], axis=1)

  df = d1.join(d2)
  df = df.sort_values(by="timestamp", ascending=True)
  df = df.groupby('user').nth(1)
  df = df.drop(['transactions', 'timestamp'], axis=1)
  df = df.set_index('product')
  df.to_csv(output, header=False)


if __name__ == '__main__':
  commands()
