import click
import csv
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
  data = data.groupby('user')['status'].sum()
  data = data.sort_values(axis=0, ascending=False)
  data = data[:10]

  data.to_csv(output, header=False)

if __name__ == '__main__':
  commands()


# cmd
# py trans_analytic_1.py run --input="input/input_data.csv" --output "output/output_1.csv"