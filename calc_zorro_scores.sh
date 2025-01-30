#!/bin/bash

# Record start time
start_time=$(date +%s)
echo "Script started at: $(date)"

# Base directory containing RV11, RV12, etc.
base_dir="/mnt/d/Thesis_MS/DataSet/bb3_release"

# Loop through each subfolder (RV11, RV12, etc.)
for subfolder in RV11 RV12 RV20 RV30 RV40 RV50; do
    echo "Processing $subfolder..."

    # Define paths
    fasta_dir="$base_dir/$subfolder/fasta_format"
    output_dir="$fasta_dir/zorro_scores"

    # Create zorro_scores folder if it doesn't exist
    mkdir -p "$output_dir"

    # Process each FASTA file in fasta_format
    for fasta_file in "$fasta_dir"/*.fasta; do
        # Get the base name of the file (without extension)
        base_name=$(basename "$fasta_file" .fasta)

        # Define output files
        zorro_output="$output_dir/${base_name}_zorro.txt"
        csv_output="$output_dir/${base_name}.csv"

        # Run Zorro to generate scores
        echo "Running Zorro on $fasta_file..."
        echo $zorro_output
        zorro $fasta_file > $zorro_output
        echo $?

        # Check if Zorro ran successfully
        if [ $? -ne 0 ]; then
            echo "Error: Zorro failed for $fasta_file due to $?. Skipping..."
            continue
        fi

        # Load the alignment and Zorro scores
        echo "Generating CSV for $fasta_file..."
        {
            # Print header
            echo "column_index,alignment_column,zorro_score"

            # Read the alignment and scores
            column_index=1
            while IFS= read -r zorro_score; do
                # Extract the alignment column (skip lines starting with '>')
                alignment_column=$(awk -v col="$column_index" '/^>/ {next} {print substr($0, col, 1)}' "$fasta_file" | tr '\n' '-')
                alignment_column=${alignment_column%-}  # Remove trailing dash

                # Skip all-gap columns
                if [[ "$alignment_column" =~ ^-+$ ]]; then
                    echo "Warning: Skipping all-gap column $column_index"
                    continue
                fi

                # Append to CSV
                echo "$column_index,$alignment_column,$zorro_score"

                # Increment column index
                column_index=$((column_index + 1))
            done < "$zorro_output"
        } > "$csv_output"

        echo "Saved CSV: $csv_output"
    done
done

# Record end time
end_time=$(date +%s)
echo "Script ended at: $(date)"

# Calculate time difference
time_diff=$((end_time - start_time))
echo "Total time taken: $time_diff seconds"
