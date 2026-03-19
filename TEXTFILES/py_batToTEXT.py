import os

def merge_scripts_to_txt(output_name="combined_files.txt"):
    # Target extensions
    extensions = ('.py', '.bat')
    
    # Get all matching files in the current directory
    files = [f for f in os.listdir('.') if f.endswith(extensions)]
    
    if not files:
        print("No .py or .bat files found in the current directory.")
        return

    with open(output_name, 'w', encoding='utf-8') as outfile:
        for filename in files:
            # Avoid merging the output file into itself
            if filename == output_name:
                continue
            
            # Write a header with the filename
            outfile.write(f"{'='*30}\n")
            outfile.write(f"SOURCE FILE: {filename}\n")
            outfile.write(f"{'='*30}\n\n")
            
            try:
                with open(filename, 'r', encoding='utf-8', errors='ignore') as infile:
                    outfile.write(infile.read())
            except Exception as e:
                outfile.write(f"[Error reading file: {e}]\n")
            
            # Add spacing between file contents
            outfile.write("\n\n")

    print(f"Success! {len(files)} files merged into '{output_name}'.")

if __name__ == "__main__":
    merge_scripts_to_txt()
