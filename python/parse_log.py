def parse_log_line(log_line: str) -> dict | None:
    """
    Parses a single log line into a structured dictionary.

    The expected log format is: "TIMESTAMP [LOG_LEVEL] MESSAGE"
    Example: "2024-05-20T13:45:10Z [INFO] User 'alice' logged in successfully."

    Args:
        log_line: A string representing a single line from a log file.

    Returns:
        A dictionary containing the 'timestamp', 'log_level', and 'message'
        if the log line is valid, otherwise None.
    """
    # TODO: Implement the parsing logic here.
    # 1. Check if the log_line is valid. If not, return None.
    # 2. Split the line into its constituent parts: timestamp, log_level, and message.
    #    Remember that the message itself can contain spaces.
    # 3. Clean up the log_level to remove the square brackets.
    # 4. Create and return a dictionary with the extracted parts.

    # L1 = log_line.split(' ', 2)

    if ( 
        not isinstance(log_line, str) 
        or not log_line.strip() 
        or '[' not in log_line 
        or ']' not in log_line
        # or log_line.count('[') !=1
        # or log_line.count(']') !=1
        or len(log_line.split(' ')) < 3
    ):
        return None

    timestamp, log_level, message = log_line.split(' ', 2)

    if (
        not timestamp 
        or not log_level 
        or not message
        or not log_level.startswith('[')
        or not log_level.endswith(']')
    ):

        return None


    log_level = log_level.strip('[]')

    return {
        'timestamp': timestamp,
        'log_level': log_level,
        'message': message
    }



    pass