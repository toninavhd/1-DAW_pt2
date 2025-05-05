def run(input_path: str) -> list:
    with open(input_path) as f:
        nums_rows = f.readlines()
        len_matrix = len(nums_rows[0].strip().split())
        csum = [0] * len_matrix

        for row in nums_rows:
            nums = row.strip().split()
            for col in range(len_matrix):
                csum[col] += int(nums[col])
    return csum


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
