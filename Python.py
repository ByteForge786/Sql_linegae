import codecs

def clean_file(input_file, output_file):
    try:
        with codecs.open(input_file, 'r', encoding='utf-8', errors='ignore') as file_in:
            content = file_in.read()
        
        with codecs.open(output_file, 'w', encoding='utf-8') as file_out:
            file_out.write(content)
        
        print(f"File cleaned successfully. Output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage
input_file = 'path/to/your/input_file.txt'
output_file = 'path/to/your/output_file.txt'

clean_file(input_file, output_file)
