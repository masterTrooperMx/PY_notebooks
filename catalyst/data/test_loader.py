import sys, argparse, csv, json
#from settings import *
def load_settings(fileN):
    if fileN:
        with open(fileN, 'r') as f:
            return json.loads(f.read())
    else:
        return 0
def print_settings(settings):
    for key in settings:
        print(key, ": ", settings[key])
    
settings = load_settings('./settings.json')
print_settings(settings)
# command arguments
parser = argparse.ArgumentParser(description='load csv cols',\
 fromfile_prefix_chars="@" )
parser.add_argument('file1', help='csv file to import', action='store')
parser.add_argument('file2', help='csv file to import', action='store')
args = parser.parse_args()
# check with settings
for x in range(1, settings['no_files']):
    csv_file=""
    fname = "csv_file=args.file%s"%x
    print(fname)
    #csv_file = args.file
    exec(fname)
    # open csv file
    with open(csv_file, 'r') as csvfile:

        # get number of columns
        for line in csvfile.readlines():
            array = line.split(',')
            first_item = array[0]

        num_columns = len(array)
        csvfile.seek(0)

        reader = csv.reader(csvfile, delimiter=',')
        included_cols = [1, 2, 6, 7]

        for row in reader:
            content = list(row[i] for i in included_cols)
            print(content)