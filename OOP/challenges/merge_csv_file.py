def merge_csv(output_file, *file_paths):
    result = ''
    for file in file_paths:
        with open(file, 'r', encoding='utf-8') as file:
            one_read = file.read()
        lines = one_read.split('\n')
        header = lines[0]
        result = result + '\n' + '\n'.join(lines[1:])
    result = header + result
    with open(output_file, 'w') as file:
        file.write(result)
    return result


path1 = r'C:\python_tmp\1.csv'
path2 = r'C:\python_tmp\2.csv'
output = r'C:\python_tmp\output.csv'
print(merge_csv(output, path1, path2))