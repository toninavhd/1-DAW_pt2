def run(feeling: str) -> str:

    match feeling:
        case 'happy':
            emoji = '😀'
        case 'sad':
            emoji = '😔'
        case 'angry':
            emoji = '😡'
        case 'pensive':
            emoji = '🤔'
        case 'surprised':
            emoji = '😮'
        case _:
            emoji = None

    return emoji


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
