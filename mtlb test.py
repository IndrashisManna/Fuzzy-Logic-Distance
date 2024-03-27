import matlab

% Specify the file path

file_path = 'G:\Python code\Fuzzy logic\file1.csv';

% Import the CSV file into a MATLAB table
data = readtable(file_path);

% Extract the first three columns from the table
col1 = data.col1;
col2 = data.col2;
col3 = data.col3;

% Create a 3D lookup table using the first three columns
lookup_table = zeros(length(col1), length(col2), length(col3));
for i = 1:length(col1)
    for j = 1:length(col2)
        for k = 1:length(col3)
            lookup_table(i, j, k) = col1(i) * col2(j) * col3(k);  % Example calculation, replace with your logic
        end
    end
end

% Display the 3D lookup table
disp(lookup_table);
