def tag_cleaner(tag:str) -> str:
    tag = tag.split()[0][1:]
    return tag.rstrip('>')

def run(tag1: str, tag2: str) -> bool:  
    if len(tag_cleaner(tag1)) != len(tag_cleaner(tag2)):
        return False
    
    return True


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
