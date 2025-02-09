def cfreq(elements, /, string=False):
    
    if not elements:
        if string:
            return ""
        else:
            return []
    
    result = []
    current_element = elements[0]
    count = 0
    for element in elements:
        if element == current_element:
            count += 1
        else:
            result.append((current_element, count))
            current_element = element
            count = 1
    result.append((current_element, count))

    if string:
        return ",".join([f"{elem}:{freq}" for elem, freq in result])
    else:
        return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(cfreq)
