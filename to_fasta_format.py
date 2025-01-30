import os
import numpy as np

def to_fasta(file_path):
    """
    Reads a Multiple Sequence Alignment (MSA) file and returns a 2D NumPy array with sequences and their names.
    :param file_path: Path to the MSA file.
    :return: 2D NumPy array with two columns: sequence names and sequences.
    """
    sequences = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('//'):  # End of the header part
                break
            if not line.startswith(' Name:'):
                continue
            parts = line.split()
            sequences[parts[1]] = ""  # Initialize sequence with empty string

        for line in file:
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            
            parts = line.split()
            if parts:
                seq_name = parts[0]
                if seq_name in sequences:
                    sequences[seq_name] += ''.join(parts[1:])  # Concatenate sequence parts

    # Convert to 2D numpy array
    names = np.array(list(sequences.keys()))
    seqs = np.array(list(sequences.values()))
    fasta_format_alignment = np.column_stack((names, seqs))    
    fasta_format_alignment[:, 1] = np.char.replace(fasta_format_alignment[:, 1], ".", "-")
    return fasta_format_alignment

def process_folders(input_dir):
    """
    Traverse each folder in the input directory and process .msf files.
    :param input_dir: Path to the input directory.
    """
    # Traverse each folder in the input directory
    for root, dirs, files in os.walk(input_dir):
        for dir_name in dirs:
            # Check if the folder name starts with 'RV'
            if dir_name.startswith('RV'):
                folder_path = os.path.join(root, dir_name)
                process_files_in_folder(folder_path)

def process_files_in_folder(folder_path):
    """
    Process .msf files in a folder and convert them to .fasta format.
    :param folder_path: Path to the folder containing .msf files.
    """
    # Create a directory named 'fasta_format' within each folder
    fasta_dir = os.path.join(folder_path, 'fasta_format')
    os.makedirs(fasta_dir, exist_ok=True)

    # Find all files with .msf extension in the folder
    msf_files = [f for f in os.listdir(folder_path) if f.endswith('.msf')]
    for msf_file in msf_files:
        # Execute to_fasta function on each .msf file
        fasta_output = to_fasta(os.path.join(folder_path, msf_file))

        # Write the output to a file with the same name in the 'fasta_format' directory
        fasta_file_path = os.path.join(fasta_dir, msf_file.replace('.msf', '.fasta'))
        with open(fasta_file_path, 'w') as f:
            for seq_data in fasta_output:
                seq_name, seq_seq = seq_data
                f.write(f'>{seq_name}\n{seq_seq}\n')

def main():
    """
    Main function to execute the script.
    """
    # Example usage
    input_dir = '/Users/abrar.rahman/Desktop/Thesis_MS/DataSet/bb3_release'
    process_folders(input_dir)

if __name__ == "__main__":
    main()
