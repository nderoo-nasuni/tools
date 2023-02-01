import csv
# For help contact Nick DeRoo
# The goal of this tool is to find customers with Config INI variables in a accounts.ini query from the NOC.

# To download an account.ini search use this URL
# https://account.nasuni.com/dashboard/reports/custom/?id=148 

# Running
# python3 csv_tool_v2.py

def find_var(x,var):
    x = str(x)
    cvar = "#%s" % var
    for i in range(len(x.split(sep="\n"))):
        if (var in x.split(sep="\n")[i] and
                cvar not in x.split(sep="\n")[i]):
            return x.split(sep="\n")[i].split("=")[1]

def main():

    # put your input and output filenames here:
    input_file = "local_conf.csv"
    output_file = "local_hard_limit_out_new.csv"

    # enter your config ini values you want to find in the below list
    ini_config_items = ["CLOUDVOLMGR_CURL_GET_TIMEOUT", "CLOUDVOLMGR_CURL_PUT_TIMEOUT", "CLOUDVOLMGR_CURL_MERGE_GET_TIMEOUT", "CLOUDVOLMGR_OVERWRITE_LICENSE_MAX_THREADS"]
    #ini_config_items = ["UNITYFS_OPENFILE_HARDLIMIT"]

    #Update your header here
    # Example config.ini
    #header = ["company", "user_uuid", "ini_text"]
    # Example local.conf
    header = ["Company/Name	Installed", "Last Activity", "Build", "Local.conf", "Cloud Capacity", "Files", "Subscription"]

    results = []
    with open(input_file, 'r') as f, open(output_file, 'w') as outf:
        csv_file = csv.reader(f, delimiter=',')
        writer = csv.writer(outf)
        header = header + ini_config_items
        results.append(header)
        for csv_row in csv_file:
            for ini_config in ini_config_items:
                value = find_var(csv_row[2], ini_config)
                #if ini_config = "CLOUDVOLMGR_CURL_GET_TIMEOUT" and value < 600: # can be used to filter results.
                csv_row.append(value)
            results.append(csv_row)

        for row in results:
            writer.writerow(row)


if __name__ == "__main__":
    main()