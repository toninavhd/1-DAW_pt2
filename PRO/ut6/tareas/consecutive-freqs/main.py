def cfreq(elements, /, string=False):
    result = []
    if elements:
        current_element = elements[0]
        count = 1
        for element in elements[1:]:
            if element == current_element:
                count += 1
            else:
                result.append((current_element, count))
                current_element = element
                count = 1
        result.append((current_element, count))

    if string:
        result_string = ''
        for element in result:
            result_string += f'{element[0]}:{element[1]},'
        return result_string.rstrip(',')
    else:
        return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(cfreq)
